from pathlib import Path
import hashlib, json, shutil, datetime
root=Path.cwd(); source=root/'output/vigia_os_sistema'; package=Path(r'C:\Users\45061155890\Desktop\Escape_Room_Pacote_Completo'); target=package/'02_SISTEMA_OFFLINE'
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
for name in ['catastrophic-failure.js','engine.js','countdown.js','session-settings.js']:
 assert sha(source/name)==sha(target/name),name
assert '#time-up:not([hidden]),#time-up:not([hidden]) *{cursor:none!important}' in (source/'catastrophic-failure.css').read_text(encoding='utf-8')
assert 'catastrophic-failure.css?v=2-cursor-hidden' in (source/'index.html').read_text(encoding='utf-8')
backup=root/'tmp/backups'/('cursor_pane_'+datetime.datetime.now().strftime('%Y%m%d_%H%M%S'));backup.mkdir(parents=True)
for name in ['catastrophic-failure.css','index.html']:
 shutil.copy2(target/name,backup/name);shutil.copy2(source/name,target/name);assert sha(source/name)==sha(target/name)
inventory=package/'INVENTARIO_PACOTE.json';shutil.copy2(inventory,backup/inventory.name)
files=[{'arquivo':str(p.relative_to(package)),'bytes':p.stat().st_size,'sha256':sha(p)} for p in sorted(package.rglob('*')) if p.is_file() and p!=inventory]
inventory.write_text(json.dumps({'revisao':'2026-11-19 VIG.IA — cursor oculto na pane','pasta':str(package),'quantidade_arquivos':len(files),'total_bytes':sum(x['bytes'] for x in files),'arquivos':files},ensure_ascii=False,indent=2),encoding='utf-8')
print('Atualizado:',target,'Backup:',backup)
