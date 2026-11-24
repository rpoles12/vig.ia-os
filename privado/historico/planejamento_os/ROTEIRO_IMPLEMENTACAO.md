# VIGIA OS - roteiro da nova experiência

O Arquivo Corrompido | Proposta para aprovação | 19/11/2026

Esta entrega planeja a transformação do terminal em uma área de trabalho fictícia de computador. As imagens são referências de direção visual. Nenhuma alteração deste planejamento foi aplicada ao sistema em uso.

## 1. Decisão central

A investigação acontece dentro de um computador comprometido. O grupo abre aplicativos, recupera arquivos e reconstrói o incidente antes que o processo de apagamento termine. Cada resposta correta recupera informações e melhora a capacidade de orientação da VIGIA/3.

A área de trabalho será a navegação principal. Terá papel de parede, atalhos com nomes claros, barra de tarefas, relógio real e janelas de aplicativos. A experiência continuará funcionando inteiramente offline no navegador, inclusive pela abertura local do index.html. O computador representado é uma interface do jogo: não será necessário acessar o explorador real do Windows.

Direção recomendada: aparência reconhecível de um computador, com o roxo e os elementos cyber do projeto. A familiaridade deve ajudar a investigação. As informações essenciais precisam aparecer sem exigir que o participante descubra gestos escondidos.

## 2. O que permanece e o que muda

Permanecem a narrativa, as 25 evidências digitais, os três fragmentos de áudio, as transcrições, os seis documentos físicos, as respostas oficiais, a IA offline e a reconstituição final. Preservam-se a aceitação de respostas corretas sem consulta prévia, o envio por Enter e a ajuda contextual depois de erros.

A interface com abas será substituída por aplicativos em janelas. O painel de progresso vira recuperação de memória; o relógio passa a representar o prazo até o apagamento; os documentos bloqueados ganham representação de arquivos corrompidos; a tela de tempo esgotado passa a ser uma falha azul de sistema.

O fluxo final permanece no mesmo computador: conclusões corretas, chave visível por 30 segundos para anotação no papel, tela para digitar a chave e abertura automática da recapitulação. Isso evita depender de uma segunda estação e de uma transferência manual de estado entre computadores.

## 3. Mapa dos aplicativos

| Aplicativo | Função | Ação principal |
| --- | --- | --- |
| Arquivos | Explorar, pesquisar e abrir as evidências | Abrir documento |
| IA · VIGIA/3 | Orientar, comparar informações e indicar caminhos | Perguntar ou pedir dica |
| Registros | Registrar identidade, acessos e conclusões | Confirmar resposta |
| Cronologia | Ordenar os seis eventos do incidente | Validar sequência |
| Áudios | Ouvir fragmentos e consultar transcrições | Reproduzir ou ler |

Cronologia terá atalho próprio e também poderá ser aberta pelo aplicativo Registros. Os dois acessos abrirão a mesma instância e o mesmo estado, evitando atividades duplicadas.

O arquivo final de reconstituição aparecerá como mídia protegida. Sua abertura só será liberada depois da inserção da chave, preservando o percurso aprovado.

## 4. Área de trabalho e navegação

### Distribuição visual

Atalhos com símbolo e nome ficam à esquerda. O centro permanece livre para janelas. O papel de parede usa preto, circuitos discretos e um anel fragmentado de memória. Arquivos corrompidos relevantes aparecem em uma área própria do desktop, com no máximo três atalhos de recuperação; os demais ficam no explorador. Assim a tela não vira um conjunto de 25 ícones.

O topo reserva uma faixa de sistema: objetivo atual à esquerda e prazo de apagamento à direita. As janelas, inclusive maximizadas, respeitam essa faixa e a barra de tarefas. O relógio e a porcentagem nunca desaparecem atrás de um documento.

Na barra inferior, IA e Registros ficam lado a lado, fixos e identificados por texto. O mini-player fica à esquerda desses dois atalhos. Arquivos e Cronologia permanecem fixados no restante da barra; o relógio real e a data ficam no canto direito. As ilustrações mostram a família visual; esta ordem funcional prevalece na implementação.

### Abrir, minimizar e fechar

- Um clique abre ou traz um aplicativo à frente. Duplo clique também funciona, sem abrir instâncias duplicadas.
- A barra de título oferece minimizar, maximizar/restaurar e fechar, com descrição acessível.
- Fechar ou minimizar preserva respostas digitadas, pergunta da IA, posição da cronologia, busca e áudio em reprodução.
- O botão Área de trabalho minimiza as janelas. Clicar em um aplicativo da barra o restaura.
- Arrastar pela barra de título é opcional; nenhuma tarefa depende de posicionar uma janela manualmente.
- A versão inicial terá uma janela principal e uma janela auxiliar de documento. A IA poderá ocupar um painel ao lado do documento em telas largas. Em telas menores, alternam-se as mesmas instâncias.
- A janela ativa precisa ter foco e borda evidentes. Janelas reabertas nunca podem ficar fora da área visível.

Não haverá menus decorativos que pareçam funcionais e não façam nada. Botões desabilitados explicarão o motivo, por exemplo: “Disponível após confirmar os acessos”.

## 5. Início da rodada

Antes da partida, a tela de preparação pede papel, caneta e teste de som. O clique “Iniciar investigação” prepara a reprodução de áudio, inicia a contagem de 12:30 e abre a área de trabalho com 8% de memória. O início não dependerá de áudio automático antes de um clique.

Uma orientação curta, dispensável, aponta três ações: ouvir a mensagem inicial, abrir Arquivos e consultar a IA. A mensagem não bloqueia os aplicativos. Uma vez dispensada, continua disponível em “Como usar” na área de trabalho.

Texto do objetivo inicial: “Identifique o perfil legado para recuperar o próximo bloco de dados”. O sistema sugere um caminho, mas permite abrir qualquer conteúdo já disponível e registrar uma resposta correta imediatamente.

## 6. Explorador de arquivos

### Estrutura

A janela terá caminho de navegação, voltar, subir pasta, busca, modos lista/ícones, categorias à esquerda e detalhes do item selecionado à direita. Categorias: Todos, Identidade, Acessos, Financeiro, Incidente, Corrompidos e Recuperados agora.

As categorias são filtros do catálogo existente. O mesmo documento não terá cópias com nomes diferentes. O caminho apresentado será fictício, por exemplo “Este computador > Arquivo do incidente > Acessos”. Datas e tamanhos exibidos devem vir de metadados definidos; datas ilustrativas dos mockups não serão usadas como pistas por acidente.

Um clique seleciona e mostra a prévia. O botão “Abrir documento”, Enter com o item selecionado ou duplo clique abrem o leitor. A prévia não substitui o documento integral.

### Estados dos arquivos

| Estado | Aparência | Comportamento |
| --- | --- | --- |
| Disponível | Ícone normal e texto legível | Abre o documento |
| Não consultado | Pequena marca de novo conteúdo | Continua disponível, sem obrigatoriedade |
| Corrompido | Ícone com fratura, cor reduzida e cadeado | Explica a etapa necessária; não abre a pista |
| Recuperado agora | Ícone restaurado e selo NOVO | Aparece no filtro de recuperados |
| Consultado | Marca discreta de leitura | Pode ser reaberto livremente |

Conteúdo bloqueado não deve aparecer em miniaturas legíveis, busca, prévia, dicas ou nome que entregue sua resposta. Antes da recuperação, usar nomes neutros como “Bloco de acessos”, “Registro temporal” e “Fragmento de mídia”.

Ao recuperar uma etapa, os arquivos correspondentes mudam de estado, com transição visual de até 800 ms. Um aviso oferece “Ver arquivos recuperados”; não abre vários documentos sozinho. O grupo pode continuar preenchendo respostas. Os selos de novidade permanecem até os itens serem consultados ou o grupo dispensar a indicação.

### Leitor

O leitor preserva a imagem original da evidência, com ajuste à janela, zoom, navegação anterior/próximo e rolagem. Oferece “Perguntar à IA sobre este arquivo” e “Registrar resposta”. O primeiro leva o documento atual como contexto; o segundo abre e foca o campo relevante sem perder a posição do leitor.

Não acrescentar horários, conclusões ou destaques sobre as evidências que alterem o nível de interpretação já aprovado. T3 continua ajudando a localizar o confronto; CAM01 continua exigindo leitura da integridade dos trechos.

## 7. IA como aplicativo

A IA terá nome, símbolo constante, porcentagem de memória, capacidade atual e explicação do próximo avanço. Seu campo terá exemplos clicáveis: “Por onde começar?”, “Onde encontro essa informação?”, “Como comparo estes registros?” e sugestões próprias da etapa.

As respostas continuam organizadas em orientação curta, passos, documentos e ações. Os documentos indicados abrem diretamente no leitor. As ações podem abrir Registros, Cronologia ou Áudios. Perguntas de seguimento preservam o contexto já existente.

| Memória | Capacidade exibida | Apoio esperado |
| --- | --- | --- |
| 8% | Orientação inicial | Explicar objetivo e sugerir comparação entre os primeiros registros |
| 34% | Relações e acessos | Diferenciar acesso físico e digital e indicar cruzamentos |
| 67% | Reconstrução temporal | Ajudar na sequência; após validá-la, interpretar os registros do evento |
| 100% | Memória integral | Sustentar a explicação completa na recapitulação |

A validação da cronologia amplia a capacidade temporal dentro dos mesmos 67%. Não criar uma etapa de 85%, pois os áudios atuais anunciam 67%. O motor continua sendo a assistente local já existente, sem prometer compreensão irrestrita ou dependência de internet.

A presença constante virá de um atalho fixo identificado, mensagem de disponibilidade na abertura, ação no leitor e ajuda nos erros. Lembretes contextuais de 45 segundos podem continuar como pequenos avisos sem som; serão suspensos enquanto o usuário digita ou durante a chave, recapitulação e falha. Não abrir o aplicativo sozinho.

## 8. Registros e respostas

O aplicativo mostra as quatro etapas com estado: pendente, disponível e concluída. Exibe uma pergunta por tarefa, campos bem identificados e botão de confirmação. Placeholders finais: “Nome Sobrenome”, “Ex 1234” e “HH:MM”. Rótulos das conclusões devem especificar a identidade do invasor, a credencial usada para entrar no prédio e o minuto do confronto fatal.

Enter e Enter numérico enviam o formulário ativo pelo mesmo caminho do botão. Não enviar enquanto houver composição de texto, em campos multilinha ou ao pressionar Enter em outro aplicativo.

Erro aparece junto ao campo: motivo, documentos recomendados e ação de consultar IA. As indicações respeitam a disponibilidade real do catálogo. Resposta correta é válida mesmo que o documento nunca tenha sido aberto.

O atalho “Registrar resposta” dentro de um documento ou resposta da IA abre o aplicativo na altura do campo e o foca. O atalho principal da área de trabalho/barra de tarefas e Alt+2 abrem o topo do aplicativo, equivalente à navegação principal atual.

## 9. Cronologia intuitiva

A instrução será “Organize do primeiro ao último evento”. Haverá seis posições numeradas e cartões com área de arrasto evidente. Ao mover, o cartão terá cópia fantasma, posição de encaixe destacada e espaço reservado para evitar saltos confusos.

Arrastar não será a única forma: botões subir/descer e controles de teclado permitem a mesma ordenação. Em telas pequenas, usar lista vertical com alvos grandes, sem depender de arrasto horizontal. O botão de validar só avalia a sequência, sem exigir consulta aos documentos.

Se houver erro, apresentar Catraca lateral, Extrato de ocorrências e Log L1, com T3 no meio, além de ajuda da IA. O feedback orienta a comparar os registros sem reorganizar automaticamente a sequência correta. Ao acertar, +15s, mídia restaurada, Fragmento 03 e CAM01 disponíveis e formulário final liberado.

## 10. Player de áudio

O aplicativo apresenta os três fragmentos, o estado de acesso, reprodução/pausa, avanço e retorno de 10 segundos, barra de progresso, volume e transcrição. Uma waveform discreta pode ser desenhada pela interface; não é necessário gerar imagens para cada segundo.

O mini-player da barra de tarefas mostra o áudio atual e permite pausar e ajustar volume de qualquer aplicativo. Fechar a janela não interrompe o áudio. Só pode existir uma narração ativa por vez; a entrada na reconstituição encerra a reprodução anterior.

Separar volume de narração e efeitos, com silenciamento claro e persistente durante a rodada. A transcrição deve continuar acessível para quem não puder ouvir. Tempos mostrados nas imagens são ilustrativos; a duração deve ser lida do arquivo real.

## 11. Progressão canônica e arquivos recuperados

| Marco | Memória | Evidências disponíveis | Mudança e próximo passo |
| --- | --- | --- | --- |
| Início | 8% | 8 de 25 | Arquivo inicial e Fragmento 01; identificar o perfil |
| Identidade correta | 34% | 23 de 25 | Recuperar 15 evidências de acessos/finanças e Fragmento 02; +15s |
| Dois acessos corretos | 67% | 24 de 25 | Recuperar T3, habilitar a cronologia; +15s |
| Cronologia correta | 67% | 25 de 25 | Recuperar CAM01 e Fragmento 03; liberar conclusões; +15s |
| Conclusões corretas | 100% | 25 de 25 | Conter apagamento, parar o relógio e mostrar a chave |

As quantidades acima contam evidências do catálogo, não áudios. Os 17 arquivos inicialmente bloqueados ganham apresentação corrompida sem criar novas pistas obrigatórias. Três atalhos neutros do desktop representam os blocos principais e remetem ao explorador.

A memória é integridade recuperada, não tempo de vida do computador. A barra sempre cresce por validação. O relógio sempre diminui com o tempo, exceto pelos três bônus. São indicadores diferentes, com rótulos e formatos distintos.

O ganho de +15s será explicado como adiamento do apagamento após recuperar um bloco. Aviso pequeno por 2 segundos, sem botão, sem escurecer fundo e sem bloquear digitação. A animação do aviso não define o valor do bônus.

## 12. Prazo de apagamento e falha azul

Texto permanente: “Dados serão apagados em 12:30”. O tempo real da barra de tarefas serve apenas como relógio do computador; os horários das evidências pertencem ao incidente. Usar rótulos distintos para não confundir esses três tempos.

Preservar a duração atual: 750 segundos iniciais e três bônus únicos de 15 segundos, chegando a 795 segundos de orçamento total. Minimizar aplicativos, ler documentos e ouvir áudios não pausa a contagem. O cálculo será baseado em tempo decorrido, para que troca de abas e queda de quadros não concedam tempo indevido.

| Restante | Visual | Som |
| --- | --- | --- |
| Acima de 60s | Painel roxo estável | Efeitos usuais |
| De 60s a 11s | Aviso âmbar e texto “Apagamento iminente” | Alertas em 60, 45, 30, 20 e 15s |
| De 10s a 1s | Numeral evidente e pulsação leve | Tique-taque a cada segundo |
| 0s | Substituir toda a experiência por tela azul | Chiado curto, com término e volume controlado |

Ao zerar: congelar interação pública, pausar narração, cancelar avisos pendentes, tocar chiado de aproximadamente 1,2 segundo com entrada e saída suaves e mostrar a falha azul. O efeito respeita o silenciamento. Não usar estroboscopia nem ciclos sonoros intermináveis.

Texto proposto para a falha: “O computador encontrou um problema e os dados desta sessão ficaram indisponíveis.” Abaixo: “Prazo de recuperação encerrado · 00:00”, “Memória recuperada: XX%”, “Chame a equipe responsável.” e código fictício “VIGIA_DATA_TIMEOUT”. O percentual representa memória recuperada, não uma simulação de reparo.

A falha é encenada dentro do navegador; não apaga arquivos reais, não reinicia o computador e não mostra um botão público para burlar o prazo. A operação preserva a autorização de continuação sem cronômetro e o reinício completo já existentes.

Se um bônus elevar novamente o restante acima de um limite de alerta, a aparência volta à faixa correspondente; não repetir o mesmo alerta em duplicidade no mesmo segundo. No limite exato de expiração, o motor decide primeiro se a rodada ainda está ativa: uma resposta enviada após o prazo não pode reabrir a sessão.

## 13. Chave, recuperação e recapitulação

Conclusões corretas suspendem o processo de apagamento e encerram o relógio de análise. O sistema chega a 100% e passa a um fluxo dedicado sem aplicativos ou atalhos públicos capazes de reapresentar a chave.

1. Mostrar painel central “Anote a chave no caderno”, com a chave oficial, contagem individual de 30 segundos, barra regressiva e tique-taque. Chamar atenção com o efeito sonoro já aprovado.
2. Permitir confirmar a anotação antes do prazo. Ao confirmar ou zerar, apagar a chave do conteúdo visível e abrir imediatamente a inserção. Esc e minimizar não ocultam essa etapa.
3. Mostrar tela roxa de recuperação, campo “XXXX-XXXX-XXXX” e botão “Recuperar arquivo”. Enter envia; erro orienta conferir a anotação sem revelar a resposta.
4. Após chave correta, limpar o campo e iniciar automaticamente a reconstituição narrada existente. Não iniciar antes da autorização.
5. Ao final, exibir encerramento de sessão. Uma revisão do filme pode ser permitida após a autorização; a chave não reaparece.

A imagem de referência usa uma chave mascarada para não expor a solução nas pranchas. O código oficial BA17-2847-2246 permanece inalterado na futura implementação. A proteção é de percurso do jogo, coerente com o sistema local atual.

O prazo de apagamento já estará contido durante a anotação e a inserção. A contagem de 30 segundos pertence só à exposição da chave. Não somar esse tempo ao cronômetro da investigação.

## 14. Arquitetura para viabilizar a mudança

Manter uma única aplicação e um único estado compartilhado. As janelas serão apresentações desse estado. Abrir ou fechar um aplicativo não poderá recriar o motor, duplicar contadores ou reiniciar áudio.

| Componente | Responsabilidade planejada |
| --- | --- |
| engine.js | Preservar validações, disponibilidade e percentuais |
| data.js | Preservar catálogo, IDs e soluções; adicionar metadados de apresentação separados |
| vigia.js | Preservar conhecimento, contexto, níveis e filtros de documentos |
| countdown.js | Preservar tempo, bônus e sinais; adaptar apresentação e conferência do prazo |
| feedback.js | Preservar efeitos; acrescentar chiado de falha e sons discretos de janela/recuperação |
| app.js | Adaptar controle de rodada e ligações entre os aplicativos |
| desktop.js, windows.js | Novos módulos clássicos para desktop, foco, dimensões e instâncias |
| desktop.css, apps.css | Novos estilos do ambiente e aplicativos |
| catalog-ui.js | Metadados de pastas, ícones e estados corrompidos, sem duplicar o gabarito |

Os nomes dos novos arquivos são proposta técnica, não arquivos já implementados. Usar scripts locais clássicos ou solução compatível com file://, caminhos relativos e fontes locais. Evitar dependências de CDN, requisições de rede e carregamento obrigatório via fetch para o catálogo.

Eventos internos previstos: rodada iniciada, resposta validada, memória alterada, conteúdo recuperado, áudio alterado, prazo crítico, tempo esgotado, chave exibida, chave ocultada e recapitulação autorizada. Todos serão derivados do estado real; animações não concedem progresso.

Separar estado da investigação, estado visual das janelas e estado do áudio. O reset limpa os três, além de bônus, alertas, rascunhos, histórico de consulta, chave e autorizações. Manter o comportamento atual de nova rodada ao recarregar; recuperação de partida após atualização da página seria uma decisão separada.

## 15. Ordem de implementação após aprovação

| Fase | Entrega concreta | Critério para avançar |
| --- | --- | --- |
| 1. Congelar referência | Cópia datada do pacote, inventário e percurso atual registrados | Gabarito, mídias, regras e pontos de entrada conferidos |
| 2. Estrutura do desktop | Papel de parede, barra, relógio, painel de prazo e janelas vazias | Abrir/fechar/restaurar e foco funcionam nas resoluções-alvo |
| 3. Migrar aplicativos | Arquivos/leitor, Registros, Cronologia, IA e Áudios ligados ao motor existente | Percurso completo sem regressão nas respostas |
| 4. Recuperação de dados | Ícones corrompidos, filtros, novos arquivos e bônus breve | Contagens 8/23/24/25 e memória 8/34/67/100 corretas |
| 5. Tensão e encerramento | Alertas, chiado, falha azul, chave e recuperação | Expiração bloqueia; chave só libera filme no momento certo |
| 6. Ajuste visual e acesso | Ícones finais, contraste, teclado, zoom e telas menores | Nenhuma ação depende apenas de arrasto, cor ou som |
| 7. Homologação e entrega | Testes offline, piloto com grupo, documentação e inventário atualizados | Aprovação no computador do evento e cópia de retorno disponível |

Priorizar uma versão funcional com as mídias existentes antes dos acabamentos. Cada fase deve ser conferida antes da seguinte. A instalação do pacote novo só acontece depois da aprovação deste planejamento e da validação da versão implementada.

## 16. Critérios de aceite e testes necessários

- Percurso correto completo: início, identidade, dois acessos, cronologia, conclusões, anotação por 30s, inserção e recapitulação automática.
- Aceitar respostas certas sem abrir evidências ou ouvir áudios; rejeitar incorretas com documentos úteis e disponíveis.
- Enter normal e numérico funcionam nos formulários; não acionam formulários de janelas inativas.
- Fechar, minimizar, restaurar e alternar apps preservam rascunhos, ordem dos cartões, busca e reprodução.
- Não criar duplicatas de janela, ouvintes, narração ou temporizadores ao clicar repetidamente.
- Cada bônus ocorre uma vez: máximo de +45s; aviso some em 2s sem botão e sem roubar foco.
- Catálogo passa de 8 para 23, 24 e 25 documentos; bloquear prévias e links de conteúdo ainda não recuperado.
- IA respeita os níveis, reavalia a consulta após evolução e abre apenas documentos disponíveis.
- Cronologia funciona com arrasto, setas, teclado e toque; encaixe e alteração de ordem são claros.
- Painel de apagamento, mini-player e IA/Registros ficam acessíveis em todos os aplicativos da investigação.
- Testar passagem do prazo, retorno de aba em segundo plano, bônus perto dos limites, clique no instante de expiração e múltiplos alertas.
- Em 0s, bloquear atalhos, formulários e leitores; respeitar silêncio; permitir somente a operação autorizada.
- Não voltar à chave por histórico, atalhos ou reabertura de app; código incorreto não abre a reconstituição.
- Reset prepara nova rodada sem vestígios do grupo anterior; recarregar mantém o comportamento documentado.
- Abrir por file:// sem internet no computador real; conferir fontes, imagens, som, transcrições e caminhos do encerramento.
- Conferir 1920x1080, 1366x768 e 1280x720; ajustar ao zoom de 125%; em telas estreitas usar app maximizado, barra compacta e catálogo responsivo.
- Respeitar preferência de movimento reduzido, foco visível e leitura por teclado; texto crítico não fica só em imagem.

## 17. Riscos de experiência e decisões recomendadas

Muitas janelas podem atrapalhar: começar com uma principal e uma auxiliar, mantendo alternância clara na barra. Ícones corrompidos podem parecer defeito real: o clique deve explicar o bloqueio dentro da narrativa e orientar qual tarefa recupera o bloco.

A busca pode entregar pistas antes do momento: resultados e prévias seguem o mesmo filtro do motor. Sons simultâneos podem encobrir falas: usar uma narração por vez, alertas breves e ajuste temporário de volume quando necessário.

A mudança de visual pode exigir locução nova se contradisser instruções antigas. Antes da implementação, conferir os três fragmentos e a narração; reaproveitar tudo que continuar coerente e listar apenas as frases que precisarem de ajuste. Não regravar por padrão.

O orçamento atual permite até 13:15 de investigação, mais 30s de exposição da chave e cerca de 4:15 de recapitulação: aproximadamente 18 minutos, além do tempo gasto digitando a chave e da preparação. Não reduzir prazos ou cortar o filme automaticamente. O piloto deve medir o tempo real do percurso e orientar eventual ajuste aprovado.

Recomendações para aprovação: cinco aplicativos com Cronologia própria; IA e Registros juntos na barra; arquivos corrompidos vinculados às evidências existentes; uma estação física; quatro percentuais canônicos; apagamento contido nas conclusões; tela azul apenas na falha; seis impressos atuais preservados.

## 18. Referências visuais e produção de assets

As dez pranchas mostram: área de trabalho/início, explorador, IA, Registros, Cronologia, player, recuperação de memória, família de ícones, urgência/falha e sequência final. Consultar a galeria para imagens em tamanho completo e notas de execução.

Os mockups orientam composição, cores, símbolos e hierarquia; não são capturas de um sistema implementado. Microtextos, metadados, arranjos de janelas e tempos ilustrativos serão alinhados ao roteiro antes da implementação. A lista detalhada está em ASSETS_NECESSARIOS.csv e na galeria.

Gerar PNG para fundos e ilustrações que realmente se beneficiem de imagem. Ícones de interface, botões, estados, cronômetros, barras e texto devem preferencialmente ser SVG/HTML/CSS para permanecerem nítidos e acessíveis. Não gerar telas inteiras como imagens de fundo da aplicação.

As referências foram produzidas com a ferramenta nativa de geração de imagens, usando a primeira área de trabalho como referência de estilo. Os prompts integrais e o registro de geração acompanham a entrega. Os PNGs desta entrega são referências, não o conjunto final de assets de produção.

## 19. Parâmetros visuais para a implementação

Paleta: fundo #08070C, janela #14111C, ação principal #6426C9, foco #A66BFF, texto claro #E8DCFF, recuperação em ciano discreto e alerta em âmbar. A tela de falha usa azul #153B9A. Manter contraste legível; brilho será um acabamento, sem halo atrás de textos longos.

Usar Space Grotesk nos títulos e IBM Plex Mono em relógios, códigos e pequenos rótulos. Corpo de leitura precisa permanecer confortável, preferencialmente entre 16 e 18px no computador de uso. Números do prazo terão largura fixa para evitar deslocamento a cada segundo.

Escala inicial: ícones de desktop de 56-64px com área clicável mínima de 80x88px; controles de 40-44px; barra inferior de 64-80px; cantos de janelas de 12-16px. A faixa superior deve se adaptar ao espaço disponível, mantendo o prazo e o objetivo fora das janelas. Essas medidas são ponto de partida e serão ajustadas na homologação a 1280x720.

Os mockups usam um painel de prazo amplo para tornar a ideia visível. Na aplicação, compactar o painel e permitir que as janelas aproveitem a largura abaixo da faixa superior. Em 1280x720, não reduzir todo o conteúdo proporcionalmente até os textos ficarem pequenos: compactar controles e permitir rolagem apenas dentro do aplicativo.

Em celular ou tela estreita, uma janela ocupa a área útil e o alternador inferior substitui o arranjo livre. A tarefa permanece a mesma; nenhuma resposta, evidência ou pista muda por causa do tamanho da tela.

Os ícones dos aplicativos terão silhuetas distintas. Bloqueio, novidade, reprodução e erro usarão símbolo e texto além de cor. As animações de recuperação poderão ser desligadas pela preferência de movimento reduzido, mantendo a mesma informação textual.
