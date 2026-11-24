from pathlib import Path
import hashlib,json,shutil,datetime
ROOT=Path(__file__).resolve().parents[2]
SOURCE=ROOT/'output/vigia_os_sistema'
PACKAGE=Path(r'C:\Users\45061155890\Desktop\Escape_Room_Pacote_Completo')
TARGET=PACKAGE/'02_SISTEMA_OFFLINE'
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
for name in ['app.js','engine.js','data.js','vigia.js','desktop.js','countdown.js','ambient.js','session-settings.js','session-settings.css','desktop-interactions.js','desktop-interactions.css']:
    assert sha(SOURCE/name)==sha(TARGET/name),name
index=(SOURCE/'index.html').read_text(encoding='utf-8')
assert 'catastrophic-failure.js?v=1' in index and 'transmission-failure.js?v=1' not in index
assert 'SINAL PERDIDO' not in (SOURCE/'catastrophic-failure.js').read_text(encoding='utf-8')
audio=json.loads((SOURCE/'audio/failure/licenca.json').read_text(encoding='utf-8'))
for entry in audio['files']:
    p=SOURCE/'audio/failure'/entry['file'];assert sha(p)==entry['sha256']
names=['catastrophic-failure.js','catastrophic-failure.css','feedback.js','index.html','assets/os/failure/cracked-glass-v1.png','assets/os/failure/GERACAO.md','audio/failure/tv-static-noise-152056.mp3','audio/failure/glass-cracking-504028.mp3','audio/failure/electric-hum-141075.mp3','audio/failure/CREDITOS.md','audio/failure/licenca.json','VIGIA_OS_LEIA-ME.md','VIGIA_OS_V2.md']
backup=ROOT/'tmp/backups'/('pane_catastrofica_'+datetime.datetime.now().strftime('%Y%m%d_%H%M%S'))
backup.mkdir(parents=True)
for name in names:
    dst=TARGET/name;old=backup/name
    if dst.exists():old.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(dst,old)
    dst.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(SOURCE/name,dst)
    assert sha(SOURCE/name)==sha(dst)
guide=PACKAGE/'05_DOCUMENTACAO/VIGIA_OS_IMPLEMENTADO.md'
shutil.copy2(guide,backup/'guia_principal.md');shutil.copy2(SOURCE/'VIGIA_OS_LEIA-ME.md',guide)
reports=PACKAGE/'05_DOCUMENTACAO/Registros_de_verificacao'
shutil.copy2(ROOT/'tmp/vigia_os_impl/pane_catastrofica.png',reports/'PANE_CATASTROFICA_20261119.png')
report={'date':'2026-11-19','changes':names,'backup':str(backup),'browser':{'qa_round_seconds':8,'all_three_mp3_ready_state':4,'durations_seconds':{'static':15.046531,'hum':21.342031,'glass':1.704},'three_tracks_playing_on_expiry':True,'three_tracks_still_playing_after_repeated_cycles':True,'native_loop_enabled':True,'escape_does_not_dismiss':True,'authorized_continuation_pauses_and_rewinds_all':True,'error_blocks':32,'glass_png_loaded_width':1672,'no_visible_title_or_central_panel':True,'console_errors':[]},'sound':json.loads((ROOT/'tmp/vigia_os_impl/pane_audio.json').read_text(encoding='utf-8')),'game':json.loads((ROOT/'tmp/vigia_os_impl/motor.json').read_text(encoding='utf-8')),'ambient':json.loads((ROOT/'tmp/vigia_os_impl/trilha.json').read_text(encoding='utf-8')),'audio_assets':audio,'image':{'file':'assets/os/failure/cracked-glass-v1.png','size':[1672,941],'mode':'RGBA','tool':'built-in image_gen','generation_record':'assets/os/failure/GERACAO.md'},'preserved':['Padrão de 12:30 e +15s','Seleção de etapas e login de configurações','Chave e recapitulação','Música ambiente de40% com redução durante mídias','Grade invisível de atalhos','Bloqueio após o fim do prazo']}
(reports/'PANE_CATASTROFICA_20261119.json').write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf-8')
inventory=PACKAGE/'INVENTARIO_PACOTE.json';shutil.copy2(inventory,backup/inventory.name)
files=[{'arquivo':str(p.relative_to(PACKAGE)),'bytes':p.stat().st_size,'sha256':sha(p)} for p in sorted(PACKAGE.rglob('*')) if p.is_file() and p!=inventory]
inventory.write_text(json.dumps({'revisao':'2026-11-19 VIG.IA — pane catastrófica e loops Pixabay','pasta':str(PACKAGE),'quantidade_arquivos':len(files),'total_bytes':sum(x['bytes'] for x in files),'arquivos':files},ensure_ascii=False,indent=2),encoding='utf-8')
result={'updated':names,'backup':str(backup),'package_files':len(files),'entry':str(TARGET/'index.html')}
(ROOT/'tmp/vigia_os_impl/PUBLICACAO_PANE_CATASTROFICA.json').write_text(json.dumps(result,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps(result,ensure_ascii=False))
