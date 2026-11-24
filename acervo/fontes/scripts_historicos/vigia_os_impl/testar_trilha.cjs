const fs=require('fs'),path=require('path'),vm=require('vm'),assert=require('assert');
const root=path.resolve(__dirname,'../..'),source=path.join(root,'output/vigia_os_sistema');
let now=0,next=0,checks=0;const frames=new Map(),timers=new Map(),listeners=new Map(),elements=new Map();
const check=(value,message)=>{assert(value,message);checks++};
function el(){return {value:0,hidden:false,dataset:{},classList:{toggle(){}},setAttribute(k,v){this[k]=v},before(){},textContent:'',title:''}}
for(const id of ['mini-transcript','music-volume-value','music-volume','music-toggle','music-state'])elements.set('#'+id,el());elements.set('.mini-menu-heading span',el());
const narration={paused:true,ended:false},video={paused:true,ended:false};let bg;
const doc={body:{append(node){bg=node}},createElement(tag){const node=el();if(tag==='audio')Object.assign(node,{paused:true,ended:false,volume:1,currentTime:0,playCount:0,fail:false,addEventListener(){},play(){this.playCount++;if(this.fail)return Promise.reject(Error('autoplay'));this.paused=false;return Promise.resolve()},pause(){this.paused=true}});return node},querySelector(s){return elements.get(s)},querySelectorAll(s){return s==='audio,video'?[narration,video,bg].filter(Boolean):[]},addEventListener(type,fn){if(!listeners.has(type))listeners.set(type,[]);listeners.get(type).push(fn)}};
const context={document:doc,VigiaIcons:{svg:()=>''},performance:{now:()=>now},requestAnimationFrame(fn){const id=++next;frames.set(id,fn);return id},cancelAnimationFrame(id){frames.delete(id)},setTimeout(fn,ms){const id=++next;timers.set(id,{fn,at:now+ms});return id},clearTimeout(id){timers.delete(id)}};context.window=context;vm.createContext(context);vm.runInContext(fs.readFileSync(path.join(source,'ambient.js'),'utf8'),context);
function advance(ms){now+=ms;for(const [id,t] of [...timers])if(t.at<=now){timers.delete(id);t.fn()}const callbacks=[...frames.values()];frames.clear();for(const fn of callbacks)fn(now)}
function event(type,target){for(const fn of listeners.get(type)||[])fn({target})}
const near=(expected,message)=>check(Math.abs(bg.volume-expected)<.00001,message);
(async()=>{
 const api=context.VigiaAmbient;check(bg.paused,'Não toca antes de iniciar');check(bg.loop===true,'Mesma faixa em loop');check(bg.src==='audio/trilha/long-note-one.mp3','Arquivo local fixo');
 api.start();await Promise.resolve();advance(1200);near(.4,'Volume ambiente inicial');check(!bg.paused,'Inicia por ação da rodada');
 narration.paused=false;event('play',narration);advance(200);near(.048,'Redução forte durante narração');
 video.paused=false;event('play',video);narration.paused=true;event('pause',narration);advance(1200);near(.048,'Vídeo mantém redução quando a narração para');
 video.paused=true;event('pause',video);advance(1200);near(.4,'Pausa do vídeo devolve volume ambiente');
 narration.paused=false;event('play',narration);advance(200);narration.ended=true;event('ended',narration);advance(1200);near(.4,'Fim da narração devolve volume');narration.paused=true;narration.ended=false;
 elements.get('#music-volume').oninput({target:{value:'.25'}});advance(1200);near(.25,'Controle independente da trilha');
 elements.get('#music-toggle').onclick();advance(200);near(0,'Silêncio da trilha');elements.get('#music-toggle').onclick();await Promise.resolve();advance(1200);near(.25,'Retoma volume escolhido');
 api.duckFor(1500);advance(200);near(.03,'Efeito de falha recebe espaço sonoro');advance(1400);advance(1200);near(.25,'Recupera volume após efeito');
 check(bg.playCount===1,'Narrações e telas não reiniciam a música');
 bg.currentTime=123;api.reset();advance(2000);check(bg.paused&&bg.currentTime===0,'Reinício interrompe e volta ao começo');near(0,'Nenhum fade pendente depois do reset');
 bg.fail=true;api.start();await Promise.resolve();await Promise.resolve();check(elements.get('#music-state').textContent.includes('Clique'),'Bloqueio de reprodução orienta ativação');bg.fail=false;elements.get('#music-toggle').onclick();await Promise.resolve();advance(1200);check(!bg.paused,'Reprodução pode ser ativada por clique');
 const file=path.join(source,'audio/trilha/long-note-one.mp3');check(fs.statSync(file).size>1000000,'Arquivo de áudio incorporado');check(fs.readFileSync(file).subarray(0,3).toString()==='ID3','Arquivo MP3 válido');
 const report={date:'2026-11-19',result:'passed',checks,coverage:['mesma faixa local em loop','volume ambiente e redução de88%','áudio e vídeo sobrepostos','retorno gradual após pausa/fim','controle e silêncio independentes','efeito de tela azul','reinício limpo','ativação após bloqueio de autoplay']};fs.writeFileSync(path.join(root,'tmp/vigia_os_impl/trilha.json'),JSON.stringify(report,null,2));console.log(JSON.stringify(report));
})().catch(e=>{console.error(e);process.exitCode=1});
