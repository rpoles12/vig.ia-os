from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
import json, shutil, re, wave, numpy as np

ROOT=Path(__file__).resolve().parents[2]
OUT=ROOT/'output/video_inicial'
DEMO=ROOT/'tmp/video_inicial/demo_os'
SOURCE=ROOT/'output/vigia_os_sistema'
FONT=ROOT/'assets/fontes/SpaceGrotesk-Bold.ttf'
MONO=ROOT/'assets/fontes/IBMPlexMono-Regular.ttf'
DEMO.mkdir(parents=True,exist_ok=True)
shutil.copytree(SOURCE,DEMO,dirs_exist_ok=True,ignore=shutil.ignore_patterns('encerramento','failure'))
data=json.loads((SOURCE/'data.js').read_text(encoding='utf-8').split('=',1)[1].strip().rstrip(';'))

protected={'Bryan Almeida':'Pessoa Exemplo','Bryan':'Pessoa Exemplo','bryanalmeida':'pessoaexemplo','bryan':'pessoaexemplo','Helena Duarte':'Exemplo Físico','Helena':'Exemplo Físico','helenaduarte':'exemplofisico','helena':'exemplofisico','Marcelo Vieira':'Exemplo Digital','Marcelo':'Exemplo Digital','marcelovieira':'exemplodigital','marcelo':'exemplodigital','Carlos Mendes':'Pessoa Fictícia','Carlos':'Pessoa Fictícia','BA17-2847-2246':'XXXX-XXXX-XXXX','2847':'0000','2246':'1000','22:46':'10:00','22:47':'10:01','2247':'1001','B_A_17':'P_EXEMPLO','NORTHSTAR':'EMPRESA FICTÍCIA'}
def sanitize(text):
    for before,after in protected.items():text=text.replace(before,after)
    return text
data=json.loads(sanitize(json.dumps(data,ensure_ascii=False)))
data['key']['answers']['identity']=['Pessoa Exemplo']
data['key']['answers']['generated_protocol']='XXXX-XXXX-XXXX'
data['key']['answers']['credential']=['0000']
data['key']['answers']['critical_time']=['10:00']
for i,e in enumerate(data['evidence'],1):
    e['title']=f'Documento de exemplo {i:02}'
    e['file']=f'evidencias/DEMO_{i:02}.png'
    canvas=Image.new('RGB',(1200,1500),'#eeeaf4');draw=ImageDraw.Draw(canvas)
    draw.rectangle((0,0,1200,200),fill='#20142e')
    draw.text((90,60),'ARQUIVO DEMONSTRATIVO',font=ImageFont.truetype(str(FONT),43),fill='#ddc6ff')
    draw.text((90,270),e['title'],font=ImageFont.truetype(str(FONT),47),fill='#261438')
    draw.text((90,365),'CONTEÚDO FICTÍCIO • TUTORIAL',font=ImageFont.truetype(str(MONO),26),fill='#714694')
    for row,text in enumerate(['Este documento ensina a consultar os arquivos.','Os dados desta tela não pertencem ao caso.','Use os controles para ampliar e ler os detalhes.','Compare registros durante a investigação.']):
        draw.text((90,480+row*75),text,font=ImageFont.truetype(str(MONO),26),fill='#4b405a')
    for y,w in [(880,810),(930,920),(980,640),(1100,870),(1150,740)]:draw.rounded_rectangle((90,y,90+w,y+12),radius=5,fill='#d0c8db')
    draw.text((90,1320),'SEM PISTAS OU RESPOSTAS DO JOGO',font=ImageFont.truetype(str(MONO),24),fill='#714694')
    path=DEMO/e['file'];path.parent.mkdir(parents=True,exist_ok=True);canvas.save(path)
events=['Abrir o caderno','Separar as folhas','Ler as instruções','Reunir os exemplos','Comparar as anotações','Conferir a sequência']
for i,c in enumerate(data['cards']):
    c.update(title=events[i],description='Evento fictício usado apenas para demonstrar o movimento dos cartões.',visible_time=f'PASSO {i+1}',time_label=f'PASSO {i+1}',alt=events[i])
    c.pop('image',None)
data['vigia']['timed_hints']=[]
(DEMO/'data.js').write_text('window.CASE_DATA='+json.dumps(data,ensure_ascii=False)+';',encoding='utf-8')
for path in list(DEMO.glob('*.js'))+list(DEMO.glob('*.html')):
    if path.name=='data.js':continue
    text=sanitize(path.read_text(encoding='utf-8'))
    if path.name=='app.js':
        text=re.sub(r"const titles=\{.*?\};",'const titles=Object.fromEntries(D.evidence.map(e=>[e.id,e.title]));',text,count=1)
        text=text.replace("audio01:'Fragmento 01 · Inicialização',audio02:'Fragmento 02 · Acessos',audio03:'Fragmento 03 · Memória parcial do confronto'","audio01:'Áudio demonstrativo',audio02:'Exemplo de áudio 02',audio03:'Exemplo de áudio 03'")
    if path.name=='desktop.js':
        text=re.sub(r"function notesUpdate\(s\)\{.*?\n }",lambda m:m[0],text,flags=re.S) if False else text
        a=text.index('function notesUpdate(s){');b=text.index(' // Explorer:',a)
        text=text[:a]+'''function notesUpdate(s){$('#start-stage').textContent='Consultar os exemplos';$('#start-memory').textContent=s.memory+'% de memória';$('#notes-content').innerHTML='<h2>Próximos passos</h2><p>Abra Arquivos para consultar os documentos disponíveis.</p><p>Compare as informações e registre a conclusão da equipe.</p><p>Se precisar de direção, converse com a VIG.IA.</p><p class="notes-meta">Este arquivo acompanha o avanço da investigação.<br><br>CONTEÚDO FICTÍCIO • TUTORIAL</p>'}\n'''+text[b:]
    path.write_text(text,encoding='utf-8')
bridge='''(()=>{
const make=VigiaEngine.criarVigia;
VigiaEngine.criarVigia=(...args)=>{const e=make(...args);e.orientar=()=>({intent:'tutorial',title:'Comece pelos documentos',text:'Abra o aplicativo Arquivos, consulte os registros disponíveis e compare suas observações. Depois, use Registros para enviar a conclusão da equipe. Este é um exemplo de orientação.',memory:e.estado().memory,steps:[],docs:[],actions:[{tab:'files',label:'Abrir Arquivos'}],followups:[]});return e};
const settings=VigiaSettings.current;VigiaSettings.current=()=>({...settings(),autoNarration:false,timeWarnings:false,durationSeconds:750});
window.VigiaAmbient={start(){},reset(){},stop(){},duck(){},unduck(){}};
})();'''
(DEMO/'tutorial-bridge.js').write_text(bridge,encoding='utf-8')
html=(DEMO/'index.html').read_text(encoding='utf-8')
html=re.sub(r'<script src="ambient.js[^\"]*"></script>','',html)
html=html.replace('<script src="app.js','<script src="tutorial-bridge.js"></script><script src="app.js')
html=html.replace('Pessoa Fictícia morreu após um confronto na sala técnica. Um lote de projetos foi copiado e os registros foram comprometidos.','Sessão demonstrativa. Todos os dados exibidos são fictícios e não revelam o caso.')
(DEMO/'index.html').write_text(html,encoding='utf-8')
rate=24000;t=np.arange(rate*20)/rate;signal=(np.sin(t*2*np.pi*220)*.025*np.exp(-t%1)*np.minimum(t,1)*np.minimum(20-t,1));pcm=(signal*32767).astype('<i2')
for path in (DEMO/'audio').glob('*.wav'):
    with wave.open(str(path),'wb') as f:f.setnchannels(1);f.setsampwidth(2);f.setframerate(rate);f.writeframes(pcm.tobytes())
# Preserve only neutral transcriptions in this isolated copy.
p=DEMO/'audio/roteiros.js'
p.write_text('window.VIGIA_AUDIO='+json.dumps([{'id':x,'texto':'Áudio de exemplo. Esta gravação demonstra os controles do player. Não contém pistas do caso.'} for x in ['audio01','audio02','audio03']],ensure_ascii=False)+';',encoding='utf-8')
print('Cópia demonstrativa preparada:',DEMO)
