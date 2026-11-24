## Revisão vigente — VIG.IA OS v2 / 19-11-2026

Esta revisão substitui as descrições anteriores da interface. Entrada: 02_SISTEMA_OFFLINE/index.html.

- Desktop somente com atalhos maiores: Arquivos, VIG.IA, Registros, Áudios, Próximos passos.txt e Lixeira. Retirados os atalhos decorativos de arquivos corrompidos e os painéis de texto.
- Todos os aplicativos na barra de tarefas, com indicador de janela aberta/ativa. Tempo até o apagamento, memória, mini-player, efeitos e relógio ficam na mesma barra. Retirados os botões flutuantes duplicados de IA e respostas.
- Próximos passos.txt atualiza suas orientações conforme identidade, acessos, cronologia e conclusões. Lembretes acompanham a etapa atual e avisos anteriores são descartados na troca de fase.
- Cronologia é uma etapa de Registros. Não existe aplicativo separado. Enter continua enviando respostas e os bônus de15s permanecem.
- Explorador com blocos e prévias dos documentos, navegação com ícones e abertura do documento em janela auxiliar com um clique. Busca e filtros mantidos.
- IA em conversa com histórico, balões opostos, avatares, exemplos e campo de mensagem fixo na parte inferior da janela. Memória e capacidades acessíveis no cabeçalho. As orientações evoluem com a investigação.
- Janelas independentes podem ficar abertas simultaneamente. Barra de tarefas alterna/restaura/minimiza. Posição, tamanho, maximização, conversa e rascunhos são preservados durante a rodada. Arraste pelo título, redimensione pelo canto inferior direito; duplo clique no título maximiza/restaura. Há animações de entrada, saída e minimização, respeitando preferência de movimento reduzido.
- Regras, respostas, documentos, áudios, bônus, tela azul e sequência de anotação por30s → código → filme foram preservados. Reiniciar limpa o estado das janelas e da conversa. Recarregar inicia nova rodada.
- Conferência:105 verificações automatizadas aprovadas; percurso no navegador, envio com Enter, etapas/atualização das notas, prévia e abertura por clique, conversa, minimizar/restaurar/maximizar com rascunho preservado,30s de anotação e código incorreto/correto liberando o filme. Consultar o relatório de verificação v2. Abertura direta local e percepção do som devem ser conferidas no computador do evento; a política do navegador de teste impede file://.

## Atualização vigente - VIG.IA OS / 19-11-2026

Esta seção substitui descrições antigas de navegação por abas e encerramento roxo de tempo esgotado. A entrada continua em02_SISTEMA_OFFLINE/index.html.

- A navegação principal é uma área de trabalho com5 aplicativos: Arquivos, IA, Registros, Cronologia e Áudios. Barra fixa inclui mini-player, IA e Registros lado a lado, efeitos e relógio real. O painel superior informa o prazo até o apagamento.
- Uma janela principal preserva estado dos aplicativos; minimizar e fechar não apagam rascunhos. O leitor é auxiliar. Em telas largas, IA e documento podem ficar lado a lado.
- Explorador: categorias, busca, lista/ícones, prévia, Enter/duplo clique e arquivos corrompidos com nomes neutros. O catálogo passa por8/23/24/25 evidências. Blocos do desktop e selos de novidade acompanham a recuperação.
- Memória8/34/67/100; validar a cronologia mantém67% e amplia a interpretação temporal. Respostas certas continuam aceitas sem leitura obrigatória. As perguntas finais, chave,25 documentos e sequência oficial foram preservados.
- Bônus de15s para identidade, acessos e cronologia, uma vez cada, com aviso breve de2s sem botão. Prazo de produção750s, orçamento máximo795s. A exposição final da chave tem30s independentes.
- Ao expirar: tela azul VIGIA_DATA_TIMEOUT, chiado de1,2s respeitando silêncio, áudio pausado e interação pública bloqueada. Nada é apagado do Windows. Operação autenticada pode autorizar continuação sem prazo ou reiniciar.
- Conclusões corretas contêm o apagamento; anotar chave por30s, ocultar, digitar e liberar automaticamente o filme continuam obrigatórios. Um fluxo não contorna o outro.
- Novos desktop.js e desktop.css; fundo e ícones em assets/os. app.js adapta apresentação ao motor. engine.js preservado. Os campos image legados dos cartões apontavam para arquivos inexistentes e foram retirados: os6 cartões continuam compostos em HTML, com texto e IDs preservados.
- Conferência:104 testes automatizados de regras e caminhos, efeitos simulados, percurso HTTP com erros/Enter/bônus/arrasto/30s/chave/filme, falha isolada de12s e continuação autorizada. Layouts1280x636,1366x768,1920x1080 e390x844. Abertura file:// bloqueada pela política do navegador de teste: homologação no equipamento do evento e percepção de som continuam pendentes.
- Backup anterior mantido no workspace em tmp/backups/vigia_os_20261119_090842. Consultar VIGIA_OS_LEIA-ME.md e o relatório VERIFICACAO_VIGIA_OS_20261119.json.

# Sistema offline — guia rápido atualizado

Abra `index.html` no navegador. Copie esta pasta inteira, sem separar nem renomear arquivos. A aplicação funciona localmente; homologar no computador definitivo sem internet.

## O que está implementado

- Cinco áreas públicas: Arquivo, Respostas, Cronologia, Áudios e VIG.IA.
- 24 evidências digitais com bloqueios progressivos e leitor ampliável.
- IA testemunha local determinística; não é serviço generativo conectado.
- Três fragmentos e transcrições equivalentes.
- Cronologia de seis cartões com setas e arraste; ordem correta dispara Fragmento 03 e mantém a aba Respostas.
- Protocolo final `BA17-2847-2246`; identidade, credencial e minuto precisam estar certos.
- Depois do protocolo correto, o filme HTML local abre em modal quase em tela cheia e começa a narração única de `audio/final_completo.wav` sincronizada às cenas.
- Modal adaptável, cenas ajustadas para caber sem rolagem, saída por botão/Esc e barra compacta (progresso, play/pause, tempo, legendas e som).
- Painel reservado via `Ctrl+Shift+O`, credencial local `7SET-OPERACAO`; reset em duas ações.

O filme não é um MP4. Ele usa cenas/imagens, animações e conteúdo local em `encerramento/filme/`. Se o navegador bloquear a reprodução automática, use o botão de reprodução oferecido pelo próprio filme. O sistema não guarda a sessão após fechar ou atualizar a página.

Para a resolução completa, estrutura técnica, dependências e contingências, consulte `../05_DOCUMENTACAO/00_GUIA_DE_CONTINUIDADE/`. Os READMEs antigos de especificação foram preservados com identificação de histórico; eles não são a fonte do comportamento atual.


## Atualização vigente - 17/11/2026: conclusões e código

Esta atualização substitui descrições anteriores conflitantes sobre consulta obrigatória e abertura automática do filme.

- As conclusões finais perguntam quem invadiu o Repositório Vértice, qual credencial foi usada para entrar no prédio e em que minuto ocorreu o confronto fatal. Respostas: Bryan/BA-17, 2847 e 22:46.
- Abrir documentos ou iniciar/ler o Fragmento 03 não é requisito para aceitar uma resposta correta. Permanecem a progressão por identidade, acessos e cronologia, as respostas oficiais e a validação dos três campos. O formulário final fica disponível após validar a cronologia.
- Confirmar os campos gera BA17-2847-2246, para o relógio e mostra um resumo objetivo e o botão Copiar código. O filme não abre automaticamente. Enquanto a etapa seguinte não for definida, a reconstituição preservada pode ser aberta manualmente pelo botão.
- Recomendação de continuidade: uma segunda tela local de recuperação no mesmo computador, recebendo o código para liberar o filme. Essa segunda tela ainda não foi implementada; não anunciar como pronta. Outro computador só é indicado se a equipe quiser uma segunda estação física e puder operá-la.
- CAM01 passou a ser um relatório de integridade: início e extensão dos trechos, cabeçalho sem quadros e eventos de diagnóstico/reposítorio. Não há horário final em destaque. S-02: 22:44:00 + 152 s = 22:46:32; o cabeçalho S-03 e as respostas posteriores não ampliam a cobertura visual. Isso não define o segundo exato da morte.
- Impressão complementar: seis páginas A4 verticais em Escape_Room_6_Documentos_Complementares_A4.pdf. Quatro pistas (L1, A17, H1, RVM) e dois documentos administrativos sem vínculo com o incidente. Imprimir 100%, frente única; misturar pelo cenário. O PDF original de nove páginas de cenário continua válido e independente.
- Roteiros antigos e testes que exigiam A17/Fragmento 03 consultados estão superados nesse ponto. Áudio e transcrições foram preservados. Piloto, prova física, file:// e equipamento definitivo continuam sujeitos a homologação.


## Atualização vigente - pistas de horário e código em exibição única

Revisão de 17/11/2026. Substitui as descrições anteriores sobre tela de código persistente, botão Copiar código e possibilidade de voltar para conferi-lo.

- T3, Extrato de ocorrências, é o 25º documento do catálogo. Fica disponível após confirmar os acessos, antes de resolver a cronologia. A tabela mistura a ordem de extração e inclui entrada, sessão, alerta, chegada à sala, confronto (22:46), fim da cópia (22:47) e saída. Não exige nova interpretação de segundos nem fixa o segundo exato da morte.
- No erro de cronologia, o botão para T3 aparece entre catraca e Log L1. No erro de horário, é a primeira indicação: procurar o confronto na sala técnica e usar o minuto dessa linha. CAM01 e transcrição continuam como conferências adicionais.
- Os campos finais têm placeholders Nome Sobrenome, Ex 1234 e HH:MM.
- Acertar as conclusões abre automaticamente um modal central com o código BA17-2847-2246 e seis tons de atenção moderados. A opção de silenciar os efeitos é respeitada. O modal orienta anotar no papel; não há botão para copiar digitalmente.
- Não há fechamento por Esc ou botão X. O grupo marca “Já anotamos o código completo no papel” para habilitar “Anotamos. Ocultar código e continuar”. Ao confirmar, o código é apagado do conteúdo do modal e não reaparece ao navegar pelas abas. A página de conclusão não repete código nem os três valores que o formam.
- A confirmação de anotação é mantida na sessão da aba, inclusive após recarregar quando o navegador suporta sessionStorage. Isso não salva o progresso da investigação. Reinicializar sessão pelo painel da equipe limpa a confirmação para o próximo grupo. Não é uma proteção contra inspeção dos arquivos locais.
- Separar papel e caneta antes da rodada. Não fechar a janela antes de o grupo conferir a anotação. O filme segue disponível manualmente; a etapa de digitar o código ainda não foi criada.
- Os seis documentos complementares para impressão permanecem iguais. T3 foi acrescentado ao sistema, e sua matriz PDF está em 04_PRODUCAO_E_EDITAVEIS/Fontes_documentos_complementares/.


## Fluxo final vigente - terminal de recuperação no mesmo computador

Atualização de 17/11/2026. A segunda tela agora está implementada e substitui as instruções anteriores de filme manual ou etapa seguinte ainda não criada.

1. Concluir a investigação gera o código e abre o pop-up sonoro para anotação no papel.
2. Confirmar que o código foi anotado apaga sua exibição e leva automaticamente a uma tela de fundo roxo, sem navegação pública, com o campo XXXX-XXXX-XXXX e o botão Recuperar arquivo.
3. Código vazio ou incorreto mantém a tela e orienta conferir a anotação. A validação aceita o mesmo código com letras minúsculas, espaços ou sem separadores. Não mostra a resposta correta.
4. O código correto libera e abre automaticamente o modal da reconstituição, iniciando a narração contínua. Essa autorização é exigida também pela abertura manual e pelos comandos do filme.
5. O campo digitado é limpo após o acerto; fechar o filme não reapresenta o código. A reconstituição pode ser revista depois da liberação. A confirmação de anotação permanece de exibição única.
6. Reinicializar pelo painel da equipe limpa também a autorização do terminal, a entrada e a mensagem de erro, preparando o próximo grupo.

Conferido em prévia HTTP local: percurso completo; transição pop-up → tela roxa; placeholder; rejeição de vazio e código incorreto; atalho Alt+2 não contorna a etapa; código correto abre modal com botão Pausar e tempo 00:00 / 04:15; campo limpo e ausência de erros de carregamento. Execução file://, som e equipamento definitivo permanecem sujeitos à homologação.


## Atualização vigente — anotação por 30 segundos e terminal cyber

Revisão de 17/11/2026. Esta seção prevalece sobre descrições anteriores da confirmação persistente entre partidas e da anotação sem limite de tempo.

- Fluxo: acertar as conclusões → exibição obrigatória do código para anotação no caderno → inserção do código → recapitulação narrada automática após o acerto.
- A exibição tem uma contagem independente de 30 segundos, barra regressiva e tique-taque alternado a cada segundo. O tempo de análise fica parado. Os efeitos respeitam a opção de silêncio existente.
- Ao zerar, o código é apagado e abre-se automaticamente a inserção. O grupo também pode marcar que anotou e continuar antes do prazo. Esc não fecha a exibição; não há retorno para consultar a chave.
- A confirmação pertence à partida atual, assim como as respostas. Recibos antigos em sessionStorage não são restaurados: essa restauração fazia novas investigações pularem a anotação. Recarregar continua iniciando uma investigação nova; reinicializar pela operação limpa contagem e autorizações.
- A tela de inserção recebe fundo roxo com grade, painel escuro, detalhes de terminal, fontes e marca locais. Mantém XXXX-XXXX-XXXX como exemplo. Entrada vazia ou incorreta não libera o filme nem revela a resposta.
- O código correto limpa o campo e abre a reconstituição com narração. Atalhos de navegação não contornam as etapas.
- Separar caderno e caneta antes da rodada. Os seis documentos físicos continuam iguais.


## Atualização vigente — VIG.IA com apoio contextual e memória progressiva

Revisão de 17/11/2026. Esta seção substitui a consulta antiga limitada às poucas intenções de data.js. O jogo continua local e offline.

- Presença da assistente na abertura, na navegação destacada IA · VIG.IA, numa faixa contextual e num botão flutuante. A faixa alterna lembretes a cada 45 segundos conforme a etapa; não substitui mensagens de erro e não abre diálogos por conta própria.
- Tela própria com explicação do apoio, exemplos de perguntas, campo de consulta, resposta organizada em explicação, passos, documentos e ações. Perguntas relacionadas permitem aprofundar; perguntas curtas de seguimento podem retomar o assunto anterior.
- No leitor de documentos, IA abre a consulta sobre o registro atual. Nos erros, Pedir ajuda à IA considera a etapa e, no formulário final, o campo incorreto de horário.
- Conhecimento: 55 assuntos, 580 expressões cadastradas, normalização de acentos/pontuação/identificadores e abreviações, além de aproximação de palavras para erros curtos de grafia. Não é um modelo generativo nem consulta fontes externas. Consultas não reconhecidas pedem especificação e oferecem caminhos seguros.
- A evolução usa os percentuais canônicos 08% → 34% → 67% → 100%, preservando os áudios aprovados. 08%: orientação e comparação inicial. 34%: relações entre pessoas, acessos e finanças. 67%: análise cruzada da cronologia; validá-la libera também interpretação temporal de câmera e confronto, sem mudar o percentual anunciado no Fragmento 03. 100%: relações completas e responsabilidades.
- A tela exibe memória, capacidade atual, níveis e o que fazer para a próxima recuperação. Ao voltar à IA após uma mudança de capacidade, a última pergunta é reavaliada com o novo contexto.
- Três níveis de dica por etapa: orientação, comparação e ajuda direta. A consulta não é condição para aceitar respostas corretas.
- Documentos indicados são filtrados pela disponibilidade real, com botões que abrem o leitor ou a transcrição. Ações abrem Arquivo, Respostas, Cronologia ou Áudios. A IA não contorna a progressão, não valida respostas por conta própria e não reapresenta a chave final.
- Limites das evidências preservados: crachá não identifica sozinho o portador; conta remota não comprova presença; oferta não comprova pagamento; fim da cópia não é o confronto; cabeçalho vazio não é vídeo; último quadro não é o segundo exato da morte. O relato completo do ato fatal permanece para a memória integral.
- Fontes vigentes: vigia.js guarda assuntos, redações, grafias, recuperação e reconhecimento; engine.js fornece contexto e validações; app.js integra consulta, ações e interface. As intenções antigas em data.js são conteúdo legado; o caminho ativo usa vigia.js.
- Percurso da chave preservado: exibição por 30 segundos com tique-taque → inserção → recapitulação automática no acerto. Lembretes e atalhos da IA ficam ocultos durante esse percurso.

Verificação: 3.351 consultas automatizadas em cinco contextos de progresso, incluindo 112 perguntas independentes com variações de caixa, acento e cortesia; nenhuma falha nos casos testados. Conferência HTTP local de fontes e links, evolução, erro contextual, dicas, recapitulação e console. Não representa compreensão irrestrita de qualquer frase. Piloto, file:// e equipamento definitivo permanecem sujeitos à homologação.


## Atualização vigente — tempo, bônus, envio e rodapé

Revisão de 19/11/2026. Esta seção substitui instruções antigas de continuação pública automática após o cronômetro zerar e de botões flutuantes em posições separadas.

- A investigação começa com 12:30. Confirmar identidade, confirmar os dois acessos e validar a cronologia acrescentam 15 segundos por etapa, uma única vez. Total máximo de bônus: 45 segundos; janela máxima: 13:15. Erros e repetições não concedem tempo. O protocolo final encerra a análise e não concede novo bônus.
- Cada bônus abre um aviso central com a identidade roxa, +15 SEGUNDOS, a etapa confirmada e o restante no instante do acréscimo. O aviso fecha pelo botão ou automaticamente após 2,8 segundos. O cronômetro continua correndo durante o aviso. Ensaio sem tempo e continuação autorizada após o esgotamento não concedem bônus.
- Alertas sonoros no último minuto: 60, 45, 30, 20 e 15 segundos. Nos últimos 10 segundos, tique-taque alternado a cada segundo. Ao zerar, sinal de encerramento. Efeitos respeitam o silenciamento; Web Audio é preparado no clique de início para favorecer reprodução posterior.
- Ao zerar, abre a tela roxa Tempo esgotado, com 00:00, memória preservada e orientação para chamar a equipe. Áudio da investigação para; atalhos públicos ficam ocultos; Esc e navegação não fecham a tela. A rodada fica encerrada.
- A equipe continua acessando Ctrl+Shift+O e a credencial de operação. Após esgotamento, aparece Autorizar continuação sem cronômetro, que preserva o progresso e mantém 00:00. Reinicializar limpa também bônus, esgotamento e autorização de continuação.
- A exibição da chave por 30 segundos tem contador separado. O tempo da análise, inclusive alertas finais, para quando as conclusões são confirmadas. Anotar → inserir → recapitulação automática permanece vigente.
- Enter normal e Enter numérico enviam identidade, acessos, conclusões e inserção da chave. Campos incompletos recebem o mesmo retorno visual do botão; composição de texto não é interceptada. Botões de envio têm tipo explícito e o envio por teclado usa o mesmo formulário.
- Áudio, IA e Respostas ficam num rodapé fixo comum. Áudio à esquerda; IA e Respostas lado a lado à direita, alinhados pela borda inferior. Os dois atalhos permanecem disponíveis nas telas de investigação, inclusive na própria aba correspondente. Em telas estreitas, áudio fica numa linha acima, com os dois atalhos juntos abaixo. Conteúdo reserva espaço para os controles.
- Atalhos para Respostas levam à altura do campo ativo e o focam, incluindo leitor de documentos, botão flutuante e ações da IA. Se não houver campo, vão à ação pendente. A navegação principal Respostas e seu atalho Alt+2 abrem o topo da página, sem saltar ao campo.
- countdown.js concentra tempo disponível, bônus sem repetição e sinalização por segundo. app.js integra relógio, formulários, avisos, equipe e atalhos; feedback.js sintetiza os sons; style.css e index.html organizam a apresentação. vigia.js explica a regra atual ao perguntar sobre o tempo.

Conferência: 56 verificações de contagem, bônus, avisos, reinício e validações; 6 verificações de áudio com dispositivo simulado. Percurso HTTP local com os três bônus, Enter/Enter numérico, campos incompletos, atalhos, reinicialização e chave/recapitulação. Expiração conferida em cenário abreviado de 12 segundos, com Escape, Alt+2 e autorização da equipe; a duração real de 750 segundos foi verificada no módulo original. Sem erros de console no percurso.

A janela máxima de 13:15, somada à narração de 4:15, permite até 17:30. A duração total continua pendente de piloto. Volume no equipamento definitivo e execução file:// permanecem sujeitos a homologação.


## Atualização vigente — bônus breve sem botão

Revisão de 19/11/2026. Substitui o diálogo de bônus com botão e fechamento em 2,8 segundos.

O acréscimo de 15 segundos aparece num aviso pequeno, roxo, com a etapa confirmada, contagem de 2 segundos e barra regressiva. Some sozinho, não tem botão, não escurece a tela e não bloqueia o formulário. O próximo campo pode ser preenchido enquanto o aviso está visível. O acréscimo continua sendo de 15 segundos, uma vez por etapa; a contagem de 2 segundos se refere apenas à duração da notificação. Reinicializar ou esgotar o tempo também remove o aviso.

Conferido por HTTP local: envio com Enter, bônus visível com 2s e zero botões, nenhum diálogo aberto, foco no próximo campo, preenchimento durante a notificação e desaparecimento automático. Demais regras de tempo e encerramento preservadas.
