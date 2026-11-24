const fs=require('fs'),vm=require('vm'),assert=require('assert'),path=require('path');
const root=path.resolve(__dirname,'../..'),dir=path.join(root,'output/vigia_os_sistema'),box={};box.window=box;vm.createContext(box);for(const name of ['data.js','vigia.js','engine.js','countdown.js'])vm.runInContext(fs.readFileSync(path.join(dir,name),'utf8'),box);
let checks=0;const eq=(a,b)=>{assert.deepStrictEqual(a,b);checks++};
const definitions=box.VigiaEngine.stages,ids=Array.from(definitions,s=>s.id),D=box.CASE_DATA;
const create=stages=>box.VigiaEngine.criarVigia(D.vigia,D.key,{stages});
function submit(e,id,valid=true){return id==='identity'?e.validarIdentidade(valid?'Bryan Almeida':'Carlos'):id==='access'?e.validarAcessos({fisico:valid?'Helena Duarte':'Marcelo',digital:'Marcelo Vieira'}):id==='chronology'?e.validarCronologia(valid?D.key.correct_order:[...D.key.correct_order].reverse()):e.validarProtocolo({identidade:'Bryan',credencial:'2847',horario:valid?'22:46':'22:47'})}
for(let mask=1;mask<16;mask++){
 const selected=ids.filter((id,i)=>mask&(1<<i)),e=create(selected),timer=box.VigiaCountdown.create();let previous=8;
 eq(e.estado().memory,8);eq(e.estado().protocolConfirmed,false);eq(e.estado().skippedStages.length,4-selected.length);
 for(const id of ids.filter(id=>!selected.includes(id)))eq(submit(e,id).ok,false);
 for(const id of selected){
  const current=definitions.find(stage=>selected.includes(stage.id)&&!e.estado()[stage.flag]);eq(current.id,id);
  const guide=e.orientar('qual é a próxima etapa?').text;
  if(!selected.includes('identity'))eq(/identidade foi confirmada/i.test(guide),false);
  if(!selected.includes('access'))eq(/acessos estão confirmados/i.test(guide),false);
  if(!selected.includes('chronology'))eq(/sequência foi validada/i.test(guide),false);
  const locked=selected[selected.indexOf(id)+1];if(locked)eq(submit(e,locked).ok,false);
  eq(submit(e,id,false).ok,false);eq(e.estado().protocolConfirmed,false);
  const result=submit(e,id);eq(result.ok,true);
  const state=e.estado();eq(state.memory>=previous,true);previous=state.memory;
  eq(e.perfilIA().memory,state.memory);eq(e.orientar('qual é a próxima etapa?').memory,state.memory);
  if(id!=='protocol'){eq(timer.award(id,0).added,15);eq(timer.award(id,1),null)}
  eq(state.protocolConfirmed,id===selected.at(-1));
  if(id===selected.at(-1))eq(result.protocol,'BA17-2847-2246');
 }
 eq(timer.totalBonus(),selected.filter(id=>id!=='protocol').length*15);eq(e.estado().memory,100);
 e.reiniciar();eq(e.estado().memory,8);eq(e.estado().protocolConfirmed,false);eq(JSON.stringify(e.estado().enabledStages),JSON.stringify(selected));
 for(const id of ids.filter(id=>!selected.includes(id)))eq(submit(e,id).ok,false);
 e.configurarEtapas(['protocol']);eq(e.estado().chronologyOrdered,true);eq(e.estado().memory,8);eq(submit(e,'protocol').ok,true);
}
assert.throws(()=>create([]),/Selecione/);checks++;assert.throws(()=>create(['invalid']),/Selecione/);checks++;
const onlyConclusions=create(['protocol']);const files=D.evidence.filter(e=>e.stage===0||e.stage===1&&onlyConclusions.estado().identityConfirmed||e.stage===2&&onlyConclusions.estado().accessesConfirmed||e.stage===3&&onlyConclusions.estado().chronologyOrdered);eq(files.length,25);
const report={date:'2026-11-19',result:'passed',checks,combinations:15,coverage:['Todas as combinações não vazias das quatro etapas','Sequência de pré-requisitos sem bloqueios','Respostas erradas e etapas excluídas rejeitadas','Bônus apenas de etapas selecionadas','Memória proporcional e coerente na VIG.IA','Geração da mesma chave ao concluir a última etapa','Reinício preserva seleção e limpa progresso','Todos os documentos disponíveis no modo somente conclusões']};fs.writeFileSync(path.join(root,'tmp/vigia_os_impl/etapas.json'),JSON.stringify(report,null,2));console.log(JSON.stringify(report));
