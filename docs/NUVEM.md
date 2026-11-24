# Armazenamento na nuvem e publicação

## Configuração vigente

O projeto completo vai para o **repositório privado** [rpoless/vig.ia-os-escape-room](https://github.com/rpoless/vig.ia-os-escape-room). Isso inclui código, áudio, vídeo, impressos, cartaz, editáveis, gabarito documentado, referências, matrizes, ZIPs de identidade e histórico. A Vercel publica apenas o jogo em `dist/`, construído a partir de `public/`.

| Área | GitHub privado | Site para jogadores |
| --- | --- | --- |
| `public/` | Sim | Sim |
| `materiais/` | Sim | Não |
| `docs/`, `scripts/`, `tests/` | Sim | Não |
| `privado/` e suas fontes | Sim | Não |
| `dist/` | Recriada pelo build | Seu conteúdo é o site |
| Caches, temporários, `.env*` | Não | Não |

Os relatórios e as capturas relevantes da entrega estão preservados em `privado/verificacao/`. O diretório `.reports/` é a área de trabalho dos testes e pode conter caches; não precisa ser enviado. A cópia Python compilada em `__pycache__/` também é regenerável e fica fora do Git.

## O que o nome privado significa

`privado/` é uma divisão do projeto, não uma pasta com senha própria. Quem tiver permissão no repositório privado consegue consultar essa pasta. Em um repositório público, ela e seu histórico também seriam públicos. O campo `private: true` do `package.json` não muda a visibilidade do GitHub: selecione **Private** na própria configuração do repositório.

## O que fica fora do site

O `vercel.json` define `outputDirectory: dist`, e o build copia exclusivamente `public/`. Essa é a fronteira entre o material interno e as páginas dos jogadores. `.vercelignore` também lista a pasta da equipe, como exclusão adicional nos fluxos de envio que a utilizam. Não dependa somente do nome da pasta ou da regra de ignore para definir o conteúdo do site.

A integração com GitHub pode acessar o repositório autorizado para construir o site. Isso é diferente de disponibilizar todos os arquivos aos visitantes. Na Vercel, mantenha Root Directory na raiz, Build Command `npm run build` e Output Directory `dist`.

## Quando os arquivos realmente estão na nuvem

1. O repositório está configurado como **Private**.
2. Os arquivos foram incluídos em um commit.
3. O push terminou com sucesso para `origin/main`.
4. O commit aparece no GitHub, com `privado/` entre suas pastas.

Editar ou criar um commit local não envia arquivos por si só. Depois de cada mudança que deve ser preservada na nuvem, faça novo commit e push. O clone de outro computador recupera os arquivos versionados; `npm ci` e `npm run build` recriam a saída do site.

## Referências

- [Visibilidade dos repositórios do GitHub](https://docs.github.com/en/repositories/creating-and-managing-repositories/about-repositories).
- [Output Directory na Vercel](https://vercel.com/docs/builds/configure-a-build#output-directory).
- [Guia de publicação deste projeto](PUBLICACAO.md).
