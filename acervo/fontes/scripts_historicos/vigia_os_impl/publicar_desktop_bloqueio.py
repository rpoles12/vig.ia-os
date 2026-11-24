from pathlib import Path
import hashlib,json,shutil
ROOT=Path(__file__).resolve().parents[2]
SOURCE=ROOT/'output/vigia_os_sistema'
PACKAGE=Path(r'C:\Users\SEU_USUARIO\Desktop\Escape_Room_Pacote_Completo').resolve()
TARGET=PACKAGE/'02_SISTEMA_OFFLINE'
BACKUP=Path((ROOT/'tmp/vigia_os_impl/DESKTOP_LOCK_BACKUP.txt').read_text(encoding='utf-8'))
assert BACKUP.resolve().is_relative_to((ROOT/'tmp/backups').resolve())
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
for name in ['engine.js','data.js','countdown.js','feedback.js','ambient.js']:
    assert sha(SOURCE/name)==sha(TARGET/name),name
for name in ['app.js','desktop.js','index.html']:
    assert sha(TARGET/name)==sha(BACKUP/name),'Arquivo principal alterado: '+name
assert '750+bonus' in (SOURCE/'countdown.js').read_text(encoding='utf-8')
assert 'baseVolume=.40' in (SOURCE/'ambient.js').read_text(encoding='utf-8')
changed=[]
for p in SOURCE.rglob('*'):
    if not p.is_file():continue
    rel=p.relative_to(SOURCE);dst=TARGET/rel
    if dst.exists() and sha(p)==sha(dst):continue
    old=BACKUP/rel
    if dst.exists() and not old.exists():old.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(dst,old)
    dst.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(p,dst)
    assert sha(p)==sha(dst)
    changed.append(str(rel))
guide=PACKAGE/'05_DOCUMENTACAO/VIGIA_OS_IMPLEMENTADO.md'
shutil.copy2(guide,BACKUP/'guia_principal.md');shutil.copy2(SOURCE/'VIGIA_OS_LEIA-ME.md',guide)
reports=PACKAGE/'05_DOCUMENTACAO/Registros_de_verificacao'
for src,dst in [('desktop_contexto.png','DESKTOP_CONTEXTO_20261119.png'),('tela_azul_bloqueada.png','TELA_AZUL_BLOQUEADA_20261119.png')]:
    shutil.copy2(ROOT/'tmp/vigia_os_impl'/src,reports/dst)
report={'date':'2026-11-19','changes':changed,'backup':str(BACKUP),'browser':{'icon_drag_does_not_launch_app':True,'positions_preserved_between_apps':True,'icon_bounds_above_taskbar':True,'context_menu_mouse_and_keyboard':True,'context_menu_open_notes':True,'refresh_preserves_position_and_countdown':True,'organize_restores_grid':True,'reset_clears_positions':True,'isolated_expiry_seconds':12,'blue_screen_escape_repeated_blocked':True,'blue_screen_alt2_blocked':True,'desktop_inert_and_hidden_on_expiry':True,'operator_auth_cancel_stays_locked':True,'operator_authorized_overtime_unlocks':True},'automated':{'game':json.loads((ROOT/'tmp/vigia_os_impl/motor.json').read_text(encoding='utf-8')),'sound':json.loads((ROOT/'tmp/vigia_os_impl/som.json').read_text(encoding='utf-8')),'music':json.loads((ROOT/'tmp/vigia_os_impl/trilha.json').read_text(encoding='utf-8'))},'production_preserved':{'initial_seconds':750,'bonus_seconds':15,'ambient_volume':.4,'key_and_evidence':True},'limitations':['A abertura file:// é bloqueada pela política do navegador de teste; testes de interface feitos em HTTP local.']}
(reports/'DESKTOP_BLOQUEIO_20261119.json').write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf-8')
inventory=PACKAGE/'INVENTARIO_PACOTE.json';shutil.copy2(inventory,BACKUP/inventory.name)
files=[{'arquivo':str(p.relative_to(PACKAGE)),'bytes':p.stat().st_size,'sha256':sha(p)} for p in sorted(PACKAGE.rglob('*')) if p.is_file() and p.name!='INVENTARIO_PACOTE.json']
inventory.write_text(json.dumps({'revisao':'2026-11-19 VIG.IA — desktop e bloqueio persistente','pasta':str(PACKAGE),'quantidade_arquivos':len(files),'total_bytes':sum(x['bytes'] for x in files),'arquivos':files},ensure_ascii=False,indent=2),encoding='utf-8')
result={'updated_files':len(changed),'package_files':len(files),'backup':str(BACKUP),'entry':str(TARGET/'index.html'),'production_duration_preserved':True}
(ROOT/'tmp/vigia_os_impl/PUBLICACAO_DESKTOP_BLOQUEIO.json').write_text(json.dumps(result,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps(result,ensure_ascii=False))
