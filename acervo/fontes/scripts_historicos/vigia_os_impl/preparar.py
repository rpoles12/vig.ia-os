from pathlib import Path
import re,json,shutil
ROOT=Path(__file__).resolve().parents[2]
S=ROOT/'output/vigia_os_sistema'
assets=S/'assets/os';assets.mkdir(parents=True,exist_ok=True)
paths={
'files':'<path d="M7 16h18l6 7h26v31H7z" fill="url(#g)"/><path d="M7 16v-5h17l7 7h26v7H7z" fill="#c59bff"/><path d="M8 26h49v28H8z" fill="url(#g)"/>',
'vigia':'<g fill="none" stroke="#d9b9ff" stroke-width="1.8"><path d="M32 5 56 21 51 48 32 59 10 46 7 21Z M32 5 21 23 7 21 32 45 56 21 21 23 10 46 32 45 51 48 44 23 32 5 M21 23h23l-12 22V59 M7 21h49"/></g>',
'solve':'<rect x="14" y="12" width="37" height="46" rx="5" fill="url(#g)" stroke="#d1adff" stroke-width="2"/><rect x="24" y="7" width="17" height="12" rx="4" fill="#c59bff"/><path d="M23 30h19M23 39h19M23 48h13" stroke="#eadbff" stroke-width="3" stroke-linecap="round"/>',
'media':'<g stroke="url(#g)" stroke-width="4" stroke-linecap="round"><path d="M8 29v6M16 22v20M24 13v38M32 6v52M40 16v32M48 24v16M56 29v6"/></g>',
'timeline':'<path d="M8 32h48" stroke="#b17aff" stroke-width="4"/><g fill="#9f5af5" stroke="#d4afff" stroke-width="2"><circle cx="8" cy="32" r="5"/><circle cx="32" cy="32" r="8"/><circle cx="56" cy="32" r="5"/></g><circle cx="32" cy="32" r="3" fill="#f1e5ff"/>',
'broken':'<path d="M14 5h25l13 13v41H14z" fill="#8b839c"/><path d="M39 5v14h13" fill="#c7bed7"/><path d="m34 7-7 17 12 9-14 13 6 13" fill="none" stroke="#17121f" stroke-width="4"/>',
'file':'<path d="M14 5h25l13 13v41H14z" fill="#37214e" stroke="#ba8be9" stroke-width="2"/><path d="M39 5v14h13M23 29h20M23 38h20M23 47h14" fill="none" stroke="#d9c0f4" stroke-width="3"/>',
'desktop':'<g fill="url(#g)"><rect x="9" y="9" width="19" height="19" rx="3"/><rect x="36" y="9" width="19" height="19" rx="3"/><rect x="9" y="36" width="19" height="19" rx="3"/><rect x="36" y="36" width="19" height="19" rx="3"/></g>'}
for name,path in paths.items():
    (assets/(name+'.svg')).write_text('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64"><defs><linearGradient id="g" x2="0.8" y2="1"><stop stop-color="#d0a4ff"/><stop offset="1" stop-color="#7931d4"/></linearGradient></defs>'+path+'</svg>',encoding='utf-8')
index=(S/'index.html').read_text(encoding='utf-8')
index=index.replace('</head>','<link rel="stylesheet" href="desktop.css?v=vigia-os-1"></head>')
index=index.replace('<script src="feedback.js','<script src="desktop.js?v=vigia-os-1"></script><script src="feedback.js')
index=index.replace('20261119-bonus-breve','20261119-vigia-os-1')
index=index.replace('<title>VIGIA/3 · Arquivo do incidente</title>','<title>VIGIA OS · O Arquivo Corrompido</title>')
index=index.replace('placeholder="Informe sua conclusão"','placeholder="Nome Sobrenome"')
index=index.replace('name="fisico" autocomplete','name="fisico" placeholder="Nome Sobrenome" autocomplete').replace('name="digital" autocomplete','name="digital" placeholder="Nome Sobrenome" autocomplete')
index=index.replace('Janela de análise: 12:30. Comece pelo Log L1 e pelo arquivo estudantil.','Os dados deste computador serão apagados em 12:30. Separem papel e caneta. Cada etapa validada recupera arquivos e pode adiar o apagamento.')
index=index.replace('Iniciar análise<i','Iniciar investigação<i')
index=index.replace('A ordem segue da esquerda para a direita, linha por linha.','As posições seguem de cima para baixo.').replace('A ordem segue da esquerda para a direita, linha por linha.','As posições seguem de cima para baixo.')
index=index.replace('<p>Prefere clicar?','<p>Alternativa por teclado ou clique:')
(S/'index.html').write_text(index,encoding='utf-8')

app=(S/'app.js').read_text(encoding='utf-8')
def section(start,end,new):
    global app
    a=app.index(start);b=app.index(end,a)
    app=app[:a]+new+app[b:]
section(' function renderFiles(){',' function renderAudio(){',""" function renderFiles(){
  VigiaDesktop.catalog(E.estado(),available(),filter,$('#search').value,openDoc,titles,group);
 }
""")
section(' function renderAudio(){',' function render(){',""" function renderAudio(){VigiaDesktop.media(E.estado(),play,transcribe)}
""")
app=app.replace("if(!['files','solve','timeline','media','vigia','reconstruction','recovery'].includes(id))return;","if(!['desktop','files','solve','timeline','media','vigia','reconstruction','recovery'].includes(id))return;")
app=app.replace("closePublicDialogs();document.querySelectorAll('.pane')", "if(['recovery','reconstruction'].includes(id))closePublicDialogs();else if($('#textdialog').open)$('#textdialog').close();document.querySelectorAll('.pane')")
app=app.replace("document.body.dataset.view=id;renderAiPresence();", "document.body.dataset.view=id;VigiaDesktop.open(id);renderAiPresence();")
section(' function focusAnswerField(){',' function updateAnalysisClock(){',""" function focusAnswerField(){
  if(document.body.dataset.view!=='solve'||document.querySelector('dialog:modal'))return;
  const input=[...$('#solve').querySelectorAll('input')].find(el=>el.getClientRects().length&&!el.disabled);
  const target=input||$('#sequence-ready:not([hidden]) button')||$('#open-ending');
  if(target?.getClientRects().length){target.focus({preventScroll:true});target.scrollIntoView({block:'center',behavior:'instant'})}
 }
""")
app=app.replace("return left}\n function formatTime", "VigiaDesktop.deadline(left,{started,contained:E.estado().protocolConfirmed,paused:!running,demo,overtime:overtimeAllowed});return left}\n function formatTime")
# The source may use CRLF; normalize the hook independently.
if 'VigiaDesktop.deadline(left' not in app:
    app=app.replace("return left}","VigiaDesktop.deadline(left,{started,contained:E.estado().protocolConfirmed,paused:!running,demo,overtime:overtimeAllowed});return left}",1)
app=app.replace("function maySubmit(){if(timeExpired)","function maySubmit(){const now=Date.now();if(running)elapsed+=(now-last)/1000;last=now;if(timeExpired)")
app=app.replace("let title,copy,label;", "VigiaDesktop.sync(s,{started,expired:timeExpired});let title,copy,label;")
app=app.replace("if(!$('#viewer').open)$('#viewer').showModal();", "if(!$('#viewer').open)$('#viewer').show();VigiaDesktop.reader();")
app=app.replace("function openDoc(id){if(!started)return;", "function openDoc(id){if(!started||timeExpired||E.estado().protocolConfirmed)return;")
app=app.replace("function transcribe(id){if(id==='audio03'", "function transcribe(id){if(!started||timeExpired||E.estado().protocolConfirmed||id==='audio02'&&!E.estado().identityConfirmed)return;if(id==='audio03'")
app=app.replace("function play(id){const s=E.estado();", "function play(id){if(!started||timeExpired||E.estado().protocolConfirmed)return;const s=E.estado();")
app=app.replace("currentAudio=id;player.pause();", "currentAudio=id;VigiaDesktop.audioCurrent(id,audioNames[id]);player.pause();")
app=app.replace("document.querySelector('dialog[open]')", "document.querySelector('dialog:modal')")
app=app.replace("$('#ai-reminder').hidden=sharedHidden||view==='vigia'||E.estado().protocolConfirmed;", "$('#ai-reminder').hidden=sharedHidden||view==='vigia'||E.estado().protocolConfirmed;VigiaDesktop.visibility(sharedHidden,E.estado().protocolConfirmed);")
app=app.replace("if(!started||E.estado().protocolConfirmed||document.querySelector('dialog:modal'))return;aiReminderIndex++", "if(!started||E.estado().protocolConfirmed||document.querySelector('dialog:modal')||['INPUT','TEXTAREA'].includes(document.activeElement.tagName))return;aiReminderIndex++")
app=app.replace("tab('files');play('audio01')", "tab('desktop');VigiaDesktop.welcome();play('audio01')")
app=app.replace("const autoScroll=()=>{if(lastY>window.innerHeight-75)window.scrollBy(0,10);else if(lastY<155)window.scrollBy(0,-10);", "const autoScroll=()=>{const host=$('#window-body'),rect=host.getBoundingClientRect();if(lastY>rect.bottom-60)host.scrollTop+=10;else if(lastY<rect.top+60)host.scrollTop-=10;")
app=app.replace("A ordem segue da esquerda para a direita, linha por linha.","As posições seguem de cima para baixo.")
app=app.replace("storage.clear();tab('files',false);cards();render();$('#intro').showModal();", "window.VigiaSession={open:tab,doc:openDoc,play,transcribe,help:openAssistant,state:()=>E.estado(),filter(value){filter=value;document.querySelectorAll('[data-filter]').forEach(b=>b.setAttribute('aria-pressed',String(b.dataset.filter===value)));renderFiles()}};\n storage.clear();tab('desktop',false);cards();render();$('#intro').showModal();")
app=app.replace("storage.clear();notice('Sessão aguardando autorização.');cards();render();tab('files',false)","storage.clear();VigiaDesktop.reset();notice('Sessão aguardando autorização.');cards();render();tab('desktop',false)")
app=app.replace("if(focus){if(id==='solve'", "if(focus){if(id==='desktop')VigiaDesktop.focusHome();else if(id==='solve'")
(S/'app.js').write_text(app,encoding='utf-8')
feedback=(S/'feedback.js').read_text(encoding='utf-8')
feedback=feedback.replace("function deadlineExpired(){stop();deadlineTone([[440,0,.32],[330,.38,.32],[220,.76,.65]])}","""function deadlineExpired(){
  stop();stopClock();if(!enabled)return;prime();
  try{if(!context)return;const buffer=context.createBuffer(1,Math.ceil(context.sampleRate*1.2),context.sampleRate),data=buffer.getChannelData(0);for(let i=0;i<data.length;i++)data[i]=(Math.random()*2-1)*.4;
   const source=context.createBufferSource(),gain=context.createGain(),filter=context.createBiquadFilter(),now=context.currentTime;source.buffer=buffer;filter.type='lowpass';filter.frequency.value=4200;gain.gain.setValueAtTime(.0001,now);gain.gain.linearRampToValueAtTime(.22,now+.06);gain.gain.exponentialRampToValueAtTime(.0001,now+1.2);source.connect(filter);filter.connect(gain);gain.connect(context.destination);source.start();active.push(source);source.onended=()=>{source.disconnect();filter.disconnect();gain.disconnect();active=active.filter(n=>n!==source)};
  }catch{}
 }""")
(S/'feedback.js').write_text(feedback,encoding='utf-8')
print('Desktop preparado; motor e conteúdo preservados.')
