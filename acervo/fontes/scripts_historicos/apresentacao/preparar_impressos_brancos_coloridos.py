"""White-paper adaptation retaining the original color photographs and palette."""
from pathlib import Path
from collections import Counter
import json
import zlib
from pypdf import PdfReader, PdfWriter
from pypdf.generic import ContentStream, NameObject, FloatObject, DictionaryObject, BooleanObject

ROOT=Path(__file__).resolve().parents[1]
SRC=Path(r'C:\Users\SEU_USUARIO\Desktop\Escape_Room_Pacote_Completo\01_PARA_IMPRESSAO\Escape_Room_Impressao_Completa_A4.pdf')
DEST=ROOT/'output/pdf/Escape_Room_Impressao_Completa_A4_Fundo_Branco_Colorido.pdf'
QA=ROOT/'tmp/pdfs/impressos_brancos_coloridos'
QA.mkdir(parents=True,exist_ok=True)
reader=PdfReader(SRC)
writer=PdfWriter()
writer.clone_document_from_reader(reader)
stats=Counter()
seen=set()

def numbers(values):
    return [FloatObject(v) for v in values]

def rgb8(r,g,b):
    return (r/255,g/255,b/255)

PURPLE=rgb8(100,38,201)
INK=rgb8(20,17,28)
MUTED=rgb8(91,83,99)

def map_color(args):
    rgb=tuple(float(v) for v in args)
    if max(rgb)<.10:
        return (1,1,1),True
    if min(rgb)>.75:
        return INK,False
    if rgb[2]>.90 and rgb[0]>.60:
        return PURPLE,False
    if rgb[2]>.70 and rgb[1]<.30:
        return rgb,False
    if max(rgb)-min(rgb)>.02:
        return MUTED,False
    return rgb,False

def recolor_stream(contents):
    stream=ContentStream(contents,writer)
    new=[]
    bg=False
    stack=[]
    for args,op in stream.operations:
        if op==b'q':
            stack.append(bg)
        elif op==b'Q' and stack:
            bg=stack.pop()
        if op in (b'rg',b'RG'):
            color,is_bg=map_color(args)
            new.append((numbers(color),op))
            if op==b'rg':
                bg=is_bg
            stats['color_operations']+=1
        elif op in (b'f',b'f*') and bg:
            new.extend([
                ([],b'q'),(numbers(rgb8(170,157,190)),b'RG'),
                ([FloatObject(.35)],b'w'),
                (args,b'B*' if op==b'f*' else b'B'),([],b'Q')
            ])
            stats['cut_outlines']+=1
        else:
            new.append((args,op))
    stream.operations=new
    return stream

def recolor_resources(resources):
    for ref in resources.get('/XObject',{}).values():
        obj=ref.get_object()
        if id(obj) in seen:
            continue
        seen.add(id(obj))
        if obj.get('/Subtype')=='/Form':
            stream=recolor_stream(obj)
            obj.set_data(stream.get_data())
            if '/Resources' in obj:
                recolor_resources(obj['/Resources'])
        elif obj.get('/Subtype')=='/Image':
            iw,ih=int(obj['/Width']),int(obj['/Height'])
            if (iw,ih)==(1600,480) and '/SMask' in obj:
                # Same official wordmark and alpha, purple for white paper.
                obj._data=zlib.compress(bytes((100,38,201))*(iw*ih),9)
                obj[NameObject('/Filter')]=NameObject('/FlateDecode')
                obj.pop(NameObject('/DecodeParms'),None)
                stats['purple_wordmarks']+=1
            else:
                # Portrait streams are not decoded, replaced or recolored.
                stats['original_color_portraits']+=1

for p in writer.pages:
    p[NameObject('/Contents')]=writer._add_object(recolor_stream(p.get_contents()))
    recolor_resources(p['/Resources'])
writer.add_metadata({
    '/Title':'O Arquivo Corrompido - Impressao A4 - Fundo branco com cores',
    '/Subject':'Fotos coloridas originais e identidade violeta em fundo branco. 9 paginas A4 horizontal. Tamanho real 100%, frente unica.',
    '/Creator':'Adaptacao cromatica para impressao em papel branco',
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
    assert original.extract_text()==adapted.extract_text(),i
    a=[(args,op) for args,op in ContentStream(original.get_contents(),reader).operations if op in geometry_ops]
    b=[(args,op) for args,op in ContentStream(adapted.get_contents(),check).operations if op in geometry_ops]
    assert a==b,i
    for name,ref in original['/Resources'].get('/XObject',{}).items():
        obj=ref.get_object()
        if obj.get('/Subtype')=='/Image' and (obj['/Width'],obj['/Height'])!=(1600,480):
            out=adapted['/Resources']['/XObject'][name].get_object()
            assert obj.get_data()==out.get_data(),(i,name)
            assert out['/ColorSpace']=='/DeviceRGB'
assert stats['cut_outlines']==27
report={'output':str(DEST),'pages':9,'white_background':True,'original_color_photos_preserved':True,'original_content_and_geometry_preserved':True,'stats':dict(stats)}
(QA/'conferencia.json').write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps(report,ensure_ascii=False))
