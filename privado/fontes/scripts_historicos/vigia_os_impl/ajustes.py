from pathlib import Path
root=Path(__file__).resolve().parents[2]/'output/vigia_os_sistema'
p=root/'desktop.js';s=p.read_text(encoding='utf-8')
s=s.replace("b.classList.contains('corrupted')?'corrupt':'recent'","b.classList.contains('corrupted')?'corrupt':'all'")
s=s.replace("files.querySelector('.file-tools').after(explorer);","files.querySelector('.file-tools').after(explorer);const footer=document.createElement('div');footer.className='explorer-footer';footer.append($('#file-count'));explorer.after(footer);")
s=s.replace("if(ev.pointerId!==e.pointerId)return;el.style.left=", "if(ev.pointerId!==e.pointerId)return;if(!(ev.buttons&1)){end(ev);return}el.style.left=")
s=s.replace("Math.max(104,Math.min(innerHeight-130,ev.clientY-dy))", "Math.max(parseFloat(getComputedStyle(document.documentElement).getPropertyValue('--os-top'))+17,Math.min(innerHeight-180,ev.clientY-dy))")
s=s.replace("const end=ev=>{if(ev.pointerId!==e.pointerId)return;", "const end=ev=>{if(ev.pointerId!==e.pointerId)return;")
# Typing and switching apps cannot move an abandoned drag capture.
s=s.replace("handle.addEventListener('pointercancel',end)})}","handle.addEventListener('pointercancel',end);handle.addEventListener('lostpointercapture',end,{once:true})})}")
p.write_text(s,encoding='utf-8')
p=root/'app.js';s=p.read_text(encoding='utf-8')
s=s.replace("if(['recovery','reconstruction'].includes(id))closePublicDialogs();", "if(['recovery','reconstruction'].includes(id)||$('#viewer').open&&!(id==='vigia'&&innerWidth>=1500))closePublicDialogs();")
# Keep focus scrolling inside the window, instead of scrolling fixed ancestors.
s=s.replace("target.scrollIntoView({block:'center',behavior:'instant'})", "const host=$('#window-body');host.scrollTop+=target.getBoundingClientRect().top-host.getBoundingClientRect().top-host.clientHeight/2+target.offsetHeight/2")
s=s.replace("$('#reply').scrollIntoView({block:'nearest',behavior:'smooth'});", "const host=$('#window-body');host.scrollTop+=Math.max(0,$('#reply').getBoundingClientRect().top-host.getBoundingClientRect().top-60);")
p.write_text(s,encoding='utf-8')
print('Ajustes de ergonomia e foco aplicados.')
