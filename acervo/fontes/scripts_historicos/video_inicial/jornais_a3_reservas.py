from pathlib import Path
from PIL import Image
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A3
from reportlab.lib.utils import ImageReader
from pypdf import PdfReader
import hashlib,json
ROOT=Path(__file__).resolve().parents[2];SOURCE=ROOT/'output/pdf/jornais_investigacao/v3_fundo_branco';OUT=ROOT/'output/pdf/jornais_investigacao/a3_com_reservas';OUT.mkdir(parents=True,exist_ok=True)
names=['Jornal_01_A4.png','Jornal_02_A4.png','Manchetes_A4.png'];pdf=OUT/'Jornais_A3_Duas_Copias.pdf'
c=canvas.Canvas(str(pdf),pagesize=A3);c.setTitle('Jornais e manchetes A3 - dois conjuntos completos')
for copy in range(2):
    for name in names:
        im=Image.open(SOURCE/name).convert('RGB');w,h=A3;m=14.17;scale=min((w-2*m)/im.width,(h-2*m)/im.height)
        c.setFillColorRGB(1,1,1);c.rect(0,0,w,h,stroke=0,fill=1)
        c.drawImage(ImageReader(im),(w-im.width*scale)/2,(h-im.height*scale)/2,im.width*scale,im.height*scale,mask=[245,255,245,255,245,255]);c.showPage()
c.save();pages=PdfReader(pdf).pages;assert len(pages)==6
for p in pages:assert abs(float(p.mediabox.width)-A3[0])<.1 and abs(float(p.mediabox.height)-A3[1])<.1
for i in range(3):
    a=pages[i].get_contents().get_data();b=pages[i+3].get_contents().get_data();assert a==b
(OUT/'IMPRESSAO.json').write_text(json.dumps({'paper_mm':[297,420],'orientation':'portrait','pages':6,'copies_of_each_sheet':2,'order':['jornal 1','jornal 2','manchetes','jornal 1 - reserva','jornal 2 - reserva','manchetes - reserva'],'print':'A3, escala 100%, frente única, uma cópia do PDF; as reservas já estão incluídas.','proportion':'A3 e A4 compartilham a proporção da série A; arte ampliada uniformemente, sem distorção.','background':'branco puro','resampling':'Nenhuma resolução artificial acrescentada; imagens originais preservadas.','sha256':hashlib.sha256(pdf.read_bytes()).hexdigest()},ensure_ascii=False,indent=2),encoding='utf-8')
print(pdf)
