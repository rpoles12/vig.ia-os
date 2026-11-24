# Repositório público e portfólio

O projeto é público em https://github.com/rpoless/vig.ia-os-escape-room para apresentar a experiência e seu processo de produção. Código, mídia, impressos, editáveis, histórico e gabarito documentado fazem parte do versionamento.

`acervo/` substitui o antigo nome `privado/` e reúne os bastidores com spoilers. Qualquer visitante do repositório pode consultar esse conteúdo. Os documentos históricos preservam decisões anteriores, que não representam a política atual.

O site da Vercel serve exclusivamente `dist/`, construída de `public/`. Acervo, documentos do portfólio e impressos estão no GitHub, sem aparecer na interface do jogo. `.vercelignore` lista as áreas excluídas nos fluxos que a utilizam; a fronteira de publicação é a pasta de saída do build.

Caches, temporários, dependências instaladas, saídas geradas e credenciais reais `.env*` continuam ignorados. O campo `private: true` em `package.json` evita publicação acidental no npm e não torna o GitHub privado.

Uma mudança fica na nuvem após commit e push. O responsável faz o envio pelo GitHub Desktop. Veja [Publicação](PUBLICACAO.md).
