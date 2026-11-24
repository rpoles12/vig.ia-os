from pathlib import Path
import shutil, datetime
ROOT=Path(__file__).resolve().parents[2]
BASE=ROOT/'output/vigia_os_sistema'
BACKUP=ROOT/'tmp/backups'/('player_cursores_'+datetime.datetime.now().strftime('%Y%m%d_%H%M%S'))
BACKUP.mkdir(parents=True)
for name in ['desktop.js','os-v2.css','index.html']:
    shutil.copy2(BASE/name,BACKUP/name)
p=BASE/'desktop.js';s=p.read_text(encoding='utf-8')
start=s.index('<div id="mini-player">');end=s.index('<div id="bar-status">',start)
s=s[:start]+'''<div id="mini-player" role="group" aria-label="Player rápido de áudio"><button id="mini-toggle" aria-label="Reproduzir áudio">${glyph('play')}</button><div class="mini-content"><button id="mini-open" title="Abrir player de áudios"><span id="mini-title">Mensagem inicial</span><span class="mini-meta"><small id="mini-state">Pronto para ouvir</small><time id="mini-time">00:00</time></span></button><input id="mini-seek" type="range" min="0" max="100" step=".1" value="0" aria-label="Posição do áudio na barra de tarefas" disabled></div><button id="mini-options" aria-label="Opções do áudio" aria-expanded="false" aria-controls="mini-menu" title="Opções do áudio"><svg class="icon" viewBox="0 0 24 24" aria-hidden="true"><circle cx="5" cy="12" r="1.5"/><circle cx="12" cy="12" r="1.5"/><circle cx="19" cy="12" r="1.5"/></svg></button><div id="mini-menu" hidden><div class="mini-menu-heading"><span>Áudio da investigação</span><small id="mini-volume-value">100%</small></div><div class="mini-volume-row"><button id="mini-mute" aria-label="Silenciar narração" title="Silenciar narração">${glyph('audio')}</button><label><span class="sr-only">Volume da narração</span><input id="mini-volume" class="os-volume" type="range" min="0" max="1" step=".05" value="1" aria-label="Volume da narração"></label></div><button id="mini-transcript">${glyph('file')}<span>Ler transcrição</span></button><button id="mini-full-player">${glyph('audio')}<span>Abrir player completo</span>${glyph('arrow')}</button></div></div>'''+s[end:]
s=s.replace("$('#mini-open').onclick=()=>launch('media');", "$('#mini-open').onclick=()=>{closeAudioMenu();launch('media')};")
s=s.replace("$('#mini-transcript').onclick=$('#audio-app-transcript').onclick=()=>VigiaSession?.transcribe(selectedAudio);", "$('#mini-transcript').onclick=$('#audio-app-transcript').onclick=()=>{closeAudioMenu();VigiaSession?.transcribe(selectedAudio)};")
anchor=" const ft=t=>"
assert s.count(anchor)==1
s=s.replace(anchor,""" function closeAudioMenu(){ $('#mini-menu').hidden=true;$('#mini-options').setAttribute('aria-expanded','false') }
 $('#mini-options').onclick=()=>{const menu=$('#mini-menu');menu.hidden=!menu.hidden;$('#mini-options').setAttribute('aria-expanded',String(!menu.hidden))};
 $('#mini-full-player').onclick=()=>{closeAudioMenu();launch('media')};
 $('#mini-seek').oninput=e=>{if(Number.isFinite(player.duration)&&player.duration)player.currentTime=Number(e.target.value)/100*player.duration};
 let lastNarrationVolume=1;
 $('#mini-mute').onclick=()=>{if(player.volume>0){lastNarrationVolume=player.volume;player.volume=0}else player.volume=lastNarrationVolume||1;$('#ending-audio').volume=player.volume};
 document.addEventListener('pointerdown',e=>{if(!$('#mini-player').contains(e.target))closeAudioMenu()});
 document.addEventListener('keydown',e=>{if(e.key==='Escape'&&!$('#mini-menu').hidden){e.preventDefault();e.stopImmediatePropagation();closeAudioMenu();$('#mini-options').focus()}},true);
 const ft=t=>""")
start=s.index(' function audioUpdate(){');end=s.index(" ['play','pause'",start)
s=s[:start]+''' function audioUpdate(){
  const hasAudio=!!player.getAttribute('src'),playing=hasAudio&&!player.paused&&!player.ended;
  const control=$('#mini-toggle'),mode=playing?'pause':'play';
  if(control.dataset.mode!==mode){control.dataset.mode=mode;control.innerHTML=glyph(mode)}
  control.setAttribute('aria-label',playing?'Pausar áudio':'Reproduzir áudio');control.title=playing?'Pausar áudio':'Reproduzir áudio';
  $('#mini-player').classList.toggle('is-playing',playing);
  $('#audio-app-toggle').textContent=playing?'Ⅱ':'▶';
  $('#mini-title').textContent=audioTitle.replace(/^Fragmento \\d+ · /,'');
  $('#mini-open').title='Abrir player · '+audioTitle;$('#mini-open').setAttribute('aria-label','Abrir player: '+audioTitle);
  $('#mini-state').textContent=playing?'Reproduzindo':player.ended?'Concluído':hasAudio?'Pausado':'Pronto para ouvir';
  $('#audio-app-title').textContent=audioTitle;
  const duration=Number.isFinite(player.duration)&&player.duration>0,progress=duration?player.currentTime/player.duration*100:0;
  $('#mini-time').textContent=ft(player.currentTime)+(duration?' / '+ft(player.duration):'');
  $('#audio-app-time').textContent=ft(player.currentTime)+' / '+ft(player.duration);$('#audio-seek').value=progress;
  const seek=$('#mini-seek');seek.value=progress;seek.disabled=!duration;seek.style.setProperty('--progress',progress+'%');seek.setAttribute('aria-valuetext',ft(player.currentTime)+(duration?' de '+ft(player.duration):''));
  $('.audio-console').classList.toggle('is-playing',playing);
  document.querySelectorAll('.os-volume').forEach(el=>el.value=player.volume);
  $('#mini-volume-value').textContent=Math.round(player.volume*100)+'%';
  $('#mini-mute').setAttribute('aria-label',player.volume===0?'Reativar narração':'Silenciar narração');$('#mini-mute').title=player.volume===0?'Reativar narração':'Silenciar narração';$('#mini-mute').classList.toggle('is-muted',player.volume===0);
  document.querySelectorAll('[data-audio-id]').forEach(el=>el.classList.toggle('is-active',el.dataset.audioId===selectedAudio))
 }
'''+s[end:]
s=s.replace("function visibility(hidden,final){", "function visibility(hidden,final){if(hidden||final)closeAudioMenu();")
s=s.replace("reset(){home();", "reset(){closeAudioMenu();lastNarrationVolume=1;home();")
p.write_text(s,encoding='utf-8')
p=BASE/'index.html';s=p.read_text(encoding='utf-8').replace('</head>','<link rel="stylesheet" href="taskbar-player.css?v=1"></head>').replace('desktop.js?v=vigia-os-2-typing','desktop.js?v=vigia-os-2-player');p.write_text(s,encoding='utf-8')
shutil.copy2(BASE/'desktop.js',ROOT/'producao/vigia_os_impl/desktop_v2.js')
print('Player reorganizado. Backup:',BACKUP)
