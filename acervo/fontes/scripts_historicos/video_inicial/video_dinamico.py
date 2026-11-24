from pathlib import Path
import importlib.util,json,subprocess,shutil,sys
from PIL import Image,ImageDraw
ROOT=Path(__file__).resolve().parents[2];P=Path(__file__).parent
spec=importlib.util.spec_from_file_location('base_video',P/'montar_video.py');B=importlib.util.module_from_spec(spec);spec.loader.exec_module(B)
OUT=ROOT/'output/video_inicial/v3_dinamico';TMP=ROOT/'tmp/video_inicial/v3_dinamico';A=OUT/'assets';R=TMP/'renders'
for p in [OUT,TMP,A,R,OUT/'audio',OUT/'storyboard']:p.mkdir(parents=True,exist_ok=True)
definitions=[
(1,6,'O incidente','Incidente no Vértice. Arquivos danificados. Sua equipe precisa descobrir o que aconteceu.'),
(2,5,'O prazo','Os dados serão apagados ao fim do prazo. Acompanhem o relógio.'),
(3,3,'A missão','Investiguem. Comparem evidências. Reconstruam os fatos.'),
(12,11,'Explore a sala','Consultem o painel de funcionários. Procurem as pastas e o crachá escondidos na sala. Comparem esses materiais com os registros do computador.'),
(4,8,'Navegue pelo OS','Abram os aplicativos pelos ícones. Minimizem as janelas e voltem a elas pela barra de tarefas.'),
(5,11,'Consulte os arquivos','No Explorador, pesquisem e abram os documentos. Ampliem os detalhes e comparem as informações entre arquivos e materiais da sala.'),
(6,9,'Ouça os registros','No player, reproduzam, pausem ou voltem a um trecho. Usem a transcrição e os controles da barra de tarefas.'),
(7,12,'Converse com a VIG.IA','Peçam ajuda à VIGIA: onde procurar ou como comparar informações. Digitem e enviem. Quanto mais memória recuperada, mais completas serão as orientações.'),
(8,11,'Registre as conclusões','Em Registros, preencham a resposta e enviem pelo botão ou Enter. Se errarem, sigam a orientação e consultem os documentos indicados.'),
(9,8,'Organize a cronologia','Na cronologia, arrastem os cartões do primeiro ao último evento. Confiram a ordem antes de validar.'),
(10,8,'Acompanhe a investigação','Próximos passos mostra o objetivo atual. Acompanhem tempo e memória. Separem papel e caneta para anotações.'),
(11,8,'A investigação começa agora','Anotem a chave quando aparecer. Ela libera a recapitulação. Os arquivos estão nas suas mãos. Comecem a investigação.')]
old={s['id']:s for s in B.SCENES};scenes=[];start=0
for id,d,title,voice in definitions:
    s={**old[id],'start':start,'duration':d,'short_title':title,'voice':voice};scenes.append(s);start+=d
(OUT/'cenas.json').write_text(json.dumps(scenes,ensure_ascii=False,indent=2),encoding='utf-8')
B.SCENES=scenes;B.TOTAL=start;B.OUT=OUT;B.ASSETS=A;B.STORY=OUT/'storyboard';B.RENDERS=R;B.TMP=TMP
FF=ROOT/'tmp/video_inicial/ffmpeg.exe';B.FF=FF
for p in (ROOT/'output/video_inicial/assets').glob('*.png'):shutil.copy2(p,A/p.name)
def save_text(text,path,w=1150,h=100,size=48):
    im=Image.new('RGBA',(w,h));d=ImageDraw.Draw(im);d.rounded_rectangle((2,2,w-2,h-2),radius=12,fill='#160c23ed',outline='#8d60ba',width=2);d.text((25,20),text,font=B.font(size),fill='#f3e6ff');im.save(path)
def assets():
    B.create_assets()
    clean=Image.open(A/'fundo.png').convert('RGBA');ImageDraw.Draw(clean).rectangle((0,0,1350,120),fill='#0a0710');clean.save(A/'fundo.png')
    for s in scenes:save_text(s['short_title'],A/f'heading_{s["id"]}.png',w=1250,h=100,size=48)
    calls={4:['Abra pelos ícones','Minimize e volte pela barra'],5:['Pesquise o documento','Abra e amplie','Compare com os materiais da sala'],6:['Reproduza • Pause • Volte','Transcrição e controle na barra'],7:['Onde procurar? Como comparar?','Envie sua mensagem','Mais memória = mais apoio'],8:['Preencha a resposta','Botão ou Enter','Errou? Siga os documentos indicados'],9:['Segure → Arraste → Solte','Do primeiro ao último evento'],10:['Objetivo atual em Próximos passos','Tempo e memória na barra','Bônus conforme a configuração']}
    for id,texts in calls.items():
        for j,text in enumerate(texts):save_text(text,A/f'call_{id}_{j}.png',w=950,h=80,size=33)
    for i,word in enumerate(['INVESTIGUE','COMPARE','RECONSTRUA']):save_text(word,A/f'mission_{i}.png',w=680,h=135,size=70)
    save_text('XXXX-XXXX-XXXX',A/'key.png',w=800,h=130,size=70)
    return calls
def render(s,capture,calls):
    id=s['id'];dur=s['duration'];args=[];g=[];ix=0
    def inp(p,seek=None):
        nonlocal ix
        if seek is None:args.extend(['-loop','1','-framerate','30','-i',str(p)])
        else:args.extend(['-ss',str(max(0,seek)),'-i',str(p)])
        ix+=1;return ix-1
    def layer(cur,i,name,x,y,at=0,end=None):
        end=dur if end is None else end
        g.append(f'[{i}:v]format=rgba,fade=t=in:st={at}:d=0.22:alpha=1,fade=t=out:st={end-.2}:d=0.2:alpha=1[l{i}]')
        g.append(f'[{cur}][l{i}]overlay=x=\'{x}\':y=\'{y}\':enable=\'between(t,{at},{end})\':shortest=1[{name}]');return name
    def slide(x,at,dx=-250):return f'{x}+{dx}*pow(max(0,1-(t-{at})/.42),3)'
    bg=inp(A/'fundo.png');g.append(f'[{bg}:v]format=yuv420p[b]');cur='b'
    if 4<=id<=10:
        seg=next(x for x in capture['segments'] if x['id']==id)
        spans={4:12.4,5:13.0,6:11.5,7:15.5,8:12.5,9:9.3,10:9.5};span=spans[id]
        i=inp(capture['video'],seg['start']-1.01)
        # Real screen actions are kept; idle tails are removed. Camera settles in,
        # then makes a modest approach to the application, returning for taskbar context.
        g.append(f'[{i}:v]trim=duration={span},setpts=(PTS-STARTPTS)*{dur/span},fps=30,scale=w=\'trunc((1320+160*sin(PI*min(t/{dur},1)))/2)*2\':h=-2:eval=frame,setsar=1[v]')
        g.append(f'[{cur}][v]overlay=x=\'(W-w)/2\':y=\'145-(h-825)*.45\':shortest=1[screen]');cur='screen'
        texts=calls[id];step=dur/len(texts)
        for j in range(len(texts)):
            at=.8+j*step;end=min(dur-.1,at+step-.25)
            i=inp(A/f'call_{id}_{j}.png');cur=layer(cur,i,f'c{j}',slide(80,at),790,at,end)
    elif id==1:
        g=[]
        i=inp(A/'abertura_corredor.png');g.append(f'[{i}:v]scale=2048:1152,crop=1920:1080:x=\'64+35*sin(t/3)\':y=36[bg]');cur='bg'
        for k,(at,x,y) in enumerate([(.1,100,195),(1.7,320,435),(3.3,170,680)]):
            i=inp(A/f'manchete_{k}.png');g.append(f'[{i}:v]rotate=angle={[-.028,.018,-.015][k]}:fillcolor=none[r{k}]');g.append(f'[r{k}]fade=t=in:st={at}:d=0.25:alpha=1[l{i}]');g.append(f'[{cur}][l{i}]overlay=x=\'{slide(x,at,700 if k%2 else -700)}\':y={y}:enable=\'gte(t,{at})\'[h{k}]');cur=f'h{k}'
    elif id==12:
        for k in range(3):
            at=.3+k*1.4;i=inp(A/f'fisico_{k}.png');cur=layer(cur,i,f'p{k}',slide(90+k*590,at,-350),f'350+7*sin((t-{at})*2)',at)
        i=inp(A/'titulo_12.png');cur=layer(cur,i,'physicaltext',0,0)
    elif id==2:
        for k in range(8):
            i=inp(A/f'bloco_{k}.png');cur=layer(cur,i,f'd{k}',f'{1170+k%3*170}+90*sin(t*1.1+{k})',f'{150+k//3*210}+45*cos(t+{k})',.1*k)
        i=inp(A/'titulo_02.png');cur=layer(cur,i,'data',slide(0,0),0)
    elif id==3:
        for k in range(3):
            at=k*.6;i=inp(A/f'mission_{k}.png');cur=layer(cur,i,f'm{k}',slide(150+k*520,at,450 if k%2 else -450),300+k*160,at)
    else:
        i=inp(A/'key.png');cur=layer(cur,i,'key',slide(560,.3),380,.3,3.7)
        i=inp(A/'titulo_11.png');cur=layer(cur,i,'end',slide(0,3.7),0,3.7)
    if id not in [1,12,3,11]:
        i=inp(A/f'heading_{id}.png');cur=layer(cur,i,'heading',slide(80,0),18)
    subs=(R/f'subs_{id:02}.ass').relative_to(ROOT).as_posix()
    g.append(f'[{cur}]ass=\'{subs}\',setsar=1,format=yuv420p[out]')
    B.run(args+['-filter_complex_threads','2','-filter_complex',';'.join(g),'-map','[out]','-t',dur,'-an','-c:v','libx264','-preset','veryfast','-crf',19,'-threads',4,'-r',30,R/f'cena_{id:02}.mp4'],R/f'cena_{id:02}.log')
    print('Cena dinâmica',id,'concluída',flush=True)
def main():
    if '--prepare' in sys.argv:
        print(OUT/'cenas.json');return
    calls=assets()
    # Remove excessive synthesis pauses before choosing a modest speech tempo.
    for s in scenes:
        voice=OUT/f'audio/voz_{s["id"]:02}.wav';raw=OUT/f'audio/voz_original_{s["id"]:02}.wav'
        if not raw.exists():shutil.copy2(voice,raw)
        B.run(['-i',raw,'-af','silenceremove=start_periods=1:start_duration=0.04:start_threshold=-45dB:stop_periods=-1:stop_duration=0.25:stop_threshold=-45dB:stop_silence=0.14','-c:a','pcm_s16le',voice])
    B.audio_and_subtitles();capture=json.loads((ROOT/'output/video_inicial/capturas/gravao.json').read_text(encoding='utf-8'))
    for s in scenes:
        p=R/f'cena_{s["id"]:02}.mp4'
        if not p.exists() or p.stat().st_size<1024 or '--force' in sys.argv:render(s,capture,calls)
    concat=R/'concat.txt';concat.write_text('\n'.join("file '"+(R/f'cena_{s["id"]:02}.mp4').as_posix()+"'" for s in scenes),encoding='utf-8')
    B.run(['-f','concat','-safe',0,'-i',concat,'-i',OUT/'audio/trilha_mixada.wav','-map','0:v','-map','1:a','-vf','setsar=1','-c:v','libx264','-preset','veryfast','-crf',19,'-threads',4,'-c:a','aac','-b:a','192k','-t',B.TOTAL,'-movflags','+faststart',OUT/'VIGIA_OS_Tutorial_Curto_v3.mp4'],R/'export.log')
    for j,s in enumerate(scenes):
        B.run(['-ss',s['start']+min(4,s['duration']/2),'-i',OUT/'VIGIA_OS_Tutorial_Curto_v3.mp4','-frames:v',1,OUT/f'storyboard/{j+1:02}_quadro.png'])
    (OUT/'PLANEJAMENTO.json').write_text(json.dumps({'duration':B.TOTAL,'base_duration':166,'saved_seconds':166-B.TOTAL,'preserved':['incidente e desafio','prazo de apagamento','painel, pastas e crachá escondidos','navegação e barra','consulta, pesquisa e zoom','áudio e transcrição','chat e memória da IA','envio por Enter e orientação dos erros','arrasto e validação','objetivo, tempo, memória e bônus configurável','anotação da chave e recapitulação'],'motion':['manchetes em camadas e rotação','cartões físicos independentes','dados em trajetórias distintas','tipografia em sequência','câmera se aproxima e retorna nos apps','gravações sem pausas finais','legendas de ação com entrada e saída','transição da chave para o desafio final'],'scenes':scenes},ensure_ascii=False,indent=2),encoding='utf-8')
    print('Vídeo de 100 segundos exportado.',flush=True)
if __name__=='__main__':main()
