const fs=require('fs'),vm=require('vm'),assert=require('assert'),path=require('path');
const root=path.resolve(__dirname,'../..'),dir=path.join(root,'output/vigia_os_sistema'),out=path.join(root,'tmp/vigia_os_impl');fs.mkdirSync(out,{recursive:true});
const context={};context.window=context;vm.createContext(context);for(const file of ['data.js','vigia.js','engine.js','countdown.js'])vm.runInContext(fs.readFileSync(path.join(dir,file),'utf8'),context);
let n=0;const eq=(a,b)=>{assert.deepStrictEqual(a,b);n++};
const D=context.CASE_DATA,e=context.VigiaEngine.criarVigia(D.vigia,D.key),t=context.VigiaCountdown.create();
const files=()=>D.evidence.filter(x=>x.stage===0||x.stage===1&&e.estado().identityConfirmed||x.stage===2&&e.estado().accessesConfirmed||x.stage===3&&e.estado().chronologyOrdered);
eq(D.evidence.length,25);eq(files().length,8);eq(e.estado().memory,8);eq(e.validarAcessos({fisico:'Helena',digital:'Marcelo'}).ok,false);eq(e.validarCronologia(D.key.correct_order).ok,false);
eq(e.validarIdentidade('Carlos').ok,false);eq(e.validarIdentidade('Bryan Almeida').ok,true);eq(e.estado().evidenceSeen.length,0);eq(files().length,23);eq(e.estado().memory,34);eq(t.award('identity',0).added,15);eq(t.award('identity',1),null);
eq(e.validarAcessos({fisico:'Marcelo',digital:'Helena'}).ok,false);eq(e.validarAcessos({fisico:'Helena Duarte',digital:'Marcelo Vieira'}).ok,true);eq(files().length,24);eq(e.estado().memory,67);eq(t.award('access',0).added,15);
eq(e.validarCronologia([...D.key.correct_order].reverse()).ok,false);eq(e.validarCronologia(D.key.correct_order).ok,true);eq(files().length,25);eq(e.estado().memory,67);eq(t.award('chronology',0).added,15);eq(t.totalBonus(),45);eq(t.remaining(0),795);
eq(e.validarProtocolo({identidade:'Bryan',credencial:'2847',horario:'22:47'}).ok,false);eq(e.validarProtocolo({identidade:'Bryan',credencial:'2847',horario:'22:46'}).ok,true);eq(e.estado().memory,100);eq(e.estado().evidenceSeen.length,0);eq(D.key.answers.generated_protocol,'BA17-2847-2246');eq(t.award('protocol',0),null);
for(const query of ['onde encontro os documentos?','onde registro minha resposta?','quanto tempo temos?','como mover os cartões?'])eq(!!e.orientar(query).text,true);
eq(t.remaining(794.5),1);eq(t.remaining(795),0);eq(t.award('identity',795),null);t.reset();eq(t.totalBonus(),0);eq(t.remaining(0),750);eq(t.signal(690),'warning');eq(t.signal(690.5),null);for(let i=10;i>0;i--)eq(t.signal(750-i),'urgent');eq(t.signal(750),'expired');eq(t.signal(751),null);
e.reiniciar();eq(e.estado().memory,8);eq(e.estado().identityConfirmed,false);eq(files().length,8);
// Every catalog/card media path and every local script/style reference must exist.
for(const x of D.evidence)eq(fs.existsSync(path.join(dir,x.file)),true);for(const x of D.cards){eq(!!x.title&&!!x.description,true);if(x.image)eq(fs.existsSync(path.join(dir,x.image)),true)}
const html=fs.readFileSync(path.join(dir,'index.html'),'utf8');for(const m of html.matchAll(/(?:src|href)="([^"#]+)"/g)){const p=m[1].split('?')[0];if(!p.includes(':'))eq(fs.existsSync(path.join(dir,p)),true)}
const result={date:'2026-11-19',checks:n,result:'passed',coverage:['Progressão 8/34/67/100 e catálogo8/23/24/25','Todas as respostas sem consulta a documentos','Bônus únicos, limites, reset e alertas','Gabarito e caminhos de mídias','Consultas básicas da assistente']};fs.writeFileSync(path.join(out,'motor.json'),JSON.stringify(result,null,2));console.log(JSON.stringify(result));
