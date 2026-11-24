from pathlib import Path
import shutil,json
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib.colors import HexColor
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import Paragraph,Table,TableStyle
from reportlab.lib.styles import ParagraphStyle

base=Path(r'C:\Users\SEU_USUARIO\Desktop\Escape_Room_Pacote_Completo')
work=Path('tmp/pistas_codigo');work.mkdir(parents=True,exist_ok=True)
stage=work/'sistema';shutil.copytree(base/'02_SISTEMA_OFFLINE',stage,dirs_exist_ok=True)
font=base/'04_PRODUCAO_E_EDITAVEIS/Fontes_e_licencas'
pdfmetrics.registerFont(TTFont('Space',str(font/'SpaceGrotesk-Bold.ttf')))
pdfmetrics.registerFont(TTFont('Mono',str(font/'IBMPlexMono-Regular.ttf')))
pdf=work/'T3_extrato_ocorrencias.pdf';c=canvas.Canvas(str(pdf),pagesize=A4);W,H=A4
c.setTitle('Extrato de ocorrências - T3');c.setFillColor(HexColor('#6426c9'));c.rect(42,H-62,35,4,fill=1,stroke=0)
c.setFont('Mono',9);c.drawString(42,H-84,'REPOSITÓRIO VÉRTICE / REGISTROS CORRELACIONADOS')
c.setFillColor(HexColor('#201c29'));c.setFont('Space',25);c.drawString(42,H-124,'Extrato de ocorrências')
sty=ParagraphStyle('body',fontName='Mono',fontSize=10,leading=16,textColor=HexColor('#201c29'))
small=ParagraphStyle('small',parent=sty,fontSize=9,leading=14)
def para(text,y):
 p=Paragraph(text,sty);_,h=p.wrap(W-84,H);p.drawOn(c,42,y-h);return y-h-20
y=para('Recorte recuperado de serviços diferentes. A ordem de extração não representa a ordem dos acontecimentos. Os horários usam a mesma referência local.',H-150)
rows=[['HORA LOCAL','ORIGEM','OCORRÊNCIA'],['22:47','Repositório','Cópia do V-17 concluída.'],['22:31','Catraca lateral','Entrada com credencial 2847.'],['22:44','Porta técnica','Entrada de Carlos na sala técnica.'],['22:46','Sala técnica','Confronto registrado. Trecho parcial; continuidade comprometida.'],['22:36','Autenticação','Sessão RV-MANUT iniciada.'],['22:49','Saída de emergência','Acionamento do acesso de saída.'],['22:41','Sensor local','Alerta encaminhado ao segurança.']]
t=Table([[Paragraph(v,small) for v in row] for row in rows],colWidths=[79,117,W-280])
t.setStyle(TableStyle([('BACKGROUND',(0,0),(-1,0),HexColor('#eae3f2')),('GRID',(0,0),(-1,-1),.4,HexColor('#c8bfce')),('VALIGN',(0,0),(-1,-1),'TOP'),('LEFTPADDING',(0,0),(-1,-1),8),('RIGHTPADDING',(0,0),(-1,-1),8),('TOPPADDING',(0,0),(-1,-1),10),('BOTTOMPADDING',(0,0),(-1,-1),10)]));_,h=t.wrap(W-84,H);t.drawOn(c,42,y-h);y-=h+25
y=para('Os campos de confronto, cópia e saída descrevem operações distintas. O relatório de mídia detalha a cobertura visual; este extrato registra o minuto de cada ocorrência, sem estabelecer o segundo exato da morte.',y)
assert y>70
c.setFont('Mono',7);c.setFillColor(HexColor('#665f70'));c.drawString(42,42,'T3 / DOCUMENTO CENOGRÁFICO - PESSOAS E FATOS FICTÍCIOS');c.save()

def read(name):return (stage/name).read_bytes().decode('utf-8')
def write(name,text):(stage/name).write_bytes(text.encode('utf-8'))

data=read('data.js')
needle='"evidence": ['
assert needle in data
data=data.replace(needle,needle+'{"id":"T3","title":"Extrato de ocorrências","file":"evidencias/T3_extrato_ocorrencias.png","stage":2},',1)
data=data.replace('"O áudio e a câmera registram o mesmo evento.", "Compare o minuto anunciado no Fragmento 03 com o último registro da câmera.", "A câmera termina às 22:46:32. No protocolo, informe o minuto do evento: 22:46."','"Abra o Extrato de ocorrências e localize a linha da sala técnica.", "Use o minuto da ocorrência de confronto, não o horário de conclusão da cópia.", "No extrato, o confronto é às 22:46; a cópia termina às 22:47. Informe 22:46."')
write('data.js',data)

engine=read('engine.js').replace("'22:47 corresponde ao fim da cópia. Compare o áudio com a câmera.'", "'22:47 é o fim da cópia. Abra o Extrato de ocorrências e procure a linha do confronto na sala técnica.'").replace("'Horário não confirmado. Compare o áudio com a câmera.'", "'Abra o Extrato de ocorrências: procure o confronto na sala técnica e informe apenas o minuto (HH:MM).'")
write('engine.js',engine)

html=read('index.html').replace('<input name="identidade" autocomplete=', '<input name="identidade" placeholder="Nome Sobrenome" autocomplete=').replace('<input name="credencial" inputmode=', '<input name="credencial" placeholder="Ex 1234" inputmode=')
start=html.index('<section id="ending"');end=html.index('</section><div class="context-actions">',start)
html=html[:start]+'''<section id="ending" class="work-card success final-report" aria-labelledby="final-message-title" hidden>
 <p class="eyebrow">CONCLUSÕES CONFIRMADAS</p><h3 id="final-message-title" tabindex="-1">Continue com sua anotação</h3>
 <p class="final-lead">O código foi exibido para registro no papel. Use sua anotação na próxima etapa. Ele não será mostrado novamente nesta sessão.</p>
 <button class="primary" id="open-ending"><i data-icon="play"></i>Abrir reconstituição</button>
</section>'''+html[end+len('</section>'):]
popup='''<dialog id="code-popup" class="code-popup" aria-labelledby="code-popup-title" aria-describedby="code-popup-instructions">
<p class="eyebrow">ATENÇÃO / CÓDIGO RECUPERADO</p><h2 id="code-popup-title" tabindex="-1">Anotem este código no papel</h2>
<p id="code-popup-instructions">Vocês precisarão dele na próxima etapa. Confiram todos os caracteres antes de continuar. Depois de fechar esta janela, o código não poderá ser consultado novamente.</p>
<strong id="code" aria-label="Código para anotar"></strong>
<label class="code-check"><input type="checkbox" id="code-written">Já anotamos o código completo no papel.</label>
<button id="confirm-code-written" class="primary" type="button" disabled>Anotamos. Ocultar código e continuar</button>
</dialog>
'''
html=html.replace('<dialog id="intro"',popup+'<dialog id="intro"',1)
for asset in ['app.js','data.js','engine.js','feedback.js','style.css']:
    html=html.replace('"'+asset+'"','"'+asset+'?v=20261117-pistas-codigo"')
write('index.html',html)

app=read('app.js')
app=app.replace("let selectedCard=null", "let codeAcknowledged=false;try{codeAcknowledged=sessionStorage.getItem('vigia-code-acknowledged')==='yes'}catch{}\n let selectedCard=null",1)
app=app.replace("CAM01:'Integridade da mídia · CAM01'", "CAM01:'Integridade da mídia · CAM01',T3:'Extrato de ocorrências'")
app=app.replace("(e.stage===3&&s.chronologyOrdered)","(e.stage===2&&s.accessesConfirmed)||(e.stage===3&&s.chronologyOrdered)")
app=app.replace("function tab(id,focus=true){", "function tab(id,focus=true){\n  if($('#code-popup').open)return;")
app=app.replace("$('#code').textContent=s.protocolConfirmed?D.key.answers.generated_protocol:'';", "if(!$('#code-popup').open)$('#code').textContent='';")
app=app.replace("if(s.protocolConfirmed){title='Código disponível';copy='Use o código gerado na próxima etapa.';label='Ver código';nextAction=()=>tab('solve')}", "if(s.protocolConfirmed){title='Código registrado';copy='Continue com o código anotado no papel. Não há nova exibição nesta sessão.';label='Continuar';nextAction=()=>tab('solve')}")
app=app.replace("if(fields.includes('horario')||!s.fragment03Consulted)suggestions.push(['CAM01','Compare o último registro da câmera com o minuto citado no Fragmento 03.'],['audio03','Leia o relato recuperado e diferencie o confronto do término da cópia.']);", "if(fields.includes('horario'))suggestions.push(['T3','Procure a linha do confronto na sala técnica. Use o minuto dessa ocorrência; a cópia termina em outro horário.'],['CAM01','Conferência adicional: o trecho S-02 começa às 22:44 e dura 152 segundos. Cabeçalhos sem imagem não contam.'],['audio03','O relato cita o minuto do confronto. Compare com a linha correspondente no extrato.']);")
app=app.replace("['L1','Confira o horário em que a sessão foi iniciada.'],['APOIO_03_pessoas_registros'", "['T3','Compare entrada, sessão, alerta, chegada à sala e confronto. As linhas foram extraídas fora da ordem; reorganize pelos horários.'],['L1','Confira o horário em que a sessão foi iniciada.'],['APOIO_03_pessoas_registros'")
app=app.replace("$('#ending').scrollIntoView({block:'start'});$('#final-message-title').focus({preventScroll:true})", "showCodeOnce()")
start=app.index(" $('#copy-code').onclick=")
end=app.index(" window.addEventListener('message'",start)
app=app[:start]+''' function showCodeOnce(){
  if(codeAcknowledged){notice('O código já foi exibido. Use sua anotação no papel.');$('#ending').scrollIntoView({block:'start'});$('#final-message-title').focus({preventScroll:true});return}
  closePublicDialogs();$('#code-written').checked=false;$('#confirm-code-written').disabled=true;$('#code').textContent=D.key.answers.generated_protocol;$('#code-popup').showModal();$('#code-popup-title').focus();
 }
 $('#code-written').onchange=()=>{$('#confirm-code-written').disabled=!$('#code-written').checked};
 $('#code-popup').addEventListener('cancel',e=>e.preventDefault());
 $('#code-popup').addEventListener('close',()=>{$('#code').textContent=''});
 $('#confirm-code-written').onclick=()=>{
  if(!$('#code-written').checked)return;codeAcknowledged=true;try{sessionStorage.setItem('vigia-code-acknowledged','yes')}catch{}
  $('#code').textContent='';$('#code-popup').close();notice('Código ocultado. Continue com a anotação no papel.','success');render();$('#ending').scrollIntoView({block:'start'});$('#final-message-title').focus({preventScroll:true});
 };
'''+app[end:]
app=app.replace("resetArmed=false;player.pause();player.removeAttribute('src');", "resetArmed=false;codeAcknowledged=false;try{sessionStorage.removeItem('vigia-code-acknowledged')}catch{}$('#code').textContent='';$('#code-written').checked=false;$('#confirm-code-written').disabled=true;player.pause();player.removeAttribute('src');",1)
write('app.js',app)

feedback=read('feedback.js').replace("[[523,0,.10],[659,.11,.10],[784,.22,.10],[1047,.34,.22]]", "[[659,0,.14],[880,.18,.14],[1047,.36,.23],[659,.72,.14],[880,.90,.14],[1047,1.08,.30]]")
write('feedback.js',feedback)
write('style.css',read('style.css')+'''
.code-popup{width:min(680px,calc(100vw - 32px));max-height:calc(100dvh - 32px);overflow:auto;padding:clamp(24px,4vw,42px);border:2px solid #c69aff;border-radius:18px;background:linear-gradient(145deg,#30203e,#120d1b);color:#efe5ff;box-shadow:0 0 65px #a66bff35;text-align:center;animation:code-arrive .3s ease-out}
.code-popup::backdrop{background:#08050de6;backdrop-filter:blur(6px)}
.code-popup h2{font-family:Space,sans-serif;font-size:clamp(27px,4vw,38px);line-height:1.2;margin:10px 0 20px}
.code-popup p{font-size:14px;line-height:1.8;max-width:100%}
.code-popup #code{display:block;margin:25px 0;padding:20px 10px;border:1px solid #be91ef;border-radius:9px;background:#100a18;color:#dfbdff;font-family:Mono,sans-serif;font-size:clamp(20px,4vw,35px);letter-spacing:1px;line-height:1.4;overflow-wrap:anywhere}
.code-check{display:flex!important;flex-direction:row!important;align-items:center;justify-content:center;gap:12px;font-size:13px!important;line-height:1.7;text-align:left;margin:22px 0;cursor:pointer}
.code-check input{width:21px!important;min-height:21px!important;height:21px;flex:0 0 21px;accent-color:#a66bff}
.code-popup button{width:100%;min-height:52px;justify-content:center;white-space:normal;line-height:1.5}
.code-popup button:disabled{opacity:.4;cursor:not-allowed}
@keyframes code-arrive{from{opacity:0;transform:translateY(14px) scale(.97)}to{opacity:1;transform:none}}
''')
print('Prévia preparada em '+str(stage.resolve()))
