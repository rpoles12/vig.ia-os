'use strict';
const D=window.FILME, $=s=>document.querySelector(s), voice=$('#voice');
const starts=[0,6.73,24.979,30.239,36.759,56.438,67.358,71.838,87.273,91.793,97.833,122.020,127.130,130.270,139.780,153.095,160.475,165.755,168.025,186.978,192.908,198.9,201.928,206.468,223.405,249.905];
const names=['A sala recuperada','As conexões solucionadas','Bryan e seu plano','A proposta NORTHSTAR','O banco de projetos','A ameaça a Helena','A credencial cedida','Bryan utiliza o crachá','Marcelo sob pressão','A fraude financeira','A conta temporária','A sessão começa','Cópia iniciada','Carlos recebe o alerta','Os envolvidos se encontram','A pressão durante o confronto','O empurrão','A queda contra a bancada','Vítima e responsável','A memória interrompida','A cópia termina','A saída de Bryan','A ligação anônima','Marcelo desativa a conta','Responsabilidades separadas','Arquivo recuperado'];
const escape=s=>String(s).replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
const image=(key,cls='original')=>`<img class="${cls}" src="${D.refs[key]}" alt="${escape(key)}">`;
const reveal=(html,at=0,out=null,cls='')=>`<div class="reveal ${cls}" data-in="${at}" ${out===null?'':`data-out="${out}"`}>${html}</div>`;
const heading=(title,kicker='RECONSTITUIÇÃO · REGISTROS RECUPERADOS')=>`<div class="kicker">${kicker}</div><h2 class="scene-title">${title}</h2>`;
const panel=(title,body,cls='')=>`<div class="panel ${cls}"><h3>${title}</h3>${body}</div>`;
const doc=(key,h=400)=>`<div class="doc-box" style="height:${h}px">${image(key)}</div><small class="doc-tag">${key} · EVIDÊNCIA ORIGINAL</small>`;
const call=(label,headline,detail='',at=0,out=null)=>reveal(`<div class="callout"><div class="label">${label}</div><div class="headline">${headline}</div>${detail?`<div class="detail">${detail}</div>`:''}</div>`,at,out);
const inset=(key,title,at=0,out=null)=>reveal(`<aside class="inset"><small>${title}</small>${image(key)}</aside>`,at,out);
const photos=new Set([1,3,6,7,8,9,11,12,13,14,15,16,17,18,19,20,21,22,23,24,26]);
const times={8:'22:31',12:'22:36',13:'22:38',14:'22:41',15:'22:43 → 22:44',16:'22:44 → 22:46',17:'22:46',18:'22:46',19:'22:46',20:'22:46:32',21:'22:47',22:'22:49',23:'22:52',24:'22:54'};
const overlays={
 1:reveal('<div class="opening"><div class="kicker">MEMÓRIA RECUPERADA · 100%</div><h2>Protocolo confirmado.</h2><p>CÓDIGO REGISTRADO</p></div>',0,4.2)+reveal('<div class="opening"><div class="kicker">EVIDÊNCIAS CORRELACIONADAS</div><h2>Vocês solucionaram<br>o caso.</h2></div>',4.2),
 3:call('BRYAN ALMEIDA · BA-17','O articulador da invasão.','O objetivo era obter os projetos tecnológicos.'),
 6:call('HELENA DUARTE','Uma ameaça contra o sobrinho.','O uso indevido do crachá foi usado para pressioná-la.')+inset('H1','H1 · MENSAGEM RECUPERADA',5),
 7:call('ACESSO FÍSICO','Helena cedeu a credencial 2847.','Titular do crachá ≠ pessoa que o utilizou.')+inset('CRACHA','CREDENCIAL ORIGINAL · 2847',1),
 8:call('CREDENCIAL DE HELENA','Quem entrou foi Bryan.','22:31 · Acesso físico ao prédio.',0,7)+call('DISTINÇÃO IMPORTANTE','Rafael não participou da invasão.','As entradas anteriores foram usadas como chantagem.',7),
 9:call('MARCELO VIEIRA · TÉCNICO DE TI','A colaboração foi remota.','Marcelo não estava na sala do incidente.'),
 11:call('ACESSO DIGITAL','18:10 · Criação da conta RV-MANUT.','Alertas de rede reduzidos por seis minutos.',0,13)+inset('RVM','RVM · AUDITORIA ORIGINAL',1,13)+call('FORNECER ACESSO ≠ EXECUTAR A INVASÃO','Helena: acesso físico. Marcelo: acesso digital.','A assinatura recuperada vinculou a operação a Bryan.',13),
 12:call('SEQUÊNCIA DO INCIDENTE','Bryan inicia a sessão.','22:31 · Entrada → 22:36 · Sessão'),
 13:call('REPOSITÓRIO VÉRTICE','A cópia dos projetos é iniciada.','22:38 · Lote V-17'),
 14:call('O SENSOR LOCAL CONTINUAVA ATIVO','Carlos recebe o alerta.','Redução de alertas de rede ≠ sensor local desativado.'),
 15:call('22:43 · RETORNO DE HELENA','Helena volta para recuperar o crachá.','',0,4.8)+call('22:44 · CHEGADA DE CARLOS','Carlos confronta Bryan.','O plano de sair sem ser interceptado havia falhado.',4.8),
 16:call('CHANTAGEM DURANTE O CONFRONTO','Bryan pressiona Helena a intervir.','Carlos havia relacionado o crachá a Helena.'),
 17:call('22:46 · MOMENTO DECISIVO','Helena empurra Carlos.','A intervenção tinha o objetivo de fazê-lo soltar Bryan.'),
 18:call('CONSEQUÊNCIA DO EMPURRÃO','A queda contra a bancada foi fatal.'),
 19:call('HELENA: DUAS CONDIÇÕES SIMULTÂNEAS','Vítima da chantagem. Responsável pelo empurrão.','Uma condição não elimina a outra.',0,7.22)+call('RESPONSABILIDADES DISTINTAS','Bryan articulou o plano e as ameaças.','Não foi ele quem realizou o empurrão.',7.22,13.58)+call('COLABORAÇÃO REMOTA','Marcelo forneceu acesso digital.','Não estava na sala técnica.',13.58),
 20:call('EVIDÊNCIA CAM01','22:46:32 · Último registro da câmera.','A imagem de fundo é uma reconstituição, não uma gravação.')+inset('CAM01','CAM01 · REGISTRO ORIGINAL',.8),
 21:call('22:47 · REPOSITÓRIO VÉRTICE','Cópia concluída.','',0,3)+call('APÓS A CÓPIA','Bryan corrompe os registros.','A corrupção dificultou a reconstrução do incidente.',3),
 22:call('22:49 · SAÍDA','Bryan deixa o local.'),
 23:call('22:52 · HELENA','Uma ligação anônima.','O registro não identifica aqui o destinatário.'),
 24:call('22:54 · MARCELO','Conta temporária desativada.','Operação realizada remotamente.',0,5.04)+reveal(`<div class="comparison">${heading('Dois horários. Dois acontecimentos.','A RESPOSTA FINAL EXIGIA O MOMENTO CRÍTICO')}<div class="grid columns2">${panel('CONFRONTO FATAL','<div class="value">22:46</div><p>Minuto da intervenção<br>que causou a queda fatal.</p>','primary')}${panel('TÉRMINO DA CÓPIA','<div class="value">22:47</div><p>Conclusão da cópia<br>dos projetos tecnológicos.</p>')}</div><div class="protocol"><span>MINUTO CRÍTICO</span><strong>PROTOCOLO · 2246</strong></div></div>`,5.04),
 26:reveal(`<div class="ending-box"><div class="kicker">VIG.IA · MEMÓRIA 100%</div><h2>Arquivo recuperado.</h2><p>Parabéns! Vocês solucionaram o caso.</p><div class="ending-line"></div><div class="kicker">INVESTIGAÇÃO CONCLUÍDA</div></div><img class="logo" src="${D.refs.LOGO}" alt="7set.dev">`,0)
};
function graphic(n){
 if(n===2)return heading('As conexões finalmente fazem sentido.')+`<div class="grid columns3">${reveal(panel('01 · IDENTIDADE',`${image('BRYAN','portrait')}<p>Bryan Almeida</p><small>Assinatura vinculada a BA-17</small>`),0)}${reveal(panel('02 · CREDENCIAL',`${doc('CRACHA',220)}<p>2847 · Helena Duarte</p><small>Utilizada por Bryan</small>`),2.3)}${reveal(panel('03 · MOMENTO CRÍTICO','<div class="value">22:46</div><p>Confronto fatal</p><small>Não confundir com 22:47,<br>o término da cópia.</small>'),5)}</div>`+reveal('<div class="connector"></div><div class="protocol"><span>IDENTIDADE · CREDENCIAL · MINUTO</span><strong>CÓDIGO REGISTRADO</strong></div>',8.2);
 if(n===4)return heading('Uma proposta motivada por dinheiro.')+`<div class="grid columns2">${reveal(panel('NORTHSTAR → BRYAN ALMEIDA','<div class="value">R$ 15.000</div><p>Valor oferecido pela cópia<br>completa do lote V-17.</p><small>Oferta não significa pagamento.</small>'),0)}${reveal(panel('N1 · PROPOSTA RECUPERADA',doc('N1',440)),.6)}</div>`;
 if(n===5)return heading('O alvo: o banco de projetos tecnológicos.','REPOSITÓRIO VÉRTICE · LOTE V-17')+`<div class="grid projects-layout">${reveal(doc('V17',460),0)}<div>${['Célula robotizada modular','Sistema de visão de baixo custo','Controlador de eficiência energética'].map((t,i)=>reveal(`<div class="project-row"><span>0${i+1}</span><strong>${t}</strong></div>`,i*.5)).join('')}${reveal('<p class="summary-note">Oferta e cópia comprovadas.<br><b>Pagamento e entrega não comprovados.</b></p>',5,12.5)}${reveal('<div class="protocol"><span>ACESSO FÍSICO</span><strong>+</strong><span>ACESSO DIGITAL</span></div>',12.5)}</div></div>`;
 if(n===10)return heading('A fraude se tornou instrumento de pressão.')+`<div class="grid columns2">${reveal(panel('SEIS REEMBOLSOS IRREGULARES',`<div class="notes-grid">${['NF318','NF318B','NF427','NF427B','NF512','NF512B'].map(k=>image(k)).join('')}</div><small>Três serviços apresentados duas vezes.<br>Sem autorização e sem execução.</small>`),0)}${reveal(panel('TOTAL DOS LANÇAMENTOS','<div class="value">R$ 3.840</div><p>Bryan utilizou as provas<br>para ameaçar Marcelo.</p><p class="accent">Colaboração sob chantagem.</p>'),1)}</div>`;
 if(n===25)return heading('Cada pessoa teve um papel diferente.')+`<div class="grid columns3" id="roles">${[['BRYAN','Bryan Almeida','Planejou a invasão<br>e realizou as ameaças.'],['HELENA','Helena Duarte','Cedeu a credencial<br>e provocou a queda fatal.'],['MARCELO','Marcelo Vieira','Forneceu acesso digital<br>remoto sob coação.']].map((c,i)=>reveal(panel(c[1],`${image(c[0],'portrait')}<p>${c[2]}</p>`),i*.7)).join('')}</div>`+reveal(`<div class="victim">${image('CARLOS')}<div><strong>CARLOS MENDES · VÍTIMA</strong><p>Recebeu o alerta e confrontou Bryan.</p></div></div>`,2.6)+reveal('<div class="summary-note accent">Evidências conectadas. Incidente reconstituído.</div>',14);
 return '';
}
const scenes=starts.map((start,i)=>({n:i+1,start,end:starts[i+1]??D.duration,title:names[i]}));
for(const s of scenes){
 const el=document.createElement('section');el.className='scene';el.dataset.frame=s.n;
 if(photos.has(s.n)){
  const f=s.n===26?1:s.n;
  el.innerHTML=`<img class="photo" src="assets/fotos/${String(f).padStart(2,'0')}.png" alt="${escape(s.title)}"><div class="shade"></div>${s.n!==1&&s.n!==26?'<div class="recon">RECONSTITUIÇÃO DO INCIDENTE</div>':''}${times[s.n]?`<div class="time-badge">${times[s.n]}</div>`:''}${overlays[s.n]??''}`;
 }else{el.classList.add('graphic');el.innerHTML=graphic(s.n);}
 $('#scenes').append(el);s.el=el;s.photo=el.querySelector('.photo');s.reveals=[...el.querySelectorAll('.reveal')];
}
function format(t){return `${String(Math.floor(t/60)).padStart(2,'0')}:${String(Math.floor(t%60)).padStart(2,'0')}`;}
D.blocks.forEach((b,i)=>{
 const btn=document.createElement('button');btn.innerHTML=`<small>${format(b.start)} · TRECHO ${i+1}</small><strong>${escape(b.title)}</strong>`;btn.onclick=()=>seek(b.start,true);$('#chapters').append(btn);
 const article=document.createElement('article');article.innerHTML=`<h2>${format(b.start)} · ${escape(b.title)}</h2><p>${escape(b.text)}</p>`;$('#transcript').append(article);
});
const clamp=(v,a=0,b=1)=>Math.max(a,Math.min(b,v)),ease=v=>1-Math.pow(1-clamp(v),3);
const dissolve=new Set([2,6,9,20,26]);
let current=-1,subKey='',showCaptions=true,dragging=false,audioContext,lastSoundTime=-100,hasStarted=false,externalController=window.parent!==window,externalPaused=true,externalEnded=false,externalTime=0;
function sendCommand(action,details={}){if(!externalController)return false;window.parent.postMessage({type:'vigia-movie-command',action,...details},'*');return true;}
function movieTime(){return externalController?externalTime:voice.currentTime;}
function animateScene(s,t){
 const local=t-s.start,p=clamp(local/(s.end-s.start));
 if(s.photo){const fixed=[7,13,15,16,17,18,19,20,23].includes(s.n);const zoom=fixed?1:1+(.025*p);s.photo.style.transform=`scale(${zoom})`;}
 for(const r of s.reveals){const at=Number(r.dataset.in),out=r.dataset.out===undefined?Infinity:Number(r.dataset.out),enter=ease((local-at)/.4),exit=1-ease((local-out)/.25),a=enter*exit;r.style.opacity=a;r.style.visibility=a>0?'visible':'hidden';r.style.transform=`translateY(${(1-enter)*18}px)`;}
 if(s.n===25){const rolePanels=s.el.querySelectorAll('#roles .panel');const active=local<6?0:local<12?1:local<17?2:-1;rolePanels.forEach((r,i)=>r.style.borderColor=i===active?'#c59aff':'#47325f');}
}
function wrapCaption(t){const words=t.split(' ');let a='',b='';for(const w of words){if(!b&&a.length+w.length<Math.max(35,t.length/2+5))a+=(a?' ':'')+w;else b+=(b?' ':'')+w;}return a+(b?'\n'+b:'');}
function draw(t){
 t=clamp(t,0,D.duration);const idx=Math.max(0,scenes.findLastIndex(s=>s.start<=t));const s=scenes[idx],elapsed=t-s.start;
 if(idx!==current){current=idx;for(const q of scenes){q.el.classList.remove('active');q.el.style.opacity=0;}s.el.classList.add('active');}
 if(dissolve.has(s.n)&&elapsed<.4&&idx>0){const prev=scenes[idx-1];prev.el.classList.add('active');prev.el.style.opacity=1;animateScene(prev,prev.end);s.el.style.opacity=ease(elapsed/.4);}else{s.el.style.opacity=1;if(idx>0)scenes[idx-1].el.classList.remove('active');}
 animateScene(s,t);
 const block=Math.max(0,D.blocks.findLastIndex(b=>b.start<=t));$('#chapter-name').textContent=D.blocks[block].title;[...$('#chapters').children].forEach((b,i)=>b.classList.toggle('current',i===block));
 if(!dragging)$('#seek').value=t;$('#clock').textContent=`${format(t)} / ${format(D.duration)}`;
 const c=showCaptions?D.captions.find(c=>t>=c.start&&t<c.end):null;const key=c?.text??'';
 if(key!==subKey){subKey=key;$('#subtitle').replaceChildren();if(c){const span=document.createElement('span');span.textContent=wrapCaption(c.text);$('#subtitle').append(span);}}
 document.documentElement.dataset.frame=s.n;
}
function resize(){const box=$('#viewport'),w=box.clientWidth,h=box.clientHeight,scale=Math.min(w/1920,h/1080);$('#stage').style.transform=`scale(${scale})`;$('#stage').style.left=`${(w-1920*scale)/2}px`;$('#stage').style.top=`${(h-1080*scale)/2}px`;}
new ResizeObserver(resize).observe($('#viewport'));resize();
async function play(){
 if(sendCommand('play'))return;
 try{if(voice.ended||voice.currentTime>=D.duration-.05)voice.currentTime=0;await voice.play();hasStarted=true;$('#start').hidden=true;$('#error').hidden=true;}catch(e){$('#error').hidden=false;$('#error').textContent='A reprodução foi bloqueada pelo navegador. Selecione Reproduzir para iniciar a narração.';}
}
function toggle(){if(externalController){sendCommand(externalPaused?'play':'pause');return}if(voice.paused)play();else voice.pause();}
function seek(t,resume=false){t=clamp(t,0,D.duration-.001);if(sendCommand('seek',{time:t,resume})){externalTime=t;draw(t);return}voice.currentTime=t;draw(voice.currentTime);if(resume)play();}
$('#start').onclick=play;$('#play').onclick=toggle;$('#back').onclick=()=>seek(movieTime()-10);$('#forward').onclick=()=>seek(movieTime()+10);
$('#seek').addEventListener('input',e=>{dragging=true;seek(Number(e.target.value));});$('#seek').addEventListener('change',()=>dragging=false);$('#seek').addEventListener('pointerup',()=>dragging=false);
$('#volume').oninput=e=>{if(sendCommand('volume',{value:Number(e.target.value)}))return;voice.volume=Number(e.target.value);voice.muted=false;$('#mute').textContent='Som';};
$('#mute').onclick=()=>{if(sendCommand('mute'))return;voice.muted=!voice.muted;$('#mute').textContent=voice.muted?'Sem som':'Som';};
$('#cc').onclick=()=>{showCaptions=!showCaptions;$('#cc').setAttribute('aria-pressed',String(showCaptions));draw(movieTime());};
$('#fullscreen').onclick=async()=>{try{if(document.fullscreenElement)await document.exitFullscreen();else await $('#player').requestFullscreen();}catch(e){$('#error').hidden=false;$('#error').textContent='Use F11 para ampliar a janela do navegador.';}};
$('#transcript-toggle').onclick=()=>{const p=$('#transcript');p.hidden=!p.hidden;$('#transcript-toggle').setAttribute('aria-expanded',String(!p.hidden));};
voice.onplay=()=>{$('#play').textContent='Ⅱ';$('#play').setAttribute('aria-label','Pausar');};voice.onpause=()=>{$('#play').textContent='▶';$('#play').setAttribute('aria-label','Reproduzir');};
voice.onended=()=>{draw(D.duration);$('#play').textContent='↻';$('#play').setAttribute('aria-label','Rever reconstituição');};
voice.addEventListener('error',()=>{$('#error').hidden=false;$('#error').textContent='Áudio não encontrado. Mantenha a pasta assets junto deste HTML.';});
window.addEventListener('message',e=>{if(e.source!==window.parent||e.data?.type!=='vigia-movie-state')return;const s=e.data;externalPaused=!!s.paused;externalEnded=!!s.ended;externalTime=clamp(Number(s.time)||0,0,D.duration);if(s.reset){hasStarted=false;externalTime=0;$('#start').hidden=false;$('#error').hidden=true;draw(0);return}if(!externalPaused){hasStarted=true;$('#start').hidden=true;$('#error').hidden=true}else if(s.blocked){$('#start').hidden=false;$('#error').hidden=false;$('#error').textContent=s.error||'O navegador bloqueou o início automático. Selecione Reproduzir para continuar.'}draw(externalTime);$('#play').textContent=externalEnded?'↻':externalPaused?'▶':'Ⅱ';$('#play').setAttribute('aria-label',externalEnded?'Rever reconstituição':externalPaused?'Reproduzir':'Pausar');if(Number.isFinite(s.volume))$('#volume').value=String(s.volume);$('#mute').textContent=s.muted?'Sem som':'Som';});
document.addEventListener('keydown',event=>{
 if(!externalController)return;
 if(VigiaKeyboard.operatorShortcut(event)){
  event.preventDefault();
  event.stopImmediatePropagation();
  window.parent.postMessage({type:'vigia-movie-operator'},'*');
 }else if(VigiaKeyboard.blocksBrowser(event)||VigiaKeyboard.appShortcut(event,['files','vigia','solve','media'])){
  event.preventDefault();
  event.stopImmediatePropagation();
 }
},true);
document.addEventListener('keydown',e=>{if(['INPUT','BUTTON','TEXTAREA'].includes(document.activeElement.tagName))return;if(e.code==='Space'){e.preventDefault();toggle();}if(e.code==='ArrowRight'){e.preventDefault();seek(movieTime()+10);}if(e.code==='ArrowLeft'){e.preventDefault();seek(movieTime()-10);}});
// Audio currentTime is the only animation clock: pause, seek and buffering stay synchronized.
function tick(){draw(movieTime());requestAnimationFrame(tick);}draw(0);requestAnimationFrame(tick);
// Preload only photographic sources; documents and portraits are already present in the DOM.
for(const s of scenes)if(s.photo)s.photo.decoding='async';
window.startMovie=play;
window.pauseMovie=()=>voice.pause();
window.rewindMovie=()=>{voice.pause();voice.currentTime=0;draw(0);$('#start').hidden=false;$('#error').hidden=true;};
window.RECONSTITUICAO={scenes:scenes.map(({n,start,end,title})=>({n,start,end,title})),seek,draw,duration:D.duration};
