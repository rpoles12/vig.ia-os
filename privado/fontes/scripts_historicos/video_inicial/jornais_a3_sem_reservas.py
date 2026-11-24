from pathlib import Path
import json,hashlib
from pypdf import PdfReader,PdfWriter
from reportlab.lib.pagesizes import A3
ROOT=Path(__file__).resolve().parents[2]
source=ROOT/'output/pdf/jornais_investigacao/a3_com_reservas/Jornais_A3_Duas_Copias.pdf'
out=ROOT/'output/pdf/jornais_investigacao/a3_sem_reservas';out.mkdir(parents=True,exist_ok=True)
target=out/'Jornais_A3_3_Folhas.pdf';reader=PdfReader(source);writer=PdfWriter()
for page in reader.pages[:3]:writer.add_page(page)
writer.add_metadata({'/Title':'Jornais e manchetes A3 - três folhas, sem reservas'})
with target.open('wb') as f:writer.write(f)
pages=PdfReader(target).pages;assert len(pages)==3
for i,p in enumerate(pages):
    assert abs(float(p.mediabox.width)-A3[0])<.1 and abs(float(p.mediabox.height)-A3[1])<.1
    assert p.get_contents().get_data()==reader.pages[i].get_contents().get_data()
(out/'IMPRESSAO.json').write_text(json.dumps({'pages':3,'paper_mm':[297,420],'copies_of_each_sheet':1,'order':['jornal 1','jornal 2','manchetes'],'print':'A3, retrato, escala 100%, frente única. Imprimir uma cópia do arquivo. Sem páginas de reserva.','sha256':hashlib.sha256(target.read_bytes()).hexdigest()},ensure_ascii=False,indent=2),encoding='utf-8')
print(target)
