from pathlib import Path
from PIL import Image
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib.utils import ImageReader
from pypdf import PdfReader
import json,hashlib
ROOT=Path(__file__).resolve().parents[2];OUT=ROOT/'output/divulgacao'
image=OUT/'O_Arquivo_Corrompido_Cartaz_03-12.png';pdf=OUT/'O_Arquivo_Corrompido_Cartaz_03-12_A4.pdf'
im=Image.open(image).convert('RGB');w,h=A4;m=14.17;scale=min((w-2*m)/im.width,(h-2*m)/im.height)
c=canvas.Canvas(str(pdf),pagesize=A4);c.setTitle('O Arquivo Corrompido - 03/12, das 7h às 15h')
c.drawImage(ImageReader(im),(w-im.width*scale)/2,(h-im.height*scale)/2,im.width*scale,im.height*scale);c.showPage();c.save()
reader=PdfReader(pdf);assert len(reader.pages)==1 and abs(float(reader.pages[0].mediabox.width)-w)<.1
(OUT/'ARQUIVOS_COM_DATA.json').write_text(json.dumps({'primary_asset':image.name,'pdf':pdf.name,'event_date':'03/12','event_time':'7h às 15h','image_pixels':[im.width,im.height],'page_mm':[210,297],'print':'A4, retrato, 100%; margem de 5 mm; arte sem distorção.','upscaled':False,'image_sha256':hashlib.sha256(image.read_bytes()).hexdigest(),'pdf_sha256':hashlib.sha256(pdf.read_bytes()).hexdigest()},ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps({'png':str(image),'pdf':str(pdf)},ensure_ascii=False))
