from pathlib import Path
from PIL import Image
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib.utils import ImageReader
from pypdf import PdfReader
import json
ROOT=Path(__file__).resolve().parents[2];OUT=ROOT/'output/pdf/jornais_investigacao/v3_fundo_branco'
pdf=OUT/'Kit_Jornais_e_Manchetes_A4_Branco.pdf';c=canvas.Canvas(str(pdf),pagesize=A4);c.setTitle('Jornais e manchetes - fundo branco para impressão econômica')
for name in ['Jornal_01_A4.png','Jornal_02_A4.png','Manchetes_A4.png']:
    im=Image.open(OUT/name).convert('RGB');w,h=A4;m=14.17;scale=min((w-2*m)/im.width,(h-2*m)/im.height)
    c.setFillColorRGB(1,1,1);c.rect(0,0,w,h,stroke=0,fill=1)
    # PDF prepress: near-white paper pixels knock out to the pure white page.
    # This avoids printing a pale tint left by image generation or compression.
    c.drawImage(ImageReader(im),(w-im.width*scale)/2,(h-im.height*scale)/2,im.width*scale,im.height*scale,mask=[245,255,245,255,245,255]);c.showPage()
c.save();reader=PdfReader(pdf);assert len(reader.pages)==3
for page in reader.pages:assert abs(float(page.mediabox.width)-A4[0])<.1
(OUT/'IMPRESSAO.json').write_text(json.dumps({'pages':3,'size':'A4','scale':'100%','background':'RGB 255,255,255; paper values 245–255 are knocked out in the PDF onto a pure white page.','images':'Edited with integrated image_gen; text and page layout inspected before PDF output.','preserved':'Manchetes, artigos, ilustrações, colunas e recortes; sem respostas do caso.'},ensure_ascii=False,indent=2),encoding='utf-8')
print(pdf)
