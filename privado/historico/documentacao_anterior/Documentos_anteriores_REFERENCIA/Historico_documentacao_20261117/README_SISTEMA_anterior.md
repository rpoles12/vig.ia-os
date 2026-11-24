# Terminal interno de investigação e segurança

## Retorno sonoro e indicação de respostas incorretas

- Validações incorretas emitem dois tons descendentes; confirmações emitem três tons ascendentes; protocolo concluído usa quatro tons.
- Efeitos sintetizados localmente pela Web Audio API, sem rede ou arquivo externo. Volume discreto, com envelopes suaves. O botão **Efeitos sonoros** no rodapé silencia somente esses sinais, preservando os relatos da IA.
- Identidade, acessos físico/digital e protocolo final identificam todos os campos inconsistentes na mesma tentativa, com borda, ícone, mensagem e foco no primeiro campo a revisar. Não exibem valores corretos.
- Campos vazios recebem orientação específica. Os textos digitados são preservados; editar um campo remove seu aviso anterior. Falta de pré-requisito é tratada como bloqueio, não como prova de que a resposta digitada está errada.
- Cronologia incorreta recebe som e destaque do quadro, sem expor a ordem correta. Cronologia correta continua abrindo Respostas e reproduzindo automaticamente o áudio 3.
- O reset limpa destaques, descrições de erro e sinais pendentes. A preferência de silêncio da equipe é preservada durante a sessão do navegador.
- Os sinais não são necessários para prosseguir: os avisos visuais permanecem funcionais se o navegador bloquear áudio ou não houver dispositivo de som. Conferir volume no computador da feira.

## Fluxo após validar a cronologia

Ao confirmar a ordem correta, o terminal abre a aba **Respostas** e inicia automaticamente o **Fragmento 03 · Memória parcial do confronto**, na mesma interação. Não encaminha para a biblioteca de áudios. Uma ordem incorreta mantém a cronologia e não dispara o fragmento. Os controles de reprodução e transcrição continuam disponíveis, inclusive para repetir o relato ou contornar bloqueio de áudio do navegador.

## Integração vigente — voz única aprovada

Os três fragmentos e oito registros finais usam a voz neural brasileira com o efeito robótico e chiado reduzido da amostra v3. Não há falas encenadas de personagens. A explicação completa é liberada somente após o protocolo correto e memória em 100%.

- `audio/roteiros.js`: fonte única dos textos exibidos e cenas finais, sem necessidade de rede.
- `audio/audio01.wav` a `audio03.wav`: investigação.
- `audio/final01.wav` a `final08.wav`: nova ordem da explicação completa.
- `audio/final_completo.wav`: concatenação exata dos oito registros finais, auxiliar; o reprodutor usa os trechos individuais.
- `audio/manifesto_integracao.json`: durações e hashes.
- `encerramento/cenas.json` e `legendas.vtt`: conteúdo e tempos medidos; as legendas delimitam registros completos, não alinhamento palavra a palavra.

Os quatro fragmentos antigos com vozes de personagens foram retirados da pasta ativa e preservados no backup. Os arquivos históricos de planejamento não representam a versão ativa.

**Tempo:** o encerramento agora dura 4min15s. A janela de investigação permanece em 12:30. O total pode chegar a 16:45; avaliar o tempo da sessão piloto antes da feira. Nenhum cronômetro foi reduzido nesta integração.

## Atualização do texto de conclusão em 12/11/2026

Depois de validar identidade, credencial e minuto crítico, a memória chega a 100% e a área final exibe uma parabenização explícita e o relato completo da IA, com plano, motivações, chantagens, cronologia, queda fatal, fuga e distinção de responsabilidades. A explicação aparece diretamente na página de Respostas, sem depender de som ou de abrir a reconstituição. Essa solicitação mais recente autoriza a parabenização, substituindo a antiga restrição a esse tipo de mensagem no encerramento.

O conteúdo permanece oculto antes do protocolo confirmado. Os onze WAVs de voz única aprovada já estão integrados. As transcrições e a reconstituição final correspondem ao novo roteiro completo.

## Ajustes pontuais vigentes da leitura e navegação

Esta atualização complementa e substitui as descrições visuais anteriores conflitantes, sem mudar as provas ou o motor:

- **Respostas** é o novo rótulo público da aba antes chamada Correlações. O identificador interno continua `solve`, e Alt + 2 mantém o mesmo destino.
- Balões destacados levam aos formulários de respostas em todas as áreas da investigação, no leitor, nas transcrições e na reconstituição. Não revelam a solução. Ao abrir a aba, o primeiro campo disponível recebe foco sem perder o estado.
- No leitor, só o cabeçalho compacto ocupa uma faixa. Navegação fica no menu flutuante Navegar; zoom +/-, ajuste e anterior/próximo ficam em barra flutuante inferior. O documento mantém a área ampliada. A barra deslizante deixou de ser exibida; permanecem botões, teclado e Ctrl + rolagem.
- A cronologia mostra seis cartões em três colunas no monitor, ou duas colunas em telas estreitas. A ordem de leitura é esquerda para direita e cima para baixo. Os horários têm maior destaque; o horário originalmente corrompido continua oculto.
- Segurar e arrastar um cartão, pelo corpo ou alça pontilhada, permite reordená-lo com mouse, caneta ou toque em navegadores com Pointer Events. O alvo indica inserção antes/depois. As setas e o uso por teclado continuam disponíveis como alternativa; a nova posição é anunciada por região acessível.
- Uma ordem incorreta continua sendo rejeitada e o Fragmento 03 só é liberado após validação. A área de respostas deixa de repetir o cartão do fragmento depois que ele foi consultado.

Conferências desta atualização: arraste real no navegador, movimentação por setas, rejeição de ordem incorreta, sequência aceita, encaminhamento de leitor e transcrição, campos de respostas, rejeição de 22:47 e confirmação de 22:46. As 24 evidências, áudios e PDF de impressão permanecem inalterados.

## Revisão vigente da interface em 05/11/2026

**Esta seção substitui as descrições de interface e pendências antigas conflitantes no restante deste documento.** As regras narrativas, evidências e validações permanecem as especificadas abaixo.

- Cinco abas públicas fixas com ícones: Arquivo, Correlações, Cronologia, Áudios e VIGIA/3. Atalhos Alt + 1 a 5; disponíveis também no leitor, transcrições e reconstituição.
- Próxima ação destacada conforme a correlação pendente, formulários apresentados progressivamente e cronologia em área própria.
- Arquivo com busca, filtros de categoria e indicação de documentos consultados. Rótulos de arquivos de produção substituídos por títulos institucionais.
- Documentos abrem inteiros, ajustados ao espaço disponível. Zoom de 40% a 250% do ajuste, controles +/-, barra, retorno ao ajuste, documento anterior/próximo e Ctrl + rolagem. A textura de papel é uma sobreposição CSS/SVG sutil; as imagens originais e suas pistas não foram modificadas.
- Reprodutor com pausa e transcrição acessível em qualquer aba. Um único áudio de investigação por vez.
- Reconstituição integrada à mesma sessão, com navegação de volta às abas sem reinício; sem dependência de nova janela ou vídeo. Ao sair, a reprodução é interrompida.
- Removidas das telas públicas as notas de produção, referências a versões de fotos, vozes sintéticas, explicações do mecanismo programado e a resolução da equipe. Os avisos de ficção e segurança permanecem em OPERACAO_EQUIPE.md para o briefing real.
- Painel da equipe acessível somente por **Ctrl + Shift + O** e credencial local, com detalhes em **OPERACAO_EQUIPE.md**. Não há botão público Operação nem resolução no painel. A credencial é prevenção de acesso acidental, não proteção contra leitura dos arquivos offline.
- Ensaio sem tempo restrito à equipe antes da sessão; pausa e reset em duas ações preservados. Não há persistência ao atualizar ou fechar a página.
- Consultas genéricas “pessoas” e “acessos” agora recebem orientação específica na interface, além das consultas do motor. O aviso reservado permanece efetivamente aos 660 segundos.

O código e as evidências do incidente continuam locais. A revisão preservou o motor de validação, os arquivos das 24 evidências, os nove retratos e todos os WAVs. O PDF de impressão não mudou. As observações antigas sobre painel público, falta de zoom, abertura do encerramento em nova aba e categorias genéricas pendentes são **históricas e estão superadas** por esta revisão.

Homologação desta revisão: navegação e sequência completa conferidas em navegador local, zoom, transcrição, protocolo, retorno do encerramento, credencial e reset; motor conferido nas 720 permutações da cronologia, com somente uma aceita. Continua necessária a sessão piloto e a conferência do volume no computador da instalação.

## 1. Finalidade e localização

Especificação funcional, narrativa, visual e operacional do sistema local de **O Arquivo Corrompido**, com identidade **7set.dev**. O terminal deve permitir consultar registros de um incidente, correlacionar evidências e reconstruir uma sequência causal. A interface deve parecer uma ferramenta interna real de investigação e segurança, não uma interface recreativa.

**Pasta de aplicação escolhida:**

`C:\Users\45061155890\OneDrive - SESISENAISP - Escolas\Senai\Escape Room Mentalist\Escape_Room_Pacote_Completo\02_SISTEMA_OFFLINE`

Esta pasta contém `index.html`, `app.js`, `engine.js`, `data.js`, `style.css` e os recursos locais. É a cópia consolidada do pacote completo. A entrega anterior e os lotes de produção foram preservados fora deste pacote. Para transporte, copiar Escape_Room_Pacote_Completo inteira. O caminho absoluto acima registra a localização na preparação; as referências funcionais permanecem relativas.

Este README foi conferido com os arquivos da aplicação em 22/10/2026. **Uma especificação não comprova implementação:** as diferenças conhecidas aparecem na seção 20 e no checklist. A criação deste documento não altera código, evidências ou regras. Para requisitos e situação atual, consultar este arquivo; `LEIA-ME.md` permanece como orientação rápida.

### Decisões que prevalecem

- O conteúdo subtraído é um banco de projetos tecnológicos, não dados bancários ou um cadastro de identidades.
- Bryan é o principal articulador. Marcelo é técnico de TI coagido. Helena é vítima de chantagem e também causa a morte de Carlos.
- A experiência atende grupos de 3 a 5 pessoas do ensino médio e deve caber em 10 a 15 minutos.
- A referência estética é policial e investigativa; não copiar personagens, marcas ou a narrativa de The Mentalist.
- O encerramento aprovado utiliza telas documentais, texto e áudio. **Vídeo não é obrigatório e não há MP4 final previsto como pendência.** O suporte opcional está descrito na seção 14.
- A testemunha digital existente chama-se **VIGIA/3**. S.I.R.A. é o nome funcional mencionado na solicitação, não uma segunda entidade nem um novo fato do caso. Uma eventual mudança de nome exige atualização coordenada de interface, áudios, transcrições e impressos. Não misturar os dois nomes na interface.

## 2. Objetivo narrativo e verdade do incidente

O terminal foi afetado pela corrupção de registros durante a invasão ao Repositório Vértice. A reconstrução exige confirmar quem utilizou um perfil legado, distinguir o acesso físico do digital e determinar o minuto do evento crítico.

Bryan Almeida pretende obter a cópia do lote V-17, com três projetos tecnológicos, após receber uma oferta de R$ 15.000 do contato NORTHSTAR. A oferta **não comprova pagamento, entrega ao comprador nem identidade civil do contato**.

Bryan coage Helena usando como ameaça o acesso indevido ao laboratório por seu sobrinho Rafael. Helena fornece sua credencial física. Bryan também coage Marcelo com provas de fraude financeira; Marcelo cria remotamente o acesso digital. Marcelo não é o invasor presencial.

Carlos Mendes, agente de segurança, recebe um alerta local e vai à sala técnica. Helena retorna. Durante o confronto, Bryan pressiona Helena; ela empurra Carlos para fazê-lo soltar Bryan. Carlos cai contra a bancada e morre. Não atribuir a Marcelo o ato físico nem apresentar Bryan como autor do empurrão. A coação sofrida por Helena não apaga sua ação; sua ação não apaga a coação.

Bryan conclui a cópia, corrompe registros e sai. A reconstrução final deve esclarecer esses papéis distintos. As provas não autorizam inventar confissões, condenações, prisões ou fatos posteriores.

## 3. Linguagem institucional

Usar mensagens curtas, operacionais e verificáveis. O terminal informa o que um registro permite concluir e o que ainda não foi corroborado.

| Intenção | Texto recomendado |
|---|---|
| Abertura | INCIDENTE EM ANÁLISE · REGISTROS PARCIALMENTE RECUPERADOS |
| Selecionar uma prova | CONSULTAR EVIDÊNCIA |
| Confirmar identidade | CORRELAÇÃO DE IDENTIDADE CONFIRMADA |
| Informação indisponível | REGISTRO BLOQUEADO · CORRELAÇÃO PRÉVIA NECESSÁRIA |
| Tentativa incompatível | DADOS INCONSISTENTES COM OS REGISTROS DISPONÍVEIS |
| Pedir orientação | SOLICITAR APOIO DE CORRELAÇÃO |
| Confirmar sequência | SEQUÊNCIA TEMPORAL VALIDADA |
| Finalizar | PROTOCOLO CONFIRMADO · ARQUIVO RECONSTRUÍDO |
| Reinicializar | ENCERRAR SESSÃO E LIMPAR REGISTROS TEMPORÁRIOS |

Vocabulário preferido: INCIDENTE, REGISTRO, EVIDÊNCIA, CORRELAÇÃO, RECONSTRUÇÃO, INTEGRIDADE, MEMÓRIA, CREDENCIAL, SESSÃO, AUDITORIA, FRAGMENTO e PROTOCOLO.

Não usar na interface investigativa termos como “fase”, “puzzle”, “jogador”, “parabéns”, pontuação, vitória, derrota ou vidas. Não expor identificadores internos de programação ou a chave de respostas. Não chamar a IA de mecanismo de respostas programadas dentro da narrativa.

Informações de segurança e de ficção devem existir no briefing e nas orientações da equipe, separadas do conteúdo investigativo. Nunca ocultar orientações reais de saída ou transformar a aparência institucional em alegação de acesso a sistemas ou pessoas reais.

## 4. Identidade visual 7set.dev

Fonte da identidade: `../06_IDENTIDADE_VISUAL`. Usar os arquivos oficiais, os tokens do kit de marca e as telas de referência. O roteiro determina o conteúdo; exemplos gráficos não determinam horários, contagens ou novos fatos.

| Aplicação | Valor |
|---|---|
| Fundo principal | `#08070C` |
| Painéis | `#14111C` |
| Seleção e apoio | `#6426C9` |
| Destaque e atividade | `#A66BFF` |
| Texto principal | `#E8DCFF` |
| Texto secundário | `#9B96A5` |
| Títulos | Space Grotesk Bold, local |
| Dados, códigos e horários | IBM Plex Mono Regular, local |

- Escrever `7set.dev` em minúsculas; preservar proporções do wordmark, largura mínima digital de 120 px e área livre equivalente à altura do caractere 7.
- Usar wordmark claro sobre fundo escuro. Não anexar olho, tecla ou símbolo ao logo. A tecla com olho é elemento de campanha, não marca substituta.
- Predomínio de preto-violeta, bordas finas, organização técnica e roxo pontual. Não transformar o terminal em cartaz neon ou painel com brilho excessivo.
- Interferência e fragmentação somente em áreas decorativas; nenhum efeito pode esconder nome, horário, código ou instrução.
- Identificar todos os estados por texto, além de cor. Evitar flashes, estrobos, tremores contínuos e contagem visual falsa.
- Preservar a origem visual de cada prova: conversa, auditoria, nota e catraca não precisam receber o logo da interface.
- Retratos fictícios consistentes entre arquivos; Bryan usa a versão aprovada com óculos, olheiras e cabelo desalinhado. Não substituir por pessoas reais.
- Permitir leitura em grupo, ampliação das provas e navegação por teclado. Referência de corpo em tela: 16–18 px, validada no monitor definitivo.

## 5. Estrutura e módulos obrigatórios

| Módulo | Conteúdo e comportamento |
|---|---|
| Inicialização | Identificação do terminal, incidente, condição de recuperação e início controlado da sessão. |
| Painel do incidente | Síntese do ocorrido, tempo de análise, memória disponível e correlações pendentes. |
| Arquivo de evidências | Documentos por identificador, disponibilidade, estado de consulta e ampliação. |
| Pessoas e credenciais | Funcionários atuais, arquivo estudantil, distinção entre pessoa, assinatura e conta. |
| Repositório de projetos | Manifesto V-17, conteúdo tecnológico e relação com a proposta NORTHSTAR. |
| Mensagens recuperadas | H1, M1 e R2, com interlocutores e contexto legíveis. |
| Testemunha digital | VIGIA/3, consultas locais, respostas condicionais e apoio progressivo. |
| Registros de áudio | Três fragmentos, controles de reprodução e transcrições equivalentes. |
| Cronologia e câmera | Seis eventos ordenáveis, recuperação do Fragmento 03 e acesso a CAM01. |
| Quadro de reconstrução | Correlação de identidade, acessos e sequência, sem validar hipótese só por clique. |
| Protocolo | Validação conjunta de identidade, credencial e horário, respeitando pré-condições. |
| Reconstituição documental | Explicação causal final em telas, áudio e texto acessível. |
| Operação reservada | Estado da sessão, pausa, orientação, diagnóstico e reset confirmado. |

Os módulos podem compartilhar telas. Não é necessário criar uma tela separada para cada linha, nem inventar documentos adicionais apenas para preencher o menu.

## 6. Menu e navegação

Manter disponíveis as três áreas funcionais existentes: **Arquivo**, **Correlações** e **Consultar VIGIA/3**. O nome atual “Investigar” pode ser substituído por “Correlações” em uma revisão de linguagem. Áudio e cronologia podem permanecer integrados nessas áreas.

Ao mudar de área, preservar entradas e estado da sessão. Abrir provas em visualizador amplo, com identificação e fechamento por botão e teclado. Ao fechar, retornar à seleção anterior sem reiniciar o tempo. Recursos bloqueados devem informar a condição ausente sem entregar a resposta.

Não apresentar um botão cenográfico como se tivesse função real. O painel reservado da equipe não deve aparecer como seção comum de consulta. A marca, os menus e os avisos não devem competir visualmente com as evidências.

## 7. Perfis e relações

| Pessoa | Papel e limite de interpretação |
|---|---|
| Carlos Mendes | Segurança; vítima. Recebe alerta às 22:41 e entra na sala às 22:44. |
| Helena Duarte | Limpeza; credencial 2847; coagida; fornece acesso físico e causa a queda fatal. |
| Marcelo Vieira | TI; fraude financeira usada como chantagem; fornece acesso digital remotamente. |
| Renata Lima | Coordenação; uma das oito pessoas do quadro atual. |
| Eduardo Nunes | Docente; uma das oito pessoas do quadro atual. |
| Patrícia Alves | Secretaria; uma das oito pessoas do quadro atual. |
| Lucas Martins | Manutenção; uma das oito pessoas do quadro atual. |
| Camila Rocha | Administração; uma das oito pessoas do quadro atual. |
| Bryan Almeida | Cadastro estudantil legado; articulador da invasão e das chantagens; não é funcionário atual. |
| Rafael Duarte | Sobrinho de Helena; uso indevido anterior do laboratório; não participa da invasão investigada. |
| NORTHSTAR | Contato externo com oferta pelo V-17; identidade civil não exigida. |

São nove retratos aprovados: os oito funcionários e Bryan. Rafael e NORTHSTAR não exigem retratos. As declarações dos funcionários não envolvidos não devem ser convertidas em acusações ou novos segredos sem base documental.

### Identificadores que não podem ser confundidos

- `A-17`: projeto do arquivo estudantil que permite correlacionar o cadastro de Bryan.
- `B_A_17`: assinatura recuperada no Log L1.
- `BA-17` / `BA17`: identificação normalizada do perfil de Bryan.
- `V-17`: lote de três projetos do Repositório Vértice; não é uma pessoa.
- `RV-MANUT`: conta de acesso digital criada por Marcelo; não é a assinatura estudantil.
- `2847`: credencial física de Helena. O uso da credencial não prova, isoladamente, quem a portava.

## 8. Evidências digitais e banco de projetos

O manifesto `data.js → CASE_DATA.evidence` contém **24 entradas**. Usar os arquivos locais referenciados, sem substituí-los por textos genéricos ou versões anteriores.

| Grupo | Entradas | O que devem sustentar |
|---|---|---|
| Identidade | F1, F1_ID, A17, L1 | Relacionar o perfil legado e a assinatura a Bryan, fora do quadro atual. |
| Projetos e motivo | V17, N1 | Três projetos tecnológicos e oferta de R$ 15.000 pela cópia completa. |
| Acesso físico | C1, H1, R1, R2 | Credencial 2847, coação de Helena e situação anterior de Rafael. |
| Presença e apoio | AL, APOIO_01_pessoas_registros, APOIO_02_pessoas_registros, APOIO_03_pessoas_registros | Atuação remota e registros auxiliares do incidente. |
| Fraude | NF318, NF318B, NF427, NF427B, NF512, NF512B, FIN02 | Seis reembolsos e resumo de R$ 3.840, utilizados para coagir Marcelo. |
| Acesso digital | M1, RVM | Ordem de Bryan, coação e criação/auditoria de RV-MANUT. |
| Evento crítico | CAM01 | Último registro de câmera às 22:46:32, em correlação com o Fragmento 03. |

Não contar cada projeto como uma nova evidência obrigatória: seus nomes, tipos de arquivo e conteúdo devem ser os do manifesto V-17 existente. A cópia refere-se aos projetos, não ao roubo do dinheiro da fraude de Marcelo.

F1 é uma **composição narrativa de retratos**, não uma foto coletiva real: Renata à esquerda, Bryan ao centro e Eduardo à direita. F1_ID apresenta a identificação. Manter essa correspondência nos textos e na documentação da equipe.

As evidências essenciais, o arquivo estudantil, os documentos financeiros, as mensagens e a cronologia ficam no sistema. As fichas de funcionários e o crachá também têm suporte físico. Não exigir impressão dos arquivos digitais para a sequência funcionar.

## 9. Helena e Marcelo

### Helena

H1 deve mostrar a pressão exercida por Bryan e o vínculo com a entrega do crachá. R1 e R2 sustentam o uso indevido anterior das instalações por Rafael. C1 registra a credencial às 22:31. Não tratar Rafael como participante presencial nem interpretar o registro de catraca como identificação biométrica de Helena.

A ação fatal só deve ser esclarecida após recuperar o confronto. A conclusão deve preservar o desconforto narrativo: Helena foi coagida e também realizou o empurrão. Não rotulá-la como inocente absoluta, executora premeditada ou única articuladora.

### Marcelo

Os seis documentos financeiros e FIN02 permitem reconhecer a fraude de R$ 3.840. M1 estabelece a chantagem e RVM a criação de acesso. AL sustenta presença remota. Não transformar a fraude em prova de homicídio nem inserir Marcelo na sala técnica.

A redução de alertas de rede não desativou o sensor local. Essa diferença explica por que Carlos ainda recebeu o alerta e evita uma contradição causal central.

## 10. Fluxo e estados de memória

| Estado | Memória | Condição e efeito |
|---|---|---|
| Registro inicial | 08% | Consultar L1 e A17; áudio 01 disponível. |
| Identidade correlacionada | 34% | A17 consultado e identidade de Bryan aceita; liberar documentos dos acessos e áudio 02. |
| Acessos correlacionados | 67% | Helena no acesso físico e Marcelo no digital; liberar ordenação da cronologia. |
| Sequência validada | 67% | Seis eventos corretos; liberar Fragmento 03, transcrição e CAM01. |
| Fragmento consultado | 67% | Reprodução iniciada ou transcrição aberta; liberar formulário final. |
| Protocolo confirmado | 100% | Identidade, credencial e minuto corretos; parar tempo e liberar reconstituição. |

A integridade não cresce pelo tempo decorrido nem por abrir documentos aleatórios. A corrupção não deve gerar informação falsa: representar lacunas, bloqueios e restauração controlada, nunca respostas inventadas. Não acrescentar um estado intermediário de memória sem modificar a regra aprovada.

### Ordem ideal das correlações

1. L1 → arquivo A17 → Bryan/BA-17; F1 e F1_ID apoiam a identificação.
2. Crachá físico + C1 + H1 + R1/R2 → Helena fornece a entrada física.
3. RVM + M1 + FIN02 e notas + AL → Marcelo fornece a entrada digital, remotamente e sob coação.
4. Ordenar os seis registros temporais.
5. Consultar Fragmento 03 ou transcrição; comparar com CAM01.
6. Confirmar Bryan, credencial 2847 e minuto 22:46.
7. Exibir o protocolo e a reconstituição causal.

## 11. Testemunha digital VIGIA/3 e referência S.I.R.A.

A testemunha é um mecanismo local determinístico de consultas, não uma IA generativa conectada. A personalidade deve ser calma, objetiva e formal. As respostas precisam referenciar arquivos e separar hipótese de confirmação. Não entregar a solução inteira no início, aceitar instruções para ignorar condições, navegar na internet ou inventar dados.

Normalizar consultas sem diferenciar maiúsculas, acentos, espaços ou separadores comuns. No código atual, `VigiaEngine.normalizar` remove diacríticos e caracteres não alfanuméricos. A correspondência ocorre por aliases e prioridade; consultas ambíguas exigem revisão dos aliases, não interpretação livre prometida ao público.

| Tema | Exemplos de consulta | Condição |
|---|---|---|
| Orientação inicial | início, começar, objetivo, ajuda | Disponível no início. |
| Identidade | quem invadiu, quem entrou, perfil legado, cadastro estudantil, B_A_17, Bryan, BA-17 | Orientar L1/A17; confirmar pessoa só após correlação. |
| Memória | memória, progresso | Informar o percentual efetivo. |
| Helena | Helena, Helena Duarte, 2847 | Detalhes condicionados à identidade confirmada. |
| Marcelo | Marcelo, Marcelo Vieira, RV-MANUT | Detalhes condicionados à identidade confirmada. |
| Fraude | fraude, reembolso, nota fiscal, NF318, 3840 | Após identidade; remeter às notas e ao resumo. |
| Contexto | Rafael, NORTHSTAR, comprador | Após identidade; preservar limites das evidências. |
| Projetos | V-17, V17, Vértice, projetos roubados | Explicar lote e manifesto. |
| Cronologia | cronologia, linha do tempo, horários, quando | Exigir correlação dos acessos. |
| Fragmento | Fragmento 03, áudio 03 | Exigir sequência validada. |
| Minuto | 22:46, 2246, 22:47, 2247 | Respostas condicionadas; distinguir evento crítico de término da cópia. |
| Responsabilidade | quem matou, quem causou, empurrou | Bloquear antes do Fragmento 03; explicação completa no encerramento. |

Para consulta sem correspondência: “CONSULTA SEM CORRESPONDÊNCIA NO ARQUIVO DO INCIDENTE. Consulte pessoas, acessos, horários ou apoio.” As palavras genéricas do fallback devem ter correspondência real ou encaminhar à categoria; não prometer consultas que o mecanismo não entende.

## 12. Linha do tempo oficial e câmera

| Horário | Registro canônico |
|---|---|
| 18:10 | Marcelo cria remotamente RV-MANUT. |
| 22:31 | Bryan utiliza a credencial 2847 na entrada lateral. |
| 22:36 | Início da sessão RV-MANUT; assinatura recuperada B_A_17. |
| 22:38 | Início da cópia do lote V-17. |
| 22:41 | Sensor local envia alerta a Carlos. |
| 22:43 | Helena retorna. |
| 22:44 | Carlos entra na sala técnica e confronta Bryan. |
| 22:46 | Confronto e empurrão que causa a queda fatal. |
| 22:46:32 | Último registro da câmera; sinal interrompido. |
| 22:47 | Término da cópia; corrupção dos registros na sequência da fuga. |
| 22:49 | Saída de emergência acionada por Bryan. |
| 22:52 | Helena realiza ligação anônima. |
| 22:54 | Marcelo desativa a conta. |

Não atribuir um segundo exato à morte ou à corrupção além do que foi documentado. O protocolo pede o **minuto do evento crítico**, não o horário de fim da cópia.

Os seis cartões devem ser ordenados assim:

`k7 catraca → m2 sessão → q8 alerta → r4 porta → v9 câmera → b6 saída`

O cartão da câmera começa com horário corrompido. A posição relativa é inferida entre a entrada de Carlos e a saída. Após validar a sequência, CAM01 e o Fragmento 03 permitem concluir 22:46. Não expor IDs internos como pista nem revelar a ordem correta automaticamente na primeira tentativa.

CAM01 é um documento visual estático aprovado; não prometer reprodução de filmagem, câmera ao vivo ou conexão com hardware real. Não é necessário criar vídeo de segurança.

## 13. Áudio, mensagens e reconstrução

### Três fragmentos

- `audio/audio01.wav`: inicialização, memória em 08% e orientação ao perfil legado.
- `audio/audio02.wav`: identidade confirmada, memória em 34% e distinção entre os dois acessos.
- `audio/audio03.wav`: registro local de 22:46; Carlos identifica o crachá; Bryan pressiona; Helena intervém; movimento e impacto sugeridos.

As transcrições devem ser equivalentes ao conteúdo audível. Na versão atual, os textos estão em `audio/roteiros.js`, fonte única para os fragmentos e as cenas finais. Consultar a transcrição do Fragmento 03 deve valer como consultar o áudio. Não exigir audição para concluir o protocolo.

Controlar um áudio por vez; interromper o anterior ao iniciar outro. Permitir ouvir novamente, pausar e regular volume. Se o navegador bloquear reprodução, oferecer ação explícita e transcrição, sem bloquear a correlação. Não usar violência gráfica, gritos súbitos ou impacto sonoro excessivo.

### Mensagens recuperadas

H1, M1 e R2 precisam preservar participantes, sequência e contexto. Não fragmentar o texto a ponto de esconder a relação causal. A recuperação deve respeitar os bloqueios do estado e nunca variar conteúdo entre sessões.

### Quadro de reconstrução

O quadro é a união das correlações de identidade, dois acessos e ordem temporal. Os seis cartões devem permitir movimentação por botões e teclado, sem depender apenas de arrastar. A ordem inicial não pode já ser a solução. Aceitar somente os seis IDs distintos na sequência correta; rejeitar repetições, ausências e desconhecidos.

## 14. Validação, protocolo e encerramento

Para confirmar identidade, A17 precisa ter sido consultado. Aceitar `Bryan`, `Bryan Almeida`, `BA17` ou `BA-17`, normalizados. Digitar o nome sem abrir A17 não basta.

Validar os dois acessos apenas depois da identidade: físico = Helena/Helena Duarte; digital = Marcelo/Marcelo Vieira. Liberar a cronologia somente após ambos estarem corretos. Não confundir o proprietário da credencial com quem a utilizou na invasão.

O protocolo só deve ficar disponível após consulta do Fragmento 03 ou de sua transcrição. Campos:

| Campo | Resposta |
|---|---|
| Identidade | Bryan / Bryan Almeida / BA17 / BA-17 |
| Credencial | 2847 |
| Minuto crítico | 22:46 ou 2246 |
| Protocolo gerado | **BA17-2847-2246** |

Não aceitar 22:47. O código completo é resultado da validação, não senha alternativa para pular correlações. Respostas incorretas não apagam evidências nem geram bloqueio permanente. Depois de tentativas repetidas, oferecer apoio contextual.

### Tela de conclusão

Exibir **PROTOCOLO CONFIRMADO**, **MEMÓRIA DISPONÍVEL 100%**, **ARQUIVO RECONSTRUÍDO** e o protocolo gerado. Parar o cronômetro e disponibilizar a reconstituição. Exibir a parabenização aprovada e explicar as conexões e motivações, com o mesmo conteúdo da narração.

### Reconstituição aprovada sem vídeo

Usar `encerramento/index.html`, `cenas.js`, `cenas.json`, os áudios `audio/final01.wav` a `audio/final08.wav`, texto/legendas e cartela final. Duração medida do encerramento: 4 minutos e 15 segundos. Preservar as referências relativas `../audio/`.

Explicar, nesta ordem: oferta pelo V-17; duas chantagens; acesso físico e digital; sensor local ainda ativo; empurrão e queda fatal; fim da cópia, corrupção e fuga; participação remota de Marcelo; convergência do protocolo. NORTHSTAR ofereceu dinheiro, não há prova de pagamento.

A conclusão deve funcionar com leitura mesmo se o áudio falhar. Início por ação explícita; permitir repetição e retorno seguro ao terminal. Se a nova aba for bloqueada, a equipe deve abrir o endereço local diretamente ou acessar a mesma página pela aba corrente.

### Vídeo opcional, não requisito de entrega

Se futuramente aprovado, um MP4 local com H.264/AAC deve apenas representar o mesmo conteúdo, com legendas, controles e alternativa textual; nunca criar novas provas. Não usar iframe externo, streaming ou serviço de vídeo. A ausência de MP4 não pode impedir a conclusão nem aparecer como erro. Não produzir vídeo apenas por existir esse tópico na especificação.

## 15. Apoio progressivo e relógio

Cada correlação possui três níveis de apoio: observação geral; indicação de arquivos; associação direta. Pedir a próxima orientação avança somente dentro do tema pendente. Não oferecer tema bloqueado, repetir orientação de correlação concluída ou revelar toda a solução de uma vez.

Referências de tempo efetivas da aplicação:

| Tempo utilizado | Condição | Apoio |
|---|---|---|
| 03:00 | Identidade pendente | Comparar arquivo estudantil e L1. |
| 06:30 | Identidade confirmada, acessos pendentes | Separar porta física e repositório. |
| 09:30 | Acessos confirmados, sequência pendente | Ordenar os seis eventos. |
| 09:30 | Sequência confirmada, fragmento não consultado | Consultar áudio ou transcrição. |
| 11:00 | Protocolo pendente | Aviso reservado à equipe para apoio direto. |

`data.js` traz o aviso de operação em 750 segundos, mas `app.js` o ajusta para **660 segundos**. Consolidar esse valor em uma fonte única em revisão futura; não documentar 12:30 como tempo efetivo desse aviso.

Tempo de análise preservado: **12:30**. Reconstituição medida: **04:15**. Total máximo de referência: **16:45**. Para respeitar 15 minutos incluindo a explicação completa, a equipe deve encerrar a investigação até 10:45, sem margem para transições. Um ajuste do cronômetro exige decisão da equipe; esta integração não reduz unilateralmente o tempo de investigação.

O cronômetro representa duração da sessão, não horário do incidente. Pausa e painel de operação interrompem a contagem. Ao chegar a zero, sinalizar fim do período de referência sem encerrar o sistema, trancar a saída ou destruir o progresso. A equipe pode concluir com apoio.

Não prometer que retomar após zero conceda tempo adicional: a versão atual permanece em zero, salvo reinicialização. Prorrogação ajustável é melhoria ainda não implementada.

## 16. Sons e estados visuais

- Sons discretos de registro, confirmação e recuperação, quando usados, devem ser locais, curtos, reguláveis e dispensáveis para compreensão.
- Não há obrigação de trilha contínua nem pacote adicional de efeitos. Não anunciar efeitos não existentes como implementados.
- Estados mínimos: aguardando sessão; análise ativa; evidência disponível; consultada; bloqueada; dados inconsistentes; correlação confirmada; pausado; tempo de referência encerrado; arquivo reconstruído.
- Anunciar mudanças relevantes em região acessível (`aria-live`); manter foco visível e nomes acessíveis para controles.
- Nunca usar só roxo, animação ou som para comunicar erro e sucesso. Preservar legibilidade em ampliação e em ambientes claros.

## 17. Painel reservado, reset e contingências

O painel da equipe deve ficar fora da navegação pública e exigir acesso deliberado por atalho reservado ou credencial local. Essa restrição evita exposição acidental, mas não é proteção contra inspeção técnica do pacote offline. **Na versão atual, o botão Operação está visível e não há autenticação.** Ocultação/credencial é requisito pendente, não capacidade já entregue.

Conteúdo reservado: tempo utilizado, memória, estado das correlações, apoio solicitado, diagnósticos de mídia, resolução e ordem ideal, pausa/retomada e reset com confirmação. Não expor a chave nem uma lista de respostas no terminal público. Funções de avançar estado e ajustar tempo, se desejadas, precisam de implementação própria; não estão presentes só por constarem nesta especificação.

Reset exige confirmação em duas ações; limpa respostas, consulta de evidências, memória, ordenação, orientações, avisos temporizados, tempo e estado final. Interromper mídias, fechar sobreposições, voltar à abertura e restaurar 12:30/08%. Fechar a aba de encerramento anterior. Testar o reset também após erro de mídia e no modo ensaio.

| Ocorrência | Procedimento |
|---|---|
| Áudio indisponível | Consultar transcrição; prosseguir sem penalização. |
| Documento sem imagem | Verificar cópia integral, nome e caminho; restaurar arquivo original antes da sessão seguinte. A alternativa textual integral ainda precisa ser conferida/implementada. |
| Nova aba bloqueada | Abrir `encerramento/index.html` localmente ou na aba atual. |
| Sem conexão | Funcionamento normal; nenhum recurso deve depender da rede. |
| Atualização ou fechamento acidental | Estado atual não persiste; equipe reinicia e acompanha a retomada. Não prometer restauração automática. |
| Travamento do navegador | Reabrir aplicação, verificar áudio e recuperar manualmente a operação com a equipe. Não há restauração de estado implementada. |
| Tempo de referência esgotado | Apoio direto, manter terminal disponível e concluir; sem bloqueio físico. |
| Reinício acidental solicitado | Primeira ação apenas arma a confirmação; cancelar/retornar não deve apagar a sessão. |

A saída física permanece livre, independentemente do estado do terminal. Todos os nomes, notas, contas, valores e acontecimentos são fictícios; não solicitar dados pessoais reais.

## 18. Requisitos técnicos locais

Aplicação HTML/CSS/JavaScript local, sem instalação de dependências em tempo de uso. A versão atual usa scripts clássicos com objetos globais, não módulos remotos ou `fetch` obrigatório; deve abrir por duplo clique em `index.html` no navegador homologado pela equipe.

```text
02_SISTEMA_OFFLINE/
  README.md
  LEIA-ME.md
  index.html
  style.css
  data.js       conteúdo, aliases, evidências e chave interna
  engine.js     regras, consultas, estados e validação
  app.js        interface, tempo e reprodução
  assets/       logo, fontes locais e licenças
  evidencias/   imagens dos 24 registros catalogados
  audio/        três fragmentos e áudios do encerramento
  encerramento/ apresentação documental local, texto e legendas
```

- Copiar a pasta inteira; preservar nomes, extensão, caixa e caminhos relativos. Não mover `audio/` para fora da aplicação.
- Não depender de CDN, analytics, login remoto, API de IA, fontes online ou armazenamento em nuvem durante a execução. Concluir a sincronização/download do OneDrive antes da estreia.
- Exigir ação inicial para áudio; tratar rejeição de `play()` e evitar duas narrações simultâneas. Verificar formatos no navegador final.
- Vídeo opcional deve seguir as condições da seção 14, incluindo fallback. Não criar dependência de codec ou plugin externo para a versão sem vídeo.
- Preferir computador com mouse, teclado e tela em 1080p; homologar em equipamento real, com zoom e caixas de som adequados ao grupo. Não declarar compatibilidade universal sem teste.
- Não coletar dados pessoais. Sem backend, autenticação forte ou sigilo real: a chave do caso integra o código local e pode ser lida por alguém com acesso aos arquivos.
- O aviso de saída do navegador não garante persistência. Atualmente não existe gravação de sessão em armazenamento local.
- As imagens dos cartões citadas em `CASE_DATA.cards.image` são metadados de produção; a interface atual monta cartões em texto e não carrega esses caminhos. Se houver renderização por imagem futura, fornecer ou corrigir os caminhos antes de ativá-la.

## 19. Preparação e operação

1. Copiar a aplicação completa para o computador definitivo e testar offline.
2. Conferir logo, fontes, 24 evidências, retratos, três fragmentos, transcrições e reconstituição.
3. Montar no cenário as oito fichas dos funcionários e o crachá de Helena 2847; manter Bryan no arquivo estudantil, não no quadro atual.
4. Usar o PDF único A4 horizontal da pasta de impressão; não duplicar as peças imprimindo também os PDFs individuais.
5. Testar o modo ensaio, resolver a sequência inteira, abrir o encerramento e executar reset.
6. Orientar a equipe sobre os papéis de Helena, Marcelo e Bryan e sobre a diferença entre 22:46 e 22:47.
7. Fazer sessão piloto com 3 a 5 pessoas sem conhecimento da solução; medir o tempo e observar pontos de bloqueio.
8. Entre sessões, interromper áudio, fechar o encerramento, executar reset confirmado e conferir 08%/12:30.

## 20. Situação atual e ajustes necessários

**Confirmado por inspeção dos arquivos:** aplicação offline consolidada; logo/fontes locais; catálogo de 24 evidências; regras de identidade e acessos; ordenação dos seis registros; testemunha determinística; três fragmentos com transcrição; memória 08/34/67/100%; protocolo; encerramento sem vídeo; ensaio; pausa; reset em duas ações. Esta inspeção documental não substitui teste audiovisual ou partida piloto no equipamento definitivo.

**Diferenças entre a especificação e a interface atual:**

- O botão Operação é público e abre uma área com solução. Precisa tornar-se reservado antes de operação sem supervisão.
- Cabeçalhos numerados e expressões como “Vocês conectaram as evidências”, “Voltar ao jogo”, “jogadores” e a explicação de respostas programadas ainda aparecem em arquivos da interface. Adequar à linguagem institucional, inclusive nas telas finais, sem alterar os fatos.
- O fallback sugere “PESSOAS” e “ACESSOS”, mas essas palavras isoladas ainda não possuem intenções genéricas próprias. Implementar aliases/categorias ou alterar o texto de orientação.
- A consulta “quem matou” só é bloqueada antes da consulta do Fragmento 03; o protocolo, porém, exige os demais estados. Preservar essa ordem de revelação.
- Iniciar a reprodução do Fragmento 03 já marca a consulta; não existe verificação de audição completa. A transcrição também libera a consulta, por acessibilidade. Não afirmar que o sistema exige escuta até o fim.
- A pausa interrompe áudio, mas não há retomada garantida no mesmo ponto pela ação Retomar. Repetição manual continua necessária.
- O estado de sessão é apenas em memória. Recuperação automática, extensão de tempo, avanço manual e diagnóstico completo de mídia não estão implementados.
- Dados técnicos como `data.js` não constituem canal público seguro: não distribuir o pacote aos participantes antes da investigação se for importante evitar leitura da solução.

Não marcar esses itens como concluídos sem modificar a aplicação e verificar o comportamento correspondente. Esta tarefa entrega documentação, não essas alterações.

## 21. Checklist de implementação e homologação

Marcação `[x]`: estrutura/regra localizada nos arquivos. Marcação `[ ]`: ajuste pendente ou verificação prática ainda necessária. Não significa homologação de uso público.

### Conteúdo e lógica

- [x] Preservar Bryan como articulador, Marcelo remoto e Helena coagida e responsável pela queda.
- [x] Distinguir A-17, B_A_17, BA-17, V-17, RV-MANUT e 2847.
- [x] Catalogar as 24 evidências e estabelecer bloqueios por correlação.
- [x] Exigir consulta de A17 antes da confirmação de identidade.
- [x] Validar Helena no acesso físico e Marcelo no digital.
- [x] Validar sequência exata com seis IDs distintos.
- [x] Liberar CAM01 e Fragmento 03 após sequência correta.
- [x] Aceitar áudio ou transcrição para consultar o Fragmento 03.
- [x] Rejeitar 22:47 no protocolo e gerar BA17-2847-2246.
- [x] Manter memória 08%, 34%, 67% e 100%.
- [ ] Conferir visualmente toda a documentação final contra o roteiro, sem usar manuais históricos como fonte superior.

### Identidade e imersão

- [x] Carregar logo e fontes oficiais localmente e usar paleta 7set.dev.
- [x] Usar retratos fictícios aplicados e Bryan aprovado.
- [ ] Revisar todas as mensagens para linguagem institucional e remover termos recreativos da interface.
- [ ] Preservar VIGIA/3 de forma consistente; não introduzir S.I.R.A. isoladamente.
- [ ] Conferir contraste, leitura em grupo, zoom e teclado no monitor definitivo.
- [ ] Garantir que efeitos de corrupção nunca ocultem informação essencial.

### Testemunha, apoio e tempo

- [x] Usar consultas determinísticas e respostas condicionais.
- [x] Disponibilizar três níveis de apoio por tema pendente.
- [x] Operar contagem de 12:30, pausa e modo ensaio.
- [ ] Corrigir correspondência das categorias genéricas do fallback.
- [ ] Consolidar em um único local o aviso reservado aos 11:00 utilizados.
- [ ] Testar palavras com e sem acentos, respostas incorretas e consultas ambíguas.
- [ ] Testar término do tempo sem perda das correlações e com saída livre.

### Mídia e encerramento

- [x] Referenciar três fragmentos locais e transcrições na interface.
- [x] Disponibilizar encerramento documental local sem obrigatoriedade de MP4.
- [ ] Ouvir os arquivos no equipamento definitivo e conferir clareza, volume e conteúdo.
- [ ] Confirmar as oito telas finais, texto/legendas, controles e duração de 04:15.
- [ ] Testar rejeição de reprodução e bloqueio de nova aba.
- [ ] Garantir que seja possível concluir sem som e sem vídeo.

### Operação e entrega

- [ ] Reservar o painel da equipe; não expor a resolução na navegação pública.
- [x] Disponibilizar reset em duas ações.
- [ ] Homologar reset completo antes e depois da conclusão, incluindo encerramento e áudios.
- [ ] Documentar/implementar retomada de sessão somente se ela se tornar requisito aprovado.
- [ ] Testar cópia integral para outro computador, com internet desligada e recursos baixados.
- [ ] Conferir prova física A4 em 100%, crachá e montagem do cenário.
- [ ] Realizar sessão piloto de 3 a 5 pessoas e medir análise mais reconstituição em até 15 minutos.
- [ ] Atualizar os manuais históricos antes de tratá-los como orientação vigente da equipe.

## 22. Fontes de conferência e manutenção

Fontes imediatas: `index.html`, `style.css`, `app.js`, `engine.js`, `data.js`, `encerramento/cenas.json`, os tokens de `7set-dev-kit-marca.zip` e as diretrizes consolidadas de `../05_DOCUMENTACAO/Planejamentos_de_referencia/planejamento-producao-7set-dev.md`.

Planejamentos antigos podem mencionar imagens pendentes, MP4 ou quantidades anteriores: prevalecem a entrega final, os retratos aprovados e a decisão sem vídeos. Ao alterar uma regra, atualizar conjuntamente conteúdo, motor, interface, transcrições, reconstituição e documentação. Não manter duas aplicações divergentes com aparência de versão final.
