from pathlib import Path
p=Path(__file__).resolve().parents[2]/'output/vigia_os_sistema/app.js'
s=p.read_text(encoding='utf-8').replace("$('#timeline').hidden=!s.accessesConfirmed||s.protocolConfirmed;","$('#timeline').hidden=!s.accessesConfirmed||s.chronologyOrdered;")
s=s.replace("$('#closeviewer').onclick=()=>$('#viewer').close();", "$('#closeviewer').onclick=()=>$('#viewer').close();document.addEventListener('keydown',e=>{if(e.key==='Escape'&&$('#viewer').open&&!document.querySelector('dialog:modal')){e.preventDefault();$('#viewer').close()}});")
p.write_text(s,encoding='utf-8')
