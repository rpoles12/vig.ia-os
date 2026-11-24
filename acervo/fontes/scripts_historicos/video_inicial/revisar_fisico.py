from pathlib import Path
import json,shutil
ROOT=Path(__file__).resolve().parents[2];P=ROOT/'producao/video_inicial';O=ROOT/'output/video_inicial'
backup=ROOT/'tmp/video_inicial/base_antes_materiais_fisicos'
if not backup.exists():
    backup.mkdir(parents=True)
    for n in ['cenas.json','montar_video.py','verificar_video.py','PROJETO.md']:shutil.copy2(P/n,backup/n)
    shutil.copytree(O/'storyboard',backup/'storyboard')
scenes=json.loads((backup/'cenas.json').read_text(encoding='utf-8'))
for s in scenes:
    if s['start']>=42:s['start']+=16
physical={'id':12,'start':42,'duration':16,'kind':'physical','title':'A sala também\nfaz parte do caso.','label':'INVESTIGAÇÃO FÍSICA','body':'Consulte o painel de funcionários.\nProcure as pastas e o crachá escondidos.\nCompare com os registros do OS.','voice':'A investigação também acontece fora do computador. Consultem o painel de funcionários e procurem as pastas e o crachá escondidos na sala. Comparem esses materiais com os registros do sistema. Uma informação pode ajudar a interpretar outra.'}
scenes.insert(3,physical)
(P/'cenas.json').write_text(json.dumps(scenes,ensure_ascii=False,indent=2),encoding='utf-8')
t=(backup/'montar_video.py').read_text(encoding='utf-8')
t=t.replace("RENDERS=TMP/'renders'","RENDERS=TMP/'renders_v2'")
t=t.replace("SCENES=json.loads((Path(__file__).parent/'cenas.json').read_text(encoding='utf-8'))","SCENES=json.loads((Path(__file__).parent/'cenas.json').read_text(encoding='utf-8'))\nTOTAL=max(s['start']+s['duration'] for s in SCENES)")
t=t.replace("s=SCENES[id-1]","s=next(s for s in SCENES if s['id']==id)")
t=t.replace('rate*150','rate*TOTAL').replace("'-t',150","'-t',TOTAL").replace('1800*s["start"]/150','1800*s["start"]/TOTAL')
t=t.replace("'VIGIA_OS_Introducao_Tutorial.mp4'","'VIGIA_OS_Introducao_Tutorial_v2.mp4'")
t=t.replace('tmp/video_inicial/renders/subs_', 'tmp/video_inicial/renders_v2/subs_')
t=t.replace("if not p.exists() or '--force'", "if not p.exists() or p.stat().st_size<1024 or '--force'")
t=t.replace('Duração: 2min30.','Duração: 2min46.')
t=t.replace("captions={1:","captions={12:'Animação do painel de funcionários, pastas e crachá sem dados ou esconderijos; orientação para cruzar materiais físicos e digitais.',1:")
t=t.replace("base().save(ASSETS/'fundo.png');", "create_physical_assets();base().save(ASSETS/'fundo.png');")
t=t.replace("    elif id==1:\n", "    elif id==12:\n        i=img(ASSETS/'fundo.png');chain.append(f'[{i}:v]format=yuv420p[b]');current='b'\n        for k in range(3):\n            i=img(ASSETS/f'fisico_{k}.png');current=over(current,i,f'p{k}',animated_x(90+k*590,1+k*2.5,-130),350,1+k*2.5)\n        i=img(ASSETS/'titulo_12.png');current=over(current,i,'t',animated_x(0),0)\n    elif id==1:\n")
t=t.replace("        if id==1:\n", "        if id==12:\n            for k in range(3):im.alpha_composite(Image.open(ASSETS/f'fisico_{k}.png'),(90+k*590,350))\n            im.alpha_composite(Image.open(ASSETS/'titulo_12.png'))\n        elif id==1:\n")
physical_code='''
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

'''
t=t.replace('def create_assets():',physical_code+'def create_assets():')
(P/'montar_video.py').write_text(t,encoding='utf-8')
v=(backup/'verificar_video.py').read_text(encoding='utf-8').replace('Tutorial.mp4','Tutorial_v2.mp4').replace('seconds-150','seconds-166').replace('range(1,12)','range(1,13)')
(P/'verificar_video.py').write_text(v,encoding='utf-8')
with (P/'PROJETO.md').open('a',encoding='utf-8') as f:f.write('\n\n## Revisão 24/11/2026\n\nInserida cena de 16 segundos entre a missão e o tutorial digital: consultar o painel de funcionários, procurar pastas e crachá escondidos na sala e comparar os materiais físicos com os registros do OS. Ilustrações genéricas, sem dados ou esconderijos. Duração final: 2min46. Versão anterior preservada. Duas páginas de jornal A4 criadas para a abertura física da investigação.\n')
print('Revisão preparada: 166 segundos, 12 cenas.')
