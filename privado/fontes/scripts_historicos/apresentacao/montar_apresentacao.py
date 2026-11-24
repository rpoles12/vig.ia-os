from pathlib import Path
import json
from PIL import Image
from reportlab.pdfgen import canvas
from reportlab.lib.colors import HexColor
from reportlab.lib.utils import ImageReader
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from pypdf import PdfReader

ROOT = Path(__file__).resolve().parents[1]
ASSETS = ROOT / 'assets'
IMAGES = ASSETS / 'imagens'
FONTS = ASSETS / 'fontes'
VALIDATION = ROOT / 'revisao' / 'pdf' / 'validacao'
OUT = ROOT / 'output' / 'pdf'
OUT.mkdir(parents=True, exist_ok=True)
VALIDATION.mkdir(parents=True, exist_ok=True)
IMAGE_PATHS = {
    'capa.png': IMAGES / 'conceitos' / 'capa.png',
    'estacao.png': IMAGES / 'conceitos' / 'estacao.png',
    'grupo.png': IMAGES / 'conceitos' / 'grupo.png',
    'terminal_arquivo.png': IMAGES / 'capturas' / 'terminal_arquivo.png',
    'terminal_vigia.png': IMAGES / 'capturas' / 'terminal_vigia.png',
    'manifesto.png': IMAGES / 'documentos' / 'manifesto.png',
    'ficha_renata.png': IMAGES / 'documentos' / 'ficha_renata.png',
    'marca.png': IMAGES / 'identidade' / 'marca.png',
}

pdfmetrics.registerFont(TTFont('Space', str(FONTS / 'SpaceGrotesk-Bold.ttf')))
pdfmetrics.registerFont(TTFont('Mono', str(FONTS / 'IBMPlexMono-Regular.ttf')))
W, H = 960, 540
BG = '#08070C'
TEXT = '#E8DCFF'
MUTED = '#B8AFC8'
ACCENT = '#A66BFF'
PANEL = '#14111C'
pdf_path = OUT / 'O_Arquivo_Corrompido_Apresentacao_SESI.pdf'
c = canvas.Canvas(str(pdf_path), pagesize=(W, H), pageCompression=1)
c.setTitle('O Arquivo Corrompido | Apresentação à direção do SESI')
c.setAuthor('Projeto escolar - 7set.dev')
c.setSubject('Experiência investigativa para a feira escolar, sem revelar a solução do caso')
c.setCreator('Apresentação do projeto O Arquivo Corrompido')
c.setViewerPreference('DisplayDocTitle', 'true')
checks = []

def rect(x, y, w, h, fill):
    c.setFillColor(HexColor(fill))
    c.rect(x, H-y-h, w, h, fill=1, stroke=0)

def text(x, y, value, size=20, font='Mono', color=TEXT):
    c.setFont(font, size)
    c.setFillColor(HexColor(color))
    c.drawString(x, H-y-size, value)
    width = pdfmetrics.stringWidth(value, font, size)
    checks.append({'page':c.getPageNumber(),'text':value,'box':[x,y,x+width,y+size]})
    assert x >= 0 and x + width <= W+0.2, (c.getPageNumber(), value, x+width)
    assert y >= 0 and y+size <= H, (c.getPageNumber(), value, y+size)

def lines(x, y, value, size=20, font='Mono', color=TEXT, leading=None):
    leading = leading or size*1.32
    for i, line in enumerate(value.split('\n')):
        text(x, y+i*leading, line, size, font, color)
    return y+len(value.split('\n'))*leading

def paragraph(x, y, value, width, size=20, font='Mono', color=TEXT, leading=None):
    chunks = []
    for source_line in value.split('\n'):
        row = ''
        for word in source_line.split():
            candidate = (row+' '+word).strip()
            if pdfmetrics.stringWidth(candidate, font, size) <= width:
                row = candidate
            else:
                if row:
                    chunks.append(row)
                row = word
        chunks.append(row)
    return lines(x, y, '\n'.join(chunks), size, font, color, leading)

def photo(name, x, y, w, h, mode='cover', anchor=(.5,.5)):
    path = IMAGE_PATHS[name]
    with Image.open(path) as im:
        iw, ih = im.size
    scale = max(w/iw,h/ih) if mode=='cover' else min(w/iw,h/ih)
    dw, dh = iw*scale, ih*scale
    dx, dy = x+(w-dw)*anchor[0], y+(h-dh)*anchor[1]
    c.saveState()
    p = c.beginPath()
    p.rect(x,H-y-h,w,h)
    c.clipPath(p,stroke=0)
    c.drawImage(ImageReader(str(path)),dx,H-dy-dh,dw,dh,mask='auto')
    c.restoreState()

def logo(x=54,y=35,w=128):
    # Preserve the official full logo asset and its internal clear space.
    with Image.open(IMAGE_PATHS['marca.png']) as im:
        iw,ih = im.size
    c.drawImage(str(IMAGE_PATHS['marca.png']),x,H-y-w*ih/iw,w,w*ih/iw,mask='auto')

def footer(n, concept=False):
    text(56,513,'O ARQUIVO CORROMPIDO',9.5,'Mono',MUTED)
    text(444,513,'SESI / PROJETO ESCOLAR',9.5,'Mono',MUTED)
    text(870,511,f'{n:02d} / 09',10,'Mono',ACCENT)

def base(n,kicker,title=None):
    rect(0,0,W,H,BG)
    text(56,37,kicker.upper(),10,'Mono',ACCENT)
    if title:
        text(56,76,title,41,'Space')
    footer(n)

def end():
    c.showPage()

# 01 / Cover
photo('capa.png',0,0,W,H)
logo(41,30,158)
text(56,145,'EXPERIÊNCIA INVESTIGATIVA',11,'Mono',ACCENT)
lines(52,183,'O Arquivo\nCorrompido',68,'Space',leading=70)
lines(56,355,'Um escape room para\na feira escolar do SESI',21,'Mono',leading=29)
text(56,455,'APRESENTAÇÃO À DIREÇÃO',10.5,'Mono',MUTED)
text(659,481,'Ambientação conceitual',9.5,'Mono',MUTED)
footer(1)
end()

# 02 / Proposal
base(2,'A proposta')
photo('estacao.png',402,0,558,494,anchor=(.51,.5))
rect(0,0,390,494,BG)
text(56,37,'A PROPOSTA',10,'Mono',ACCENT)
lines(56,78,'Uma investigação\nem equipe',37,'Space',leading=44)
text(56,204,'3 a 5',58,'Space',ACCENT)
text(58,269,'participantes por grupo',16,'Mono')
text(56,318,'15 min',58,'Space',ACCENT)
text(58,384,'duração prevista',16,'Mono')
lines(58,431,'Cenário físico e\nterminal digital offline',16,'Mono',leading=23)
text(569,472,'Estação ilustrativa / conceito de montagem',9,'Mono',TEXT)
end()

# 03 / Narrative premise, only a safe existing evidence
base(3,'A premissa','O incidente')
lines(56,158,'Projetos copiados.\nRegistros corrompidos.\nUma morte a esclarecer.',29,'Space',leading=39)
paragraph(56,309,'O grupo reúne os vestígios para compreender o que aconteceu na sala técnica.',470,20,leading=28)
text(56,434,'Ficção de suspense,',16,'Mono',MUTED)
text(56,457,'sem violência gráfica.',16,'Mono',MUTED)
photo('manifesto.png',603,95,267,378,mode='contain')
text(607,479,'Documento do jogo / manifesto do lote',8.8,'Mono',MUTED)
end()

# 04 / The participants' role
base(4,'A experiência','O papel dos participantes')
photo('grupo.png',0,147,610,343,anchor=(.5,.5))
lines(650,184,'Comparar\nregistros.',27,'Space',leading=32)
lines(650,284,'Discutir\nhipóteses.',27,'Space',leading=32)
lines(650,384,'Sustentar\nconclusões.',27,'Space',leading=32)
text(56,468,'Ilustração conceitual',9.5,'Mono',TEXT)
end()

# 05 / Investigation route, no answers
base(5,'A investigação','O caminho da investigação')
steps = [
    (56,164,'01','Identificar um perfil','Comparar registros e reconhecer a ligação entre eles.'),
    (510,164,'02','Distinguir os acessos','Entender como a entrada física se relaciona ao acesso digital.'),
    (56,308,'03','Reconstruir a cronologia','Ordenar acontecimentos e recuperar o fragmento decisivo.'),
    (510,308,'04','Confirmar a conclusão','Reunir as descobertas em um protocolo e acompanhar a explicação.'),
]
for x,y,n,title,body in steps:
    text(x,y,n,28,'Mono',ACCENT)
    text(x,y+39,title,23,'Space')
    paragraph(x,y+75,body,391,17.5,leading=24)
text(56,471,'Cada correlação recupera parte do arquivo.',19,'Space',ACCENT)
end()

# 06 / Real application capture
base(6,'A testemunha digital')
text(56,74,'VIGIA/3',58,'Space')
paragraph(485,76,'Uma testemunha digital que participa da investigação e orienta a consulta aos registros.',414,19,leading=27)
text(56,170,'Orientações progressivas e áudios com transcrições.',20,'Space')
text(56,211,'CAPTURA REAL DO SISTEMA / CONSULTA INICIAL',9.5,'Mono',ACCENT)
photo('terminal_vigia.png',56,240,848,249,mode='contain')
end()

# 07 / Educational goals, expressed as goals rather than outcomes
base(7,'Objetivos de aprendizagem','O valor educativo')
text(56,135,'Habilidades que a experiência busca estimular',16,'Mono',MUTED)
learning=[
    (56,207,'Leitura crítica','Comparar documentos e reconhecer o que cada registro permite concluir.'),
    (510,207,'Raciocínio lógico','Relacionar pistas e ordenar acontecimentos para explicar o incidente.'),
    (56,351,'Colaboração','Discutir hipóteses e construir uma conclusão em grupo.'),
    (510,351,'Segurança da informação','Distinguir pessoas, credenciais e registros de acesso.'),
]
for x,y,title,body in learning:
    text(x,y,title,26,'Space',ACCENT)
    paragraph(x,y+45,body,391,18,leading=26)
end()

# 08 / Actual materials and honest status
base(8,'Materiais do projeto','O que já foi desenvolvido')
photo('terminal_arquivo.png',56,149,455,332,mode='contain')
photo('ficha_renata.png',405,281,136,193,mode='contain')
text(567,153,'Sistema digital',24,'Space',ACCENT)
paragraph(567,188,'Terminal offline, evidências e consultas à VIGIA/3.',330,17.5,leading=24)
text(567,260,'Materiais físicos',24,'Space',ACCENT)
paragraph(567,295,'Fichas de personagens, crachá e sinalização para impressão.',330,17.5,leading=24)
text(567,367,'Conteúdo narrativo',24,'Space',ACCENT)
paragraph(567,402,'Áudios com transcrições e reconstituição final do caso.',330,17.5,leading=24)
text(56,486,'Primeira aplicação com público prevista para a feira.',11,'Mono',MUTED)
end()

# 09 / Closing
photo('capa.png',0,0,W,H,anchor=(.65,.5))
c.saveState()
c.setFillColor(HexColor(BG))
c.setFillAlpha(.27)
c.rect(0,0,W,H,fill=1,stroke=0)
c.restoreState()
text(56,58,'A EXPERIÊNCIA NA FEIRA',11,'Mono',ACCENT)
lines(52,155,'Os visitantes\nassumem a\ninvestigação.',55,'Space',leading=60)
lines(56,376,'Uma explicação construída\na partir das evidências.',21,'Mono',leading=29)
logo(715,397,170)
footer(9)
end()
c.save()

# Structural and answer-leak checks, separate from visual review.
reader = PdfReader(str(pdf_path))
assert len(reader.pages)==9
all_text='\n'.join(p.extract_text() or '' for p in reader.pages)
for forbidden in ['2847','22:46','2246','BA17','Bryan','Helena','Marcelo','NORTHSTAR']:
    assert forbidden.casefold() not in all_text.casefold(), forbidden
for i,p in enumerate(reader.pages):
    assert abs(float(p.mediabox.width)/float(p.mediabox.height)-16/9)<.001
    assert (p.extract_text() or '').strip(), i
(VALIDATION/'layout_bounds.json').write_text(json.dumps(checks,ensure_ascii=False,indent=2),encoding='utf-8')
(VALIDATION/'extracted_text.txt').write_text(all_text,encoding='utf-8')
print(json.dumps({'pdf':str(pdf_path),'pages':len(reader.pages),'size_bytes':pdf_path.stat().st_size,'answer_leak_check':'passed'},ensure_ascii=False))
