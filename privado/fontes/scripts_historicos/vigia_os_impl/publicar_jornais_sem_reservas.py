from pathlib import Path
import shutil,hashlib,json,datetime
ROOT=Path(__file__).resolve().parents[2];PACKAGE=Path(r'C:\Users\45061155890\Desktop\Escape_Room_Pacote_Completo');PRINT=PACKAGE/'01_PARA_IMPRESSAO'
source=ROOT/'output/pdf/jornais_investigacao/a3_sem_reservas';backup=ROOT/'tmp/backups'/('jornais_sem_reserva_'+datetime.datetime.now().strftime('%Y%m%d_%H%M%S'));backup.mkdir(parents=True)
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
pdf=source/'Jornais_A3_3_Folhas.pdf';target=PRINT/pdf.name
if target.exists():shutil.copy2(target,backup/target.name)
shutil.copy2(pdf,target);assert sha(pdf)==sha(target)
old=PRINT/'Jornais_A3_Duas_Copias.pdf'
if old.exists():shutil.move(str(old),str(backup/old.name))
meta=PRINT/'Jornais_A3_Orientacao.json'
if meta.exists():shutil.copy2(meta,backup/meta.name)
shutil.copy2(source/'IMPRESSAO.json',meta)
section='''\n## Jornais em A3\n\nNa pasta 01_PARA_IMPRESSAO do pacote, Jornais_A3_3_Folhas.pdf contém três páginas A3 em retrato: jornal 1, jornal 2 e manchetes. Imprimir uma cópia do PDF em papel A3, tamanho real (100%), frente única. Há uma única cópia de cada folha, sem reservas. O fundo permanece branco puro e a arte foi ampliada uniformemente, sem distorcer a proporção.\n'''
for i,guide in enumerate([ROOT/'output/vigia_os_sistema/VIGIA_OS_LEIA-ME.md',PACKAGE/'02_SISTEMA_OFFLINE/VIGIA_OS_LEIA-ME.md',PACKAGE/'05_DOCUMENTACAO/VIGIA_OS_IMPLEMENTADO.md']):
    shutil.copy2(guide,backup/f'guia_{i}.md');text=guide.read_text(encoding='utf-8');marker='\n## Jornais em A3';assert marker in text;guide.write_text(text.split(marker)[0]+section,encoding='utf-8')
inventory=PACKAGE/'INVENTARIO_PACOTE.json';shutil.copy2(inventory,backup/inventory.name)
files=[{'arquivo':str(p.relative_to(PACKAGE)),'bytes':p.stat().st_size,'sha256':sha(p)} for p in sorted(PACKAGE.rglob('*')) if p.is_file() and p!=inventory]
inventory.write_text(json.dumps({'revisao':'2026-11-24 - jornais A3, três folhas sem reservas','pasta':str(PACKAGE),'quantidade_arquivos':len(files),'total_bytes':sum(p['bytes'] for p in files),'arquivos':files},ensure_ascii=False,indent=2),encoding='utf-8')
print(target)
