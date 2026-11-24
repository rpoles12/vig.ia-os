"""Adapt the original print PDF to white paper without moving its contents.

Only color operators and image color spaces change. Piece outlines replace the
dark fills as cut boundaries. Original text, paths, transformations and sizes
are retained. This is print preparation of a native PDF, not raster rebuilding.
"""
from pathlib import Path
from collections import Counter
import json
import zlib
from PIL import Image
from pypdf import PdfReader, PdfWriter
from pypdf.generic import (
    ContentStream, NameObject, FloatObject, NumberObject,
    ArrayObject, DictionaryObject, BooleanObject,
)

ROOT = Path(__file__).resolve().parents[1]
SRC = Path(r'C:\Users\45061155890\Desktop\Escape_Room_Pacote_Completo\01_PARA_IMPRESSAO\Escape_Room_Impressao_Completa_A4.pdf')
DEST = ROOT/'output/pdf/Escape_Room_Impressao_Completa_A4_Fundo_Branco.pdf'
QA = ROOT/'tmp/pdfs/impressos_brancos'
DEST.parent.mkdir(parents=True,exist_ok=True)
QA.mkdir(parents=True,exist_ok=True)
reader = PdfReader(SRC)
writer = PdfWriter()
writer.clone_document_from_reader(reader)
stats = Counter()
seen = set()

def gray(value):
    return [FloatObject(value)]

def luminance(args):
    rgb = tuple(float(x) for x in args)
    return .2126*rgb[0]+.7152*rgb[1]+.0722*rgb[2]

def map_color(args, stroke=False):
    rgb=tuple(float(x) for x in args)
    # Uniform white paper in place of the black-violet background.
    if max(rgb)<.10:
        return 1.0,True
    # Main text and bright accent both need strong monochrome contrast.
    if min(rgb)>.75:
        return 0.0,False
    if rgb[2]>.90 and rgb[0]>.60:
        return 0.0,False
    # Technical rules and small decorative rectangles stay restrained.
    if rgb[2]>.70 and rgb[1]<.30:
        return (.55 if stroke else .30),False
    # Secondary information remains readable, including on the badge.
    if max(rgb)-min(rgb)>.02:
        return (.60 if stroke else .28),False
    return min(luminance(rgb),.38),False

def recolor_stream(contents,pdf):
    stream=ContentStream(contents,pdf)
    new=[]
    bg_fill=False
    stack=[]
    for args,op in stream.operations:
        if op==b'q':
            stack.append(bg_fill)
        elif op==b'Q' and stack:
            bg_fill=stack.pop()
        if op in (b'rg',b'RG'):
            stroke=op==b'RG'
            v,is_background=map_color(args,stroke)
            new.append((gray(v),b'G' if stroke else b'g'))
            if not stroke:
                bg_fill=is_background
            stats['vector_color_operations']+=1
        elif op in (b'g',b'k'):
            if op==b'g':
                value=float(args[0])
                bg_fill=value<.1
                new.append((gray(1.0 if bg_fill else min(value,.38)),b'g'))
            else:
                raise ValueError('Unexpected CMYK fill')
        elif op in (b'f',b'f*') and bg_fill:
            # The path and its coordinates are unchanged. Use a hairline
            # boundary so white pieces can still be cut to the original size.
            new.extend([
                ([],b'q'),(gray(.60),b'G'),
                ([FloatObject(.35)],b'w'),
                (args,b'B*' if op==b'f*' else b'B'),([],b'Q')
            ])
            stats['piece_outlines']+=1
        else:
            new.append((args,op))
    stream.operations=new
    return stream

def recolor_resources(resources):
    for obj_ref in resources.get('/XObject',{}).values():
        obj=obj_ref.get_object()
        identity=id(obj)
        if identity in seen:
            continue
        seen.add(identity)
        if obj.get('/Subtype')=='/Form':
            new=recolor_stream(obj,writer)
            obj.set_data(new.get_data())
            if '/Resources' in obj:
                recolor_resources(obj['/Resources'])
        elif obj.get('/Subtype')=='/Image':
            iw,ih=int(obj['/Width']),int(obj['/Height'])
            assert obj['/BitsPerComponent']==8
            assert obj['/ColorSpace']=='/DeviceRGB'
            if (iw,ih)==(1600,480) and '/SMask' in obj:
                # Official wordmark becomes black; preserve original alpha.
                pixels=bytes(iw*ih)
                stats['black_wordmarks']+=1
            else:
                # Neutral print conversion. Identity, crop and dimensions stay.
                rgb=Image.frombytes('RGB',(iw,ih),obj.get_data())
                pixels=rgb.convert('L').tobytes()
                stats['grayscale_portraits']+=1
            obj._data=zlib.compress(pixels,9)
            obj[NameObject('/Filter')]=NameObject('/FlateDecode')
            obj[NameObject('/ColorSpace')]=NameObject('/DeviceGray')
            for field in ['/DecodeParms','/Decode']:
                obj.pop(NameObject(field),None)

for p in writer.pages:
    p[NameObject('/Contents')]=writer._add_object(recolor_stream(p.get_contents(),writer))
    recolor_resources(p['/Resources'])

writer.add_metadata({
    '/Title':'O Arquivo Corrompido - Impressao completa A4 - Fundo branco',
    '/Subject':'9 paginas A4 horizontal. Fundo branco, elementos monocromaticos e retratos em tons de cinza. Tamanho real 100%, frente unica.',
    '/Creator':'Adaptacao para impressao economica do PDF original',
})
writer._root_object[NameObject('/ViewerPreferences')]=DictionaryObject({
    NameObject('/PrintScaling'):NameObject('/None'),
    NameObject('/Duplex'):NameObject('/Simplex'),
    NameObject('/DisplayDocTitle'):BooleanObject(True),
})
with DEST.open('wb') as f:
    writer.write(f)

check=PdfReader(DEST)
assert len(check.pages)==len(reader.pages)==9
geometry_ops={b'cm',b're',b'm',b'l',b'c',b'v',b'y',b'h',b'Tm',b'Td',b'TD',b'Tf',b'Tj',b'TJ',b'Do'}
for i,(original,adapted) in enumerate(zip(reader.pages,check.pages),1):
    assert original.mediabox==adapted.mediabox
    assert original.extract_text()==adapted.extract_text(),f'Text mismatch on page {i}'
    a=[(args,op) for args,op in ContentStream(original.get_contents(),reader).operations if op in geometry_ops]
    b=[(args,op) for args,op in ContentStream(adapted.get_contents(),check).operations if op in geometry_ops]
    assert a==b,f'Layout mismatch on page {i}'
    assert all(op not in [b'rg',b'RG',b'k',b'K'] for args,op in ContentStream(adapted.get_contents(),check).operations)
    for ref in adapted['/Resources'].get('/XObject',{}).values():
        obj=ref.get_object()
        if obj.get('/Subtype')=='/Image':
            assert obj['/ColorSpace']=='/DeviceGray'
assert stats['piece_outlines']==27,stats
report={
    'source':str(SRC),'output':str(DEST),'pages':9,
    'paper_mm':[297,210],'background':'white',
    'all_text_preserved':True,'all_original_geometry_preserved':True,
    'all_graphics_monochrome':True,'stats':dict(stats),
}
(QA/'conferencia.json').write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps(report,ensure_ascii=False))
