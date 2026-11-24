from pathlib import Path
root=Path(__file__).resolve().parents[2]/'output/vigia_os_sistema'
p=root/'app.js';s=p.read_text(encoding='utf-8')
a=s.index(' function tab(');b=s.index(' function focusAnswerField()',a)
s=s[:a]+''' function tab(id,focus=true,answerField=true){
  if(timeExpired||$('#code-popup').open)return;
  if(E.estado().protocolConfirmed&&!codeAcknowledged){showCodeOnce();return}
  if(E.estado().protocolConfirmed&&codeAcknowledged&&!recoveryAuthorized)id='recovery';
  const chronology=id==='timeline';if(chronology)id='solve';
  if(!['desktop','files','solve','media','vigia','notes','trash','recovery','reconstruction'].includes(id))return;
  if(id==='reconstruction'&&(!E.estado().protocolConfirmed||!recoveryAuthorized))return;
  if(id==='recovery'&&(!E.estado().protocolConfirmed||!codeAcknowledged))return;
  if(id!=='reconstruction')endingPlayer.pause();
  if(['recovery','reconstruction','desktop'].includes(id)||$('#viewer').open&&!(id==='vigia'&&innerWidth>=1500))closePublicDialogs();
  else if($('#textdialog').open)$('#textdialog').close();
  $('#recovery').hidden=id!=='recovery';$('#reconstruction').hidden=id!=='reconstruction';
  document.body.dataset.view=id;VigiaDesktop.open(id);renderAiPresence();
  if(id==='reconstruction')$('#reconstruction').showModal();
  if(id==='vigia'&&aiLastQuestion&&aiAnsweredLevel!==E.perfilIA().level)query(aiLastQuestion,{refresh:true});
  document.querySelector('.reader-menu').open=false;
  if(focus){
   if(id==='desktop')VigiaDesktop.focusHome();
   else if(id==='solve'&&chronology){requestAnimationFrame(()=>{const host=VigiaDesktop.body('solve');host.scrollTop+=Math.max(0,$('#timeline').getBoundingClientRect().top-host.getBoundingClientRect().top-16)})}
   else if(id==='solve'&&answerField)requestAnimationFrame(focusAnswerField);
   else if(['files','solve','media','vigia','notes','trash'].includes(id))VigiaDesktop.body(id).focus({preventScroll:true});
   if(id==='recovery')$('#recovery-code').focus({preventScroll:true});
   if(id==='reconstruction')$('#reconstruction-title').focus({preventScroll:true});
  }
  try{history.replaceState(null,'','#'+id)}catch{}
 }
''' +s[b:]
s=s.replace("const host=$('#window-body');host.scrollTop+=target", "const host=VigiaDesktop.body('solve');host.scrollTop+=target")
s=s.replace("const host=$('#window-body'),rect=host.getBoundingClientRect()", "const host=VigiaDesktop.body('solve'),rect=host.getBoundingClientRect()")
s=s.replace("$('#timeline-lock').hidden=s.accessesConfirmed;", "$('#timeline').hidden=!s.accessesConfirmed||s.protocolConfirmed;$('#timeline-lock').hidden=s.accessesConfirmed;")
s=s.replace("VigiaDesktop.visibility(sharedHidden,E.estado().protocolConfirmed);", "VigiaDesktop.visibility(sharedHidden,E.estado().protocolConfirmed&&(!recoveryAuthorized||['recovery','reconstruction'].includes(view)));")
s=s.replace("$('#ai-question').value=text;", "$('#ai-question').value='';")
old="$('#ai-response-status').textContent='Resposta disponível: '+r.title;$('#ai-reply-title').focus({preventScroll:true});const host=$('#window-body');host.scrollTop+=Math.max(0,$('#reply').getBoundingClientRect().top-host.getBoundingClientRect().top-60);"
new="$('#ai-response-status').textContent='Resposta disponível: '+r.title;VigiaDesktop.chat(text,{...r,docs},{refresh:!!options.refresh});"
assert old in s;s=s.replace(old,new)
s=s.replace("$('#ai-question').placeholder='Ex.: '+p.examples[0]", "$('#ai-question').placeholder='Escreva uma mensagem… Ex.: '+p.examples[0]")
p.write_text(s,encoding='utf-8')
for name,svg in {
'notes':'<path d="M14 5h25l13 13v41H14z" fill="#ece4fb"/><path d="M39 5v14h13" fill="#b88bdc"/><path d="M22 29h22M22 37h22M22 45h16" stroke="#6b438c" stroke-width="3"/>',
'trash':'<path d="m16 20 4 38h24l4-38" fill="#572881" stroke="#d3b0f4" stroke-width="2"/><path d="M12 16h40M24 15V8h16v7M27 27v22M37 27v22" fill="none" stroke="#d4b7ee" stroke-width="3" stroke-linecap="round"/>',
'user':'<circle cx="32" cy="22" r="11" fill="#d4bcf0"/><path d="M10 59v-8a22 22 0 0 1 44 0v8" fill="#9e76cc"/>'
}.items():
 (root/'assets/os'/(name+'.svg')).write_text('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64">'+svg+'</svg>',encoding='utf-8')
p=root/'index.html';s=p.read_text(encoding='utf-8');s=s.replace('</head>','<link rel="stylesheet" href="os-v2.css?v=20261119-os-v2"></head>');s=s.replace('vigia-os-1','vigia-os-2').replace('20261119-vigia-os-1','20261119-vigia-os-2');p.write_text(s,encoding='utf-8')
print('Integração v2 aplicada: janelas independentes, cronologia em Registros e chat.')
