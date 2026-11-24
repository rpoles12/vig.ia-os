from pathlib import Path
import hashlib,json,shutil,datetime
ROOT=Path(__file__).resolve().parents[2]
SOURCE=ROOT/'output/vigia_os_sistema'
PACKAGE=Path(r'C:\Users\SEU_USUARIO\Desktop\Escape_Room_Pacote_Completo')
TARGET=PACKAGE/'02_SISTEMA_OFFLINE'
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
for name in ['data.js','countdown.js','ambient.js','feedback.js','desktop-interactions.js','desktop-interactions.css','transmission-failure.js','transmission-failure.css','encerramento/filme/filme.js']:
    assert sha(SOURCE/name)==sha(TARGET/name),name
assert 'configurarEtapas' in (SOURCE/'engine.js').read_text(encoding='utf-8')
assert 'stages:Object.freeze' in (SOURCE/'session-settings.js').read_text(encoding='utf-8')
settings=(SOURCE/'session-settings.js').read_text(encoding='utf-8')
assert 'localStorage' not in settings and 'sessionStorage' not in settings
names=['engine.js','vigia.js','desktop.js','app.js','session-settings.js','session-settings.css','index.html','VIGIA_OS_LEIA-ME.md','VIGIA_OS_V2.md']
backup=ROOT/'tmp/backups'/('etapas_configuraveis_'+datetime.datetime.now().strftime('%Y%m%d_%H%M%S'))
backup.mkdir(parents=True)
for name in names:
    shutil.copy2(TARGET/name,backup/name)
    shutil.copy2(SOURCE/name,TARGET/name)
    assert sha(SOURCE/name)==sha(TARGET/name)
guide=PACKAGE/'05_DOCUMENTACAO/VIGIA_OS_IMPLEMENTADO.md'
shutil.copy2(guide,backup/'guia_principal.md');shutil.copy2(SOURCE/'VIGIA_OS_LEIA-ME.md',guide)
reports=PACKAGE/'05_DOCUMENTACAO/Registros_de_verificacao'
shutil.copy2(ROOT/'tmp/vigia_os_impl/etapas_configuraveis.png',reports/'ETAPAS_CONFIGURAVEIS_20261119.png')
report={'date':'2026-11-19','changes':names,'backup':str(backup),'browser':{'empty_selection_rejected':True,'two_stage_identity_then_conclusions':True,'only_selected_steps_visible':True,'memory_8_54_100_for_two_stages':True,'only_actual_identity_bonus':True,'two_stage_code_and_entry_and_recap':True,'single_access_starts_without_identity':True,'single_access_ends_with_code_without_final_form':True,'ai_distinguishes_skipped_stages_from_completed':True,'mobile_390x844_selection_and_actions_fit':True,'reload_restores_all_four_stages':True},'stage_tests':json.loads((ROOT/'tmp/vigia_os_impl/etapas.json').read_text(encoding='utf-8')),'game':json.loads((ROOT/'tmp/vigia_os_impl/motor.json').read_text(encoding='utf-8')),'settings':json.loads((ROOT/'tmp/vigia_os_impl/configuracoes.json').read_text(encoding='utf-8')),'preserved':{'key':'BA17-2847-2246','copy_countdown_seconds':30,'default_round_seconds':750,'default_bonus_seconds':15,'default_stages':'all four','invisible_grid':True,'transmission_failure':True},'reduced_audio':'Original recordings remain available manually; automatic instructions use text and the assistant.'}
(reports/'ETAPAS_CONFIGURAVEIS_20261119.json').write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf-8')
inventory=PACKAGE/'INVENTARIO_PACOTE.json';shutil.copy2(inventory,backup/inventory.name)
files=[{'arquivo':str(p.relative_to(PACKAGE)),'bytes':p.stat().st_size,'sha256':sha(p)} for p in sorted(PACKAGE.rglob('*')) if p.is_file() and p!=inventory]
inventory.write_text(json.dumps({'revisao':'2026-11-19 VIG.IA — seleção de etapas por público','pasta':str(PACKAGE),'quantidade_arquivos':len(files),'total_bytes':sum(x['bytes'] for x in files),'arquivos':files},ensure_ascii=False,indent=2),encoding='utf-8')
result={'updated':names,'backup':str(backup),'package_files':len(files),'entry':str(TARGET/'index.html')}
(ROOT/'tmp/vigia_os_impl/PUBLICACAO_ETAPAS.json').write_text(json.dumps(result,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps(result,ensure_ascii=False))
