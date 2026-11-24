# Arquitetura e manutenção

## Estrutura em execução

`public/index.html` é a entrada. Scripts clássicos compartilham os objetos `window.CASE_DATA`, `VigiaEngine`, `VigiaAssistant` e os controladores de interface. Preserve a ordem das tags do HTML. Não é uma aplicação React e não exige compilação de componentes.

| Arquivo / área | Responsabilidade |
| --- | --- |
| `data.js` | Catálogo, cartões e parâmetros internos do caso; contém respostas no cliente. |
| `engine.js` | Regras, validação de etapas, memória e estado da investigação. |
| `vigia.js` | Interpretação local das perguntas, níveis de memória, dicas e destinos sugeridos. |
| `countdown.js` | Duração, bônus únicos e eventos de aviso/expiração. |
| `session-settings.js` | Configuração da rodada e seleção de etapas; apenas memória da página. |
| `intro-video.js` | Primeiro vídeo obrigatório, bloqueio do relógio e replay. |
| `app.js` | Coordenação do jogo, formulários, catálogo, áudio, código e controles da equipe. |
| `desktop.js` / `desktop.css` / `os-v2.css` | Área de trabalho, apps, chat, explorador, janelas e barra de tarefas. |
| `desktop-interactions.js` | Grade invisível, arrasto, persistência de posições na sessão e menu de contexto. |
| `icons.js` / `cursors.css` / `assets/os/` | Ícones, imagens do OS, cursores e recursos visuais. |
| `ambient.js` / `ambient.css` | Trilha contínua, redução de volume durante voz/vídeo e controles. |
| `catastrophic-failure.js` / `.css` | Corrupção visual, trincas, canvas e áudio da expiração. |
| `feedback.js` | Feedbacks e apoio à apresentação das respostas. |
| `encerramento/filme/` | Reconstituição com imagens, dados de cenas e sincronização com a voz. |
| `audio/`, `video/`, `evidencias/` | Arquivos locais de mídia e documentos. |

Há arquivos de estilos e implementação de iterações anteriores preservados para compatibilidade. A lista de scripts e folhas efetivamente carregados está em `index.html` e no HTML da reconstituição. Esta consolidação não substituiu o motor do jogo nem redesenhou a interface.

## Estado e tempo

O motor mantém flags de etapas, documentos consultados, tentativas incorretas e memória. Ler um documento não é pré-condição para acertar. A seleção de etapas é resolvida antes da rodada; etapas desmarcadas são avançadas sem exigir resposta. Na configuração completa, os percentuais são 8 → 34 → 67 → 67 → 100. Nos modos reduzidos, o percentual representa as etapas escolhidas.

O relógio de investigação só é iniciado no término real do primeiro vídeo. Vozes, consulta à VIG.IA e replay do MP4 não suspendem a investigação. A exibição da chave tem um relógio próprio de 30 segundos. A reconstituição usa outro controle de reprodução. Evite unir esses relógios em uma alteração futura.

Recarregar cria uma nova rodada e restaura configurações. A página usa estado local e marcadores de sessão; não há armazenamento de partidas em servidor. O reinício pelos controles da equipe limpa o progresso e exige novamente o primeiro vídeo; a equipe deve conferir as configurações antes do próximo grupo.

## Mídia e voz

O vídeo inicial é `video/Video_inicial.mp4`. A voz aprovada é **pt-BR-FranciscaNeural**. Sua geração histórica foi autorizada pelo usuário; o jogo reproduz os arquivos já gerados e não envia roteiro a serviços de voz em execução.

Os três fragmentos são `audio/audio01.wav`, `audio02.wav` e `audio03.wav`. A narração final é `audio/final_completo.wav`; o player de reconstituição e o controlador principal sincronizam o estado por mensagens locais. A trilha fica em `audio/trilha/`; efeitos contínuos, em `audio/failure/`. Recursos antigos segmentados foram conservados na entrega para não quebrar compatibilidade.

O modo de trilha reduzida acompanha fala e vídeo. Alterações de volume devem ser avaliadas ouvindo a sala: medição ou teste automático não confirma conforto e inteligibilidade no equipamento real.

## Construção e publicação

`scripts/check.mjs` verifica arquivos referenciados, capitalização exata, parâmetros de publicação e tamanho individual. `scripts/build.mjs` remove somente a saída `dist/` dentro desta raiz e a recria com `public/`. O build não lê a pasta da equipe, não transforma mídia e não depende de ferramentas de produção antigas.

O servidor local implementa MIME, HEAD e intervalos de bytes para testar MP4 e áudio pelo navegador. Escuta em `127.0.0.1` na porta 4173 por padrão. `npm run preview` usa `dist/`, enquanto `npm start` usa `public/`. A Vercel usa a sua própria entrega estática em produção.

## Fronteira de publicação

| Área | GitHub | Site na Vercel |
| --- | --- | --- |
| `public/` | Sim | Sim, copiada para `dist/` |
| `materiais/` | Sim | Não |
| `docs/`, `tests/`, `scripts/` | Sim | Não; apenas scripts necessários participam do build |
| `acervo/` | Sim, em repositório **Public** | Não |
| `dist/`, `.reports/`, `.env*` | Não | `dist/` é gerada no build; relatórios e ambiente não são publicados |

As respostas necessárias à validação continuam em `public/data.js` e no motor. A fronteira acima separa documentos e produção; ela não oferece sigilo contra inspeção do aplicativo.

## Como alterar com segurança

1. Modifique `public/` e os documentos vigentes relacionados.
2. Ao mudar conteúdo do caso, confira consistência com impressos, transcrições, dicas e narrativa final.
3. Execute testes e build. Para mudanças no fluxo de vídeo, janelas ou expiração, execute também o teste de navegador.
4. Revise a versão servida por `npm run preview`.
5. Faça commit e push somente depois da conferência; não publique durante uma rodada em andamento.

Os editáveis e scripts históricos estão em `acervo/fontes/` e acompanham o repositório público. Alguns dependem de caminhos e ferramentas do ambiente de produção original. Eles são arquivos de origem e histórico, não dependências para jogar ou publicar.
