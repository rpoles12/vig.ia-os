from pathlib import Path
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import json, subprocess, wave, math, textwrap, shutil, sys, re
import numpy as np

ROOT=Path(__file__).resolve().parents[2]
OUT=ROOT/'output/video_inicial'; TMP=ROOT/'tmp/video_inicial'; FF=TMP/'ffmpeg.exe'
SCENES=json.loads((Path(__file__).parent/'cenas.json').read_text(encoding='utf-8'))
TOTAL=max(s['start']+s['duration'] for s in SCENES)
ASSETS=OUT/'assets'; STORY=OUT/'storyboard'; RENDERS=TMP/'renders_v2'
for p in [ASSETS,STORY,RENDERS]:p.mkdir(parents=True,exist_ok=True)
W,H=1920,1080
PURPLE='#b88aff';WHITE='#f3ecff';MUTED='#b9a7cf';BG='#0a0710'
FONTS={'bold':ROOT/'assets/fontes/SpaceGrotesk-Bold.ttf','mono':ROOT/'assets/fontes/IBMPlexMono-Regular.ttf','regular':Path('C:/Windows/Fonts/segoeui.ttf')}
def font(n=32,style='bold'):return ImageFont.truetype(str(FONTS[style]),n)
def run(args,log=None):
    cmd=[str(FF),'-hide_banner','-y']+list(map(str,args))
    if log:
        with open(log,'w',encoding='utf-8') as f:r=subprocess.run(cmd,stdout=f,stderr=f)
    else:r=subprocess.run(cmd,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    if r.returncode:raise RuntimeError('FFmpeg: '+(Path(log).read_text(encoding='utf-8')[-3500:] if log else r.stderr.decode('utf-8','replace')[-3500:]))
    return r.stdout
def wrapped(text,f,width):
    result=[]
    for para in text.split('\n'):
        line=''
        for word in para.split():
            attempt=(line+' '+word).strip()
            if f.getlength(attempt)>width and line:result.append(line);line=word
            else:line=attempt
        result.append(line)
    return result
def lines(draw,text,xy,size=40,fill=WHITE,width=1200,spacing=1.2,style='bold'):
    f=font(size,style);x,y=xy
    for line in wrapped(text,f,width):draw.text((x,y),line,font=f,fill=fill);y+=size*spacing
    return y
def geo(draw,cx,cy,r,color,width=2,angle=0):
    p=[(cx+r*math.cos(angle+i*math.pi*2/5-math.pi/2),cy+r*math.sin(angle+i*math.pi*2/5-math.pi/2)) for i in range(5)]
    for i in range(5):
        draw.line([p[i],p[(i+1)%5]],fill=color,width=width)
        draw.line([p[i],p[(i+2)%5]],fill=color,width=width)
def base(tutorial=False):
    yy,xx=np.mgrid[0:H,0:W];g=np.exp(-(((xx-1450)/1050)**2+((yy-460)/850)**2))
    a=np.zeros((H,W,3),dtype=np.uint8)
    for c,(b,s) in enumerate([(8,16),(6,7),(14,29)]):a[:,:,c]=b+g*s
    im=Image.fromarray(a).convert('RGBA');d=ImageDraw.Draw(im)
    for off in range(0,420,45):
        d.line([(W-550+off,-30),(W-170+off,300),(W-170+off,H+20)],fill=(94,58,130,30),width=2)
    d.line((60,77,1860,77),fill='#3a244d',width=1)
    d.text((62,37),'VIG.IA OS',font=font(24),fill=WHITE)
    d.text((244,43),'O ARQUIVO CORROMPIDO',font=font(16,'mono'),fill=MUTED)
    d.text((1435,43),'GUIA DE INICIALIZAÇÃO',font=font(16,'mono'),fill=MUTED)
    if tutorial:
        d.rounded_rectangle((532,104,1868,945),radius=12,fill='#0a0611',outline='#79509f',width=2)
        d.text((544,954),'CAPTURA DO SISTEMA  /  EXEMPLOS FICTÍCIOS',font=font(15,'mono'),fill='#92819f')
    return im
def title_asset(s):
    im=Image.new('RGBA',(W,H));d=ImageDraw.Draw(im)
    d.rounded_rectangle((64,166,458,205),radius=6,fill='#241331',outline='#604078')
    d.text((80,175),s['label'],font=font(16,'mono'),fill='#d5b4ff')
    y=lines(d,s['title'],(64,251),size=49,width=430,spacing=1.16)
    d.line((66,y+31,155,y+31),fill=PURPLE,width=4)
    lines(d,s['body'],(66,y+66),size=26,width=408,spacing=1.6,fill=MUTED,style='regular')
    d.text((66,878),f"{s['id']-3:02} / 07",font=font(22,'mono'),fill=PURPLE)
    return im
def card(text,k):
    im=Image.new('RGBA',(1370,240));d=ImageDraw.Draw(im)
    d.rounded_rectangle((0,0,1360,230),radius=3,fill='#ede7ed',outline='#c0adce',width=2)
    d.rectangle((0,0,10,230),fill='#8047b4')
    d.text((42,25),'ARQUIVO PÚBLICO  /  EDIÇÃO EXTRA',font=font(18,'mono'),fill='#694476')
    d.line((42,60,1315,60),fill='#9984a7',width=2)
    lines(d,text,(42,82),size=54,width=1260,spacing=1.12,fill='#201327')
    return im
HEADLINES=['Incidente interrompe operação\nno Repositório Vértice','Arquivos são encontrados danificados','Circunstâncias ainda\nestão sob investigação']

def create_physical_assets():
    im=Image.new('RGBA',(W,H));d=ImageDraw.Draw(im)
    d.text((100,151),'INVESTIGAÇÃO FÍSICA',font=font(23,'mono'),fill=PURPLE)
    lines(d,'A sala também faz parte do caso.',(95,210),size=65,width=1720)
    d.text((100,915),'Compare os materiais encontrados com os registros do OS.',font=font(32),fill='#d7bbf0')
    im.save(ASSETS/'titulo_12.png')
    for k,label in enumerate(['PAINEL DE FUNCIONÁRIOS','PASTAS ESCONDIDAS','CRACHÁ ESCONDIDO']):
        im=Image.new('RGBA',(550,500));d=ImageDraw.Draw(im)
        d.rounded_rectangle((4,4,546,494),radius=20,fill='#1b102a',outline='#775099',width=2)
        if k==0:
            d.rectangle((70,65,480,345),outline='#bb8ef0',width=4)
            for x,y in [(100,95),(230,95),(360,95),(100,220),(230,220),(360,220)]:
                d.rectangle((x,y,x+85,y+100),outline='#9270b4',width=2);d.ellipse((x+25,y+13,x+60,y+48),fill='#9c79bc');d.rounded_rectangle((x+13,y+53,x+72,y+82),radius=12,fill='#9c79bc')
        elif k==1:
            for dx,dy in [(38,-25),(18,-12),(0,0)]:
                d.rounded_rectangle((90+dx,140+dy,445+dx,345+dy),radius=12,fill='#523273',outline='#c49bf0',width=3)
                d.rectangle((105+dx,116+dy,240+dx,143+dy),fill='#8152a8')
            d.line((133,217,390,217),fill='#e0c5f8',width=5);d.line((133,250,345,250),fill='#b994d5',width=4)
        else:
            d.arc((215,25,335,135),180,360,fill='#b58bd9',width=7)
            d.rounded_rectangle((157,100,395,355),radius=15,fill='#39224e',outline='#cfabed',width=4)
            d.rounded_rectangle((230,118,321,132),radius=5,fill='#b58bd9')
            d.ellipse((236,157,310,231),fill='#ad87cf');d.rounded_rectangle((205,235,342,270),radius=17,fill='#ad87cf')
            for y in [301,320]:d.line((205,y,347,y),fill='#9270b4',width=4)
        d.text((275,415),label,font=font(23),fill=WHITE,anchor='mm')
        im.save(ASSETS/f'fisico_{k}.png')

def create_assets():
    create_physical_assets();base().save(ASSETS/'fundo.png');base(True).save(ASSETS/'fundo_tutorial.png')
    for i,text in enumerate(HEADLINES):card(text,i).save(ASSETS/f'manchete_{i}.png')
    for s in SCENES:
        if 4<=s['id']<=10:title_asset(s).save(ASSETS/f'titulo_{s["id"]:02}.png')
    for id in [2,3,11]:
        s=next(s for s in SCENES if s['id']==id);im=Image.new('RGBA',(W,H));d=ImageDraw.Draw(im)
        if id==2:
            d.text((100,240),'REGISTROS COMPROMETIDOS',font=font(23,'mono'),fill=PURPLE)
            lines(d,'O tempo\nestá correndo.',(95,300),size=96,width=1100,spacing=1.1)
            lines(d,'Recuperar os dados é apenas o começo.',(102,555),size=33,width=1050,fill=MUTED,style='regular')
            d.text((104,756),'DADOS DISPONÍVEIS  /  CONEXÕES INCOMPLETAS',font=font(19,'mono'),fill='#a18bb5')
        elif id==3:
            geo(d,1620,445,155,'#8852b2',3)
            d.text((104,224),'SUA MISSÃO',font=font(24,'mono'),fill=PURPLE)
            lines(d,'O ARQUIVO\nCORROMPIDO',(95,300),size=115,width=1400,spacing=1.03)
            d.line((104,600,1300,600),fill='#70468b',width=2)
            d.text((104,655),'Investigue. Compare. Reconstrua.',font=font(45),fill='#d8baff')
            d.text((108,767),'UMA EQUIPE  /  UM MISTÉRIO  /  UM PRAZO',font=font(23,'mono'),fill=MUTED)
        else:
            geo(d,1650,425,150,'#734798',2)
            d.text((104,246),'VIG.IA OS  /  INVESTIGAÇÃO',font=font(23,'mono'),fill=PURPLE)
            lines(d,'A investigação\ncomeça agora.',(95,325),size=104,width=1450,spacing=1.07)
            d.text((104,615),'Vocês conseguem reconstruir o que aconteceu?',font=font(36),fill='#d9bfff')
            d.text((104,858),'Separem papel e caneta.',font=font(26,'regular'),fill=MUTED)
            d.text((104,931),'MÚSICA: Long Note One — Kevin MacLeod (incompetech.com)',font=font(17,'regular'),fill='#a99ab8')
            d.text((104,957),'Licença CC BY 4.0  •  creativecommons.org/licenses/by/4.0/',font=font(17,'regular'),fill='#a99ab8')
        im.save(ASSETS/f'titulo_{id:02}.png')
    # Distinct layers for damaged records; no names, timestamps or clue text.
    for i in range(8):
        im=Image.new('RGBA',(270,170));d=ImageDraw.Draw(im)
        d.rounded_rectangle((2,2,268,168),radius=7,fill=(24,13,38,175),outline=(141,92,184,170),width=2)
        for j in range(5):
            x=20+((i*19+j*31)%65);y=24+j*25
            d.rectangle((x,y,min(245,x+100+(j*31)%90),y+5),fill=(171,127,210,50+j*15))
        im.save(ASSETS/f'bloco_{i}.png')

def subtitle_chunks(text,maxchars=76):
    parts=[]
    for sentence in re.split(r'(?<=[.!?])\s+',text):
        words=sentence.split();chunk=[]
        while words:
            if chunk and len(' '.join(chunk+[words[0]]))>maxchars:
                if chunk[-1].lower() in {'o','a','os','as','um','uma','e','de','do','da','no','na','com','pela','pelo'}:words.insert(0,chunk.pop())
                parts.append(' '.join(chunk));chunk=[]
            else:chunk.append(words.pop(0))
        if chunk:parts.append(' '.join(chunk))
    parts=[x.replace('VIGIA','VIG.IA') for x in parts]
    return parts
def ass_time(t):
    c=round(t*100);return f'{c//360000}:{c//6000%60:02}:{c//100%60:02}.{c%100:02}'
def srt_time(t):
    ms=round(t*1000);return f'{ms//3600000:02}:{ms//60000%60:02}:{ms//1000%60:02},{ms%1000:03}'
def ass_text(text):return text.replace('\\','\\\\').replace('{','').replace('}','')
ASS_HEADER='''[Script Info]
ScriptType: v4.00+
PlayResX: 1920
PlayResY: 1080
WrapStyle: 0
[V4+ Styles]
Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding
Style: Default,Segoe UI,29,&H00FFF5EF,&H000000FF,&H00120A1C,&H7F100A18,0,0,0,0,100,100,0,0,3,11,0,2,80,80,36,1
[Events]
Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text
'''
def audio_and_subtitles():
    rate=48000;n=rate*TOTAL;voice_mix=np.zeros(n,dtype=np.float32);duck=np.ones(n,dtype=np.float32)*.24;subs=[];report=[]
    for s in SCENES:
        source=OUT/f'audio/voz_{s["id"]:02}.wav'
        with wave.open(str(source)) as f:duration=f.getnframes()/f.getframerate()
        room=s['duration']-1.15;speed=max(1.08,duration/room)
        dst=OUT/f'audio/narracao_{s["id"]:02}.wav'
        run(['-i',source,'-af',f'atempo={speed:.6f},highpass=f=85,lowpass=f=10000','-ar',rate,'-ac',1,'-c:a','pcm_s16le',dst])
        with wave.open(str(dst)) as f:v=np.frombuffer(f.readframes(f.getnframes()),dtype='<i2').astype(np.float32)/32768
        rms=np.sqrt(np.mean(v*v));v*=.135/max(.001,rms);v=np.clip(v,-.82,.82)
        a=int((s['start']+.45)*rate);b=min(n,a+len(v));voice_mix[a:b]+=v[:b-a]
        # Music smoothly ducks for each spoken passage.
        for x,y,lo,hi in [(max(0,a-int(.25*rate)),a,.24,.065),(a,b,.065,.065),(b,min(n,b+int(.45*rate)),.065,.24)]:
            if y>x:duck[x:y]=np.minimum(duck[x:y],np.linspace(lo,hi,y-x,dtype=np.float32))
        parts=subtitle_chunks(s['voice']);total=sum(len(x) for x in parts);cursor=.45;local=[]
        for part in parts:
            dur=(len(v)/rate)*len(part)/total
            local.append((cursor,cursor+dur,part));subs.append((s['start']+cursor,s['start']+cursor+dur,part));cursor+=dur
        ass=ASS_HEADER+''.join(f'Dialogue: 0,{ass_time(a)},{ass_time(b)},Default,,0,0,0,,{ass_text(t)}\n' for a,b,t in local)
        (RENDERS/f'subs_{s["id"]:02}.ass').write_text(ass,encoding='utf-8-sig')
        report.append({'scene':s['id'],'original_seconds':duration,'tempo_factor':speed,'voice_seconds':len(v)/rate,'start':s['start']+.45,'end':b/rate})
    raw=run(['-i',ROOT/'output/vigia_os_sistema/audio/trilha/long-note-one.mp3','-t',TOTAL,'-ar',rate,'-ac',2,'-f','f32le','pipe:1'])
    music=np.frombuffer(raw,dtype='<f4').reshape(-1,2)[:n];mix=np.zeros((n,2),dtype=np.float32);mix[:len(music)]=music*duck[:len(music),None]
    mix+=voice_mix[:,None]
    rng=np.random.default_rng(17)
    for at in sorted({s['start'] for s in SCENES}|{1,2,4}):
        length=int(.13*rate);tt=np.arange(length)/rate
        effect=(rng.normal(size=length)*.023+np.sin(2*np.pi*(330+1300*tt)*tt)*.035)*np.exp(-tt*40)
        i=int(at*rate);mix[i:i+length]+=effect[:,None]
    fade=np.ones(n);fade[:rate*2]=np.linspace(0,1,rate*2);fade[-rate:]=np.linspace(1,0,rate)
    mix*=fade[:,None];mix=np.clip(mix,-.94,.94)
    premix=TMP/'premix.wav'
    with wave.open(str(premix),'wb') as f:f.setnchannels(2);f.setsampwidth(2);f.setframerate(rate);f.writeframes((mix*32767).astype('<i2').tobytes())
    run(['-i',premix,'-af','loudnorm=I=-16:TP=-1.5:LRA=9','-ar',rate,'-c:a','pcm_s16le',OUT/'audio/trilha_mixada.wav'])
    (OUT/'legendas.srt').write_text('\n\n'.join(f'{i+1}\n{srt_time(a)} --> {srt_time(b)}\n{t}' for i,(a,b,t) in enumerate(subs))+'\n',encoding='utf-8')
    (OUT/'audio/temporizacao.json').write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf-8')

def animated_x(x,at=0,delta=-140):return f'{x}+({delta})*pow(max(0,1-(t-{at})/0.65),3)'
def render_scene(s,capture):
    id=s['id'];duration=s['duration'];args=[];chain=[];index=0
    def img(p):
        nonlocal index
        args.extend(['-loop','1','-framerate','30','-i',p]);i=index;index+=1;return i
    def video(p,start):
        nonlocal index
        args.extend(['-ss',max(0,start),'-i',p]);i=index;index+=1;return i
    def over(current,i,out,x,y,at=0,fade=True):
        source=f'{i}:v'
        if fade:
            chain.append(f'[{source}]format=rgba,fade=t=in:st={at}:d=0.5:alpha=1[l{i}]');source=f'l{i}'
        chain.append(f'[{current}][{source}]overlay=x=\'{x}\':y=\'{y}\':enable=\'gte(t,{at})\':shortest=1[{out}]');return out
    if 4<=id<=10:
        i=img(ASSETS/'fundo_tutorial.png');chain.append(f'[{i}:v]format=yuv420p[b]');current='b'
        seg=next(x for x in capture['segments'] if x['id']==id);i=video(capture['video'],capture['offset']+seg['start'])
        chain.append(f'[{i}:v]setpts=PTS-STARTPTS,scale=1320:825,fps=30,tpad=stop_mode=clone:stop_duration=4[v]')
        chain.append('[b][v]overlay=540:112:shortest=1[vb]');current='vb'
        i=img(ASSETS/f'titulo_{id:02}.png');current=over(current,i,'t',animated_x(0),0)
    elif id==12:
        i=img(ASSETS/'fundo.png');chain.append(f'[{i}:v]format=yuv420p[b]');current='b'
        for k in range(3):
            i=img(ASSETS/f'fisico_{k}.png');current=over(current,i,f'p{k}',animated_x(90+k*590,1+k*2.5,-130),350,1+k*2.5)
        i=img(ASSETS/'titulo_12.png');current=over(current,i,'t',animated_x(0),0)
    elif id==1:
        i=img(ASSETS/'abertura_corredor.png');chain.append(f'[{i}:v]scale=2048:1152,crop=1920:1080:x=\'64+20*sin(t/10)\':y=36,eq=brightness=-0.025:saturation=0.8[b]');current='b'
        for k,(at,x,y) in enumerate([(0.8,104,175),(5.0,302,438),(9.2,160,685)]):
            i=img(ASSETS/f'manchete_{k}.png');current=over(current,i,f'h{k}',animated_x(x,at,-550 if k%2==0 else 650),y,at)
    else:
        i=img(ASSETS/'fundo.png');chain.append(f'[{i}:v]format=yuv420p[b]');current='b'
        if id==2:
            for k in range(8):
                i=img(ASSETS/f'bloco_{k}.png');x=1270+(k%3)*180;y=150+(k//3)*235
                current=over(current,i,f'd{k}',f'{x}+26*sin(t/{2+k/4}+{k})',f'{y}+16*cos(t/3+{k})',0)
        i=img(ASSETS/f'titulo_{id:02}.png');current=over(current,i,'t',animated_x(0,0,-80),0)
    subs=f'tmp/video_inicial/renders_v2/subs_{id:02}.ass'
    chain.append(f'[{current}]drawbox=x=60:y=1040:w=1800:h=3:color=0x382445:t=fill,drawbox=x=60:y=1040:w={max(2,round(1800*s["start"]/TOTAL))}:h=3:color=0xb88aff:t=fill,ass=\'{subs}\',fade=t=in:st=0:d=0.25,fade=t=out:st={duration-.3}:d=0.3,format=yuv420p[out]')
    graph=';'.join(chain);(RENDERS/f'graph_{id:02}.txt').write_text(graph,encoding='utf-8')
    args+=['-filter_complex_threads','2','-filter_complex',graph,'-map','[out]','-t',duration,'-an','-c:v','libx264','-preset','veryfast','-crf','19','-r','30','-threads','4','-movflags','+faststart',RENDERS/f'cena_{id:02}.mp4']
    run(args,RENDERS/f'cena_{id:02}.log')
    print(f'Cena {id:02} renderizada.',flush=True)

def storyboards():
    captions={12:'Animação do painel de funcionários, pastas e crachá sem dados ou esconderijos; orientação para cruzar materiais físicos e digitais.',1:'Manchetes entram em camadas; leitura sustentada e interferência breve.',2:'Blocos incompletos se deslocam ao lado da mensagem sobre o prazo.',3:'Título e missão aparecem em sequência, preparando a entrada no OS.',4:'Abrir, minimizar e restaurar aplicativos pela barra de tarefas.',5:'Pesquisar, abrir uma prévia e ampliar um documento fictício.',6:'Reproduzir e pausar um exemplo neutro; localizar a transcrição.',7:'Enviar uma pergunta genérica, observar a digitação e consultar a memória.',8:'Enviar um exemplo com Enter e observar a orientação da interface.',9:'Arrastar cartões fictícios para demonstrar a ordenação dos eventos.',10:'Consultar Próximos passos.txt e localizar tempo e memória.',11:'Sustentar o desafio final e encerrar com créditos da trilha.'}
    cards=[]
    for s in SCENES:
        id=s['id'];im=base(4<=id<=10)
        if id==12:
            for k in range(3):im.alpha_composite(Image.open(ASSETS/f'fisico_{k}.png'),(90+k*590,350))
            im.alpha_composite(Image.open(ASSETS/'titulo_12.png'))
        elif id==1:
            im=Image.open(ASSETS/'abertura_corredor.png').convert('RGBA').resize((W,H),Image.Resampling.LANCZOS)
            for k,(x,y) in enumerate([(104,175),(302,438),(160,685)]):im.alpha_composite(card(HEADLINES[k],k),(x,y))
        elif 4<=id<=10:
            files=list((OUT/'capturas').glob(f'{id:02}_*.png'))
            if files:im.alpha_composite(Image.open(files[0]).convert('RGBA').resize((1320,825),Image.Resampling.LANCZOS),(540,112))
            im.alpha_composite(title_asset(s))
        else:im.alpha_composite(Image.open(ASSETS/f'titulo_{id:02}.png'))
        frame=im.convert('RGB');frame.save(STORY/f'{id:02}_quadro.png')
        cardim=Image.new('RGB',(W,1280),'#120c1b');cardim.paste(frame,(0,0));d=ImageDraw.Draw(cardim)
        d.text((55,1110),f'CENA {id:02}  /  {s["start"]//60:02}:{s["start"]%60:02} — {(s["start"]+s["duration"])//60:02}:{(s["start"]+s["duration"])%60:02}',font=font(24,'mono'),fill=PURPLE)
        lines(d,captions[id],(55,1165),size=28,width=1800,fill=WHITE,style='regular')
        cardim.save(STORY/f'{id:02}_storyboard.png');cards.append(cardim)
    for page in range(2):
        sheet=Image.new('RGB',(1920,1540),'#09060e');d=ImageDraw.Draw(sheet)
        d.text((40,24),f'VIG.IA OS  /  STORYBOARD TÉCNICO  /  {page+1:02}',font=font(30),fill=WHITE)
        for idx,im in enumerate(cards[page*6:page*6+6]):
            x=40+(idx%3)*630;y=90+(idx//3)*710
            im=im.resize((600,400),Image.Resampling.LANCZOS);sheet.paste(im,(x,y))
            s=SCENES[page*6+idx]
            lines(d,s['voice'],(x,y+420),size=23,width=594,spacing=1.35,fill=MUTED,style='regular')
        sheet.save(STORY/f'STORYBOARD_{page+1:02}.png')
    # Human-readable plan, delivered with its visual frames.
    plan='# Storyboard — VIG.IA OS\n\nDuração: 2min46. Horizontal 1920×1080, 30fps. Narração sintética em português brasileiro.\n\nAs telas do tutorial são gravações do OS com conteúdo fictício. Nenhuma resposta ou cena da solução é mostrada.\n\n'
    for s in SCENES:
        plan+=f'## Cena {s["id"]:02} · {s["start"]//60:02}:{s["start"]%60:02} · {s["duration"]}s\n\n**Visual e movimento:** {captions[s["id"]]}\n\n**Narração:** {s["voice"]}\n\n**Texto de apoio:** {s["title"].replace(chr(10)," ")} — {s["body"].replace(chr(10)," ")}\n\n'
    (OUT/'PLANEJAMENTO_STORYBOARD.md').write_text(plan,encoding='utf-8')

def main():
    create_assets()
    if '--storyboard' in sys.argv:storyboards();print('Storyboards gerados.');return
    capture=json.loads((OUT/'capturas/gravao.json').read_text(encoding='utf-8'))
    # Playwright recording starts before navigation; a visual marker is located separately.
    capture['offset']=json.loads((OUT/'capturas/alinhamento.json').read_text(encoding='utf-8'))['offset_seconds']
    audio_and_subtitles()
    for s in SCENES:
        p=RENDERS/f'cena_{s["id"]:02}.mp4'
        if not p.exists() or p.stat().st_size<1024 or '--force' in sys.argv:render_scene(s,capture)
    concat=RENDERS/'concat.txt';concat.write_text('\n'.join("file '"+p.as_posix()+"'" for p in [RENDERS/f'cena_{s["id"]:02}.mp4' for s in SCENES]),encoding='utf-8')
    run(['-f','concat','-safe','0','-i',concat,'-i',OUT/'audio/trilha_mixada.wav','-map','0:v:0','-map','1:a:0','-vf','setsar=1','-c:v','libx264','-preset','veryfast','-crf','19','-threads','4','-c:a','aac','-b:a','192k','-t',TOTAL,'-movflags','+faststart',OUT/'VIGIA_OS_Introducao_Tutorial_v2.mp4'],RENDERS/'export.log')
    for s in SCENES:
        at=min(s['duration']-1,8 if s['id']==1 else s['duration']/2)
        run(['-ss',at,'-i',RENDERS/f'cena_{s["id"]:02}.mp4','-frames:v','1',STORY/f'{s["id"]:02}_frame_final.png'])
    print('MP4 final exportado.',flush=True)
if __name__=='__main__':main()
