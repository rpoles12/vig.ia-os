# VIG.IA OS — vídeo inicial e tutorial

Registro vigente: 19/11/2026. Versão 1.

## Pedido e escopo

Produzir planejamento do storyboard, imagens do storyboard e vídeo final a partir do roteiro já apresentado. Duração de 2 a 3 minutos, alvo de 2min30. Introduzir o incidente por manchetes, desafiar a equipe e ensinar a operação do OS com animações e gravações reais de uma cópia demonstrativa. Não revelar identidade de envolvidos, acessos, horários, códigos, relações causais ou solução por imagem, áudio, miniaturas ou legendas.

O pedido atual autoriza a execução do roteiro anterior. A direção usa a identidade existente do sistema: violeta, preto, tipografia técnica, formas geométricas e interferência breve. Formato de entrega escolhido para uso no computador: horizontal 16:9, 1920×1080, 30fps, MP4 H.264/AAC.

## Materiais e método

- Imagens: ferramenta integrada image_gen, uma ambientação abstrata para a abertura e uma prancha conceitual. Não usar geração externa paga.
- Storyboard técnico: quadros numerados derivados da composição final e de capturas da interface real.
- Tutorial: gravação de uma cópia isolada do OS, com evidências, nomes, respostas e áudios substituídos por exemplos fictícios antes da captura. O sistema de jogo não é alterado por essa preparação.
- Animação: composição local, manchetes em camadas, destaques de controles, cursor demonstrativo e transições breves.
- Voz: síntese local em português brasileiro; narração didática com pausas.
- Música: Long Note One, Kevin MacLeod, já licenciada para uso no projeto; atribuição incluída nos créditos e na documentação. Volume reduzido sob voz.
- Efeitos: cliques e interferências discretas sintetizados localmente. Não reproduzir os sons intensos da tela de falha durante o tutorial.

## Sequência planejada

| Cena | Tempo | Atenção visual e ação | Informação transmitida |
|---|---|---|---|
| 01 | 00:00–00:15 | Recortes de manchetes entram em camadas sobre instalação vazia e abstrata. | Houve um incidente; circunstâncias permanecem desconhecidas. |
| 02 | 00:15–00:30 | Manchetes se fragmentam; surgem blocos de dados incompletos. | Há registros danificados e um prazo para preservá-los. |
| 03 | 00:30–00:42 | Missão aparece em três ações: investigar, comparar, reconstruir. | A equipe deve resolver o mistério. |
| 04 | 00:42–00:55 | Gravação do desktop: abrir, minimizar e restaurar uma janela pela barra. | Como navegar pelos aplicativos. |
| 05 | 00:55–01:12 | Explorador: pesquisar, abrir documento fictício e ampliar. | Como consultar e comparar documentos. |
| 06 | 01:12–01:27 | Player: reproduzir exemplo neutro, pausar e deslocar a reprodução. | Como ouvir registros. |
| 07 | 01:27–01:45 | Chat: digitar pergunta genérica, aguardar resposta e destacar memória. | Como pedir ajuda à VIG.IA e acompanhar sua recuperação. |
| 08 | 01:45–02:02 | Registros: inserir exemplo fictício e usar Enter. | Como enviar conclusões e aproveitar orientações. |
| 09 | 02:02–02:13 | Etapa demonstrativa de cronologia: mover cartões com eventos sem relação com o caso. | Como ordenar e validar uma sequência. |
| 10 | 02:13–02:23 | Abrir Próximos passos.txt; destacar relógio e memória na barra. | Onde consultar o objetivo atual e acompanhar o prazo. |
| 11 | 02:23–02:30 | Encerramento com desafio e assinatura visual. | A investigação está pronta para começar. |

## Conteúdo protegido

Não exibir ou pronunciar respostas reais, credenciais, nomes dos personagens, código final, descrição do confronto, ordem correta ou horário de qualquer evento do caso. As telas de falha e a reconstituição final não aparecem. A demonstração de progresso deve ser genérica e não confirmar uma resposta real. Manchetes não atribuem culpa nem descrevem a mecânica do incidente.

## Entrega e revisão

Entregar MP4, storyboard em PNG, planejamento, legendas e fontes de montagem. Verificar duração, dimensões, decodificação integral, referências de mídia, recortes, legibilidade e ausência de conteúdo protegido. Registrar separadamente o que foi observado visualmente, analisado por ferramentas e o que não pôde ser ouvido ou reproduzido.


## Revisão 24/11/2026

Inserida cena de 16 segundos entre a missão e o tutorial digital: consultar o painel de funcionários, procurar pastas e crachá escondidos na sala e comparar os materiais físicos com os registros do OS. Ilustrações genéricas, sem dados ou esconderijos. Duração final: 2min46. Versão anterior preservada. Duas páginas de jornal A4 criadas para a abertura física da investigação.

## Revisão 3 - vídeo objetivo e jornais como imagens

Pedido: reduzir duração, retirar repetição e ampliar motion graphics e interações. Novo corte de 100 segundos, mantendo todos os aplicativos, investigação física, prazo, memória, anotações e desbloqueio. Preservadas as versões anteriores. Usadas gravações reais da cópia demonstrativa, com pausas finais retiradas, aproximação e retorno da câmera, textos de ação com entrada e saída, manchetes em camadas e rotação, animação independente dos materiais físicos e tipografia em sequência. Narração reescrita e sintetizada localmente, com redução de pausas antes do ajuste de tempo. Fonte: `video_dinamico.py`; roteiro vigente da revisão em `output/video_inicial/v3_dinamico/cenas.json`.

Jornais: duas páginas e uma folha de recortes geradas com image_gen integrada, em proporção A4, em vez de diagramação textual no PDF. Conteúdo conferido nas imagens, antes de montar o PDF. Imagens originais incorporadas com margem técnica de 5 mm, sem alegar resolução de 300 dpi e sem aumentar artificialmente a resolução. Estilo de jornal em papel claro, letras pretas, retícula e textura discreta. Sem uso de serviço externo pago.

## Revisão 4 - voz do sistema e papel branco

Voz identificada no manifesto do sistema: pt-BR-FranciscaNeural, rate +5%, pitch -2Hz. O usuário autorizou explicitamente o envio do roteiro ao serviço de voz da Microsoft. Geradas 12 falas, mantendo a montagem de 100 segundos e sem acrescentar chiado à locução didática. Versão de saída: `output/video_inicial/v4_francisca/VIGIA_OS_Tutorial_Francisca_v4.mp4`.

Os três jornais foram editados com image_gen para remover o papel envelhecido. Texto, colunas e ilustrações conferidos novamente. O PDF usa página RGB 255,255,255 e máscara de cor para eliminar os resíduos quase brancos do fundo. As três prévias renderizadas apresentam RGB 255 nos cantos; as fotografias mantêm os meios-tons originais. Saída: `output/pdf/jornais_investigacao/v3_fundo_branco/Kit_Jornais_e_Manchetes_A4_Branco.pdf`.
