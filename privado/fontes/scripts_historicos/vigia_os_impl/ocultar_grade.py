from pathlib import Path
import hashlib,json,shutil,datetime
root=Path(__file__).resolve().parents[2]
source=root/'output/vigia_os_sistema'
package=Path(r'C:\Users\45061155890\Desktop\Escape_Room_Pacote_Completo')
target=package/'02_SISTEMA_OFFLINE'
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
assert sha(source/'desktop-interactions.js')==sha(target/'desktop-interactions.js')
css=(source/'desktop-interactions.css').read_text(encoding='utf-8')
assert '.desktop-grid{display:none}' in css and '.desktop-grid{opacity:1}' not in css
backup=root/'tmp/backups'/('grade_invisivel_'+datetime.datetime.now().strftime('%Y%m%d_%H%M%S'))
backup.mkdir(parents=True)
for name in ['desktop-interactions.css','index.html','VIGIA_OS_LEIA-ME.md','VIGIA_OS_V2.md']:
    shutil.copy2(target/name,backup/name)
    shutil.copy2(source/name,target/name)
    assert sha(source/name)==sha(target/name)
guide=package/'05_DOCUMENTACAO/VIGIA_OS_IMPLEMENTADO.md'
shutil.copy2(guide,backup/'guia_principal.md')
shutil.copy2(source/'VIGIA_OS_LEIA-ME.md',guide)
inventory=package/'INVENTARIO_PACOTE.json'
shutil.copy2(inventory,backup/inventory.name)
data=json.loads(inventory.read_text(encoding='utf-8'))
for item in data['arquivos']:
    p=package/item['arquivo'];item.update(bytes=p.stat().st_size,sha256=sha(p))
data['total_bytes']=sum(x['bytes'] for x in data['arquivos'])
data['revisao']='2026-11-19 VIG.IA — encaixe dos atalhos com grade invisível'
inventory.write_text(json.dumps(data,ensure_ascii=False,indent=2),encoding='utf-8')
print('Grade oculta; encaixe e troca de posições preservados. Backup: '+str(backup))
