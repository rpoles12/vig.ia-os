from pathlib import Path
from PIL import Image
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib.utils import ImageReader
from pypdf import PdfReader
import json,hashlib
ROOT=Path(__file__).resolve().parents[2];OUT=ROOT/'output/divulgacao'
image=OUT/'O_Arquivo_Corrompido_Cartaz.png';pdf=OUT/'O_Arquivo_Corrompido_Cartaz_A4.pdf'
im=Image.open(image).convert('RGB');w,h=A4;margin=14.17
factor=min((w-margin*2)/im.width,(h-margin*2)/im.height);iw,ih=im.width*factor,im.height*factor
c=canvas.Canvas(str(pdf),pagesize=A4);c.setTitle('O Arquivo Corrompido - cartaz de divulgação');c.setAuthor('Projeto O Arquivo Corrompido')
c.drawImage(ImageReader(im),(w-iw)/2,(h-ih)/2,iw,ih);c.showPage();c.save()
reader=PdfReader(pdf);assert len(reader.pages)==1;assert abs(float(reader.pages[0].mediabox.width)-w)<.1
(OUT/'ARQUIVOS.json').write_text(json.dumps({'primary_asset':image.name,'pdf':pdf.name,'image_pixels':[im.width,im.height],'print_page_mm':[210,297],'print':'A4, retrato, escala 100%; margem técnica de 5 mm; imagem sem distorção.','upscaled':False,'image_sha256':hashlib.sha256(image.read_bytes()).hexdigest(),'pdf_sha256':hashlib.sha256(pdf.read_bytes()).hexdigest(),'text_review':'Conferir os textos na imagem gerada e na página renderizada antes de entregar.','source':'image_gen integrada, com três referências do usuário e papel de parede do jogo para identidade visual.'},ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps({'png':str(image),'pixels':[im.width,im.height],'pdf':str(pdf)},ensure_ascii=False))
