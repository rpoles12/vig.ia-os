"""Documentos nativos para impressão e nova evidência CAM01."""
from pathlib import Path
from xml.sax.saxutils import escape
import json
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib.colors import HexColor
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import Paragraph, Table, TableStyle
from reportlab.lib.styles import ParagraphStyle
from pypdf import PdfReader, PdfWriter

ROOT=Path(__file__).resolve().parents[1]
BASE=Path(r'C:\Users\SEU_USUARIO\Desktop\Escape_Room_Pacote_Completo')
OUT=ROOT/'output/pdf'
WORK=ROOT/'tmp/protocolo_revisao'
DOCS=WORK/'documentos'
DOCS.mkdir(parents=True,exist_ok=True)
OUT.mkdir(parents=True,exist_ok=True)
for name,file in [('Space','SpaceGrotesk-Bold.ttf'),('Mono','IBMPlexMono-Regular.ttf')]:
    pdfmetrics.registerFont(TTFont(name,str(BASE/'04_PRODUCAO_E_EDITAVEIS/Fontes_e_licencas'/file)))
W,H=A4
INK=HexColor('#201c29');PURPLE=HexColor('#6426c9');GRAY=HexColor('#665f70')
style=ParagraphStyle('body',fontName='Mono',fontSize=10,leading=16,textColor=INK)
small=ParagraphStyle('small',parent=style,fontSize=8.4,leading=12)

class Document:
    def __init__(self,path,code,title,subtitle):
        self.c=canvas.Canvas(str(path),pagesize=A4)
        self.c.setTitle(title);self.c.setAuthor('Repositório Vértice - arquivo ficcional')
        self.code=code;self.y=H-160
        c=self.c;c.setFillColor(PURPLE);c.rect(42,H-62,35,4,fill=1,stroke=0)
        c.setFont('Mono',9);c.drawString(42,H-84,'REPOSITÓRIO VÉRTICE / ARQUIVO INTERNO')
        c.setFillColor(INK);c.setFont('Space',25);c.drawString(42,H-121,title)
        c.setFont('Mono',9);c.setFillColor(GRAY);c.drawString(42,H-141,subtitle)
    def paragraph(self,text,space=16,sty=style):
        p=Paragraph(text,sty);_,h=p.wrap(W-84,H)
        assert self.y-h>65,(self.code,self.y,h)
        p.drawOn(self.c,42,self.y-h);self.y-=h+space
    def section(self,title):
        self.y-=5;self.c.setFillColor(PURPLE);self.c.setFont('Space',13);self.c.drawString(42,self.y,title);self.y-=23
    def fields(self,rows):
        for label,value in rows:
            self.c.setFillColor(GRAY);self.c.setFont('Mono',8);self.c.drawString(42,self.y,label.upper());self.y-=19
            self.c.setFillColor(INK);self.c.setFont('Mono',11);self.c.drawString(42,self.y,value);self.y-=31
    def table(self,rows,widths):
        data=[[Paragraph(escape(str(v)),small) for v in row] for row in rows]
        t=Table(data,colWidths=widths,hAlign='LEFT')
        t.setStyle(TableStyle([('BACKGROUND',(0,0),(-1,0),HexColor('#eae3f2')),('GRID',(0,0),(-1,-1),.4,HexColor('#c8bfce')),('VALIGN',(0,0),(-1,-1),'TOP'),('LEFTPADDING',(0,0),(-1,-1),8),('RIGHTPADDING',(0,0),(-1,-1),8),('TOPPADDING',(0,0),(-1,-1),9),('BOTTOMPADDING',(0,0),(-1,-1),9)]))
        _,h=t.wrap(W-84,H);assert self.y-h>65,(self.code,self.y,h);t.drawOn(self.c,42,self.y-h);self.y-=h+20
    def finish(self):
        c=self.c;c.setStrokeColor(HexColor('#b6a7c5'));c.line(42,56,W-42,56)
        c.setFillColor(GRAY);c.setFont('Mono',7);c.drawString(42,42,self.code+' / DOCUMENTO CENOGRÁFICO - PESSOAS E FATOS FICTÍCIOS')
        c.save()

paths=[]
def create(name,code,title,subtitle):
    path=DOCS/name;paths.append(path);return Document(path,code,title,subtitle)

d=create('01_L1_registro_acesso.pdf','L1','Registro de sessão','Extração parcial / autenticação e atividade no repositório')
d.fields([('Horário da sessão','22:36'),('Conta temporária','RV-MANUT'),('Assinatura recuperada','B_A_17'),('Origem do perfil','LEGADO / CADASTRO ESTUDANTIL')])
d.section('Ocorrências recuperadas')
d.table([['HORÁRIO','OCORRÊNCIA'],['22:36','Sessão autenticada. Conta temporária disponível.'],['22:38','Leitura e cópia do conjunto V-17 iniciadas.'],['22:47','Transferência do conjunto concluída.']], [72,W-156])
d.paragraph('A conta de autenticação e a assinatura de operação são campos distintos. O nome civil não consta nesta extração.')
d.finish()

d=create('02_A17_arquivo_estudantil.pdf','A17','Arquivo estudantil','Projeto A-17 / cadastro histórico preservado')
d.fields([('Responsável pelo projeto','Bryan Almeida'),('Vínculo do registro','Cadastro estudantil antigo'),('Projeto','A-17'),('Identificação nos arquivos','BA-17')])
d.section('Convenção de identificação')
d.paragraph('BA-17 era a identificação utilizada pelo responsável nos arquivos do projeto A-17. O cadastro pertence ao arquivo estudantil e não ao quadro atual de funcionários.')
d.section('Situação do cadastro')
d.table([['REGISTRO','CLASSIFICAÇÃO'],['A-17','Projeto estudantil arquivado'],['BA-17','Identificação mantida nos arquivos históricos'],['Vínculo atual','Não consta no cadastro de funcionários desta ficha']], [102,W-186])
d.finish()

d=create('03_H1_conversa_recuperada.pdf','H1','Conversa recuperada','Recorte de mensagens / sequência preservada')
d.section('Bryan Almeida → Helena Duarte')
d.paragraph('Tenho as imagens de Rafael no laboratório e os dois acessos feitos no seu crachá. Amanhã a direção recebe tudo. Deixe o 2847 disponível às 22:28. Eu devolvo hoje.',space=28)
d.section('Helena Duarte → Bryan Almeida')
d.paragraph('Ele só precisava terminar o protótipo. Pegue e devolva. Não envolva meu sobrinho.',space=28)
d.section('Helena Duarte → Bryan Almeida')
d.paragraph('Bryan, devolva meu crachá hoje.',space=32)
d.section('Condições da extração')
d.paragraph('A ordem das mensagens foi preservada. O recorte não contém todos os metadados da conversa. Não há confirmação de identidade do portador da credencial neste documento.',sty=small)
d.finish()

d=create('04_RVM_auditoria_conta.pdf','RVM','Auditoria de conta','Registro administrativo / concessão temporária')
d.fields([('Conta auditada','RV-MANUT'),('Criação','18:10'),('Responsável pela criação','Marcelo Vieira'),('Origem administrativa','Remota')])
d.section('Permissões e alterações')
d.table([['ITEM','REGISTRO'],['Destino','Vértice / V-17'],['Alertas de rede','Redução programada por seis minutos'],['Sensor local','Não alterado por esta operação'],['Encerramento','Conta desativada às 22:54']], [125,W-209])
d.paragraph('A auditoria identifica quem criou a conta. Não identifica, por si só, quem operou presencialmente o computador durante a sessão.')
d.finish()

d=create('05_estoque_consumiveis.pdf','ADM-08','Controle de suprimentos','Almoxarifado administrativo / conferência de materiais')
d.table([['MATERIAL','SALDO','DESTINO'],['Papel A4','12 resmas','Secretaria'],['Envelopes pardos','38 unidades','Arquivo administrativo'],['Clipes metálicos','6 caixas','Expediente'],['Etiquetas adesivas','3 pacotes','Organização de pastas'],['Pastas suspensas','21 unidades','Arquivo administrativo']], [200,100,W-384])
d.section('Pendências de reposição')
d.paragraph('Solicitar nova cotação de envelopes na próxima compra de material de expediente. Separar as caixas abertas antes de encaminhar os pacotes fechados.')
d.section('Observação do setor')
d.paragraph('Conferência restrita a consumíveis. Equipamentos, credenciais e materiais de laboratório não integram esta relação.')
d.finish()

d=create('06_solicitacao_sinalizacao.pdf','ADM-12','Solicitação de sinalização','Serviços administrativos / organização das áreas comuns')
d.fields([('Área solicitante','Atendimento e recepção'),('Objeto','Revisão das placas de orientação'),('Prioridade','Rotina'),('Situação','Aguardando orçamento')])
d.section('Escopo solicitado')
d.paragraph('Conferir as placas de sanitários, recepção e sala de reuniões. Substituir suportes danificados e padronizar a altura das placas nas áreas comuns.')
d.section('Exclusões')
d.paragraph('A solicitação não contempla controles de acesso, câmeras, alarmes, sensores ou equipamentos da ala técnica.')
d.section('Encaminhamento')
d.paragraph('Apresentar proposta de materiais e quantitativos ao setor administrativo. Não há serviço executado associado a esta solicitação.')
d.finish()

writer=PdfWriter()
for p in paths:writer.append(str(p))
print_pdf=OUT/'Escape_Room_6_Documentos_Complementares_A4.pdf'
with print_pdf.open('wb') as f:writer.write(f)
assert len(PdfReader(print_pdf).pages)==6

camera=WORK/'CAM01_relatorio_integridade.pdf'
d=Document(camera,'CAM01','Integridade da mídia','Câmera da sala técnica / recuperação parcial do arquivo local')
d.paragraph('Extração de trechos de mídia e mensagens do serviço. Relógios na mesma referência local. Os eventos abaixo não possuem todos a mesma origem.',space=13,sty=small)
d.section('1. Inventário de trechos')
d.table([['TRECHO','INÍCIO LOCAL','EXTENSÃO','RESULTADO'],['S-01','22:41:00','180 s','Vídeo íntegro'],['S-02','22:44:00','152 s','Vídeo recuperado'],['S-03','22:47:00','0 s','Somente cabeçalho; sem quadros']], [62,100,76,W-322])
d.section('2. Mensagens do serviço')
d.table([['HORÁRIO','ORIGEM','RETORNO'],['22:44','Captura','Segmento S-02 em gravação.'],['--:--','Gravador','Falha na continuidade visual; carimbo desta mensagem não recuperado.'],['22:47','Repositório','Cópia V-17 concluída. Evento externo ao vídeo.'],['22:47','Recuperação','Cabeçalho S-03 localizado; nenhum quadro decodificável.'],['22:48','Diagnóstico','Serviço responde; fluxo visual indisponível.']], [67,100,W-251])
d.section('3. Critério de leitura')
d.paragraph('A extensão indica o intervalo entre o início do trecho e seu último quadro decodificável. Cabeçalhos sem quadros e respostas do diagnóstico não ampliam a cobertura visual. Mensagens do repositório registram outra operação.',sty=small,space=10)
d.paragraph('O inventário de mídia não determina o instante exato da morte. Relacionar a cobertura visual ao relato do confronto para interpretar o minuto do evento.',sty=small,space=0)
d.finish()

guide=OUT/'Escape_Room_Guia_6_Documentos_EQUIPE.md'
guide.write_text('''# Documentos complementares - equipe\n\nImprima o PDF de seis páginas em A4 vertical, tamanho real/100%, frente única. Misture as folhas pelo cenário e não apresente esta lista aos participantes. As folhas complementam o PDF de cenário existente; não o substituem.\n\n1. L1: assinatura do acesso e horários da sessão/cópia.\n2. A17: vincula BA-17 a Bryan Almeida.\n3. H1: credencial e coação de Helena.\n4. RVM: criação do acesso digital por Marcelo.\n5. ADM-08: controle de suprimentos, sem participação no caso.\n6. ADM-12: solicitação de sinalização, sem participação no caso.\n\nCatraca, contexto de Rafael, chantagem financeira, cronologia, mídia e fragmentos continuam no sistema. Não é possível reconstruir tudo apenas com estas seis folhas. Os dois documentos administrativos não introduzem outro suspeito nem outra solução.\n\nCAM01: o trecho S-02 começa às 22:44:00 e cobre 152 segundos; seu último quadro é de 22:46:32. O cabeçalho S-03 não contém imagem. A cópia às 22:47 e o diagnóstico posterior não estendem o vídeo. A comparação com o relato do confronto sustenta o minuto 22:46; não estabelece o segundo exato da morte.\n''',encoding='utf-8')
print(json.dumps({'impressao':str(print_pdf),'camera':str(camera),'guia':str(guide)},ensure_ascii=False))
