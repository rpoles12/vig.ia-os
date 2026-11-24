# Escape Room — planejamento de produção com identidade 7set.dev

Atualizado em 15/10/2026. Este documento complementa o planejamento de materiais da conversa. Define a aplicação visual e a sequência de produção. Não inicia a geração dos materiais finais.

## 1. Referências e prioridade

Pasta recebida: `C:\Users\45061155890\OneDrive - SESISENAISP - Escolas\Senai\Escape Room Mentalist\identidade-visual-7set-dev`.

Referências consultadas:

- `06-manual-e-kit/7set-dev-manual-de-marca.pdf`: regras de marca, cores, tipografia, composição e legibilidade.
- `06-manual-e-kit/7set-dev-kit-marca.zip`: logos, fontes Space Grotesk e IBM Plex Mono, licenças, README e brand-tokens.json.
- `06-manual-e-kit/7set-dev-identidade-neon.zip`: orientação de brilho e aviso de que as imagens são conceituais.
- `03-telas/01-terminal-principal.png` e `04-tela-evidencias.png`: composição e atmosfera das interfaces.
- `02-elementos-graficos/02-grades-e-texturas.png`: repertório de texturas.
- `05-mockups/07-tecla-olho-aprovada.png`: imagem de campanha aprovada.
- `04-cartazes/03-cartaz-neon.png` e `05-mockups/05-aplicacoes-identidade.png`: exemplos de aplicação.

Ordem de decisão: regras explícitas do manual e do kit; assets oficiais; telas e mockups como referência visual. O roteiro final governa nomes, acontecimentos, horários e mecânicas. Exemplos do manual e das telas não criam novos fatos do caso.

## 2. Regras de aplicação

### Marca e hierarquia

- Escrever exatamente `7set.dev`, em minúsculas. Usar os arquivos oficiais do wordmark, sem redesenhá-lo.
- Logo em Space Grotesk Bold. Não anexar olho, tecla ou outros símbolos ao wordmark.
- Preservar proporções e área livre mínima equivalente à altura do caractere 7.
- Largura mínima: 120 px em tela e 30 mm em impressão. Abaixo disso, usar o nome como texto simples, conforme manual.
- Wordmark claro em fundos escuros; preto em fundos claros; roxo quando houver contraste suficiente. Neon restrito a destaques grandes.
- `7set.dev` identifica a experiência; `VIGIA/3` identifica a testemunha digital/interface já prevista no roteiro. A identidade não renomeia personagens, arquivos ou instituições fictícias.
- Não aplicar a marca da experiência automaticamente em todas as provas. Uma nota financeira, conversa e registro de catraca devem manter a aparência de suas respectivas origens.

### Cores

| Uso | Cor |
|---|---|
| Fundo principal | #08070C |
| Painéis e superfícies | #14111C |
| Apoio e áreas gráficas | #6426C9 |
| Destaques e atividade | #A66BFF |
| Texto principal sobre escuro | #E8DCFF |
| Texto secundário | #9B96A5 |

- Preto domina; roxo neon destaca ações, seleção e atividade.
- Não usar roxo como fundo de textos longos. Não comunicar pistas ou estados somente por cor: acrescentar texto, ícone ou forma.
- Estados de sucesso ou erro devem ter rótulos explícitos. Não introduzir automaticamente verde, vermelho ou neon multicolorido.
- Testar o contraste em cada combinação real, principalmente cinza pequeno sobre preto-violeta.

### Tipografia

- Space Grotesk Bold: títulos, chamadas e marca.
- IBM Plex Mono Regular: horários, códigos, logs, dados, etiquetas e informações investigativas.
- Utilizar os arquivos de fonte incluídos no kit. A aplicação deve carregar fontes localmente e funcionar offline.
- Incorporar fontes nos PDFs e converter textos do logo em curvas quando necessário para evitar substituições. Preservar texto selecionável nos documentos sempre que possível.
- Referência inicial de corpo: 11–12 pt nos impressos A5 e 16–18 px na interface em 1080p; ajustar pelo teste no tamanho e distância reais.
- Não comprimir textos para caber: aumentar o espaço, dividir o documento ou permitir ampliação.

### Efeitos, texturas e imagens

- Usar grades, dither, interferências e fragmentação em fundos, margens, miniaturas e transições.
- Nunca aplicar glitch, desfoque ou tarjas decorativas sobre nomes, números, horários, instruções ou trechos essenciais de uma evidência.
- No neon, manter o núcleo branco/lilás nítido. A orientação do kit para o brilho é aproximadamente 8%–18% da altura das letras ou bordas; reduzir se afetar a leitura.
- A tecla com olho é imagem de campanha, não substitui o logo. O uso na abertura deve ser breve e subordinado às ações do jogador.
- Fotografias podem receber tratamento violeta moderado, mantendo rostos reconhecíveis e consistentes entre fichas, crachá e foto antiga.
- Mockups e pranchas servem como referência; não recortar textos ou elementos desses exemplos para compor os arquivos finais.
- Texto de provas será composto com tipografia real. Se houver geração de imagens, gerar fundos, retratos ou ilustrações; inserir nomes e dados depois por diagramação.

### Interface

- Recriar a linguagem de painéis, bordas finas, títulos, memória, arquivos, áudio e cronologia com componentes reais.
- Adaptar a densidade das telas ao grupo de 3–5 jogadores e ao monitor disponível. Abrir provas em área ampla com zoom.
- Diferenciar cronômetro de partida e horário dos fatos. O `15:00` da referência não é horário do crime.
- Substituir horários, IPs, códigos, documentos, contagens e personagens ilustrativos pelos dados do roteiro.
- A referência mostra quatro fragmentos de áudio, mas o planejamento do jogo prevê três. Produzir os três aprovados.
- Não adotar automaticamente o progresso 67% mostrado como exemplo no manual: os estados de memória devem seguir o roteiro e a implementação aprovados.
- Nenhum botão cenográfico deve parecer utilizável sem função. Evitar contagens falsas e elementos que sugiram pistas extras.
- As referências visuais não mudam o ritmo investigativo nem adicionam cenas de terror, desafios ou arquivos.

### Impressão

- Impressos precisam funcionar com tinta comum: o efeito neon será representado por cor plana e contraste, sem prometer fluorescência real.
- Fichas e crachá devem priorizar nomes, rostos e número 2847. Placas podem ter impacto visual maior.
- Preparar PDF no tamanho real, fontes incorporadas, margens seguras e imagens adequadas a aproximadamente 300 ppi no tamanho de uso.
- Na impressão doméstica em A4, respeitar a área imprimível. Sangria de 3 mm somente quando o processo gráfico e o formato de papel permitirem.
- Definir papel e equipamento antes de conversão de cor; para gráfica, usar o perfil solicitado. Não aplicar CMYK genérico sem necessidade.
- Fazer prova física de uma ficha e do crachá antes de imprimir o conjunto.

## 3. Inventário e formatos preservados

### Impressos

| Material | Quantidade e montagem | Saída |
|---|---|---|
| Fichas dos funcionários atuais | 8 fichas A5; 2 por A4; 4 páginas | PDF |
| Crachá Helena 2847 | 54 × 86 mm; 2 conjuntos de frente/verso em A4, para recorte e colagem | PDF |
| Central de Investigação | 1 placa A3 horizontal, com alternativa A4 | Dois PDFs |
| Terminal VIGIA/3 | A5 horizontal; 2 por A4 | PDF |
| Etiquetas | 12 unidades, aproximadamente 85 × 35 mm; 4 de cada título: Confidencial, Evidência, Acesso restrito | PDF A4 |

As versões alternativas e reservas não são itens adicionais obrigatórios de cenário. A pasta Arquivo Estudantil, arquivos do caso e cartões de cronologia permanecem digitais. Não acrescentar folders, cartazes promocionais ou outras peças apenas por aparecerem nos mockups.

### Conteúdo digital

| Conjunto | Conteúdo obrigatório | Saída |
|---|---|---|
| Personagens | 8 retratos de funcionários e Bryan; demais retratos somente se necessários | JPG de alta qualidade |
| Identidade de Bryan | Foto F1 da equipe de 2024 e identificação; ficha A-17 com BA-17; Log L1 com B_A_17 às 22:36 | Foto JPG; documentos PNG |
| Objeto do roubo | Manifesto V-17 com 3 projetos e tipos de arquivo; oferta NORTHSTAR de R$ 15.000 | PNG |
| Helena e Rafael | Registro C1: 2847 às 22:31; conversa de ameaça e devolução do crachá; duas entradas anteriores de Rafael | PNG |
| Marcelo | Conversa de coação e ordem RV-MANUT; NF-318; NF-318B; resumo de R$ 3.840; auditoria da conta criada às 18:10 e acesso ao V-17 | PNG |
| Cronologia | 6 cartões: 22:31, 22:36, 22:41, 22:44, 22:46, 22:49; revelação OUÇA O FRAGMENTO 03 | PNG/SVG e textos estruturados |
| VIGIA/3 | Áudios 01, 02 e 03; transcrições; respostas e dicas por condição | WAV/MP3, TXT, VTT quando houver sincronização, JSON |
| Final | Storyboard e roteiro; reconstrução de 70–90 s; legendas; cartela CASO RECONSTRUÍDO | PDF/PNG, MP4 1080p, SRT |
| Sistema | Telas, arquivos, zoom, progressão, cronologia, protocolo final, cronômetro e controles de operação | HTML/CSS/JS, SVG/PNG e JSON |

Documentos em proporção A4 terão referência de 1654 × 2339 px. Conversas terão páginas legíveis em vez de uma imagem excessivamente longa. Ícones usarão SVG; JPG para fotos; PNG para documentos com texto. Não haverá fundo transparente para provas que exigem superfície de leitura.

## 4. Lotes de geração

Cada lote terá relação de entradas, arquivos produzidos, conferência de conteúdo e prévia de revisão. O seguinte só deve reutilizar um modelo depois de corrigidas as falhas encontradas no anterior. Revisão interna é obrigatória em todos os lotes; validação do usuário se concentra na direção visual inicial, nas primeiras peças diagramadas e na experiência completa.

### Lote 0 — conteúdo e preparação visual

Produzir:
- Matriz canônica de personagens, papéis, projetos, datas, códigos, horários e relações causais, conferida com o roteiro final.
- Inventário de assets oficiais com versão e origem.
- Cópia de trabalho das fontes, logos e tokens, preservando a pasta recebida.
- Guia curto de aplicação e lista final das peças.

Critério para avançar: nenhum fato essencial ausente será completado por suposição. Localizar no roteiro ou registrar a pendência específica. Não alterar a solução para adaptar uma imagem de referência.

### Lote 1 — amostra visual

Produzir somente quatro amostras:
1. Uma ficha de funcionário A5.
2. Crachá de Helena 2847.
3. Log L1 digital.
4. Tela principal da VIGIA/3 com visualizador de evidência.

Saídas: PDF de prova das peças físicas, PNG do documento e prévia da tela. Dados conhecidos devem ser reais do roteiro; qualquer campo ainda pendente será sinalizado na prévia e não usado como prova final.

Conferir: cores, fontes, hierarquia, marca, leitura dos rostos, 2847, B_A_17 e 22:36; legibilidade no monitor e em impressão a 100%.

Marco: validar essa direção com o usuário antes de multiplicar as peças.

### Lote 2 — personagens e impressos

Produzir os retratos necessários e os PDFs finais: 8 fichas, crachá, duas placas e cartela de etiquetas.

Método: usar um retrato-mestre por personagem, mantendo o mesmo rosto em todas as aparições. Se os intérpretes fornecerem fotos, usar essas referências. Gerar retratos sintéticos apenas se essa direção for escolhida.

Conferir: Helena e Marcelo entre os atuais; Bryan ausente da parede; nomes e cargos aprovados; crachá 2847; tamanho real, recorte e fontes. Conferir uma prévia de cada PDF e uma prova física das peças pequenas.

### Lote 3 — Bryan e objeto do roubo

Produzir F1 e identificação, A-17, L1, manifesto V-17 e mensagem NORTHSTAR.

Conferir: mesma aparência de Bryan; ligação Bryan → BA-17 → B_A_17; horário 22:36; lote e projetos coerentes; oferta de R$ 15.000. As relações devem ser dedutíveis sem escrever a resposta explicitamente em um destaque.

### Lote 4 — Helena e acesso físico

Produzir C1, conversa Bryan/Helena e os dois registros de Rafael.

Conferir: 2847 coincide com o crachá; 22:31 é consistente; chantagem compreensível; datas anteriores de Rafael; uso da credencial não tratado automaticamente como presença de Helena.

### Lote 5 — Marcelo e acesso digital

Produzir conversa Bryan/Marcelo, NF-318, NF-318B, resumo financeiro e auditoria RV-MANUT.

Conferir: a irregularidade financeira é demonstrável; valores somam R$ 3.840; criação às 18:10; concessão ao V-17; distinção entre criação e utilização da conta; colaboração coagida e ausência física conforme roteiro.

### Lote 6 — cronologia e textos da VIGIA/3

Produzir seis cartões digitais, revelação do Fragmento 03, roteiros dos três áudios, transcrições-base, respostas, dicas e campos do protocolo final.

Conferir: cada acontecimento se apoia nas provas; sequência causal única; 22:46 interpretável; horários do crime separados do cronômetro; identificação dos arquivos não entrega a ordem; dicas graduais não antecipam etapas.

Somente depois de consolidar esses textos iniciar a gravação ou síntese de voz.

### Lote 7 — mídias e encerramento

Produzir áudios finais e legendas; roteiro e storyboard do vídeo; cartela final; edição do vídeo a partir das gravações disponíveis.

Conferir: voz compreensível; efeitos discretos; legendas fiéis; durações compatíveis com a partida; reconstrução explica Bryan como principal vilão, Marcelo coagido e Helena como vítima de chantagem e causadora da morte.

Dependência: fotografias e gravações de alunos/professores precisam ser fornecidas ou realizadas pela equipe. A produção de voz dependerá da ferramenta disponível ou das gravações fornecidas. Storyboard não será apresentado como vídeo concluído.

### Lote 8 — sistema e pacote integrado

Implementar as telas e interações com os assets consolidados; carregar fontes e mídias localmente; integrar progresso, validações, cronômetro e reinício.

Conferir uma partida completa e um reinício: todos os arquivos abrem, nenhuma informação essencial fica escondida, não há controles sem função, as dicas aparecem na condição correta, a ordenação libera o Fragmento 03 e o formulário final chama a conclusão.

Entregar o sistema offline, PDFs finais, imagens e mídias, fontes/licenças necessárias, fontes editáveis disponíveis e inventário de entrega. Registrar alterações realizadas após o teste.

## 5. Organização e controle

Estrutura prevista: `00_REFERENCIAS`, `01_IMPRESSAO`, `02_PERSONAGENS`, `03_EVIDENCIAS_DIGITAIS`, `04_CRONOLOGIA`, `05_VIGIA_AUDIO`, `06_VIDEO_FINAL`, `07_SISTEMA`, `08_EDITAVEIS`, `09_REVISAO`.

- Preservar os arquivos recebidos; trabalhar com cópias.
- Nomear arquivos por código estável e versão; por exemplo, `L1_acesso_v01.png`. Código interno não deve revelar respostas ao jogador.
- Separar prévias de finais. Cada lote terá um registro de peças, formatos, dimensões e situação.
- Não substituir arquivos aprovados sem registrar a revisão.
- Revisão de saída: conteúdo, legibilidade, consistência visual, formato correto e funcionamento na experiência.
- Marcos de revisão do usuário: amostra do lote 1; primeiras peças finais do lote 2; partida integrada do lote 8. Os demais lotes seguem os padrões consolidados e recebem revisão interna antes da entrega.

## 6. Situação da produção

Lote 0 concluído em 15/10/2026. Pacote em `output/lote-00/`, com matriz canônica, inventário de 34 conjuntos, guia visual, dados estruturados, registro de pendências e briefing das quatro amostras. Foram preservadas cópias de 16 assets recebidos e dos três documentos finais; cópias verificadas por SHA-256.

A conferência recuperou os nomes dos oito funcionários, os três projetos do V-17 e a cronologia completa. Também identificou correções editoriais necessárias: o briefing antigo revela o horário da solução, as consultas físicas precisam virar digitais, a memória 67% é canônica e o cartão E deve ocultar a hora. Detalhamento em `output/lote-00/01_MATRIZ_CANONICA.md` e `04_PENDENCIAS_E_DECISOES.md`.

Nenhuma evidência final, PDF de impressão, imagem nova ou interface final foi gerada. O próximo trabalho são as quatro amostras do lote 1. Pendências de datas, detalhamento financeiro, elenco e gravações estão registradas para os lotes correspondentes e não serão preenchidas por suposição.

Atualização de produção: lote 1 produzido em `output/lote-01/`, com dois PDFs A4 de amostra, PNGs individuais, Log L1 1654 × 2339 px, tela local HTML/CSS/JS e screenshot 1920 × 1080. O parágrafo anterior descreve o encerramento do lote 0. As amostras do lote 1 foram conferidas digitalmente; retrato e prova física continuam pendentes. Direção visual aguarda revisão do usuário antes da multiplicação para o lote 2.

Continuidade solicitada pelo usuário: lote 2 diagramado em `output/lote-02/`, seguindo o padrão do lote 1. Inclui seis PDFs: oito fichas em quatro A4, crachá com reserva, placa central A3 e alternativa A4, placa terminal com reserva e 12 etiquetas. PNGs individuais, matrizes vetoriais e nove espaços provisórios de retrato também entregues. Todas as páginas foram inspecionadas digitalmente. Fotos definitivas e prova física permanecem pendentes; a etapa de retratos não é considerada concluída como fotografia final. Próximo lote de conteúdo: 3.

Lote 3 produzido em `output/lote-03/`: ficha A-17, manifesto V-17 e mensagem NORTHSTAR diagramados; Log L1 reaproveitado com igualdade de hash; composição F1 JPG e legenda PNG em estado explicitamente provisório. Documentos em 1654 × 2339 px e F1 em 1920 × 1080. Inclui textos estruturados e orientações de integração. Nenhum impresso adicional. As imagens foram revisadas; F1 depende da fotografia e identificação do elenco. Mensagem NORTHSTAR deve ser liberada após confirmar Bryan para não antecipar a identidade. Próximo lote de conteúdo: 4.

Lote 4 produzido em `output/lote-04/`: C1, conversa H1, registros R1 e mensagem familiar R2, todos em PNG 1654 × 2339 px e revisados visualmente. Inclui transcrições estruturadas, orientação de desbloqueio e registro das adaptações editoriais. Ano, horários dos acessos antigos e local de entrega não foram inventados; as imagens omitem os detalhes pendentes e preservam as inferências essenciais. Nenhum impresso adicional. Próximo lote de conteúdo: 5. O plano tem nove lotes, numerados de 0 a 8.

Lote 5 produzido em `output/lote-05/`: 13 PNGs (M1, seis notas, resumo financeiro, RVM, relatório AL e três páginas de apoio). Usuário autorizou completar dados fictícios: pares R$ 720, R$ 560 e R$ 640, total R$ 3.840. Matriz e pendências atualizadas; cópia consolidada acompanha o lote. Os seis lançamentos são irregulares, referentes a três serviços não executados nem autorizados. AL entregue como relatório narrativo fictício; videochamada audiovisual não foi produzida. Todos os layouts foram inspecionados; integração e leitura no monitor final ainda pendentes. Próximo lote: 6.

Lote 6 produzido em `output/lote-06/`: seis cartões PNG 900 × 600, revelação e protocolo vazio 1920 × 1080, CAM01 1654 × 2339, respostas/dicas da VIGIA/3, três roteiros de áudio e adaptador de lógica offline para futura integração. Horário do cartão E oculto em arte, texto alternativo e dados de exibição. CAM01 e Fragmento 03 liberados após cronologia correta. Nove imagens inspecionadas; 720 ordens testadas, apenas uma aceita; pré-requisitos e protocolo também verificados. Sem áudio gravado nem interface completa neste lote. Próximo lote: 7.


Lotes 7 e 8 produzidos em 15/10/2026. Lote 7: três áudios WAV, locução em oito cenas, encerramento audiovisual HTML legendado, storyboard PDF e cartela PNG. Voz sintética local única Maria Desktop; sem filmagem ou MP4. Lote 8: aplicação offline integrada, 22 evidências, progressão 08/34/67/100, dicas, cronologia, protocolo, pausa, ensaio e reinício; inclui cópias dos seis PDFs de impressão aprovados. Investigação de 12min30s reserva 2min07s para encerramento dentro da janela total. Percurso concluído em navegador e motor testado com 720 permutações. Fotografias/F1, prova física, escuta humana e grupo piloto continuam pendentes e não são declarados concluídos.


Atualização vigente de retratos: os nove personagens são fictícios gerados, não elenco real. Bryan v02 aprovado pelo usuário. Retratos aplicados a fichas, crachá, A-17, F1 e cópias do sistema; F1 é uma composição de retratos com Renata/Bryan/Eduardo. Amostras e matrizes de produção atualizadas. Decisão vigente: sem vídeos. Permanecem prova física, áudio no local e partida-piloto.
