from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
SOURCE=ROOT/'output/vigia_os_sistema'
p=SOURCE/'feedback.js'
s=p.read_text(encoding='utf-8')
start=s.index(' function deadlineExpired(){')
end=s.index(' const forms=',start)
s=s[:start]+''' let failureActive=false;
 const failureTracks=[['failure-static','audio/failure/tv-static-noise-152056.mp3',.72],['failure-hum','audio/failure/electric-hum-141075.mp3',.58],['failure-glass','audio/failure/glass-cracking-504028.mp3',.86]].map(([id,src,volume])=>{
  const track=document.createElement('audio');track.id=id;track.src=src;track.volume=volume;track.loop=true;track.preload='auto';track.hidden=true;track.setAttribute('aria-hidden','true');document.body.append(track);track.addEventListener('canplay',()=>{if(failureActive&&enabled&&track.paused)track.play().catch(()=>{})});return track;
 });
 function playFailure(){if(!enabled||!failureActive)return;for(const track of failureTracks)if(track.paused)track.play().catch(()=>{})}
 function pauseFailure(){for(const track of failureTracks)track.pause()}
 function stopDeadline(){failureActive=false;pauseFailure();for(const track of failureTracks)track.currentTime=0}
 function deadlineExpired(){stop();stopClock();failureActive=true;if(enabled){prime();playFailure()}}
 document.addEventListener('pointerdown',()=>{if(failureActive)playFailure()},{passive:true});
''' +s[end:]
s=s.replace("if(!enabled){stop();stopClock()}else prime()","if(!enabled){stop();stopClock();pauseFailure()}else{prime();playFailure()}")
s=s.replace('stopClock,deadlineWarning,deadlineExpired,','stopClock,deadlineWarning,deadlineExpired,stopDeadline,')
s=s.replace("stop();stopClock()}\n };","stop();stopClock();stopDeadline()}\n };")
assert 'duration=4.8' not in s and 'stopDeadline()' in s
p.write_text(s,encoding='utf-8')
p=SOURCE/'index.html';s=p.read_text(encoding='utf-8')
s=s.replace('transmission-failure.css?v=1','catastrophic-failure.css?v=1').replace('transmission-failure.js?v=1','catastrophic-failure.js?v=1').replace('feedback.js?v=20261119-disk-corruption','feedback.js?v=20261119-pixabay-loop')
p.write_text(s,encoding='utf-8')
print('Pane visual e três loops locais integrados.')
