from pathlib import Path
import hashlib,json,shutil,datetime
ROOT=Path(__file__).resolve().parents[2]
SOURCE=ROOT/'output/vigia_os_sistema'
PACKAGE=Path(r'C:\Users\SEU_USUARIO\Desktop\Escape_Room_Pacote_Completo')
TARGET=PACKAGE/'02_SISTEMA_OFFLINE'
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
for name in ['engine.js','data.js','vigia.js','ambient.js','feedback.js','desktop.js','desktop-interactions.js','desktop-interactions.css','transmission-failure.js','transmission-failure.css']:
    assert sha(SOURCE/name)==sha(TARGET/name),name
assert 'durationSeconds:750,bonusEnabled:true,bonusSeconds:15' in (SOURCE/'countdown.js').read_text(encoding='utf-8')
assert 'baseVolume=.40' in (SOURCE/'ambient.js').read_text(encoding='utf-8')
settings=(SOURCE/'session-settings.js').read_text(encoding='utf-8')
assert 'localStorage' not in settings and 'sessionStorage' not in settings
names=['session-settings.js','session-settings.css','countdown.js','app.js','index.html','VIGIA_OS_LEIA-ME.md','VIGIA_OS_V2.md']
backup=ROOT/'tmp/backups'/('configuracoes_sessao_'+datetime.datetime.now().strftime('%Y%m%d_%H%M%S'))
backup.mkdir(parents=True)
for name in names:
    if (TARGET/name).exists():shutil.copy2(TARGET/name,backup/name)
    shutil.copy2(SOURCE/name,TARGET/name)
    assert sha(SOURCE/name)==sha(TARGET/name)
guide=PACKAGE/'05_DOCUMENTACAO/VIGIA_OS_IMPLEMENTADO.md'
shutil.copy2(guide,backup/'guia_principal.md')
shutil.copy2(SOURCE/'VIGIA_OS_LEIA-ME.md',guide)
reports=PACKAGE/'05_DOCUMENTACAO/Registros_de_verificacao'
for source,target in [('configuracoes_sessao.png','CONFIGURACOES_SESSAO_20261119.png'),('inicial_engrenagem.png','INICIAL_ENGRENAGEM_20261119.png')]:
    shutil.copy2(ROOT/'tmp/vigia_os_impl'/source,reports/target)
report={'date':'2026-11-19','changes':names,'backup':str(backup),'browser':{'gear_before_start':True,'invalid_password_rejected':True,'login_admin_accepted':True,'reopening_requires_authentication':True,'zero_duration_rejected':True,'custom_duration_05m10s':True,'custom_bonus_30s_popup_and_clock':True,'ai_time_answer_uses_configuration':True,'disabled_initial_narration':True,'close_without_save_discards_draft':True,'defaults_button':True,'operator_reset_preserves_session_configuration':True,'reload_restores_12m30s_and_15s':True,'bonus_disabled_does_not_add_time':True,'custom_20s_round_expires_with_transmission_failure':True,'responsive_390x844_header_and_actions_visible':True,'final_isolated_smoke_console_errors':[]},'configuration_tests':json.loads((ROOT/'tmp/vigia_os_impl/configuracoes.json').read_text(encoding='utf-8')),'game':json.loads((ROOT/'tmp/vigia_os_impl/motor.json').read_text(encoding='utf-8')),'defaults':{'duration_seconds':750,'bonus_enabled':True,'bonus_seconds':15,'auto_initial_narration':True,'time_warning_sounds':True},'scope':'Only JavaScript memory of this page; no configuration storage or network service.'}
(reports/'CONFIGURACOES_SESSAO_20261119.json').write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf-8')
inventory=PACKAGE/'INVENTARIO_PACOTE.json'
shutil.copy2(inventory,backup/inventory.name)
files=[{'arquivo':str(p.relative_to(PACKAGE)),'bytes':p.stat().st_size,'sha256':sha(p)} for p in sorted(PACKAGE.rglob('*')) if p.is_file() and p!=inventory]
inventory.write_text(json.dumps({'revisao':'2026-11-19 VIG.IA — configurações temporárias da sessão','pasta':str(PACKAGE),'quantidade_arquivos':len(files),'total_bytes':sum(x['bytes'] for x in files),'arquivos':files},ensure_ascii=False,indent=2),encoding='utf-8')
result={'updated':names,'backup':str(backup),'package_files':len(files),'entry':str(TARGET/'index.html')}
(ROOT/'tmp/vigia_os_impl/PUBLICACAO_CONFIGURACOES.json').write_text(json.dumps(result,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps(result,ensure_ascii=False))
