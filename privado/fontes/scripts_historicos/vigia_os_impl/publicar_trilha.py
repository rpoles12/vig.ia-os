from pathlib import Path
import json,hashlib,shutil
ROOT=Path(__file__).resolve().parents[2]
SOURCE=ROOT/'output/vigia_os_sistema'
PACKAGE=Path(r'C:\Users\45061155890\Desktop\Escape_Room_Pacote_Completo').resolve()
TARGET=PACKAGE/'02_SISTEMA_OFFLINE'
BACKUP=Path((ROOT/'tmp/vigia_os_impl/TRILHA_BACKUP.txt').read_text(encoding='utf-8'))
assert BACKUP.resolve().is_relative_to((ROOT/'tmp/backups').resolve())
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
for name in ['engine.js','data.js','countdown.js','feedback.js']:
    assert sha(SOURCE/name)==sha(TARGET/name),name
for name in ['app.js','index.html']:
    assert sha(TARGET/name)==sha(BACKUP/name),'Arquivo principal mudou: '+name
assert sha(SOURCE/'audio/trilha/long-note-one.mp3')=='665aef3a5eaba25a0108f632e85895516868813a764a58bc203702829ac4c6c1'
changed=[]
for p in SOURCE.rglob('*'):
    if not p.is_file():continue
    rel=p.relative_to(SOURCE);dst=TARGET/rel
    if dst.exists() and sha(dst)==sha(p):continue
    if dst.exists():
        old=BACKUP/rel
        if not old.exists():old.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(dst,old)
    dst.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(p,dst)
    assert sha(p)==sha(dst)
    changed.append(str(rel))
guide=PACKAGE/'05_DOCUMENTACAO/VIGIA_OS_IMPLEMENTADO.md'
if not (BACKUP/'guia_principal.md').exists():shutil.copy2(guide,BACKUP/'guia_principal.md')
shutil.copy2(SOURCE/'VIGIA_OS_LEIA-ME.md',guide)
reports=PACKAGE/'05_DOCUMENTACAO/Registros_de_verificacao'
shutil.copy2(ROOT/'tmp/vigia_os_impl/trilha_ambiente.png',reports/'TRILHA_AMBIENTE_20261119.png')
report={'date':'2026-11-19','track':json.loads((SOURCE/'audio/trilha/licenca.json').read_text(encoding='utf-8')),'volume':{'ambient':.16,'ducking_multiplier':.12,'during_narration_video':.0192,'fade_down_ms':180,'fade_up_ms':1100},'behavior':{'same_track_loop_all_stages':True,'starts_on_user_start':True,'independent_mute_and_volume':True,'blue_screen_effect_ducks_music':True,'reset_stops_and_rewinds':True,'offline_local_mp3':True},'tests':{'audio_behavior':json.loads((ROOT/'tmp/vigia_os_impl/trilha.json').read_text(encoding='utf-8')),'game_rules':json.loads((ROOT/'tmp/vigia_os_impl/motor.json').read_text(encoding='utf-8')),'browser':{'mp3_duration_seconds':440,'narration_duck_and_pause_restore':True,'video_duck_and_pause_restore':True,'same_source_and_continuing_position_across_phases':True,'mute_restore':True,'reset_stopped_at_zero':True,'console_errors':0}},'changed':changed,'backup':str(BACKUP),'limitations':['Conferir o balanço de volume no equipamento do evento.','A política do navegador de teste bloqueia file://; percurso conferido em HTTP local.']}
(reports/'TRILHA_AMBIENTE_20261119.json').write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf-8')
inventory=PACKAGE/'INVENTARIO_PACOTE.json'
if not (BACKUP/inventory.name).exists():shutil.copy2(inventory,BACKUP/inventory.name)
files=[{'arquivo':str(p.relative_to(PACKAGE)),'bytes':p.stat().st_size,'sha256':sha(p)} for p in sorted(PACKAGE.rglob('*')) if p.is_file() and p.name!='INVENTARIO_PACOTE.json']
inventory.write_text(json.dumps({'revisao':'2026-11-19 VIG.IA — trilha ambiente','pasta':str(PACKAGE),'quantidade_arquivos':len(files),'total_bytes':sum(f['bytes'] for f in files),'arquivos':files},ensure_ascii=False,indent=2),encoding='utf-8')
result={'track':'Long note One — Kevin MacLeod','changed_files':len(changed),'package_files':len(files),'backup':str(BACKUP),'entry':str(TARGET/'index.html'),'download_sha256_verified':True}
(ROOT/'tmp/vigia_os_impl/PUBLICACAO_TRILHA.json').write_text(json.dumps(result,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps(result,ensure_ascii=False))
