from pathlib import Path
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import Paragraph
from reportlab.lib.utils import ImageReader
from PIL import Image,ImageOps
import json
ROOT=Path(__file__).resolve().parents[2];OUT=ROOT/'output/pdf/jornais_investigacao';OUT.mkdir(parents=True,exist_ok=True)
W,H=A4;M=36;CW=W-2*M;INK='#171717'
from reportlab.lib.colors import HexColor
def para(c,text,x,y,w,size=10.8,font='Times-Roman',leading=None):
    p=Paragraph(text,ParagraphStyle('p',fontName=font,fontSize=size,leading=leading or size*1.3,textColor=HexColor(INK),spaceAfter=0))
    _,h=p.wrap(w,H);assert y-h>46,(text[:55],y,h)
    p.drawOn(c,x,y-h);return y-h
def line(c,y):c.setLineWidth(.6);c.line(M,y,W-M,y)
def mast(c,num,section):
    c.setFillColor(HexColor(INK));c.setStrokeColor(HexColor(INK))
    c.setFont('Times-Bold',43);c.drawCentredString(W/2,H-66,'JORNAL DO VÉRTICE')
    c.setFont('Helvetica',8);c.drawString(M,H-88,'EDIÇÃO ESPECIAL  /  ARQUIVO LOCAL');c.drawRightString(W-M,H-88,section.upper())
    line(c,H-98);c.setLineWidth(2);c.line(M,H-102,W-M,H-102)
    c.setFont('Helvetica',7);c.drawString(M,29,'Material cenográfico de O Arquivo Corrompido');c.drawRightString(W-M,29,f'FOLHA {num:02}')
def cols(c,y,a,b):
    gap=22;cw=(CW-gap)/2
    ya=y;yb=y
    for title,body in a:
        ya=para(c,title,M,ya,cw,15,'Times-Bold');ya-=7;ya=para(c,body,M,ya,cw);ya-=18
    for title,body in b:
        yb=para(c,title,M+cw+gap,yb,cw,15,'Times-Bold');yb-=7;yb=para(c,body,M+cw+gap,yb,cw);yb-=18
    c.setLineWidth(.3);c.line(W/2,y,W/2,min(ya,yb)+10)
    return min(ya,yb)
def page1(c):
    mast(c,1,'Notícia de abertura')
    y=H-125
    y=para(c,'Incidente interrompe<br/>operação no Vértice',M,y,CW,35,'Times-Bold',36)-12
    y=para(c,'Arquivos danificados e registros incompletos deixam perguntas sobre o que aconteceu no repositório.',M,y,CW,14,'Times-Italic',17)-17
    im=ImageOps.grayscale(Image.open(ROOT/'output/video_inicial/assets/abertura_corredor.png'))
    ph=160;c.drawImage(ImageReader(im),M,y-ph,CW,ph,mask='auto');y-=ph+7
    y=para(c,'Imagem ilustrativa das instalações. A apuração depende dos materiais disponíveis para consulta.',M,y,CW,8,'Helvetica',10)-15
    cols(c,y,
      [('Ocorrência ainda exige esclarecimentos','Um incidente comprometeu a operação do Repositório Vértice. Parte dos arquivos foi encontrada danificada, e os registros disponíveis ainda não permitem apresentar uma versão completa do acontecimento.<br/><br/>As informações reunidas precisam ser examinadas em conjunto. A ausência de um dado em um documento não encerra a busca: outros materiais podem oferecer contexto para sua interpretação.')],
      [('Documentos abrem a investigação','O acervo disponível reúne materiais físicos e registros em computador. Cabe à equipe observar os detalhes, comparar as fontes e separar o que está documentado do que ainda depende de confirmação.'),('Perguntas em aberto','Quem aparece nos registros? Que informações podem ser relacionadas? Como reconstruir a sequência dos fatos?<br/><br/>As respostas deverão ser sustentadas pelas evidências encontradas durante a investigação.')])
    c.showPage()
def page2(c):
    mast(c,2,'Arquivo e investigação')
    y=H-125
    y=para(c,'Informações dispersas<br/>pedem leitura em conjunto',M,y,CW,32,'Times-Bold',34)-13
    y=para(c,'A consulta começa na sala e continua na estação digital. Cada descoberta pode abrir uma nova pergunta.',M,y,CW,14,'Times-Italic',17)-21
    c.setLineWidth(1);c.rect(M,y-115,CW,115)
    for i,(title,body) in enumerate([('OBSERVAR','Ler os materiais com atenção.'),('COMPARAR','Relacionar fontes diferentes.'),('REGISTRAR','Anotar dúvidas e conclusões.')]):
        x=M+14+i*CW/3
        para(c,title,x,y-19,CW/3-24,11,'Helvetica-Bold')
        para(c,body,x,y-47,CW/3-24,11,'Times-Roman')
    y-=138
    y=cols(c,y,
      [('O espaço também guarda informação','O painel de funcionários permite consultar a composição da equipe. As pastas e os demais materiais encontrados na sala integram o acervo da investigação.<br/><br/>Observe nomes, descrições e relações que possam ser conferidos em outras fontes. Uma anotação pode ajudar a localizar um documento ou formular uma pergunta.'),('Anotações para a equipe','Registre o que encontrou e onde encontrou. Preserve a diferença entre uma observação e uma hipótese. Quando duas informações parecerem incompatíveis, retome as fontes antes de concluir.')],
      [('Uma estação, várias formas de consulta','No computador, o Explorador de Arquivos reúne documentos; o player permite ouvir registros; e a VIG.IA oferece apoio para localizar informações e orientar comparações.<br/><br/>O aplicativo Registros recebe as conclusões da equipe. O arquivo Próximos passos acompanha o avanço da investigação.'),('A apuração permanece aberta','Nenhuma manchete substitui a análise do material disponível. Reunir documentos é o primeiro passo; compreender como eles se relacionam é o desafio da investigação.')])
    y-=5;line(c,y);y-=17
    para(c,'CADERNO DE APURAÇÃO',M,y,CW,11,'Helvetica-Bold');y-=29
    for _ in range(3):
        if y<55:break
        c.setStrokeColor(HexColor('#999999'));c.setLineWidth(.35);c.line(M,y,W-M,y);y-=21
    c.showPage()
pdf=OUT/'Jornais_Inicio_Investigacao_A4.pdf';c=canvas.Canvas(str(pdf),pagesize=A4);c.setTitle('Jornal do Vértice - início da investigação');page1(c);page2(c);c.save()
# Separate sheets are convenient when copies need to be distributed independently.
from pypdf import PdfReader,PdfWriter
r=PdfReader(pdf)
for i,p in enumerate(r.pages,1):
    w=PdfWriter();w.add_page(p)
    with (OUT/f'Jornal_Folha_{i:02}_A4.pdf').open('wb') as f:w.write(f)
text='\n'.join(p.extract_text() for p in r.pages)
assert all(x not in text for x in ['2847','22:46','BA17','Bryan','Helena','Marcelo','B_A_17'])
(OUT/'IMPRESSAO.txt').write_text('Imprimir em papel A4, tamanho real (100%), orientação retrato. Preto e branco, frente única. As duas folhas compõem um jornal cenográfico inicial. Deixar juntas na entrada ou na mesa de investigação; não esconder estas folhas. O painel, as pastas e o crachá continuam compondo a investigação física. Nenhuma folha contém o gabarito.\n',encoding='utf-8')
print(pdf)
recortes=OUT/'Manchetes_Recortaveis_A4.pdf';c=canvas.Canvas(str(recortes),pagesize=A4);c.setTitle('Manchetes recortáveis - Jornal do Vértice')
c.setFont('Helvetica-Bold',10);c.drawString(M,H-35,'JORNAL DO VÉRTICE / RECORTES PARA AMBIENTAÇÃO')
items=[('Incidente interrompe operação no Vértice','Arquivos danificados deixam perguntas sobre o acontecimento.'),('Registros comprometidos desafiam a apuração','Materiais disponíveis precisam ser analisados em conjunto.'),('Circunstâncias ainda estão sob investigação','A reconstrução dos fatos depende do cruzamento de informações.'),('O que aconteceu no repositório?','Perguntas permanecem abertas enquanto a equipe examina os registros.')]
for i,(title,body) in enumerate(items):
    top=H-65-i*180
    c.setDash(3,3);c.setStrokeColor(HexColor('#999999'));c.setLineWidth(.4);c.rect(M-5,top-160,CW+10,165);c.setDash()
    c.setStrokeColor(HexColor(INK));c.setFillColor(HexColor(INK));c.setFont('Times-Bold',12);c.drawString(M+12,top-20,'JORNAL DO VÉRTICE')
    c.setFont('Helvetica',7);c.drawRightString(W-M-12,top-20,'EDIÇÃO ESPECIAL')
    c.line(M+12,top-29,W-M-12,top-29)
    y=para(c,title,M+12,top-41,CW-24,26,'Times-Bold',28)-10
    para(c,body,M+12,y,CW-24,11,'Times-Italic',14)
c.setFont('Helvetica',7);c.drawString(M,25,'Material cenográfico de O Arquivo Corrompido. Recortar pelas linhas pontilhadas.');c.save()
print(recortes)
