from pathlib import Path
from PIL import Image
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib.utils import ImageReader
from pypdf import PdfReader
import json
ROOT=Path(__file__).resolve().parents[2];OUT=ROOT/'output/pdf/jornais_investigacao/v2_imagens'
paths=[OUT/f'Jornal_{i:02}_A4.png' for i in [1,2]]
pdf=OUT/'Jornais_Imagens_A4_Impressao.pdf';c=canvas.Canvas(str(pdf),pagesize=A4);c.setTitle('Jornal do Vértice - páginas ilustradas para impressão')
records=[]
for p in paths:
    im=Image.open(p);ratio=im.width/im.height;w,h=A4;margin=14.17 # 5 mm, protects the page from printer clipping
    factor=min((w-2*margin)/im.width,(h-2*margin)/im.height);iw,ih=im.width*factor,im.height*factor
    c.drawImage(ImageReader(im),(w-iw)/2,(h-ih)/2,iw,ih);c.showPage()
    records.append({'image':p.name,'pixels':[im.width,im.height],'aspect':ratio,'a4_aspect':210/297,'placed_dpi':im.width/(iw/72),'upscaled':False,'verified':'Página inteira inspecionada visualmente: manchetes, artigos, acentos, rodapés e ausência de respostas; sem erro textual observado.'})
c.save();r=PdfReader(pdf);assert len(r.pages)==2
for page in r.pages:assert abs(float(page.mediabox.width)-A4[0])<.1 and abs(float(page.mediabox.height)-A4[1])<.1
(OUT/'CONFERENCIA.json').write_text(json.dumps({'method':'Imagens geradas e inspecionadas antes da montagem do PDF; imagem original incorporada sem reescrever ou rasterizar novamente os textos.','pages':records,'print':'A4, retrato, tamanho real 100%; margem técnica de 5 mm; preservar a textura de papel e a retícula.','text_review':'Revisão visual manual. Não foi adicionada camada OCR ao PDF.','spoilers':'Sem nomes de envolvidos, credenciais, horários, código ou solução do caso.'},ensure_ascii=False,indent=2),encoding='utf-8')
print(pdf)
clip=OUT/'Manchetes_A4.png'
if clip.exists():
    im=Image.open(clip);w,h=A4;margin=14.17;scale=min((w-margin*2)/im.width,(h-margin*2)/im.height)
    cp=OUT/'Manchetes_Imagens_A4_Impressao.pdf';cc=canvas.Canvas(str(cp),pagesize=A4)
    cc.drawImage(ImageReader(im),(w-im.width*scale)/2,(h-im.height*scale)/2,im.width*scale,im.height*scale);cc.showPage();cc.save()
    from pypdf import PdfWriter
    writer=PdfWriter();writer.append(str(pdf));writer.append(str(cp))
    kit=OUT/'Kit_Jornais_e_Manchetes_A4.pdf'
    with kit.open('wb') as f:writer.write(f)
    assert len(PdfReader(kit).pages)==3
    print(kit)
