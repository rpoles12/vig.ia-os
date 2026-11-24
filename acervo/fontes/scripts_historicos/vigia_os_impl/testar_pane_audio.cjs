const fs=require('fs'),vm=require('vm'),assert=require('assert'),path=require('path');
const root=path.resolve(__dirname,'../..'),tracks=[];let toggle,tones=0,stops=0,checks=0;
const eq=(a,b)=>{assert.deepStrictEqual(a,b);checks++};
const classList={remove(){},toggle(){}};const form={querySelectorAll(){return []},classList,addEventListener(){}};
const document={body:{append(){}},addEventListener(){},createElement(tag){if(tag!=='audio')return {setAttribute(){}};const a={paused:true,currentTime:0,plays:0,setAttribute(){},addEventListener(){},play(){this.paused=false;this.plays++;return Promise.resolve()},pause(){this.paused=true}};tracks.push(a);return a},querySelector(){return {append(node){toggle=node}}},getElementById(id){return ['identity','accessform','finalform'].includes(id)?form:{classList}}};
const param={setValueAtTime(){},exponentialRampToValueAtTime(){},linearRampToValueAtTime(){}};const node=()=>({frequency:param,connect(){},disconnect(){},start(){},stop(){stops++}});
class FakeAudio{constructor(){this.state='running';this.currentTime=0;this.destination={}}createOscillator(){tones++;return node()}createGain(){return {gain:param,connect(){},disconnect(){}}}}
const box={document,window:null,AudioContext:FakeAudio};box.window=box;vm.createContext(box);vm.runInContext(fs.readFileSync(path.join(root,'output/vigia_os_sistema/feedback.js'),'utf8'),box);
eq(tracks.length,3);for(const track of tracks){eq(track.loop,true);eq(track.paused,true);eq(track.hidden,true);eq(track.volume>0&&track.volume<=1,true);eq(fs.existsSync(path.join(root,'output/vigia_os_sistema',track.src)),true)}
box.VigiaFeedback.deadlineWarning(false,60);eq(tones,2);box.VigiaFeedback.deadlineWarning(true,10);eq(tones,3);
box.VigiaFeedback.deadlineExpired();for(const track of tracks){eq(track.paused,false);eq(track.plays,1)}eq(stops>=3,true);
for(const track of tracks)track.currentTime=35;
box.VigiaFeedback.deadlineExpired();for(const track of tracks){eq(track.currentTime,35);eq(track.plays,1)}
toggle.onclick();for(const track of tracks)eq(track.paused,true);
toggle.onclick();for(const track of tracks){eq(track.paused,false);eq(track.currentTime,35)}
box.VigiaFeedback.stopDeadline();for(const track of tracks){eq(track.paused,true);eq(track.currentTime,0)}
toggle.onclick();box.VigiaFeedback.deadlineExpired();for(const track of tracks)eq(track.paused,true);
toggle.onclick();for(const track of tracks)eq(track.paused,false);
box.VigiaFeedback.reset();for(const track of tracks){eq(track.paused,true);eq(track.currentTime,0)}
toggle.onclick();toggle.onclick();for(const track of tracks)eq(track.paused,true);
const report={date:'2026-11-19',result:'passed',checks,coverage:['Três MP3s reais e locais','Loops contínuos sem temporizador de encerramento','Reentrada não reinicia nem duplica os áudios','Mute e reativação durante a falha','Encerramento e reinício param e rebobinam todos os loops','Alertas anteriores preservados']};fs.writeFileSync(path.join(root,'tmp/vigia_os_impl/pane_audio.json'),JSON.stringify(report,null,2));console.log(JSON.stringify(report));
