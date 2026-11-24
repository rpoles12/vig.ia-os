"""Small deterministic UI assets matched to the existing purple SVG icon family."""
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
import json

ROOT=Path(__file__).resolve().parents[2]
BASE=ROOT/'output/vigia_os_sistema'
DEST=BASE/'assets/os/cursors'
DEST.mkdir(parents=True,exist_ok=True)
S=4
EDGE='#13091f';LIGHT='#f6e9ff';FILL='#b47ae9';DARK='#683198'
def canvas():return Image.new('RGBA',(32*S,32*S)),None
def poly(d,pts,fill=FILL):
    p=[(round(x*S),round(y*S)) for x,y in pts]
    d.polygon(p,fill=fill)
    d.line(p+[p[0]],fill=EDGE,width=round(3*S),joint='curve')
    d.line(p+[p[0]],fill=LIGHT,width=round(1.1*S),joint='curve')
def line(d,pts,width=1.3,color=LIGHT,outline=True):
    p=[(round(x*S),round(y*S)) for x,y in pts]
    if outline:d.line(p,fill=EDGE,width=round((width+2)*S),joint='curve')
    d.line(p,fill=color,width=round(width*S),joint='curve')
def ellipse(d,box,fill=None,width=1.3):
    b=tuple(round(x*S) for x in box)
    if fill:d.ellipse(b,fill=fill)
    d.ellipse(b,outline=EDGE,width=round((width+2)*S))
    b2=(b[0]+S,b[1]+S,b[2]-S,b[3]-S)
    d.ellipse(b2,outline=LIGHT,width=round(width*S))
def arrow(d,small=False):
    pts=[(3,2),(3,24),(9,18),(14,28),(19,25),(14,16),(24,15)]
    if small:pts=[(x*.72,y*.72) for x,y in pts]
    poly(d,pts)
    if not small:line(d,[(5.4,7.5),(5.4,18)],.8,LIGHT,False)
def base_arrow():
    im,_=canvas();d=ImageDraw.Draw(im);arrow(d);return im
assets={}
def save(name,im,label,hotspot):
    im=im.resize((32,32),Image.Resampling.LANCZOS)
    im.save(DEST/(name+'.png'),optimize=True)
    assert im.mode=='RGBA' and im.getextrema()[3][0]==0 and im.getextrema()[3][1]==255
    assets[name]={'arquivo':name+'.png','uso':label,'hotspot':hotspot,'dimensoes':[32,32]}
save('default',base_arrow(),'Navegação',[3,2])
im,_=canvas();d=ImageDraw.Draw(im)
poly(d,[(11,16),(11,4),(12,2),(15,2),(16,4),(16,12),(18,10),(21,11),(22,13),(25,13),(27,16),(27,23),(24,29),(14,29),(8,23),(4,18),(4,16),(6,14),(8,15)])
line(d,[(16,13),(16,19)],.8,DARK,False);line(d,[(21,14),(21,19)],.8,DARK,False)
save('pointer',im,'Botões e atalhos',[12,3])
im,_=canvas();d=ImageDraw.Draw(im)
for pts in [[(10,3),(14,3),(16,5),(18,3),(22,3)],[(16,5),(16,27)],[(10,29),(14,29),(16,27),(18,29),(22,29)]]:line(d,pts,1.8)
line(d,[(16,10),(16,22)],.9,FILL,False)
save('text',im,'Campos de texto',[16,16])
im,_=canvas();d=ImageDraw.Draw(im)
poly(d,[(9,18),(6,12),(6,9),(8,8),(10,10),(12,15),(10,5),(11,3),(13,3),(15,14),(15,2),(18,2),(18,14),(20,4),(23,4),(22,16),(25,8),(28,9),(27,19),(25,27),(20,30),(13,28),(7,23),(3,19),(3,16),(5,15)])
line(d,[(13,19),(15,24)],.9,DARK,False);line(d,[(19,18),(19,24)],.9,DARK,False)
save('grab',im,'Arrastar janela ou cartão',[16,16])
im,_=canvas();d=ImageDraw.Draw(im)
poly(d,[(8,19),(8,10),(11,8),(14,10),(14,7),(18,7),(20,10),(23,9),(26,11),(26,23),(23,29),(13,29),(7,24),(3,20),(3,16),(6,15)])
for x in [13,18,22]:line(d,[(x,13),(x,18)],.9,DARK,False)
save('grabbing',im,'Arrasto em andamento',[16,17])
im,_=canvas();d=ImageDraw.Draw(im)
poly(d,[(3,3),(15,3),(11,7),(25,21),(29,17),(29,29),(17,29),(21,25),(7,11),(3,15)])
line(d,[(10,10),(22,22)],1,DARK,False)
save('resize-nwse',im,'Redimensionar janela',[16,16])
im,_=canvas();d=ImageDraw.Draw(im);ellipse(d,(4,4,28,28),DARK,1.6);line(d,[(8,8),(24,24)],2.4)
save('not-allowed',im,'Ação indisponível',[16,16])
im,_=canvas();d=ImageDraw.Draw(im);arrow(d,True)
poly(d,[(23,13),(30,17),(30,25),(23,29),(16,25),(16,17)],DARK)
line(d,[(23,17),(23,21),(26,23)],1.3)
save('wait',im,'Carregamento de documento',[2,2])
for name,plus in [('zoom-in',True),('zoom-out',False)]:
    im,_=canvas();d=ImageDraw.Draw(im)
    line(d,[(20,20),(28,28)],5,FILL)
    ellipse(d,(3,3,24,24),DARK,1.5)
    line(d,[(8,13),(19,13)],1.5)
    if plus:line(d,[(13.5,8),(13.5,19)],1.5)
    save(name,im,'Ampliar documento' if plus else 'Reduzir documento',[13,13])
im,_=canvas();d=ImageDraw.Draw(im);arrow(d,True);ellipse(d,(15,14,31,30),DARK,1.2)
font=ImageFont.truetype('C:/Windows/Fonts/segoeuib.ttf',15*S)
d.text((23*S,21*S),'?',font=font,anchor='mm',fill=LIGHT,stroke_width=0)
save('help',im,'Ajuda e capacidades da IA',[2,2])

meta={'identidade':'VIGIA/3 — roxo, lilás e borda clara com contraste escuro','producao':'Desenho geométrico local para combinar com os ícones SVG do projeto; PNG RGBA com antialiasing.','tamanho_cursor':'32x32 px','cursores':assets}
(DEST/'manifest.json').write_text(json.dumps(meta,ensure_ascii=False,indent=2),encoding='utf-8')
font=ImageFont.truetype('C:/Windows/Fonts/segoeui.ttf',16)
bold=ImageFont.truetype('C:/Windows/Fonts/segoeuib.ttf',25)
preview=Image.new('RGB',(1000,690),'#100b18');d=ImageDraw.Draw(preview)
d.text((32,24),'VIGIA/3  /  CURSORES DO OS',font=bold,fill='#dfc2fa')
d.text((33,65),'11 PNGs transparentes · 32 × 32 px · visual ampliado para conferência',font=font,fill='#a991be')
for i,(name,item) in enumerate(assets.items()):
    x=24+(i%4)*244;y=108+(i//4)*187
    d.rounded_rectangle((x,y,x+230,y+170),12,fill='#21152d',outline='#573968')
    for j,color in enumerate(['#0c0811','#e8ddf0']):
        tx=x+18+j*102;ty=y+16;d.rounded_rectangle((tx,ty,tx+92,ty+91),8,fill=color)
        icon=Image.open(DEST/item['arquivo']).resize((72,72),Image.Resampling.NEAREST)
        preview.paste(icon,(tx+10,ty+9),icon)
    d.text((x+16,y+118),item['uso'],font=font,fill='#e7d6f5')
    d.text((x+16,y+141),name+'.png',font=font,fill='#a588bd')
preview.save(DEST/'previa-cursores.png',optimize=True)
print('11 cursores PNG RGBA criados em',DEST)
