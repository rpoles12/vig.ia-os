# VIG.IA OS v2 — revisão de navegação

Abra index.html na pasta completa do sistema. Não é necessária instalação ou conexão à internet.

## Aplicativos e barra

O desktop contém somente atalhos maiores e uma Lixeira vazia. Todos os aplicativos também ficam na barra inferior: Arquivos, VIG.IA, Registros, Áudios, Notas e Lixeira. A barra reúne tempo até o apagamento, memória recuperada, mini-player, efeitos e horário do computador.

Próximos passos.txt é o bloco de notas da investigação. Seu conteúdo muda automaticamente conforme as etapas são concluídas. Os lembretes também acompanham a fase atual.

## Investigação

Arquivos apresenta blocos com prévias reais das evidências. Um clique abre o documento em janela auxiliar, com zoom e atalhos de consulta. A navegação de pastas tem ícones, busca e filtros. Arquivos ainda bloqueados permanecem no filtro Corrompidos; não há atalhos decorativos deles no desktop.

Registros reúne identidade, acessos, cronologia e conclusões. A cronologia aparece no próprio aplicativo na etapa correspondente, mantendo arrasto e alternativas por clique e teclado. Enter envia os campos.

A VIG.IA funciona como conversa: perguntas à direita e respostas à esquerda, com avatares. O campo de mensagem permanece no rodapé da janela enquanto a conversa rola. Os exemplos mudam com a etapa. Memória e capacidades ficam disponíveis no cabeçalho; documentos indicados podem ser abertos pela própria resposta.

## Janelas

As janelas são independentes. Um clique na barra abre ou traz o aplicativo à frente; clicar no aplicativo já ativo o minimiza. Os indicadores mostram quais estão abertos. O botão com quatro quadrados abre o menu Iniciar. Nele, Mostrar área de trabalho recolhe todas as janelas.

Arraste a barra de título para mover. Use o canto inferior direito para redimensionar. O botão de maximização ou o duplo clique no título alterna entre tamanho normal e maximizado. Minimizar e restaurar preserva posição, tamanho, campos, conversa e rascunhos durante a rodada. Fechar também conserva o conteúdo até o reinício da rodada.

As transições têm animações de entrada, saída e minimização. A preferência de movimento reduzido do dispositivo é respeitada.

## Regras preservadas

Padrão: 12:30 iniciais; +15s únicos para identidade, acessos e cronologia, com aviso breve sem botão. Memória8/34/67/100 e catálogo8/23/24/25. As respostas corretas valem sem leitura obrigatória.

Conclusões corretas contêm o apagamento, mostram a chave por30s para anotação, ocultam a chave e abrem a entrada do código. O acerto libera automaticamente o filme. Ao esgotar o prazo da investigação, permanece a tela de falha de transmissão com efeito sonoro.

Reiniciar no painel da equipe limpa a investigação e as janelas. Recarregar a página também inicia nova rodada; o estado não persiste após fechar ou recarregar o navegador.

105 verificações automatizadas aprovadas e percurso de navegação conferido no navegador. A política do navegador de teste bloqueia a abertura file://; conferir a abertura direta e o som no computador definitivo.


## Player da barra e cursores

O player rápido tem play/pausa, nome do fragmento, posição/duração e barra para avançar ou voltar. Clique no nome para abrir o player completo. O botão de três pontos reúne volume, silenciar/reativar e transcrição. Escape ou clique fora fecha o menu. Os efeitos sonoros continuam com controle próprio.

O OS utiliza11 cursores PNG transparentes em assets/os/cursors, incluindo clique, texto, arrasto, redimensionamento, indisponível, carregamento, zoom e ajuda. Cada imagem tem32x32px e ponto ativo explícito; os cursores nativos ficam como alternativa caso uma imagem não carregue. A prévia e o manifest com os pontos ativos acompanham os PNGs.


## Menu Iniciar

O botão de quatro quadrados da barra abre o menu Iniciar do VIG.IA OS. Ele reúne os aplicativos e a opção Continuar investigação, que acompanha a fase atual e abre Registros na resposta correspondente. A memória é atualizada no cabeçalho. Mostrar área de trabalho recolhe as janelas preservando seu conteúdo. Clique fora ou pressione Escape para fechar o menu. O menu fica indisponível durante as telas de bloqueio e encerramento.


## Trilha ambiente

Long note One, de Kevin MacLeod (incompetech.com), acompanha a partida inteira em loop. A música é iniciada pelo botão Iniciar investigação e não troca ao avançar de fase. Volume padrão40%; durante narrações ou vídeos, o volume da trilha cai para12% desse valor (4,8% de volume final), com redução rápida e retorno suave ao pausar ou terminar a fala. Áudios sobrepostos mantêm a redução até que todos parem. O efeito de falha da tela de falha de transmissão também reduz temporariamente a trilha.

O menu de três pontos do player contém controles separados de narração e trilha ambiente. Silenciar uma trilha não silencia a outra. Reiniciar a rodada interrompe a música e a leva ao início, preservando a preferência de volume; a próxima partida começa com a mesma faixa.

A faixa está incorporada em audio/trilha/long-note-one.mp3 e funciona offline. Créditos e licença CC BY4.0 estão no menu de áudio, em audio/trilha/CREDITOS.md e em licenca.json. Fonte oficial: https://incompetech.com/music/royalty-free/index.html?isrc=USUAN1100418 . Arquivo original preservado; apenas loop e volume são aplicados na reprodução.


## Ícones, botão direito e tela de falha de transmissão

Os atalhos do desktop encaixam em uma grade automática invisível, inclusive durante o arrasto. Ao mover para uma célula ocupada, os dois atalhos trocam de posição, sem sobreposição. A grade se adapta ao tamanho da tela e reorganiza células que deixarem de caber. Esc cancela o arrasto e restaura as posições anteriores. Soltar um ícone após arrastar não abre seu aplicativo; um clique continua abrindo normalmente. As posições ficam apenas na memória da partida, são preservadas ao alternar entre aplicativos e voltam ao padrão ao reiniciar ou recarregar. Os ícones ficam limitados à área acima da barra de tarefas.

O botão direito no desktop abre um menu com Abrir Arquivos (ou o aplicativo do ícone selecionado), Próximos passos.txt, Registrar respostas, Organizar ícones e Atualizar área de trabalho. Atualizar preserva o tempo e o progresso. Shift+F10 abre o mesmo menu quando um atalho está em foco; setas navegam e Esc fecha.

Ao esgotar o prazo, aparece a pane catastrófica descrita abaixo, com vidro trincado, erros de transmissão e três efeitos do Pixabay em repetição contínua. A tela é uma sobreposição persistente. Esc não a fecha; os atalhos e as janelas do OS ficam bloqueados. Somente o painel autenticado da equipe pode autorizar continuação ou reiniciar a rodada. O padrão de produção é 12:30 e +15s por etapa; a engrenagem inicial permite alterar esses valores para a sessão.

## Configurações desta sessão

Antes de iniciar, use a engrenagem no canto superior direito da apresentação. Login: admin. Senha: verset.dev. Fechar e reabrir exige autenticação novamente.

O modal permite definir minutos (0–180) e segundos (0–59), com duração mínima de 1 segundo; ativar ou desativar bônus e escolher de 0 a 300 segundos por etapa; ativar ou desativar a reprodução automática da mensagem inicial e os alertas sonoros de contagem. Os bônus continuam únicos para identidade, acessos e cronologia. Os demais fragmentos continuam disponíveis no player e nas transcrições. Desativar alertas de tempo não desativa o som da falha final.

Salvar aplica a configuração à rodada e atualiza a introdução, o cronômetro, o aviso de bônus e as respostas da VIG.IA sobre tempo. Lembretes são proporcionais à duração escolhida. Fechar sem salvar descarta as alterações. Restaurar padrão preenche os valores originais; Salvar confirma.

As configurações ficam somente na memória desta página. Reiniciar a investigação pelo painel mantém esses valores até recarregar. Recarregar ou reabrir a página restaura 12:30, bônus ativo de 15 segundos, mensagem inicial automática e alertas de contagem ligados. A chave final continua com 30 segundos independentes para anotação.
## Rodadas adaptadas por público

No modal da engrenagem, as caixas Identidade, Acessos, Cronologia e Conclusões finais permitem incluir ou excluir etapas. É preciso manter ao menos uma. O padrão mantém as quatro selecionadas e é restaurado ao recarregar. Login e senha continuam os mesmos.

A rodada começa na primeira etapa selecionada e pula as desmarcadas ao avançar. Etapas dispensadas não exigem respostas e não dão bônus. Os arquivos necessários às etapas ativas são liberados automaticamente; Registros, Próximos passos.txt, os lembretes e a VIG.IA acompanham o percurso escolhido. O resumo das configurações calcula o máximo de bônus apenas pelas etapas selecionadas de identidade, acessos e cronologia.

Em rodadas reduzidas, a memória parte de 8% e cresce proporcionalmente às etapas resolvidas, chegando a 100% ao terminar. Na rodada completa, mantém os valores anteriores. As gravações originais continuam no player com aviso de que podem citar etapas da investigação completa. Para evitar orientações incompatíveis, a reprodução automática desses fragmentos fica restrita à rodada completa; na rodada reduzida, use as orientações em texto e a VIG.IA.

Se Conclusões finais estiver desmarcada, concluir a última etapa escolhida gera automaticamente a mesma chave BA17-2847-2246. Com essa etapa marcada, suas três respostas continuam obrigatórias. Em ambos os casos, permanecem a anotação da chave por 30 segundos, a inserção do código e a recapitulação.

Exemplos: Identidade + Conclusões finais elimina as correlações de acesso e o arrasto cronológico; somente Acessos encerra o enigma após os dois nomes; somente Conclusões finais abre diretamente os três campos finais, com todos os documentos disponíveis.
## Pane catastrófica após o fim do tempo

A tela de encerramento não apresenta título, painel central ou mensagem de Sinal perdido. Exibe diretamente vidro trincado sobre a área inteira, manchas de LCD, faixas corrompidas, ruído, binários e 32 blocos de erros de transmissão em movimento. Uma descrição escondida visualmente continua disponível para leitores de tela. Esc não fecha a pane e o OS permanece bloqueado.

Três MP3s originais do Pixabay compõem o áudio contínuo: TV Static Noise (Universfield), Glass Cracking (DRAGON-STUDIO) e Electric Hum (SoundsForYou). Os três ficam em repetição enquanto a pane estiver aberta; chiado e zumbido sustentam a base constante e a trinca curta se repete. O efeito sintético anterior foi substituído. Não há encerramento automático do som após alguns segundos.

Os áudios ficam incorporados em audio/failure, com fontes, licença e hashes em CREDITOS.md e licenca.json. O botão geral de efeitos sonoros é respeitado. A trilha ambiente abaixa enquanto os efeitos tocam. Autorizar continuação ou reiniciar pelo painel autenticado para e rebobina os três canais. Abrir o painel sem encerrar a pane mantém o som.

A imagem transparente fica em assets/os/failure/cracked-glass-v1.png. GERACAO.md registra a ferramenta nativa, o prompt completo e a cópia do original. A animação pausa quando a página não está visível, sem interromper os sons da pane; a preferência de movimento reduzido é respeitada.