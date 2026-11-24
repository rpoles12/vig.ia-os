# Testes e homologação

## Conferências reproduzíveis

Use Node 24 na raiz da entrega:

```bash
npm ci
npm test
npm run check
npm run build
```

Não é necessário baixar bibliotecas para as verificações padrão. Os testes exercitam progressão, respostas corretas sem leitura obrigatória, tentativas erradas, bônus únicos, limites do relógio e todas as 15 combinações não vazias de etapas. Também conferem a estrutura de publicação, referências com capitalização exata e o servidor HTTP, incluindo vídeo por intervalos de bytes.

O workflow do GitHub repete instalação, testes e build no Linux, onde diferença entre maiúsculas e minúsculas afeta os caminhos. Não marque uma publicação como concluída apenas porque o build local passou: o endereço real precisa ser aberto depois do deploy.

## Navegador, opcional

O teste visual requer Google Chrome e Playwright. Se não estiverem disponíveis no ambiente de desenvolvimento, instale temporariamente:

```bash
npm install --no-save --package-lock=false playwright@1.62.1
npm run build
npm run test:browser
```

A instalação temporária não muda o pacote da hospedagem. O teste inicia o próprio servidor de `dist/`, abre Chrome sem janela e verifica vídeo inicial, início do relógio, replay, janelas, configurações, fluxo completo de respostas, chave, inserção, reconstituição e expiração. A reprodução do primeiro vídeo é acelerada apenas durante a verificação; o fluxo continua esperando seu término real. Relatórios e capturas ficam em `.reports/` e são ignorados pelo Git.

## Conferência humana na escola

- Imprimir uma prova, conferir tamanho real e orientar A4/A3 corretamente.
- Montar o painel, esconder pastas e crachá, disponibilizar papel e caneta.
- Ajustar a sessão pela engrenagem e conferir as etapas selecionadas.
- Usar mouse e teclado reais para abrir documentos, arrastar cartões e acionar Enter nas respostas.
- Ouvir narração, fragmentos, música reduzida durante voz/vídeo e efeitos da expiração no volume escolhido para a sala.
- Concluir uma rodada, anotar o código e assistir à reconstituição.
- Em outra rodada curta, deixar o tempo terminar e confirmar que Esc não devolve a área de trabalho.
- Reiniciar para o próximo grupo e confirmar novamente tempo, etapas e som.

Som, conforto visual, legibilidade das impressões e qualidade das pistas para o público dependem dessa prova presencial. A conferência automatizada verifica funcionamento e carregamento, não substitui a experiência real.

## Resultado desta entrega · 24/11/2026

- **25 testes automáticos passaram**, incluindo as 15 combinações de etapas, progressão, bônus, servidor HTTP e links da documentação.
- **64 verificações no Chrome passaram**, cobrindo o primeiro vídeo até o fim real, início da contagem, replay, janelas, Enter, ajuda após erros, ordenação, exibição de 30s, chave correta/incorreta, reconstituição e expiração.
- **Nenhum erro de execução da página nem carregamento HTTP malsucedido** foi registrado nessa rodada de navegador.
- Os PDFs foram conferidos: 9 páginas A4 horizontais no cenário, 6 A4 verticais nos documentos, 3 A3 verticais nos jornais e 1 A4 vertical no cartaz.

Esses resultados se referem à cópia local servida por HTTP. A conferência da URL real na Vercel e da sala continua sendo uma etapa posterior à publicação na conta do responsável.
