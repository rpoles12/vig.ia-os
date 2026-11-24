from pathlib import Path
p=Path(__file__).resolve().parents[2]/'output/vigia_os_sistema/app.js'
s=p.read_text(encoding='utf-8')
old="$('#ending-frame').contentWindow?.rewindMovie?.();"
assert old in s
s=s.replace(old,"endingPlayer.pause();endingPlayer.currentTime=0;$('#ending-frame').contentWindow?.postMessage({type:'vigia-movie-state',time:0,paused:true,reset:true},'*');")
p.write_text(s,encoding='utf-8')
