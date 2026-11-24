(()=>{
 'use strict';
 const D=window.CASE_DATA,E=VigiaEngine.criarVigia(D.vigia,D.key,{stages:VigiaSettings.current().stages}),$=s=>document.querySelector(s),I=VigiaIcons;
 D.vigia.timed_hints.forEach(h=>{if(h.id==='tempo_operador')h.at_seconds=660});
 let running=false,started=false,demo=false,elapsed=0,last=Date.now(),order=D.cards.map(c=>c.id),hints={},wasRunning=false,resetArmed=false;
 const countdown=VigiaCountdown.create(VigiaSettings.current());
 const hintTimes=D.vigia.timed_hints.map(h=>h.at_seconds);
 document.addEventListener('vigia-settings-change',()=>{if(started)return;const settings=VigiaSettings.current();countdown.configure(settings);E.configurarEtapas(settings.stages);D.vigia.timed_hints.forEach((hint,i)=>{hint.at_seconds=Math.round(hintTimes[i]*settings.durationSeconds/750)});updateAnalysisClock();render()});
 let timeExpired=false,overtimeAllowed=false,bonusCloseTimer=null;
 let recoveryAuthorized=false;
 let codeAcknowledged=false,codeDeadline=0,codeInterval=null,codeSeconds=30;
 // A anotação pertence à mesma partida que as respostas; não restaurar recibos antigos.
 try{sessionStorage.removeItem('vigia-code-acknowledged')}catch{}
 let selectedCard=null,suppressMoveClickUntil=0;
 let aiLastIntent=null,aiLastQuestion="",aiReminderIndex=0,aiLastMemory=null,aiErrorFields=[],aiAnsweredLevel=null;
 let filter='all',currentDoc=null,fitScale=1,zoom=100,currentAudio=null,nextAction=()=>openDoc('L1');
 const storage={set(value){try{sessionStorage.setItem('vigia-reconstruction',value)}catch{}},clear(){try{sessionStorage.removeItem('vigia-reconstruction')}catch{}}};
 const player=$('#audio-player'),endingPlayer=$('#ending-audio');
 const texts=Object.fromEntries(window.VIGIA_AUDIO.map(s=>[s.id,s.texto]));
 const audioNames={audio01:'Fragmento 01 · Inicialização',audio02:'Fragmento 02 · Acessos',audio03:'Fragmento 03 · Memória parcial do confronto'};
 const titles={F1_ID:'Identificação da equipe',F1:'Arquivo visual da equipe',A17:'Arquivo estudantil A-17',L1:'Log L1 · Sessão recuperada',N1:'Proposta NORTHSTAR',V17:'Manifesto V-17',C1:'Catraca lateral',H1:'Conversa recuperada H1',R1:'Histórico de acessos',R2:'Mensagem familiar',AL:'Relatório de presença',APOIO_01_pessoas_registros:'Cadastro de funcionários · 01',APOIO_02_pessoas_registros:'Cadastro de funcionários · 02',APOIO_03_pessoas_registros:'Registros complementares',NF318:'Nota fiscal 318',NF318B:'Nota fiscal 318B',NF427:'Nota fiscal 427',NF427B:'Nota fiscal 427B',NF512:'Nota fiscal 512',NF512B:'Nota fiscal 512B',FIN02:'Conferência financeira',M1:'Conversa recuperada M1',RVM:'Auditoria RV-MANUT',CAM01:'Integridade da mídia · CAM01',T3:'Extrato de ocorrências'};
 const group=e=>['F1','F1_ID','A17'].includes(e.id)||e.id.startsWith('APOIO_0')?'identity':['C1','H1','R1','R2','AL','M1','RVM'].includes(e.id)?'access':e.id.startsWith('NF')||e.id==='FIN02'?'finance':'records';
 const categoryNames={identity:'IDENTIDADE',access:'ACESSOS',finance:'FINANCEIRO',records:'REGISTRO'};
 const iconFor=e=>e.id==='CAM01'?'camera':['H1','M1','R2'].includes(e.id)?'link':group(e)==='identity'?'user':group(e)==='access'?'key':'file';
 const available=()=>{const s=E.estado();return D.evidence.filter(e=>e.stage===0||(e.stage===1&&s.identityConfirmed)||(e.stage===2&&s.accessesConfirmed)||(e.stage===3&&s.chronologyOrdered))};
 function notice(text,kind=''){$('#notice-text').textContent=text;$('#notice').className='notice'+(kind?' is-'+kind:'')}
 function closePublicDialogs(){for(const id of ['viewer','textdialog','reconstruction'])if($('#'+id).open)$('#'+id).close()}
 function tab(id,focus=true,answerField=true){
  if(timeExpired||$('#code-popup').open||VigiaIntroVideo.active)return;
  if(E.estado().protocolConfirmed&&!codeAcknowledged){showCodeOnce();return}
  if(E.estado().protocolConfirmed&&codeAcknowledged&&!recoveryAuthorized)id='recovery';
  const chronology=id==='timeline'&&VigiaSettings.current().stages.includes('chronology');if(id==='timeline')id='solve';
  if(!['desktop','files','solve','media','vigia','notes','trash','introvideo','recovery','reconstruction'].includes(id))return;
  if(id==='reconstruction'&&(!E.estado().protocolConfirmed||!recoveryAuthorized))return;
  if(id==='recovery'&&(!E.estado().protocolConfirmed||!codeAcknowledged))return;
  if(id!=='reconstruction')endingPlayer.pause();
  if(['recovery','reconstruction','desktop'].includes(id)||$('#viewer').open&&!(id==='vigia'&&innerWidth>=1500))closePublicDialogs();
  else if($('#textdialog').open)$('#textdialog').close();
  $('#recovery').hidden=id!=='recovery';$('#reconstruction').hidden=id!=='reconstruction';
  document.body.dataset.view=id;VigiaDesktop.open(id);renderAiPresence();if(id==='introvideo'){player.pause();VigiaIntroVideo.replay()}
  if(id==='reconstruction')$('#reconstruction').showModal();
  if(id==='vigia'&&aiLastQuestion&&aiAnsweredLevel!==E.perfilIA().level)query(aiLastQuestion,{refresh:true});
  document.querySelector('.reader-menu').open=false;
  if(focus){
   if(id==='desktop')VigiaDesktop.focusHome();
   else if(id==='solve'&&chronology){requestAnimationFrame(()=>{const host=VigiaDesktop.body('solve');host.scrollTop+=Math.max(0,$('#timeline').getBoundingClientRect().top-host.getBoundingClientRect().top-16)})}
   else if(id==='solve'&&answerField)requestAnimationFrame(focusAnswerField);
   else if(['files','solve','media','vigia','notes','trash','introvideo'].includes(id))VigiaDesktop.body(id).focus({preventScroll:true});
   if(id==='recovery')$('#recovery-code').focus({preventScroll:true});
   if(id==='reconstruction')$('#reconstruction-title').focus({preventScroll:true});
  }
  try{history.replaceState(null,'','#'+id)}catch{}
 }
 function focusAnswerField(){
  if(document.body.dataset.view!=='solve'||document.querySelector('dialog:modal'))return;
  const input=[...$('#solve').querySelectorAll('input')].find(el=>el.getClientRects().length&&!el.disabled);
  const target=input||$('#sequence-ready:not([hidden]) button')||$('#open-ending');
  if(target?.getClientRects().length){target.focus({preventScroll:true});const host=VigiaDesktop.body('solve');host.scrollTop+=target.getBoundingClientRect().top-host.getBoundingClientRect().top-host.clientHeight/2+target.offsetHeight/2}
 }
 function updateAnalysisClock(){const left=countdown.remaining(elapsed);$('#timer').textContent=formatTime(left);$('.clock').classList.toggle('is-alert',left<=60&&started&&!E.estado().protocolConfirmed&&!overtimeAllowed);VigiaDesktop.deadline(left,{started,contained:E.estado().protocolConfirmed,paused:!running,demo,overtime:overtimeAllowed});return left}
 function formatTime(seconds){return String(Math.floor(seconds/60)).padStart(2,'0')+':'+String(seconds%60).padStart(2,'0')}
 function closeTimeBonus(){clearInterval(bonusCloseTimer);bonusCloseTimer=null;$('#time-bonus').hidden=true}
 function awardTimeBonus(stage){
  if(demo||overtimeAllowed||timeExpired||!VigiaSettings.current().stages.includes(stage))return;const award=countdown.award(stage,elapsed);if(!award)return;
  closeTimeBonus();updateAnalysisClock();$('#time-bonus-stage').textContent={identity:'IDENTIDADE CONFIRMADA',access:'ACESSOS CONFIRMADOS',chronology:'CRONOLOGIA CONFIRMADA'}[stage];
  $('#time-bonus .bonus-brief-row>strong').innerHTML='+'+award.added+'<span>s</span>';
  $('#time-bonus-copy').textContent=award.added+' segundos foram somados. Tempo restante: '+formatTime(award.remaining)+'.';
  $('#time-bonus-countdown').textContent='2s';$('#time-bonus-progress').style.transform='scaleX(1)';$('#time-bonus').hidden=false;
  const deadline=performance.now()+2000;
  bonusCloseTimer=setInterval(()=>{const left=Math.max(0,deadline-performance.now());$('#time-bonus-countdown').textContent=Math.ceil(left/1000)+'s';$('#time-bonus-progress').style.transform='scaleX('+(left/2000)+')';if(left===0)closeTimeBonus()},100);
  requestAnimationFrame(focusAnswerField);
 }
 function expireAnalysis(){
  if(timeExpired||overtimeAllowed||demo||E.estado().protocolConfirmed)return;
  VigiaIntroVideo.stopReplay();timeExpired=true;running=false;wasRunning=false;closeTimeBonus();player.pause();$('#player-dock').hidden=true;VigiaFeedback.stopClock();
  closePublicDialogs();if($('#operator-auth').open)$('#operator-auth').close();
  $('#timeup-memory').textContent=String(E.estado().memory).padStart(2,'0')+'%';updateAnalysisClock();renderAiPresence();
  $('#time-up').hidden=false;$('#timeup-title').focus();VigiaAmbient.duckFor(5500);VigiaFeedback.deadlineExpired();notice('TEMPO ESGOTADO · Transmissão interrompida.');
 }
 window.addEventListener('keydown',e=>{if(!timeExpired||$('#op').open||$('#operator-auth').open)return;if(e.ctrlKey&&e.shiftKey&&e.code==='KeyO')return;e.preventDefault();e.stopImmediatePropagation()},true);
 function maySubmit(){const now=Date.now();if(running)elapsed+=(now-last)/1000;last=now;if(timeExpired)return false;if(started&&!demo&&!overtimeAllowed&&countdown.remaining(elapsed)===0){expireAnalysis();return false}return started}
 $('#reconstruction').addEventListener('cancel',e=>{e.preventDefault();tab('solve')});
 function stage(){const s=E.estado();return s.chronologyOrdered?'horario':s.accessesConfirmed?'cronologia':s.identityConfirmed?'acessos':'identidade'}
 function renderFiles(){
  VigiaDesktop.catalog(E.estado(),available(),filter,$('#search').value,openDoc,titles,group);
 }
 function renderAudio(){VigiaDesktop.media(E.estado(),play,transcribe);let note=$('#adapted-audio-note');if(!note){note=document.createElement('p');note.id='adapted-audio-note';note.className='section-copy';$('#audios').before(note)}note.hidden=!E.estado().skippedStages.length;note.textContent='As gravações originais podem citar etapas fora desta rodada. Consulte Próximos passos.txt ou a VIG.IA para saber o que responder agora.'}
 function render(){const s=E.estado();$('#bar').style.width=s.memory+'%';$('#memory').textContent='MEMÓRIA · '+String(s.memory).padStart(2,'0')+'%';
  $('#identity').hidden=s.identityConfirmed;$('#access').hidden=!s.identityConfirmed||s.accessesConfirmed;$('#sequence-ready').hidden=!s.accessesConfirmed||s.chronologyOrdered;$('#fragment').hidden=!s.chronologyOrdered||s.fragment03Consulted||s.protocolConfirmed;$('#protocol').hidden=!s.chronologyOrdered||s.protocolConfirmed;$('#ending').hidden=!s.protocolConfirmed;if(!$('#code-popup').open)$('#code').textContent='';
  $('#timeline').hidden=!s.accessesConfirmed||s.chronologyOrdered;$('#timeline-lock').hidden=s.accessesConfirmed;$('#timeline-locked').hidden=s.accessesConfirmed;$('#timeline-work').hidden=!s.accessesConfirmed||s.chronologyOrdered;$('#timeline-done').hidden=!s.chronologyOrdered;
  $('#solve-status').textContent=s.protocolConfirmed?'CÓDIGO GERADO':s.chronologyOrdered?'CONCLUSÕES PENDENTES':s.accessesConfirmed?'SEQUÊNCIA PENDENTE':s.identityConfirmed?'ACESSOS PENDENTES':'IDENTIDADE PENDENTE';
  if(s.skippedStages.length&&!s.protocolConfirmed){const selected=VigiaEngine.stages.filter(stage=>s.enabledStages.includes(stage.id));$('#solve-status').textContent+=' · '+(selected.findIndex(stage=>!s[stage.flag])+1)+' DE '+selected.length}
  $('#ending>.eyebrow').textContent=s.skippedStages.includes('protocol')?'ETAPAS DA RODADA CONCLUÍDAS':'CONCLUSÕES CONFIRMADAS';
  [['identity',s.identityConfirmed,!s.identityConfirmed],['access',s.accessesConfirmed,s.identityConfirmed&&!s.accessesConfirmed],['time',s.chronologyOrdered,s.accessesConfirmed&&!s.chronologyOrdered],['protocol',s.protocolConfirmed,s.chronologyOrdered&&!s.protocolConfirmed]].forEach(([id,done,active])=>{const step=$('#step-'+id);step.hidden=!s.enabledStages.includes(id==='time'?'chronology':id);step.className=done?'is-done':active?'is-current':''});
  $('#sequence-ready h3').textContent=s.skippedStages.includes('access')?'Próxima etapa: cronologia':'Acessos correlacionados';
  document.querySelectorAll('[data-tab="timeline"]').forEach(button=>button.hidden=!s.enabledStages.includes('chronology'));
  VigiaDesktop.sync(s,{started,expired:timeExpired});let title,copy,label;
  if(s.protocolConfirmed){title=recoveryAuthorized?'Arquivo recuperado':'Inserir o código';copy=recoveryAuthorized?'A reconstituição está disponível.':'Use a anotação no papel para liberar o arquivo.';label=recoveryAuthorized?'Rever reconstituição':'Inserir código';nextAction=recoveryAuthorized?openEnding:()=>tab('recovery');$('#open-ending').textContent=label}
  else if(s.chronologyOrdered){title='Registrar as conclusões';copy='Informe o invasor, a credencial de entrada e o minuto do confronto fatal.';label='Gerar código';nextAction=()=>tab('solve')}
  
  else if(s.accessesConfirmed){title='Reconstruir a sequência';copy='Ordene os seis registros na cronologia do incidente.';label='Abrir cronologia';nextAction=()=>tab('timeline')}
  else if(s.identityConfirmed){title='Distinguir os dois acessos';copy='Uma credencial física e uma conta digital. Consulte os registros recuperados.';label='Correlacionar acessos';nextAction=()=>tab('solve')}
  else{title='Identificar o perfil legado';copy='Compare o Log L1 com o arquivo estudantil.';label=s.evidenceSeen.includes('A17')?'Abrir respostas':s.evidenceSeen.includes('L1')?'Abrir arquivo estudantil':'Consultar Log L1';nextAction=()=>s.evidenceSeen.includes('A17')?tab('solve'):openDoc(s.evidenceSeen.includes('L1')?'A17':'L1')}
  $('#next-title').textContent=title;$('#next-copy').textContent=copy;$('#next-label').textContent=label;renderFiles();renderAudio();renderAssistant();
  document.querySelectorAll('.answer-bubble small').forEach(el=>el.textContent=s.protocolConfirmed?'Consultar conclusões registradas':s.chronologyOrdered?'Concluir invasor, credencial e confronto':s.identityConfirmed?'Registrar suas próximas conclusões':'Informe a identidade do perfil legado');
 }
 function result(r,form=null){aiErrorFields=r.ok?[]:(r.fields||[]).map(f=>f.field);VigiaFeedback.apply(r,form);notice(r.message+(r.offerHint?' Solicite apoio de correlação na VIG.IA.':''),r.ok?'success':'error');render();showEvidenceHelp(r,form);if(r.ok){awardTimeBonus(form?.id==='identity'?'identity':form?.id==='accessform'?'access':!form?'chronology':null);if(E.estado().protocolConfirmed){running=false;closeTimeBonus();player.pause();$('#player-dock').hidden=true;showCodeOnce()}}return r.ok}
 function showEvidenceHelp(r,form){
  const host=form||$('#timeline-work');host.querySelector('.correlation-help')?.remove();if(r.ok)return;
  const s=E.estado(),fields=(r.fields||[]).map(f=>f.field);let suggestions=[];
  const identity=()=>suggestions.push(['A17','Confira o nome e a assinatura no arquivo estudantil.'],['L1','Compare a assinatura do acesso com a do arquivo estudantil.']);
  if(form?.id==='identity'||!s.identityConfirmed)identity();
  else if(form?.id==='accessform'||!s.accessesConfirmed){
   if(!fields.length||fields.includes('fisico'))suggestions.push(['H1','Leia a conversa para identificar quem cedeu a credencial física.'],['C1','Confira a credencial utilizada na entrada.']);
   if(!fields.length||fields.includes('digital'))suggestions.push(['RVM','Confira quem criou a conta de acesso ao repositório.'],['M1','Leia a instrução e a resposta na conversa sobre a conta.']);
  }else if(form?.id==='finalform'){
   if(fields.includes('identidade'))identity();
   if(fields.includes('credencial'))suggestions.push(['C1','Confira o número da credencial no registro da catraca.']);
   if(fields.includes('horario'))suggestions.push(['T3','Procure a linha do confronto na sala técnica. Use o minuto dessa ocorrência; a cópia termina em outro horário.'],['CAM01','Conferência adicional: o trecho S-02 começa às 22:44 e dura 152 segundos. Cabeçalhos sem imagem não contam.'],['audio03','O relato cita o minuto do confronto. Compare com a linha correspondente no extrato.']);
  }else suggestions.push(['C1','Confira o horário da entrada e compare com os cartões.'],['T3','Compare entrada, sessão, alerta, chegada à sala e confronto. As linhas foram extraídas fora da ordem; reorganize pelos horários.'],['L1','Confira o horário em que a sessão foi iniciada.'],['APOIO_03_pessoas_registros','Localize o alerta e os registros de presença para comparar a sequência.']);
  const allowed=new Set(available().map(e=>e.id));suggestions=suggestions.filter(([id])=>allowed.has(id)||(id==='audio03'&&s.chronologyOrdered));
  if(!suggestions.length)return;
  const box=document.createElement('aside');box.className='correlation-help';box.setAttribute('aria-label','Documentos para revisar a resposta');
  const heading=document.createElement('strong');heading.textContent='Onde conferir sua resposta';box.append(heading);
  for(const [id,reason] of suggestions){const row=document.createElement('div'),p=document.createElement('p'),button=document.createElement('button');p.textContent=reason;button.type='button';button.textContent='Abrir '+(id==='audio03'?'transcrição do Fragmento 03':titles[id]);button.onclick=()=>id==='audio03'?transcribe(id):openDoc(id);row.append(p,button);box.append(row)}
  const ask=document.createElement("button");ask.type="button";ask.className="ai-error-help";ask.textContent="Pedir ajuda à IA sobre este erro";ask.onclick=()=>openAssistant("Minha resposta deu erro");box.append(ask);
  host.append(box);
 }
 function moveCard(id,index){
  const previous=order.indexOf(id);if(previous<0)return;
  const next=order.filter(x=>x!==id);next.splice(Math.max(0,Math.min(next.length,index)),0,id);order=next;selectedCard=null;
  $('#timeline-work').classList.remove('has-sequence-error');$('#timeline-work .correlation-help')?.remove();cards();announceOrder(id);
  $('#timeline-move-status').textContent='Posição '+(order.indexOf(id)+1)+': '+D.cards.find(c=>c.id===id).title+'. Confira a ordem e clique em Validar sequência.';notice('Sequência alterada. Confira os registros e clique em Validar sequência.');
  $(`#cards li[data-event="${id}"] .drag-handle`).focus({preventScroll:true});
 }
 function selectMove(id){
  if(performance.now()<suppressMoveClickUntil)return;
  if(selectedCard&&selectedCard!==id){moveCard(selectedCard,order.indexOf(id));return}
  selectedCard=selectedCard===id?null:id;cards();
  $('#timeline-move-status').textContent=selectedCard?'Agora clique em Colocar aqui na posição desejada. Esc cancela.':'Escolha um cartão para mover. As posições seguem de cima para baixo.';
  $(`#cards li[data-event="${id}"] .drag-handle`).focus({preventScroll:true});
 }
 function cards(focusId,delta){const list=$('#cards');list.replaceChildren();order.forEach((id,i)=>{
  const c=D.cards.find(c=>c.id===id),li=document.createElement('li');li.dataset.event=id;
  li.innerHTML='<div class="event-top"><span class="card-number"></span><span class="event-time"></span><button class="drag-handle" type="button" title="Segure e arraste para reordenar"><span aria-hidden="true">⠿</span></button></div><div class="event-main"><h3></h3><p></p></div><div class="event-controls"></div>';
  li.querySelector('.card-number').textContent='Posição '+(i+1);li.querySelector('.event-time').textContent=c.time_label;
  li.classList.toggle('time-corrupted',c.time_label==='CORROMPIDO');li.querySelector('h3').textContent=c.title;li.querySelector('p').textContent=c.description;
  const handle=li.querySelector('.drag-handle');handle.textContent=selectedCard===id?'Cancelar':selectedCard?'Colocar aqui':'⠿ Mover';handle.setAttribute('aria-label',selectedCard===id?'Cancelar movimento de '+c.title:selectedCard?'Colocar na posição '+(i+1):'Mover: '+c.title);handle.setAttribute('aria-pressed',String(selectedCard===id));handle.onclick=()=>selectMove(id);li.classList.toggle('is-selected',selectedCard===id);li.classList.toggle('is-destination',!!selectedCard&&selectedCard!==id);
  [-1,1].forEach(d=>{const b=document.createElement('button');b.type='button';b.innerHTML=I.svg(d<0?'up':'down')+(d<0?'Antes':'Depois');b.setAttribute('aria-label',(d<0?'Mover uma posição antes: ':'Mover uma posição depois: ')+c.title);b.dataset.card=id;b.dataset.delta=d;b.disabled=i+d<0||i+d>=order.length;b.onclick=()=>moveCard(id,i+d);li.querySelector('.event-controls').append(b)});
  li.addEventListener('pointerdown',e=>beginDrag(e,li,id));
  list.append(li)
 });
 if(focusId){const b=$(`#cards button[data-card="${focusId}"][data-delta="${delta}"]`);if(b&&!b.disabled)b.focus();else $(`#cards button[data-card="${focusId}"]:not(:disabled)`)?.focus()}
 }
 function announceOrder(id){$('#drag-announcement').textContent=D.cards.find(c=>c.id===id).title+' na posição '+(order.indexOf(id)+1)+' de 6.'}
 function beginDrag(event,li,id){
  if(event.button!==0||event.target.closest('.event-controls')||E.estado().chronologyOrdered)return;
  if(event.pointerType==='touch'&&!event.target.closest('.drag-handle'))return;
  const startX=event.clientX,startY=event.clientY;let dragging=false,targetId=null,ghost=null,scrollFrame=null,lastY=startY;
  const clearTarget=()=>document.querySelectorAll('#cards .drop-target').forEach(el=>{el.classList.remove('drop-target');el.removeAttribute('data-drop-label')});
  const autoScroll=()=>{const host=VigiaDesktop.body('solve'),rect=host.getBoundingClientRect();if(lastY>rect.bottom-60)host.scrollTop+=10;else if(lastY<rect.top+60)host.scrollTop-=10;scrollFrame=requestAnimationFrame(autoScroll)};
  const move=e=>{
   if(e.pointerId!==event.pointerId)return;
   if(!dragging&&Math.hypot(e.clientX-startX,e.clientY-startY)<8)return;
   if(!dragging){dragging=true;li.setPointerCapture(event.pointerId);selectedCard=null;li.classList.add('is-dragging');document.body.classList.add('is-reordering');ghost=document.createElement('div');ghost.className='drag-preview';ghost.setAttribute('aria-hidden','true');ghost.textContent=D.cards.find(c=>c.id===id).title;document.body.append(ghost);scrollFrame=requestAnimationFrame(autoScroll)}
   lastY=e.clientY;ghost.style.left=Math.max(8,Math.min(window.innerWidth-240,e.clientX+16))+'px';ghost.style.top=Math.max(8,Math.min(window.innerHeight-70,e.clientY+14))+'px';clearTarget();targetId=null;
   const target=document.elementFromPoint(e.clientX,e.clientY)?.closest('#cards li');
   if(target&&target!==li){targetId=target.dataset.event;const position=order.indexOf(targetId)+1;target.classList.add('drop-target');target.dataset.dropLabel='Solte na posição '+position;$('#timeline-move-status').textContent='Solte para colocar o cartão na posição '+position+'. Os demais cartões serão reorganizados.'}
   else $('#timeline-move-status').textContent='Arraste sobre outra posição. Soltar fora dos cartões cancela o movimento.';
  };
  const finish=e=>{
   if(e.pointerId!==undefined&&e.pointerId!==event.pointerId)return;
   document.removeEventListener('pointermove',move);document.removeEventListener('pointerup',finish);document.removeEventListener('pointercancel',cancel);li.removeEventListener('lostpointercapture',cancel);document.removeEventListener('keydown',escape);clearTarget();li.classList.remove('is-dragging');document.body.classList.remove('is-reordering');ghost?.remove();cancelAnimationFrame(scrollFrame);
   if(li.hasPointerCapture(event.pointerId))li.releasePointerCapture(event.pointerId);
   if(dragging){suppressMoveClickUntil=performance.now()+350;if(targetId&&e.type!=='pointercancel')moveCard(id,order.indexOf(targetId));else{cards();$('#timeline-move-status').textContent='Movimento cancelado. A ordem foi mantida.'}}
  };
  const cancel=e=>{targetId=null;finish(e)};
  const escape=e=>{if(e.key==='Escape'){e.preventDefault();e.stopPropagation();cancel(e)}};
  document.addEventListener('keydown',escape);document.addEventListener('pointermove',move);document.addEventListener('pointerup',finish);document.addEventListener('pointercancel',cancel);li.addEventListener('lostpointercapture',cancel);
 }
 document.addEventListener('keydown',e=>{if(e.key==='Escape'&&selectedCard){selectedCard=null;cards();$('#timeline-move-status').textContent='Movimento cancelado. A ordem foi mantida.'}});
 function fitDocument(){if(!$('#docimage').naturalWidth||!$('#viewer').open)return;const box=$('#docviewport');fitScale=Math.max(.03,Math.min((box.clientWidth-70)/$('#docimage').naturalWidth,(box.clientHeight-120)/$('#docimage').naturalHeight,1)*.94);setZoom(100,false)}
 function setZoom(value,preserve=true){const v=$('#docviewport'),old=$('#scan-paper').getBoundingClientRect();const cx=(v.scrollLeft+v.clientWidth/2)/Math.max(old.width+56,v.clientWidth),cy=(v.scrollTop+v.clientHeight/2)/Math.max(old.height+56,v.clientHeight);
  zoom=Math.max(40,Math.min(250,Math.round(value/5)*5));const w=$('#docimage').naturalWidth*fitScale*zoom/100,h=$('#docimage').naturalHeight*fitScale*zoom/100;$('#scan-paper').style.width=w+'px';$('#scan-paper').style.height=h+'px';$('#zoom-range').value=zoom;$('#zoom-value').textContent=zoom+'%';$('#zoom-out').disabled=zoom<=40;$('#zoom-in').disabled=zoom>=250;
  requestAnimationFrame(()=>{v.scrollLeft=preserve?cx*Math.max(w+56,v.clientWidth)-v.clientWidth/2:0;v.scrollTop=preserve?cy*Math.max(h+56,v.clientHeight)-v.clientHeight/2:0})
 }
 function openDoc(id){if(!started||timeExpired||E.estado().protocolConfirmed)return;const list=available(),e=list.find(x=>x.id===id);if(!e){notice('REGISTRO BLOQUEADO · Confirme as correlações anteriores.');return}if($('#textdialog').open)$('#textdialog').close();currentDoc=id;const index=list.findIndex(x=>x.id===id);$('#docname').textContent=titles[id]||e.title;$('#doc-id').textContent='EVIDÊNCIA / '+(id.startsWith('APOIO')?'CADASTRO':id);$('#doc-position').textContent=(index+1)+' / '+list.length;$('#doc-prev').disabled=index===0;$('#doc-next').disabled=index===list.length-1;$('#doc-error').hidden=true;$('#doccanvas').hidden=false;$('#scan-paper').classList.toggle('is-photo',id==='F1');$('#scan-paper').style.width='0px';$('#scan-paper').style.height='0px';
  $('#docviewport').setAttribute('aria-busy','true');$('#docimage').onload=()=>{if(currentDoc!==id)return;$('#docviewport').setAttribute('aria-busy','false');E.marcarEvidencia(id);render();requestAnimationFrame(fitDocument)};$('#docimage').onerror=()=>{$('#docviewport').setAttribute('aria-busy','false');$('#doccanvas').hidden=true;$('#doc-error').hidden=false;notice('Registro visual indisponível. Solicite verificação à equipe.','error')};$('#docimage').alt=titles[id]||e.title;$('#docimage').src=e.file;if(!$('#viewer').open)$('#viewer').show();VigiaDesktop.reader();$('#zoom-fit').focus();if($('#docimage').complete&&$('#docimage').naturalWidth)requestAnimationFrame(fitDocument)
 }
 function transcribe(id){if(!started||timeExpired||E.estado().protocolConfirmed||id==='audio02'&&!E.estado().identityConfirmed)return;if(id==='audio03'&&!E.estado().chronologyOrdered)return;closePublicDialogs();if(id==='audio03'){E.consultarFragmento03();notice('FRAGMENTO CONSULTADO · Compare a câmera e registre suas respostas.')}$('#texttitle').textContent=audioNames[id];$('#textbody').textContent=texts[id];$('#textdialog').showModal();render()}
 function play(id){if(!started||timeExpired||E.estado().protocolConfirmed)return;const s=E.estado();if((id==='audio02'&&!s.identityConfirmed)||(id==='audio03'&&!s.chronologyOrdered))return;currentAudio=id;VigiaDesktop.audioCurrent(id,audioNames[id]);player.pause();player.src='audio/'+id+'.wav';$('#player-label').textContent=audioNames[id];$('#player-dock').hidden=false;player.play().catch(error=>{if(error.name!=='AbortError'&&currentAudio===id)notice('Áudio indisponível. Consulte a transcrição do registro.','error')})}
 player.addEventListener('play',()=>{if(currentAudio==='audio03'){E.consultarFragmento03();render()}});player.addEventListener('error',()=>{if(currentAudio)notice('Falha na leitura do áudio. A transcrição permanece disponível.','error')});
 $('#close-player').onclick=()=>{player.pause();$('#player-dock').hidden=true};$('#player-transcript').onclick=()=>currentAudio&&transcribe(currentAudio);
 document.querySelectorAll('[data-tab]').forEach(b=>b.onclick=()=>{if(started)tab(b.dataset.tab,true,!b.closest('.main-nav'))});document.querySelectorAll('[data-doc]').forEach(b=>b.onclick=()=>openDoc(b.dataset.doc));document.querySelectorAll('[data-filter]').forEach(b=>b.onclick=()=>{filter=b.dataset.filter;document.querySelectorAll('[data-filter]').forEach(x=>x.setAttribute('aria-pressed',String(x===b)));renderFiles()});$('#search').oninput=renderFiles;$('#next-action').onclick=()=>started&&nextAction();$('.brand').onclick=e=>{e.preventDefault();if(started)tab('files')};
 $('#identity').onsubmit=e=>{e.preventDefault();if(!maySubmit())return;if(result(E.validarIdentidade(new FormData(e.target).get('nome')),e.target)&&!E.estado().protocolConfirmed&&!E.estado().skippedStages.length&&VigiaSettings.current().stages.includes('access'))play('audio02')};$('#accessform').onsubmit=e=>{e.preventDefault();if(!maySubmit())return;if(result(E.validarAcessos(Object.fromEntries(new FormData(e.target))),e.target)&&!E.estado().protocolConfirmed)tab(E.estado().chronologyOrdered?'solve':'timeline')};$('#checkorder').onclick=()=>{if(!maySubmit())return;if(result(E.validarCronologia(order))&&!E.estado().protocolConfirmed){tab('solve');if(!E.estado().skippedStages.length)play('audio03')}};$('#listen3').onclick=()=>play('audio03');$('#transcript3').onclick=()=>transcribe('audio03');$('#finalform').onsubmit=e=>{e.preventDefault();if(!maySubmit())return;result(E.validarProtocolo(Object.fromEntries(new FormData(e.target))),e.target)};
 // Envio explícito também para formulários com vários campos e Enter numérico.
 for(const id of ['identity','accessform','finalform','recovery-form']){
  const form=$('#'+id);form.addEventListener('keydown',e=>{
   if(e.key!=='Enter'||e.isComposing||e.target.tagName!=='INPUT'||e.ctrlKey||e.altKey||e.metaKey)return;
   e.preventDefault();e.stopPropagation();if(e.repeat||document.querySelector('dialog:modal'))return;
   form.requestSubmit(form.querySelector('button[type="submit"]'));
  });
 }
 function renderAiPresence(){document.body.classList.toggle('investigation-expired',timeExpired);for(const id of ['os-desktop','os-window-layer','os-taskbar','workspace'])$('#'+id).inert=timeExpired;
  const view=document.body.dataset.view,sharedHidden=!started||timeExpired||view==='recovery'||view==='reconstruction'||E.estado().protocolConfirmed&&!recoveryAuthorized;
  $('#session-dock').hidden=sharedHidden;$('#ai-fab').hidden=sharedHidden;$('#answers-fab').hidden=sharedHidden;
  $('#ai-reminder').hidden=sharedHidden||view==='vigia'||E.estado().protocolConfirmed;VigiaDesktop.visibility(sharedHidden,E.estado().protocolConfirmed&&(!recoveryAuthorized||['recovery','reconstruction'].includes(view)));
 }
 function renderAssistant(){
  const p=E.perfilIA(),mem=String(p.memory).padStart(2,'0')+'%';
  if(aiLastMemory!==p.memory){aiReminderIndex=0;if(aiLastMemory!==null)$('#ai-response-status').textContent='Memória ampliada para '+mem+'. Novas relações disponíveis.';aiLastMemory=p.memory}
  $('#ai-nav-memory').textContent=mem;$('#ai-reminder-memory').textContent=mem;$('#ai-fab-memory').textContent=mem;
  $('#ai-memory-value').textContent=mem;$('#ai-memory-name').textContent=p.name;$('#ai-query-level').textContent=p.name.toUpperCase();
  $('#ai-memory-bar').style.width=p.memory+'%';$('.ai-memory-meter').setAttribute('aria-valuenow',String(p.memory));
  $('#ai-capabilities').textContent=p.can;$('#ai-next-memory').textContent=p.next;
  $('#ai-reminder-copy').textContent=p.reminders[aiReminderIndex%p.reminders.length];
  $('#ai-question').placeholder='Escreva uma mensagem… Ex.: '+p.examples[0];$('#ai-examples').replaceChildren();
  for(const example of p.examples){const button=document.createElement('button');button.type='button';button.textContent=example;button.onclick=()=>query(example);$('#ai-examples').append(button)}
  const state=E.estado(),selected=VigiaEngine.stages.filter(stage=>state.enabledStages.includes(stage.id)),memoryLevels=state.skippedStages.length?[{memory:8,name:'Início da rodada'},...selected.map((stage,i)=>({memory:Math.round(8+92*(i+1)/selected.length),name:stage.label}))]:VigiaAssistant.levels;
  $('#ai-memory-levels').replaceChildren();memoryLevels.forEach(item=>{const li=document.createElement('li'),percent=document.createElement('span'),name=document.createElement('span');percent.textContent=String(item.memory).padStart(2,'0')+'%';name.textContent=item.name;li.append(percent,name);li.className=item.memory<p.memory?'is-recovered':item.memory===p.memory?'is-current':'is-pending';if(item.memory===p.memory)li.setAttribute('aria-current','step');$('#ai-memory-levels').append(li)});
  if(!aiLastQuestion){$('#ai-reply-memory').textContent='MEMÓRIA · '+mem;$('#ai-reply-title').textContent=p.level?'Novas ligações estão disponíveis.':'Vamos encontrar a primeira pista.';$('#ai-reply-text').textContent=p.can+' Escolham uma pergunta ou me contem onde travaram.'}
  renderAiPresence();
 }
 function openAssistant(question){if(!started)return;tab('vigia');if(document.body.dataset.view!=='vigia')return;if(question)query(question);else $('#ai-question').focus({preventScroll:true})}
 function query(value,options={}){
  const text=String(value||'').trim();if(!text){$('#ai-question').focus();return}
  const r=E.orientar(text,{lastIntent:aiLastIntent,errorFields:aiErrorFields,...options});aiAnsweredLevel=r.level;aiLastIntent=r.intent==='fallback'?null:r.intent;aiLastQuestion=text;$('#ai-question').value='';
  if(r.intent==='tempo'){const settings=VigiaSettings.current(),eligible=VigiaEngine.stages.filter(stage=>stage.id!=='protocol'&&settings.stages.includes(stage.id)).map(stage=>stage.label.toLowerCase());r.text='Esta rodada começa com '+formatTime(settings.durationSeconds)+'. Restam '+formatTime(countdown.remaining(elapsed))+'. '+(settings.bonusEnabled&&settings.bonusSeconds>0&&eligible.length?'As etapas selecionadas de '+eligible.join(', ')+' acrescentam '+settings.bonusSeconds+' segundos por acerto, uma vez por etapa. ':'Esta rodada não tem bônus de tempo. ')+'Ao zerar, a falha de transmissão bloqueia o sistema. A anotação da chave final tem uma contagem separada de 30 segundos.'}
  $('#ai-reply-memory').textContent='MEMÓRIA · '+String(r.memory).padStart(2,'0')+'%';$('#reply').classList.toggle('is-limited',r.limited);
  $('#ai-asked').hidden=false;$('#ai-asked').textContent='Vocês perguntaram: '+text;$('#ai-reply-title').textContent=r.title;$('#ai-reply-text').textContent=r.text;
  $('#ai-reply-steps').replaceChildren();for(const step of r.steps){const li=document.createElement('li');li.textContent=step;$('#ai-reply-steps').append(li)}$('#ai-reply-steps').hidden=!r.steps.length;
  const docHost=$('#ai-reply-docs');docHost.replaceChildren();const allowed=new Set(available().map(e=>e.id));
  const docs=r.docs.filter(id=>allowed.has(id)||id==='audio01'||id==='audio02'&&E.estado().identityConfirmed||id==='audio03'&&E.estado().chronologyOrdered);docHost.hidden=!docs.length;
  if(docs.length){const heading=document.createElement('strong');heading.textContent='ONDE CONFERIR';docHost.append(heading);const list=document.createElement('div');for(const id of docs){const button=document.createElement('button');button.type='button';button.innerHTML=I.svg(id.startsWith('audio')?'audio':'file');const label=document.createElement('span');label.textContent=id.startsWith('audio')?'Ler '+audioNames[id]:titles[id]||id;button.append(label);button.onclick=()=>id.startsWith('audio')?transcribe(id):openDoc(id);list.append(button)}docHost.append(list)}
  const actions=$('#ai-reply-actions');actions.replaceChildren();for(const action of r.actions){const button=document.createElement('button');button.type='button';button.className='primary';button.textContent=action.label;button.onclick=()=>tab(action.tab);actions.append(button)}actions.hidden=!r.actions.length;
  const followups=$('#ai-followups');followups.replaceChildren();for(const question of r.followups){const button=document.createElement('button');button.type='button';button.textContent=question;button.onclick=()=>query(question);followups.append(button)}followups.hidden=!r.followups.length;
  $('#ai-response-status').textContent='Resposta disponível: '+r.title;VigiaDesktop.chat(text,{...r,docs},{refresh:!!options.refresh});
 }
 $('#ask').onsubmit=e=>{e.preventDefault();query(new FormData(e.target).get('query'))};
 $('#hint').onclick=()=>{const st=stage();hints[st]=Math.min(3,(hints[st]||0)+1);$('#ai-hint-progress').textContent='Dica '+hints[st]+' de 3 nesta etapa. Clique novamente para aprofundar.';query('dica',{hintLevel:hints[st]})};
 $('#ai-reminder-open').onclick=()=>openAssistant();$('#ai-fab').onclick=()=>openAssistant();
 $('#reader-ask-ai').onclick=()=>openAssistant(currentDoc?.startsWith('APOIO')||['F1','F1_ID'].includes(currentDoc)?'pessoas':currentDoc||'Qual documento consultar?');
 setInterval(()=>{if(!started||timeExpired||E.estado().protocolConfirmed||document.querySelector('dialog:modal')||['INPUT','TEXTAREA'].includes(document.activeElement.tagName))return;aiReminderIndex++;const p=E.perfilIA();$('#ai-reminder-copy').textContent=p.reminders[aiReminderIndex%p.reminders.length];VigiaDesktop.remind(p.reminders[aiReminderIndex%p.reminders.length])},45000);
 $('#closeviewer').onclick=()=>$('#viewer').close();document.addEventListener('keydown',e=>{if(e.key==='Escape'&&$('#viewer').open&&!document.querySelector('dialog:modal')){e.preventDefault();$('#viewer').close()}});$('#closetext').onclick=()=>$('#textdialog').close();
 $('#zoom-out').onclick=()=>setZoom(zoom-10);$('#zoom-in').onclick=()=>setZoom(zoom+10);$('#zoom-range').oninput=e=>setZoom(Number(e.target.value));$('#zoom-fit').onclick=fitDocument;$('#doc-prev').onclick=()=>{const list=available(),n=list.findIndex(e=>e.id===currentDoc);if(n>0)openDoc(list[n-1].id)};$('#doc-next').onclick=()=>{const list=available(),n=list.findIndex(e=>e.id===currentDoc);if(n<list.length-1)openDoc(list[n+1].id)};$('#docviewport').addEventListener('wheel',e=>{if(e.ctrlKey||e.metaKey){e.preventDefault();setZoom(zoom+(e.deltaY<0?10:-10))}},{passive:false});let resizeTimer;window.addEventListener('resize',()=>{clearTimeout(resizeTimer);resizeTimer=setTimeout(()=>{if($('#viewer').open)fitDocument()},180)});
 function start(isDemo=false){
  if(started||VigiaIntroVideo.active)return;
  VigiaFeedback.prime();if($('#intro').open)$('#intro').close();
  const beginRound=()=>{VigiaAmbient.start();started=true;demo=isDemo;running=!demo;elapsed=0;last=Date.now();updateAnalysisClock();notice('ANÁLISE INICIADA · '+E.perfilIA().next);tab('desktop');VigiaDesktop.welcome();if(VigiaSettings.current().autoNarration&&!E.estado().skippedStages.length)play('audio01')};
  VigiaIntroVideo.begin(beginRound,()=>$('#intro').showModal());
 }
 $('#start').onclick=()=>start(false);$('#intro').addEventListener('cancel',e=>e.preventDefault());
 const operatorCredential='7SET-OPERACAO';
 function openOperatorAuth(){if($('#op').open||$('#operator-auth').open)return;player.pause();$('#operator-code').value='';$('#auth-error').textContent='';$('#operator-auth').showModal();$('#operator-code').focus()}
 $('#auth-cancel').onclick=()=>$('#operator-auth').close();$('#auth-form').onsubmit=e=>{e.preventDefault();if($('#operator-code').value.trim().toUpperCase()!==operatorCredential){$('#auth-error').textContent='Credencial não autorizada.';return}$('#operator-auth').close();closePublicDialogs();if($('#intro').open)$('#intro').close();wasRunning=running;running=false;last=Date.now();resetArmed=false;$('#reset').innerHTML=I.svg('reset')+'Reinicializar sessão';$('#op-overtime').hidden=!timeExpired;$('#opstatus').textContent=`Memória: ${E.estado().memory}%. Tempo utilizado: ${Math.floor(elapsed)} s.${demo?' Ensaio sem tempo.':''}`;$('#op-pause').textContent=wasRunning?'Manter sessão pausada':'Retomar contagem ao retornar';$('#demo').hidden=started;$('#op').showModal()};
 $('#op-pause').onclick=()=>{wasRunning=!wasRunning;$('#op-pause').textContent=wasRunning?'Manter sessão pausada':'Retomar contagem ao retornar'};
 function resume(){resetArmed=false;running=wasRunning&&started&&!demo&&!E.estado().protocolConfirmed&&countdown.remaining(elapsed)>0;last=Date.now();$('#op').close();if(started&&!demo&&!overtimeAllowed&&countdown.remaining(elapsed)===0&&!timeExpired){expireAnalysis();return}if(!started)$('#intro').showModal();else notice(running?'ANÁLISE RETOMADA.':E.estado().protocolConfirmed?'ARQUIVO RECONSTRUÍDO.':'SESSÃO PAUSADA PELA EQUIPE.')}$('#resume').onclick=resume;$('#op').addEventListener('cancel',e=>{e.preventDefault();resume()});$('#demo').onclick=()=>{$('#op').close();start(true)};
 $('#op-overtime').onclick=()=>{if(!timeExpired)return;timeExpired=false;overtimeAllowed=true;running=false;wasRunning=false;$('#time-up').hidden=true;$('#op').close();$('#op-overtime').hidden=true;render();tab('solve');notice('CONTINUAÇÃO AUTORIZADA PELA EQUIPE · Cronômetro encerrado.');};
 $('#reset').onclick=()=>{if(!resetArmed){resetArmed=true;$('#reset').textContent='Confirmar reinicialização';return}resetArmed=false;timeExpired=false;overtimeAllowed=false;countdown.reset();closeTimeBonus();stopCodeClock();recoveryAuthorized=false;$('#recovery-error').textContent='';$('#recovery-code').removeAttribute('aria-invalid');codeAcknowledged=false;$('#time-up').hidden=true;try{sessionStorage.removeItem('vigia-code-acknowledged')}catch{}$('#code').textContent='';$('#code-written').checked=false;$('#confirm-code-written').disabled=true;player.pause();player.removeAttribute('src');player.load();currentAudio=null;$('#player-dock').hidden=true;endingPlayer.pause();endingPlayer.currentTime=0;$('#ending-frame').contentWindow?.postMessage({type:'vigia-movie-state',time:0,paused:true,reset:true},'*');VigiaIntroVideo.reset();VigiaAmbient.reset();E.reiniciar();running=false;started=false;demo=false;elapsed=0;last=Date.now();wasRunning=false;hints={};aiAnsweredLevel=null;$('#reply').classList.remove('is-limited');aiLastIntent=null;aiLastQuestion='';aiReminderIndex=0;aiLastMemory=null;aiErrorFields=[];$('#ai-asked').hidden=true;$('#ai-reply-steps').hidden=true;$('#ai-reply-docs').hidden=true;$('#ai-reply-actions').hidden=true;$('#ai-followups').hidden=true;$('#ai-hint-progress').textContent='Dicas em 3 níveis: orientação → comparação → ajuda direta.';selectedCard=null;document.querySelectorAll('.correlation-help').forEach(el=>el.remove());$('#timeline-move-status').textContent='1 → 2 → 3 → 4 → 5 → 6 · Do primeiro ao último registro';order=D.cards.map(c=>c.id);filter='all';currentDoc=null;document.querySelectorAll('form').forEach(f=>f.reset());$('#search').value='';document.querySelectorAll('[data-filter]').forEach(b=>b.setAttribute('aria-pressed',String(b.dataset.filter==='all')));$('#ai-response-status').textContent='';$('#timer').textContent=formatTime(countdown.remaining(0));$('.clock').classList.remove('is-alert');document.querySelectorAll('dialog[open]').forEach(d=>d.close());storage.clear();VigiaDesktop.reset();notice('Sessão aguardando autorização.');cards();render();tab('desktop',false);$('#intro').showModal()};
 function syncEndingMovie(extra={}){const frame=$('#ending-frame');if(!frame.contentWindow)return;frame.contentWindow.postMessage({type:'vigia-movie-state',time:endingPlayer.currentTime||0,duration:endingPlayer.duration||255.08,paused:endingPlayer.paused,ended:endingPlayer.ended,volume:endingPlayer.volume,muted:endingPlayer.muted,...extra},'*')}
 ['play','pause','timeupdate','seeked','ended','loadedmetadata','volumechange'].forEach(event=>endingPlayer.addEventListener(event,()=>syncEndingMovie()));
 $('#ending-frame').addEventListener('load',()=>syncEndingMovie());
 endingPlayer.addEventListener('error',()=>syncEndingMovie({blocked:true,error:'Faixa de narração indisponível.'}));
 function playEnding(){if(endingPlayer.ended)endingPlayer.currentTime=0;const request=endingPlayer.play();request.catch(()=>syncEndingMovie({blocked:true}));return request}
 window.addEventListener('message',e=>{if(e.source!==$('#ending-frame').contentWindow||e.data?.type!=='vigia-movie-command'||!E.estado().protocolConfirmed||!recoveryAuthorized)return;const d=e.data;if(d.action==='play')playEnding();else if(d.action==='pause')endingPlayer.pause();else if(d.action==='seek'){endingPlayer.currentTime=Math.max(0,Math.min(endingPlayer.duration||255.08,Number(d.time)||0));if(d.resume)playEnding()}else if(d.action==='volume'){endingPlayer.volume=Math.max(0,Math.min(1,Number(d.value)||0));endingPlayer.muted=false}else if(d.action==='mute')endingPlayer.muted=!endingPlayer.muted});
 function openEnding(){if(!E.estado().protocolConfirmed||!recoveryAuthorized)return;player.pause();$('#player-dock').hidden=true;storage.set('confirmed');const frame=$('#ending-frame');if(!frame.getAttribute('src'))frame.src='encerramento/filme/index.html?v=vig-ia-ambient';playEnding();tab('reconstruction');syncEndingMovie()}$('#open-ending').onclick=()=>recoveryAuthorized?openEnding():tab('recovery');
 function stopCodeClock(){clearInterval(codeInterval);codeInterval=null;codeDeadline=0;VigiaFeedback.stopClock()}
 function finishCodeDisplay(expired=false){
  if(codeAcknowledged||!E.estado().protocolConfirmed)return;
  stopCodeClock();codeAcknowledged=true;$('#code').textContent='';$('#code-popup').close();
  $('#recovery-copy').textContent=expired?'Os 30 segundos terminaram. Insira o código que vocês anotaram no caderno.':'Use o código que vocês anotaram no caderno.';
  notice('Código ocultado. Insira a anotação para recuperar o arquivo.','success');render();tab('recovery');
 }
 function updateCodeClock(){
  if(!$('#code-popup').open)return;
  const left=Math.max(0,Math.ceil((codeDeadline-performance.now())/1000));
  $('#code-countdown').textContent='00:'+String(left).padStart(2,'0');
  $('#code-timebar').style.transform='scaleX('+Math.max(0,(codeDeadline-performance.now())/30000)+')';
  $('#code-popup').classList.toggle('is-urgent',left<=10);
  if(left===0){finishCodeDisplay(true);return}
  if(left!==codeSeconds){codeSeconds=left;VigiaFeedback.clockTick(left%2===0)}
 }
 function showCodeOnce(){
  if(codeAcknowledged){notice('Use sua anotação no caderno para liberar o arquivo.');tab('recovery');return}
  if($('#code-popup').open)return;
  closePublicDialogs();stopCodeClock();$('#code-written').checked=false;$('#confirm-code-written').disabled=true;
  $('#code').textContent=D.key.answers.generated_protocol;$('#code-popup').classList.remove('is-urgent');
  $('#code-countdown').textContent='00:30';$('#code-timebar').style.transform='scaleX(1)';
  $('#code-popup').showModal();$('#code-popup-title').focus();
  codeSeconds=30;codeDeadline=performance.now()+30000;VigiaFeedback.clockTick(true);codeInterval=setInterval(updateCodeClock,100);
 }
 $('#code-written').onchange=()=>{$('#confirm-code-written').disabled=!$('#code-written').checked};
 $('#code-popup').addEventListener('cancel',e=>e.preventDefault());
 $('#code-popup').addEventListener('close',()=>{stopCodeClock();$('#code').textContent=''});
 $('#confirm-code-written').onclick=()=>{if($('#code-written').checked)finishCodeDisplay()};
 document.addEventListener('visibilitychange',()=>{if(!document.hidden&&codeDeadline)updateCodeClock()});
 $('#recovery-form').onsubmit=e=>{
  e.preventDefault();if(!E.estado().protocolConfirmed||!codeAcknowledged)return;
  const input=$('#recovery-code'),value=input.value;
  if(VigiaEngine.normalizar(value)!==VigiaEngine.normalizar(D.key.answers.generated_protocol)){
   input.setAttribute('aria-invalid','true');$('#recovery-error').textContent=value.trim()?'Código não reconhecido. Confira todos os grupos na anotação do papel.':'Digite o código anotado no papel.';input.focus();return;
  }
  recoveryAuthorized=true;input.value='';input.removeAttribute('aria-invalid');$('#recovery-error').textContent='';render();openEnding();
 };
 $('#recovery-code').addEventListener('input',()=>{$('#recovery-code').removeAttribute('aria-invalid');$('#recovery-error').textContent=''});
 window.addEventListener('message',e=>{if(e.source===$('#ending-frame').contentWindow&&e.data?.type==='vigia-navigate'&&['files','solve','timeline','media','vigia'].includes(e.data.tab))tab(e.data.tab)});
 document.addEventListener('keydown',e=>{if(e.ctrlKey&&e.shiftKey&&e.code==='KeyO'){e.preventDefault();openOperatorAuth();return}if(e.altKey&&!e.ctrlKey&&['1','2','3','4','5'].includes(e.key)&&started&&!$('#op').open&&!$('#operator-auth').open){e.preventDefault();tab(['files','solve','timeline','media','vigia'][Number(e.key)-1],true,false)}if($('#viewer').open&&!['INPUT','TEXTAREA'].includes(e.target.tagName)){if(e.key==='+'||e.key==='='){e.preventDefault();setZoom(zoom+10)}if(e.key==='-'){e.preventDefault();setZoom(zoom-10)}}});
 setInterval(()=>{
  const now=Date.now();if(running)elapsed+=(now-last)/1000;last=now;const left=updateAnalysisClock();
  if(running){
   E.avisosPorTempo(elapsed).forEach(a=>{if(a.audience==='player')notice(a.text);else $('#opstatus').textContent=a.text});
   const signal=countdown.signal(elapsed);if(signal==='expired'){expireAnalysis();return}
   if((signal==='warning'||signal==='urgent')&&VigiaSettings.current().timeWarnings)VigiaFeedback.deadlineWarning(signal==='urgent',left);
  }
 },100);
 window.addEventListener('beforeunload',e=>{if(started&&!E.estado().protocolConfirmed){e.preventDefault();e.returnValue=''}});window.addEventListener('pageshow',e=>{if(e.persisted){last=Date.now();render()}});

 $('#reset').addEventListener('click',()=>{if(resetArmed){endingPlayer.pause();endingPlayer.currentTime=0;syncEndingMovie({reset:true})}},{capture:true});$('#reset').addEventListener('click',()=>{if(!started)VigiaFeedback.reset()});
 window.VigiaSession={open:tab,doc:openDoc,play,transcribe,help:openAssistant,state:()=>E.estado(),filter(value){filter=value;document.querySelectorAll('[data-filter]').forEach(b=>b.setAttribute('aria-pressed',String(b.dataset.filter===value)));renderFiles()}};
 storage.clear();tab('desktop',false);cards();render();$('#intro').showModal();
})();
