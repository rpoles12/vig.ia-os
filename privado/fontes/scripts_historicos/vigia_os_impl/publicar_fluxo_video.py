from pathlib import Path
import hashlib,shutil,json,datetime
ROOT=Path(__file__).resolve().parents[2];S=ROOT/'output/vigia_os_sistema';PACKAGE=Path(r'C:\Users\45061155890\Desktop\Escape_Room_Pacote_Completo');TARGET=PACKAGE/'02_SISTEMA_OFFLINE'
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
proof=ROOT/'tmp/vigia_os_impl/fluxo_video/VERIFICACAO.json';verification=json.loads(proof.read_text(encoding='utf-8'));assert verification['result']=='passed' and verification['checks']>=37
expiration=ROOT/'tmp/vigia_os_impl/fluxo_video/EXPIRACAO_VIDEO.json';assert json.loads(expiration.read_text(encoding='utf-8'))=={'paused':True,'timeUp':True,'cursor':'none','timer':'00:00'}
baseline=sorted((ROOT/'tmp/backups').glob('fluxo_video_*'))[-1]
for name in ['app.js','desktop.js','index.html']:assert sha(baseline/name)==sha(TARGET/name),'Cópia final alterada desde a preparação: '+name
for name in ['engine.js','countdown.js','session-settings.js','desktop-interactions.js','ambient.js']:assert sha(S/name)==sha(TARGET/name),name
assert sha(S/'video/Video_inicial.mp4')==sha(ROOT/'output/video_inicial/v4_francisca/VIGIA_OS_Tutorial_Francisca_v4.mp4')
backup=ROOT/'tmp/backups'/('publicacao_video_'+datetime.datetime.now().strftime('%Y%m%d_%H%M%S'));backup.mkdir(parents=True)
files=['app.js','desktop.js','index.html','intro-video.js','intro-video.css','assets/os/introvideo.svg','video/Video_inicial.mp4','VIGIA_OS_LEIA-ME.md']
def install(source,dest,label):
    if dest.exists():
        previous=backup/label;previous.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(dest,previous)
    dest.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(source,dest);assert sha(source)==sha(dest)
for name in files:install(S/name,TARGET/name,Path('02_SISTEMA_OFFLINE')/name)
guide=PACKAGE/'05_DOCUMENTACAO/VIGIA_OS_IMPLEMENTADO.md';install(S/'VIGIA_OS_LEIA-ME.md',guide,Path('05_DOCUMENTACAO')/guide.name)
pdf=ROOT/'output/pdf/jornais_investigacao/a3_com_reservas/Jornais_A3_Duas_Copias.pdf'
install(pdf,PACKAGE/'01_PARA_IMPRESSAO/Jornais_A3_Duas_Copias.pdf',Path('01_PARA_IMPRESSAO')/pdf.name)
install(ROOT/'output/pdf/jornais_investigacao/a3_com_reservas/IMPRESSAO.json',PACKAGE/'01_PARA_IMPRESSAO/Jornais_A3_Orientacao.json',Path('01_PARA_IMPRESSAO/Jornais_A3_Orientacao.json'))
reports=PACKAGE/'05_DOCUMENTACAO/Registros_de_verificacao'
install(proof,reports/'FLUXO_VIDEO_INICIAL.json',Path('05_DOCUMENTACAO/Registros_de_verificacao/FLUXO_VIDEO_INICIAL.json'))
install(expiration,reports/'VIDEO_EXPIRACAO.json',Path('05_DOCUMENTACAO/Registros_de_verificacao/VIDEO_EXPIRACAO.json'))
inventory=PACKAGE/'INVENTARIO_PACOTE.json';shutil.copy2(inventory,backup/inventory.name)
items=[{'arquivo':str(p.relative_to(PACKAGE)),'bytes':p.stat().st_size,'sha256':sha(p)} for p in sorted(PACKAGE.rglob('*')) if p.is_file() and p!=inventory]
inventory.write_text(json.dumps({'revisao':'2026-11-24 - apresentação antes do relógio e jornais A3 com reservas','pasta':str(PACKAGE),'quantidade_arquivos':len(items),'total_bytes':sum(x['bytes'] for x in items),'arquivos':items},ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps({'entry':str(TARGET/'index.html'),'video':str(TARGET/'video/Video_inicial.mp4'),'print':str(PACKAGE/'01_PARA_IMPRESSAO/Jornais_A3_Duas_Copias.pdf'),'backup':str(backup),'browser_checks':verification['checks']},ensure_ascii=False))
