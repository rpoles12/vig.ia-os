(()=>{// Adaptador de conteúdo para integração futura. Sem rede, voz ou interface.
const normalizar = value => String(value ?? '').normalize('NFD').replace(/[\u0300-\u036f]/g,'').toLowerCase().replace(/[^a-z0-9]/g,'');
const stages=Object.freeze([{id:'identity',flag:'identityConfirmed',label:'Identidade',description:'Descobrir o nome ou a assinatura do invasor.',icon:'user'},{id:'access',flag:'accessesConfirmed',label:'Acessos',description:'Relacionar os acessos físico e digital.',icon:'key'},{id:'chronology',flag:'chronologyOrdered',label:'Cronologia',description:'Organizar os seis eventos do incidente.',icon:'timeline'},{id:'protocol',flag:'protocolConfirmed',label:'Conclusões finais',description:'Responder identidade, credencial e horário.',icon:'shield'}].map(Object.freeze));
function selectedStages(ids=stages.map(stage=>stage.id)){if(!Array.isArray(ids)||!ids.length||ids.some(id=>!stages.some(stage=>stage.id===id)))throw new RangeError('Selecione pelo menos uma etapa válida.');return stages.filter(stage=>ids.includes(stage.id)).map(stage=>stage.id)}
function memoryFor(state){if(state.protocolConfirmed)return 100;if(state.skippedStages?.length){const selected=stages.filter(stage=>state.enabledStages.includes(stage.id));return Math.round(8+92*selected.filter(stage=>state[stage.flag]).length/selected.length)}return state.accessesConfirmed?67:state.identityConfirmed?34:8}

function criarVigia(config, gabarito,options={}) {
  let selected=selectedStages(options.stages),state;
  function advance(){for(const stage of stages){if(state[stage.flag])continue;if(selected.includes(stage.id))break;state[stage.flag]=true}}
  function reset(){state={identityConfirmed:false,accessesConfirmed:false,chronologyOrdered:false,fragment03Consulted:false,protocolConfirmed:false,evidenceSeen:[],wrongAttempts:{},sentAlerts:[],enabledStages:[...selected],skippedStages:stages.filter(stage=>!selected.includes(stage.id)).map(stage=>stage.id)};advance()}
  reset();
  const memory=()=>memoryFor(state);
  function success(result){advance();return {...result,memory:memory(),...(state.protocolConfirmed?{protocol:gabarito.answers.generated_protocol}:{} )}}
  const identityOk=value=>gabarito.answers.identity.some(v=>normalizar(v)===normalizar(value));
  const fail=(message,field,fields=[])=>{
    if(field)state.wrongAttempts[field]=(state.wrongAttempts[field]||0)+1;
    return {ok:false,message,fields,offerHint:!!field&&state.wrongAttempts[field]>=2};
  };
  return {
    estado:()=>({...JSON.parse(JSON.stringify(state)),memory:memory()}),
    reiniciar(){reset();return this.estado();},
    configurarEtapas(ids){selected=selectedStages(ids);reset();return this.estado();},
    marcarEvidencia(id){if(!state.evidenceSeen.includes(id))state.evidenceSeen.push(id);},
    perfilIA(){return VigiaAssistant.profile(state);},
    orientar(query,context={}){
      const reply=VigiaAssistant.respond(query,state,context);
      if(state.skippedStages.length){
        reply.actions=reply.actions.map(action=>['solve','timeline'].includes(action.tab)?{tab:'solve',label:'Abrir etapa atual'}:action);
        if(['identidade','bryan'].includes(reply.intent)&&state.skippedStages.includes('identity'))reply.text='A identificação não é uma etapa separada nesta rodada. Para interpretar o perfil, compare o Log L1 com o arquivo estudantil A-17. '+this.perfilIA().next;
        if(reply.intent==='inicio')reply.text+=' As etapas desmarcadas pela equipe não são exigidas nesta rodada.';
        if(reply.intent==='codigo'&&state.skippedStages.includes('protocol')){reply.title='A chave aparece ao concluir as etapas selecionadas';reply.text='Concluam as etapas desta rodada em Registros. Depois da última resposta correta, a chave aparecerá por 30 segundos para anotação no papel; usem a anotação para abrir a recapitulação. A chave não é reapresentada pela IA.'}
      }
      return reply;
    },
    consultar(query){
      if(window.VigiaAssistant)return this.orientar(query).text;
      const q=normalizar(query);
      const intent=[...config.intents].sort((a,b)=>(b.priority||0)-(a.priority||0)).find(i=>q&&i.aliases.some(a=>q.includes(normalizar(a))));
      if(!intent)return config.fallback;
      if(intent.requires&&!state[intent.requires])return intent.locked;
      const reply=state.protocolConfirmed&&intent.final_text?intent.final_text:state.identityConfirmed&&intent.after_identity?intent.after_identity:intent.text;
      return reply.replace('{memory}',String(memory()).padStart(2,'0'));
    },
    validarIdentidade(value){
      if(!selected.includes('identity'))return fail('A identificação não faz parte desta rodada.');
      if(!identityOk(value))return fail('Identidade incompatível com o perfil legado. Compare o Log L1 com o arquivo estudantil.','identidade',[{field:'nome',message:'Identidade não confirmada. Compare o Log L1 com o arquivo estudantil.'}]);
      state.identityConfirmed=true;return success({ok:true,message:'IDENTIDADE CONFIRMADA',unlock:'audio02'});
    },
    validarAcessos({fisico,digital}){
      if(!selected.includes('access'))return fail('A correlação de acessos não faz parte desta rodada.');
      if(!state.identityConfirmed)return fail('Confirme primeiro a identidade do perfil legado.');
      const physical=['helena','helenaduarte'].includes(normalizar(fisico));
      const logical=['marcelo','marcelovieira'].includes(normalizar(digital));
      if(!physical||!logical){const fields=[];if(!physical)fields.push({field:'fisico',message:'Acesso físico não confirmado. Revise a credencial e os registros da catraca.'});if(!logical)fields.push({field:'digital',message:'Acesso digital não confirmado. Revise as mensagens e a auditoria da conta.'});return fail('CORRELAÇÃO INCONSISTENTE · Revise '+fields.map(f=>f.field==='fisico'?'o acesso físico':'o acesso digital').join(' e ')+'.','acessos',fields)}
      state.accessesConfirmed=true;return success({ok:true,message:'ACESSOS CONFIRMADOS',unlock:'cronologia'});
    },
    validarCronologia(ids){
      if(!selected.includes('chronology'))return fail('A cronologia não faz parte desta rodada.');
      if(!state.accessesConfirmed)return fail('Associe primeiro os acessos físico e digital.');
      if(!Array.isArray(ids)||ids.length!==6||new Set(ids).size!==6||!ids.every((id,i)=>id===gabarito.correct_order[i]))return fail('Sequência inconsistente. Compare os horários e a interrupção da câmera.','cronologia');
      state.chronologyOrdered=true;return success({ok:true,message:'SEQUÊNCIA CONFIRMADA',unlock:['audio03','transcricao03','CAM01']});
    },
    consultarFragmento03(){
      if(!state.chronologyOrdered)return fail('Fragmento 03 bloqueado. Reconstrua a sequência.');
      state.fragment03Consulted=true;return {ok:true,unlock:'protocolo',message:'Consulte o minuto anunciado e o último registro da câmera.'};
    },
    validarProtocolo({identidade,credencial,horario}){
      if(!selected.includes('protocol'))return fail('As conclusões finais não fazem parte desta rodada.');
      if(!state.chronologyOrdered)return fail('Valide a sequência dos registros antes de gerar o código.');
      const fields=[];
      if(!identityOk(identidade))fields.push({field:'identidade',message:'Identidade não confirmada. Revise o arquivo estudantil.'});
      if(normalizar(credencial)!=='2847')fields.push({field:'credencial',message:'Credencial não confirmada. Compare o crachá com a catraca.'});
      if(normalizar(horario)!=='2246')fields.push({field:'horario',message:normalizar(horario)==='2247'?'22:47 é o fim da cópia. Abra o Extrato de ocorrências e procure a linha do confronto na sala técnica.':'Abra o Extrato de ocorrências: procure o confronto na sala técnica e informe apenas o minuto (HH:MM).'});
      if(fields.length)return fail('PROTOCOLO INCONSISTENTE · Revise '+fields.map(f=>({identidade:'a identidade',credencial:'a credencial',horario:'o horário'})[f.field]).join(', ')+'.','protocolo',fields);
      state.protocolConfirmed=true;return {ok:true,message:'PROTOCOLO CONFIRMADO',protocol:gabarito.answers.generated_protocol,memory:memory(),unlock:'reconstituicao_final'};
    },
    dica(stage,level=1){
      const hint=config.hints[stage];
      if(!hint)return config.fallback;
      if(hint.requires&&!state[hint.requires])return 'Conclua a etapa anterior antes de consultar esta dica.';
      if(hint.stop_when&&state[hint.stop_when])return 'Esta etapa já foi confirmada.';
      return hint.levels[Math.max(0,Math.min(2,Number(level)-1||0))];
    },
    avisosPorTempo(seconds){
      const alerts=config.timed_hints.filter(h=>seconds>=h.at_seconds&&!state.sentAlerts.includes(h.id)&&!state[h.unless]&&(!h.requires||state[h.requires]));
      state.sentAlerts.push(...alerts.map(h=>h.id));
      return alerts.map(({audience,text,id})=>({audience,text,id}));
    }
  };
}

window.VigiaEngine={criarVigia,normalizar,stages,memoryFor};})();
