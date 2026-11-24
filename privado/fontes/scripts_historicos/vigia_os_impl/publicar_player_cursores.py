from pathlib import Path
import hashlib,json,shutil,datetime
ROOT=Path(__file__).resolve().parents[2]
SOURCE=ROOT/'output/vigia_os_sistema'
PACKAGE=Path(r'C:\Users\45061155890\Desktop\Escape_Room_Pacote_Completo').resolve()
TARGET=PACKAGE/'02_SISTEMA_OFFLINE'
assert str(PACKAGE)==r'C:\Users\45061155890\Desktop\Escape_Room_Pacote_Completo'
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
assert sha(SOURCE/'engine.js')==sha(TARGET/'engine.js')
assert sha(SOURCE/'data.js')==sha(TARGET/'data.js')
assert '750+bonus' in (SOURCE/'countdown.js').read_text(encoding='utf-8')
for folder in ['audio','evidencias','encerramento']:
    for p in (TARGET/folder).rglob('*'):
        if p.is_file():assert sha(p)==sha(SOURCE/p.relative_to(TARGET))
backup=ROOT/'tmp/backups'/('publicacao_player_cursores_'+datetime.datetime.now().strftime('%Y%m%d_%H%M%S'))
backup.mkdir(parents=True)
changed=[]
for p in SOURCE.rglob('*'):
    if not p.is_file():continue
    rel=p.relative_to(SOURCE);other=TARGET/rel
    if other.exists() and sha(other)==sha(p):continue
    if other.exists():
        old=backup/'02_SISTEMA_OFFLINE'/rel;old.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(other,old)
    other.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(p,other)
    assert sha(p)==sha(other)
    changed.append(str(rel))
reportdir=PACKAGE/'05_DOCUMENTACAO/Registros_de_verificacao'
reportdir.mkdir(exist_ok=True)
shutil.copy2(ROOT/'tmp/vigia_os_impl/player_novo.png',reportdir/'PLAYER_BARRA_20261119.png')
guide=PACKAGE/'05_DOCUMENTACAO/VIGIA_OS_IMPLEMENTADO.md'
if guide.exists():shutil.copy2(guide,backup/guide.name)
shutil.copy2(SOURCE/'VIGIA_OS_LEIA-ME.md',guide)
report={'date':'2026-11-19','changes':changed,'backup':str(backup),'cursors':{'count':11,'format':'PNG RGBA32x32','hotspots':'assets/os/cursors/manifest.json','preview':'assets/os/cursors/previa-cursores.png','method':'Desenho geométrico local combinado com a família SVG do OS'},'player':{'play_pause':True,'seek':True,'volume_menu':True,'mute_restore':True,'transcription':True,'single_shared_audio':True},'verification':{'automated':json.loads((ROOT/'tmp/vigia_os_impl/motor.json').read_text(encoding='utf-8')),'responsive_widths':[390,935,1366],'no_horizontal_overflow':True,'cursor_css_in_browser':True,'document_load_busy_clears':True,'local_source_console_errors':0},'preserved':['engine.js','data.js','production_countdown','all_audio_evidence_and_ending_media'],'limitations':['Abertura direta file:// bloqueada pela política do navegador de teste; validar no equipamento do evento.','Conferir percepção do som e tamanho do cursor no equipamento do evento.']}
(reportdir/'PLAYER_CURSORES_20261119.json').write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf-8')
inv=PACKAGE/'INVENTARIO_PACOTE.json'
shutil.copy2(inv,backup/inv.name)
files=[{'arquivo':str(p.relative_to(PACKAGE)),'bytes':p.stat().st_size,'sha256':sha(p)} for p in sorted(PACKAGE.rglob('*')) if p.is_file() and p.name!='INVENTARIO_PACOTE.json']
inv.write_text(json.dumps({'revisao':'2026-11-19 VIGIA OS — player e cursores PNG','pasta':str(PACKAGE),'quantidade_arquivos':len(files),'total_bytes':sum(x['bytes'] for x in files),'arquivos':files},ensure_ascii=False,indent=2),encoding='utf-8')
result={'runtime_files_updated':len(changed),'cursor_pngs':11,'package_files':len(files),'backup':str(backup),'entry':str(TARGET/'index.html')}
(ROOT/'tmp/vigia_os_impl/PUBLICACAO_PLAYER_CURSORES.json').write_text(json.dumps(result,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps(result,ensure_ascii=False))
