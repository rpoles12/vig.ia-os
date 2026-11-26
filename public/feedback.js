(()=>{
 'use strict';
 let context=null,enabled=true,active=[],clockNodes=[];
 const toggle=document.createElement('button');
 toggle.type='button';toggle.id='sound-effects';toggle.textContent='Efeitos sonoros: ligados';toggle.setAttribute('aria-pressed','true');toggle.setAttribute('aria-label','Ativar ou silenciar efeitos sonoros');
 document.querySelector('.public-footer').append(toggle);
 toggle.onclick=()=>{enabled=!enabled;toggle.textContent='Efeitos sonoros: '+(enabled?'ligados':'desligados');toggle.setAttribute('aria-pressed',String(enabled));if(!enabled){stop();stopClock();pauseFailure()}else{prime();playFailure()}};
 function prime(){if(!enabled)return;try{const Audio=window.AudioContext||window.webkitAudioContext;if(!Audio)return;context??=new Audio();if(context.state==='suspended')context.resume().catch(()=>{})}catch{}}
 function stop(){for(const oscillator of active){try{oscillator.stop()}catch{}}active=[]}
 function sound(kind){
  if(!enabled)return;
  try{
   const Audio=window.AudioContext||window.webkitAudioContext;if(!Audio)return;
   context??=new Audio();
   const notes=kind==='error'?[[220,0,.18],[165,.22,.18],[110,.44,.34]]:kind==='complete'?[[659,0,.14],[880,.18,.14],[1047,.36,.23],[659,.72,.14],[880,.90,.14],[1047,1.08,.30]]:[[523,0,.10],[659,.11,.10],[880,.23,.14]];
   const start=()=>{
    if(!enabled)return;
    stop();
    const narration=document.getElementById('audio-player');
    const speaking=narration&&!narration.paused&&!narration.ended;
    const volume=(kind==='error'?.23:.12)*(speaking?.25:1);
    const base=context.currentTime+.015;
    for(const [frequency,offset,duration] of notes){
     const osc=context.createOscillator(),gain=context.createGain(),when=base+offset;
     osc.type=kind==='error'?'sawtooth':'triangle';osc.frequency.value=frequency;if(kind==='error')osc.frequency.exponentialRampToValueAtTime(frequency*.8,when+duration);gain.gain.setValueAtTime(0,when);gain.gain.linearRampToValueAtTime(volume,when+.012);gain.gain.exponentialRampToValueAtTime(.0001,when+duration);
     osc.connect(gain);gain.connect(context.destination);osc.start(when);osc.stop(when+duration+.015);active.push(osc);
     osc.onended=()=>{osc.disconnect();gain.disconnect();active=active.filter(x=>x!==osc)};
    }
   };
   if(context.state==='suspended')context.resume().then(start).catch(()=>{});else start();
  }catch{/* Feedback visual sempre funciona mesmo sem dispositivo de áudio. */}
 }
 function stopClock(){for(const node of clockNodes){try{node.stop()}catch{}}clockNodes=[]}
 function clockTick(high){
  if(!enabled)return;
  try{
   const Audio=window.AudioContext||window.webkitAudioContext;if(!Audio)return;context??=new Audio();
   const tick=()=>{
    if(!enabled)return;
    const osc=context.createOscillator(),gain=context.createGain(),when=context.currentTime+.005;
    osc.type='triangle';osc.frequency.setValueAtTime(high?1800:1250,when);osc.frequency.exponentialRampToValueAtTime(high?750:520,when+.045);
    gain.gain.setValueAtTime(.0001,when);gain.gain.exponentialRampToValueAtTime(.15,when+.002);gain.gain.exponentialRampToValueAtTime(.0001,when+.065);
    osc.connect(gain);gain.connect(context.destination);osc.start(when);osc.stop(when+.07);clockNodes.push(osc);
    osc.onended=()=>{osc.disconnect();gain.disconnect();clockNodes=clockNodes.filter(x=>x!==osc)};
   };
   if(context.state==='suspended')context.resume().then(tick).catch(()=>{});else tick();
  }catch{/* A contagem visual permanece independente do áudio. */}
 }
 function deadlineTone(notes,volume=.22){
  if(!enabled)return;
  try{
   const Audio=window.AudioContext||window.webkitAudioContext;if(!Audio)return;context??=new Audio();
   const play=()=>{if(!enabled)return;for(const [frequency,offset,duration] of notes){
    const osc=context.createOscillator(),gain=context.createGain(),when=context.currentTime+.01+offset;
    osc.type='triangle';osc.frequency.setValueAtTime(frequency,when);osc.frequency.exponentialRampToValueAtTime(frequency*.63,when+duration);
    gain.gain.setValueAtTime(.0001,when);gain.gain.exponentialRampToValueAtTime(volume,when+.012);gain.gain.exponentialRampToValueAtTime(.0001,when+duration);
    osc.connect(gain);gain.connect(context.destination);osc.start(when);osc.stop(when+duration+.01);active.push(osc);
    osc.onended=()=>{osc.disconnect();gain.disconnect();active=active.filter(x=>x!==osc)};
   }};if(context.state==='suspended')context.resume().then(play).catch(()=>{});else play();
  }catch{/* A indicação visual independe do dispositivo de som. */}
 }
 function deadlineWarning(urgent,seconds){
  if(urgent){
   const pitch=seconds%2===0?1540:1100;
   deadlineTone([[pitch,0,.075],[pitch*.58,.13,.07]],.28);
   if(seconds===10)deadlineTone([[310,.25,.32],[440,.59,.27]]);
   return;
  }
  const pitch=seconds<=15?920:seconds<=30?770:620;
  const notes=[[pitch,0,.22],[pitch*.78,.27,.22],[pitch,.54,.29]];
  if(seconds<=30)notes.push([pitch*.58,.88,.34]);
  deadlineTone(notes);
 }
 let failureActive=false;
 const failureTracks=[['failure-static','audio/failure/tv-static-noise-152056.mp3',.72],['failure-hum','audio/failure/electric-hum-141075.mp3',.58],['failure-glass','audio/failure/glass-cracking-504028.mp3',.86]].map(([id,src,volume])=>{
  const track=document.createElement('audio');track.id=id;track.src=src;track.volume=volume;track.loop=true;track.preload='auto';track.hidden=true;track.setAttribute('aria-hidden','true');document.body.append(track);track.addEventListener('canplay',()=>{if(failureActive&&enabled&&track.paused)track.play().catch(()=>{})});return track;
 });
 function playFailure(){if(!enabled||!failureActive)return;for(const track of failureTracks)if(track.paused)track.play().catch(()=>{})}
 function pauseFailure(){for(const track of failureTracks)track.pause()}
 function stopDeadline(){failureActive=false;pauseFailure();for(const track of failureTracks)track.currentTime=0}
 function deadlineExpired(){stop();stopClock();failureActive=true;if(enabled){prime();playFailure()}}
 document.addEventListener('pointerdown',()=>{if(failureActive)playFailure()},{passive:true});
 const forms=['identity','accessform','finalform'].map(id=>document.getElementById(id));
 function clearField(input){
  input.removeAttribute('aria-invalid');input.classList.remove('field-invalid','field-confirmed');
  const error=document.getElementById(input.dataset.feedbackId);
  if(error)error.hidden=true;
  const described=(input.getAttribute('aria-describedby')||'').split(' ').filter(id=>id&&id!==input.dataset.feedbackId);
  if(described.length)input.setAttribute('aria-describedby',described.join(' '));else input.removeAttribute('aria-describedby');
 }
 function clear(form){form.querySelectorAll('input').forEach(clearField);form.classList.remove('has-field-errors')}
 for(const form of forms){
  form.noValidate=true;
  for(const input of form.querySelectorAll('input')){
   const label=input.closest('label');
   if(!input.hasAttribute('aria-label'))input.setAttribute('aria-label',[...label.childNodes].filter(n=>n.nodeType===3).map(n=>n.textContent).join(' ').trim());
   const error=document.createElement('small');error.id=form.id+'-'+input.name+'-error';error.className='field-error';error.hidden=true;label.append(error);input.dataset.feedbackId=error.id;
   input.addEventListener('input',()=>{clearField(input);if(!form.querySelector('[aria-invalid="true"]'))form.classList.remove('has-field-errors')});
  }
  form.addEventListener('reset',()=>clear(form));
 }
 window.VigiaFeedback={prime,clockTick,stopClock,deadlineWarning,deadlineExpired,stopDeadline,
  apply(result,form){
   if(form){
    clear(form);
    const errors=result.fields||[];
    for(const item of errors){
     const input=form.elements.namedItem(item.field);if(!input)continue;
     input.setAttribute('aria-invalid','true');input.classList.add('field-invalid');
     const error=document.getElementById(input.dataset.feedbackId);error.textContent='⚠ '+(input.value.trim()?item.message:'Preencha este campo antes de confirmar.');error.hidden=false;
     input.setAttribute('aria-describedby',((input.getAttribute('aria-describedby')||'')+' '+error.id).trim());
    }
    if(errors.length){form.classList.add('has-field-errors');form.querySelector('[aria-invalid="true"]')?.focus()}
   }
   const chronology=document.getElementById('timeline-work');
   if(!form)chronology.classList.toggle('has-sequence-error',!result.ok);
   if(result.ok)chronology.classList.remove('has-sequence-error');
   sound(result.ok?(result.protocol?'complete':'success'):'error');
  },
  reset(){forms.forEach(clear);document.getElementById('timeline-work').classList.remove('has-sequence-error');stop();stopClock();stopDeadline()}
 };
})();
