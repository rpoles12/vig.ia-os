from pathlib import Path
import hashlib,json,shutil,datetime
ROOT=Path(__file__).resolve().parents[2]
SOURCE=ROOT/'output/vigia_os_sistema'
PACKAGE=Path(r'C:\Users\45061155890\Desktop\Escape_Room_Pacote_Completo')
TARGET=PACKAGE/'02_SISTEMA_OFFLINE'
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
for name in ['engine.js','data.js','countdown.js','ambient.js','desktop-interactions.js','desktop-interactions.css']:
    assert sha(SOURCE/name)==sha(TARGET/name),name
assert '750+bonus' in (SOURCE/'countdown.js').read_text(encoding='utf-8')
assert 'baseVolume=.40' in (SOURCE/'ambient.js').read_text(encoding='utf-8')
assert 'transmission-failure.js?v=1' in (SOURCE/'index.html').read_text(encoding='utf-8')
names=['transmission-failure.js','transmission-failure.css','desktop.js','feedback.js','app.js','index.html','VIGIA_OS_LEIA-ME.md','VIGIA_OS_V2.md']
backup=ROOT/'tmp/backups'/('falha_transmissao_'+datetime.datetime.now().strftime('%Y%m%d_%H%M%S'))
backup.mkdir(parents=True)
for name in names:
    if (TARGET/name).exists():shutil.copy2(TARGET/name,backup/name)
    shutil.copy2(SOURCE/name,TARGET/name)
    assert sha(SOURCE/name)==sha(TARGET/name)
guide=PACKAGE/'05_DOCUMENTACAO/VIGIA_OS_IMPLEMENTADO.md'
shutil.copy2(guide,backup/'guia_principal.md')
shutil.copy2(SOURCE/'VIGIA_OS_LEIA-ME.md',guide)
reports=PACKAGE/'05_DOCUMENTACAO/Registros_de_verificacao'
shutil.copy2(ROOT/'tmp/vigia_os_impl/falha_transmissao.png',reports/'FALHA_TRANSMISSAO_20261119.png')
report={'date':'2026-11-19','changes':names,'backup':str(backup),'browser':{'isolated_qa_timeout_seconds':12,'expiry_shows_transmission_failure':True,'binary_and_error_streams':38,'escape_does_not_dismiss':True,'desktop_inert_on_expiry':True,'cancel_operator_auth_stays_locked':True,'authorized_overtime_hides_failure_and_unlocks':True,'viewport_390x844_panel_fits':True,'console_errors':[]},'sound':{'duration_seconds':4.8,'peak_gain':.85,'ambient_duck_ms':5500,'automated':json.loads((ROOT/'tmp/vigia_os_impl/som.json').read_text(encoding='utf-8')),'physical_event_speaker_listening':'not verified'},'game':json.loads((ROOT/'tmp/vigia_os_impl/motor.json').read_text(encoding='utf-8')),'music':json.loads((ROOT/'tmp/vigia_os_impl/trilha.json').read_text(encoding='utf-8')),'preserved':{'production_countdown_seconds':750,'stage_bonus_seconds':15,'ambient_volume':.4,'grid_invisible':True}}
(reports/'FALHA_TRANSMISSAO_20261119.json').write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf-8')
inventory=PACKAGE/'INVENTARIO_PACOTE.json'
shutil.copy2(inventory,backup/inventory.name)
files=[{'arquivo':str(p.relative_to(PACKAGE)),'bytes':p.stat().st_size,'sha256':sha(p)} for p in sorted(PACKAGE.rglob('*')) if p.is_file() and p!=inventory]
inventory.write_text(json.dumps({'revisao':'2026-11-19 VIG.IA — falha de transmissão e disco corrompido','pasta':str(PACKAGE),'quantidade_arquivos':len(files),'total_bytes':sum(x['bytes'] for x in files),'arquivos':files},ensure_ascii=False,indent=2),encoding='utf-8')
result={'updated':names,'backup':str(backup),'package_files':len(files),'entry':str(TARGET/'index.html')}
(ROOT/'tmp/vigia_os_impl/PUBLICACAO_FALHA_TRANSMISSAO.json').write_text(json.dumps(result,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps(result,ensure_ascii=False))
