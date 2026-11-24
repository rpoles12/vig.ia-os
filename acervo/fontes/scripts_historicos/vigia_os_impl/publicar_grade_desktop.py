from pathlib import Path
import hashlib,json,shutil,datetime
ROOT=Path(__file__).resolve().parents[2]
SOURCE=ROOT/'output/vigia_os_sistema'
PACKAGE=Path(r'C:\Users\SEU_USUARIO\Desktop\Escape_Room_Pacote_Completo').resolve()
TARGET=PACKAGE/'02_SISTEMA_OFFLINE'
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
for name in ['app.js','desktop.js','engine.js','data.js','countdown.js','ambient.js','feedback.js']:
    assert sha(SOURCE/name)==sha(TARGET/name),name
names=['desktop-interactions.js','desktop-interactions.css','index.html','VIGIA_OS_LEIA-ME.md','VIGIA_OS_V2.md']
assert all((TARGET/name).is_file() for name in names)
BACKUP=ROOT/'tmp/backups'/('grade_desktop_'+datetime.datetime.now().strftime('%Y%m%d_%H%M%S'))
BACKUP.mkdir(parents=True)
for name in names:
    shutil.copy2(TARGET/name,BACKUP/name)
    shutil.copy2(SOURCE/name,TARGET/name)
    assert sha(SOURCE/name)==sha(TARGET/name)
guide=PACKAGE/'05_DOCUMENTACAO/VIGIA_OS_IMPLEMENTADO.md'
shutil.copy2(guide,BACKUP/'guia_principal.md')
shutil.copy2(SOURCE/'VIGIA_OS_LEIA-ME.md',guide)
reports=PACKAGE/'05_DOCUMENTACAO/Registros_de_verificacao'
shutil.copy2(ROOT/'tmp/vigia_os_impl/grade_desktop.png',reports/'GRADE_DESKTOP_20261119.png')
report={'date':'2026-11-19','changes':names,'backup':str(BACKUP),'browser':{'occupied_cell_swaps_icons':True,'free_drop_snaps_to_cell':True,'refresh_preserves_positions':True,'arrange_restores_initial_grid':True,'edge_drop_stays_above_taskbar':True,'viewport_1280x720_no_overlap':True,'viewport_390x844_no_overlap':True,'viewport_600x400_no_overlap':True,'console_errors':[]},'game':json.loads((ROOT/'tmp/vigia_os_impl/motor.json').read_text(encoding='utf-8'))}
(reports/'GRADE_DESKTOP_20261119.json').write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf-8')
inventory=PACKAGE/'INVENTARIO_PACOTE.json'
shutil.copy2(inventory,BACKUP/inventory.name)
files=[{'arquivo':str(p.relative_to(PACKAGE)),'bytes':p.stat().st_size,'sha256':sha(p)} for p in sorted(PACKAGE.rglob('*')) if p.is_file() and p!=inventory]
inventory.write_text(json.dumps({'revisao':'2026-11-19 VIG.IA — grade de atalhos sem sobreposição','pasta':str(PACKAGE),'quantidade_arquivos':len(files),'total_bytes':sum(x['bytes'] for x in files),'arquivos':files},ensure_ascii=False,indent=2),encoding='utf-8')
result={'updated':names,'backup':str(BACKUP),'package_files':len(files),'entry':str(TARGET/'index.html')}
(ROOT/'tmp/vigia_os_impl/PUBLICACAO_GRADE_DESKTOP.json').write_text(json.dumps(result,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps(result,ensure_ascii=False))
