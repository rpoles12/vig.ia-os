(()=>{
 'use strict';
 const source='video/Video_inicial.mp4';
 // This section is created before the desktop builds its windows and shortcuts.
 const replay=document.createElement('section');replay.id='introvideo';replay.className='pane intro-replay';
 replay.innerHTML='<video id="intro-replay-player" controls playsinline preload="metadata" aria-label="Vídeo inicial da investigação"></video><div class="intro-replay-footer"><span>Vídeo inicial.mp4</span><a href="'+source+'" download="Video_inicial.mp4">Salvar MP4</a></div>';
 replay.querySelector('video').src=source;document.body.append(replay);
 const film=document.createElement('dialog');film.id='intro-film';film.setAttribute('aria-label','Apresentação inicial da investigação');
 film.innerHTML='<video id="intro-film-player" playsinline preload="auto" disablepictureinpicture disableremoteplayback aria-label="Apresentação inicial"></video><div id="intro-film-loading" role="status">Carregando apresentação…</div><div id="intro-film-error" hidden><h2>Não foi possível abrir a apresentação.</h2><p>Confira se a pasta do sistema contém o arquivo de vídeo e tente novamente. O tempo da rodada ainda não começou.</p><div><button id="intro-film-retry" type="button">Tentar novamente</button><button id="intro-film-back" type="button">Voltar à preparação</button></div></div>';
 document.body.append(film);
 const video=film.querySelector('video'),loading=film.querySelector('#intro-film-loading'),error=film.querySelector('#intro-film-error'),replayPlayer=replay.querySelector('video');
 const ready=document.createElement('div');ready.id='intro-film-ready';ready.innerHTML='<p>VIG.IA OS</p><h1>O arquivo corrompido.</h1><p>Uma equipe. Um mistério. Um prazo.</p><button id="intro-film-start" type="button">Iniciar <span aria-hidden="true">▶</span></button>';film.append(ready);
 const staffDialog=document.createElement('dialog');
 staffDialog.id='intro-staff';
 staffDialog.setAttribute('aria-labelledby','intro-staff-title');
 staffDialog.innerHTML=`<form>
  <h2 id="intro-staff-title">Acesso da organização</h2>
  <label>Senha <input type="password" required autocomplete="off" autofocus></label>
  <p id="intro-staff-error" role="status"></p>
  <div class="actions">
   <button type="button" data-cancel>Cancelar</button>
   <button class="primary" type="submit">Pular apresentação</button>
  </div>
 </form>`;
 document.body.append(staffDialog);
 const staffForm=staffDialog.querySelector('form');
 const staffPassword=staffForm.querySelector('input');
 const staffError=staffForm.querySelector('#intro-staff-error');
 video.src=source;video.controls=false;
 let active=false,finished=false,complete=null,cancel=null,furthest=0,generation=0;
 function failed(){if(!active)return;loading.hidden=true;ready.hidden=true;error.hidden=false;video.pause()}
 function playFirst(){
  loading.hidden=false;error.hidden=true;
  const round=generation;
  video.play().catch(()=>{if(active&&round===generation)failed()});
 }
 function reset(){generation++;active=false;finished=false;complete=null;cancel=null;furthest=0;staffDialog.close();video.pause();video.currentTime=0;replayPlayer.pause();replayPlayer.currentTime=0;ready.hidden=false;if(film.open)film.close();document.body.classList.remove('intro-film-active')}
 film.addEventListener('cancel',event=>event.preventDefault());
 film.addEventListener('contextmenu',event=>event.preventDefault());
 staffForm.querySelector('[data-cancel]').onclick=()=>staffDialog.close();
 function clearStaffForm(){staffForm.reset();staffError.textContent='';staffPassword.removeAttribute('aria-invalid')}
 staffDialog.addEventListener('close',clearStaffForm);
 staffPassword.addEventListener('input',()=>{
  staffError.textContent='';
  staffPassword.removeAttribute('aria-invalid');
 });
 staffForm.onsubmit=event=>{
  event.preventDefault();
  if(!active||!staffDialog.open)return;
  if(!VigiaSettings.acceptsTeamPassword(staffPassword.value)){
   staffPassword.value='';
   staffPassword.setAttribute('aria-invalid','true');
   staffError.textContent='Senha incorreta.';
   staffPassword.focus();
   return;
  }
  finish();
 };
 window.addEventListener('keydown',event=>{
  if(!active)return;
  if(event.ctrlKey&&event.altKey&&!event.shiftKey&&!event.metaKey&&event.code==='KeyP'){
   event.preventDefault();
   event.stopImmediatePropagation();
   if(!staffDialog.open){clearStaffForm();staffDialog.showModal();staffPassword.focus()}
   return;
  }
  if(staffDialog.open||!error.hidden||!ready.hidden)return;
  event.preventDefault();
  event.stopImmediatePropagation();
 },true);
 video.addEventListener('playing',()=>{loading.hidden=true;error.hidden=true});
 video.addEventListener('error',failed);
 video.addEventListener('timeupdate',()=>{if(active&&!video.seeking)furthest=Math.max(furthest,video.currentTime)});
 video.addEventListener('seeking',()=>{if(active&&video.currentTime>furthest+.5)video.currentTime=furthest});
 function finish(){
  if(!active)return;
  generation++;
  active=false;
  finished=true;
  video.pause();
  loading.hidden=true;
  staffDialog.close();
  document.body.classList.remove('intro-film-active');
  film.close();
  const callback=complete;
  complete=null;
  cancel=null;
  callback?.();
 }
 video.addEventListener('ended',()=>{
  if(video.ended&&Number.isFinite(video.duration)&&video.currentTime>=video.duration-.25)finish();
 });
 film.querySelector('#intro-film-retry').onclick=()=>{generation++;furthest=0;video.load();video.currentTime=0;playFirst()};
 film.querySelector('#intro-film-back').onclick=()=>{const callback=cancel;reset();callback?.()};
 ready.querySelector('button').onclick=()=>{ready.hidden=true;try{if(!document.fullscreenElement)document.documentElement.requestFullscreen?.().catch(()=>{})}catch{}playFirst()};
 window.VigiaIntroVideo={
  get active(){return active},get finished(){return finished},
  begin(onComplete,onCancel){
   if(active)return;
   if(finished){onComplete();return}
   generation++;active=true;complete=onComplete;cancel=onCancel;furthest=0;video.currentTime=0;video.playbackRate=1;
   document.body.classList.add('intro-film-active');film.showModal();video.pause();ready.hidden=false;loading.hidden=true;error.hidden=true;
   // Preparation opens the welcome screen; the participants' Start supplies sound.
   try{if(!document.fullscreenElement)document.documentElement.requestFullscreen?.().catch(()=>{})}catch{}
   ready.querySelector('button').focus();
  },
  replay(){if(!finished||active)return;replayPlayer.play().catch(()=>{})},
  stopReplay(){replayPlayer.pause();if(document.fullscreenElement===replayPlayer)document.exitFullscreen?.().catch(()=>{})},reset
 };
})();
