(()=>{
 'use strict';
 const $=s=>document.querySelector(s),track=document.createElement('audio');
 track.id='ambient-track';track.src='audio/trilha/long-note-one.mp3';track.loop=true;track.preload='metadata';track.hidden=true;track.volume=0;
 track.setAttribute('aria-hidden','true');document.body.append(track);
 let started=false,muted=false,baseVolume=.40,ducked=false,fadeFrame=0,holdUntil=0,holdTimer=0,blocked=false,failed=false,generation=0;
 const panel=document.createElement('section');panel.className='ambient-controls';panel.setAttribute('aria-label','Trilha sonora de fundo');
 panel.innerHTML=`<div class="ambient-heading"><span>Trilha ambiente</span><small id="music-volume-value">40%</small></div><div class="ambient-volume-row"><button id="music-toggle" type="button" aria-label="Silenciar trilha ambiente" aria-pressed="true" title="Silenciar trilha ambiente">${VigiaIcons.svg('audio')}</button><label><span class="sr-only">Volume da trilha ambiente</span><input id="music-volume" type="range" min="0" max="1" step=".01" value=".40" aria-label="Volume da trilha ambiente"></label></div><p id="music-state" role="status">Começa ao iniciar a investigação.</p><p class="ambient-credit">Long note One · <a href="https://incompetech.com/music/royalty-free/index.html?isrc=USUAN1100418" target="_blank" rel="noopener noreferrer">Kevin MacLeod</a><br><a href="https://creativecommons.org/licenses/by/4.0/" target="_blank" rel="noopener noreferrer">CC BY 4.0</a></p>`;
 $('#mini-transcript').before(panel);$('.mini-menu-heading span').textContent='Narração e fragmentos';
 function mediaPlaying(root){return [...root.querySelectorAll('audio,video')].some(m=>m!==track&&!m.paused&&!m.ended)}
 function foregroundPlaying(){
  if(mediaPlaying(document))return true;
  for(const frame of document.querySelectorAll('iframe')){try{if(frame.contentDocument&&mediaPlaying(frame.contentDocument))return true}catch{}}
  return false;
 }
 function showState(){
  $('#music-volume-value').textContent=Math.round(baseVolume*100)+'%';
  $('#music-volume').value=baseVolume;
  const off=muted||baseVolume===0;
  $('#music-toggle').classList.toggle('is-muted',off);$('#music-toggle').setAttribute('aria-pressed',String(!off));
  const label=off||blocked?'Ativar trilha ambiente':'Silenciar trilha ambiente';$('#music-toggle').setAttribute('aria-label',label);$('#music-toggle').title=label;
  $('#music-state').textContent=failed?'Trilha indisponível. Confira a pasta do sistema.':off?'Trilha silenciada.':blocked?'Clique para ativar a trilha.':!started?'Começa ao iniciar a investigação.':ducked?'Volume reduzido durante áudio/vídeo.':'Suspense ambiente · reprodução contínua.';
  track.dataset.mode=!started?'stopped':off?'muted':ducked?'ducked':'ambient';
 }
 function fadeTo(target,duration){
  cancelAnimationFrame(fadeFrame);fadeFrame=0;
  const from=track.volume,at=performance.now();
  if(Math.abs(from-target)<.0001){track.volume=target;return}
  const step=now=>{const ratio=Math.min(1,Math.max(0,(now-at)/duration));track.volume=Math.max(0,Math.min(1,from+(target-from)*ratio));if(ratio<1)fadeFrame=requestAnimationFrame(step);else fadeFrame=0};
  fadeFrame=requestAnimationFrame(step);
 }
 function update(){
  ducked=foregroundPlaying()||performance.now()<holdUntil;
  const target=!started||muted?0:baseVolume*(ducked?.12:1);
  fadeTo(target,target<track.volume?180:1100);showState();
 }
 function ensurePlayback(){
  if(!started||muted||baseVolume===0||!track.paused)return;
  const round=generation;
  track.play().then(()=>{if(round!==generation){if(!started)track.pause();return}blocked=false;update()}).catch(()=>{if(round===generation&&started){blocked=true;showState()}});
 }
 function observe(root){for(const type of ['play','playing','pause','ended','emptied'])root.addEventListener(type,event=>{if(event.target!==track)update()},true)}
 observe(document);
 const watchedFrames=new WeakSet();
 function observeFrame(frame){try{const root=frame.contentDocument;if(root&&!watchedFrames.has(root)){watchedFrames.add(root);observe(root)}update()}catch{}}
 for(const frame of document.querySelectorAll('iframe')){frame.addEventListener('load',()=>observeFrame(frame));observeFrame(frame)}
 document.addEventListener('load',event=>{if(event.target?.tagName==='IFRAME')observeFrame(event.target)},true);
 track.addEventListener('error',()=>{failed=true;showState()});
 $('#music-toggle').onclick=()=>{if(blocked){blocked=false;muted=false}else muted=!muted;if(!muted&&baseVolume===0)baseVolume=.40;ensurePlayback();update()};
 $('#music-volume').oninput=event=>{baseVolume=Math.max(0,Math.min(1,Number(event.target.value)||0));muted=baseVolume===0;ensurePlayback();update()};
 document.addEventListener('pointerdown',()=>{if(started&&blocked)ensurePlayback()},{passive:true});
 window.VigiaAmbient={
  start(){started=true;failed=false;ensurePlayback();update()},
  duckFor(milliseconds){holdUntil=Math.max(holdUntil,performance.now()+milliseconds);clearTimeout(holdTimer);holdTimer=setTimeout(update,milliseconds+10);update()},
  reset(){generation++;started=false;holdUntil=0;blocked=false;clearTimeout(holdTimer);cancelAnimationFrame(fadeFrame);fadeFrame=0;track.pause();track.currentTime=0;track.volume=0;showState()}
 };
 showState();
})();
