# GitHub → Vercel

Viabilidade conferida em 24/11/2026 nas documentações oficiais da [Vercel](https://vercel.com/docs/builds/configure-a-build) e do [GitHub](https://docs.github.com/en/repositories/working-with-files/managing-large-files/about-large-files-on-github).

## O que está preparado

O site é estático: HTML, CSS, JavaScript e mídia local. A Vercel aceita a importação de um [repositório do GitHub](https://vercel.com/docs/git/vercel-for-github). O preset é Other, com Node 24.x durante a construção. O navegador não depende de Node depois da publicação.

`npm run build` verifica as referências do sistema e copia apenas `public/` para `dist/`. Não há Functions, banco de dados, pagamento, variáveis secretas ou instalação de uma API de IA. O projeto não depende de `next`, `vite` ou outro framework para ser publicado.

## 1. Conferir localmente

Abra o terminal na raiz **o-arquivo-corrompido**, onde estão `package.json` e `vercel.json`:

```bash
npm ci
npm test
npm run build
npm run preview
```

Abra `http://127.0.0.1:4173`. Confira o vídeo inicial, um documento, um fragmento de áudio e as configurações. Os testes automáticos não substituem ouvir as caixas de som na sala.

## 2. Enviar para o GitHub

O destino informado pelo responsável é [rpoless/vig.ia-os-escape-room](https://github.com/rpoless/vig.ia-os-escape-room). Mantenha a visibilidade **Private** antes de enviar: `privado/` agora faz parte do versionamento, incluindo gabarito, fontes, histórico e editáveis. Repositório privado limita o acesso a esse material; não esconde o JavaScript que o site entrega aos jogadores. O Git local já foi iniciado em `main`; confira `git status`.

### Pelo GitHub Desktop

1. No GitHub, confirme que o repositório de destino está como **Private**. Ele estava público na última conferência; a preparação local não altera essa configuração.
2. No GitHub Desktop, use **File → Add local repository** e selecione a pasta final `O_Arquivo_Corrompido` do Desktop, onde estão `README.md` e `package.json`.
3. Confira que o remoto `origin` é `https://github.com/rpoless/vig.ia-os-escape-room.git` e a branch é `main`.
4. Envie o commit preparado usando **Push origin** ou **Publish branch**, conforme a opção exibida. As fontes e os materiais de `privado/` estão incluídos; caches e saídas geradas continuam ignorados.
5. Abra o repositório no GitHub e confirme que o commit e a pasta `privado/` aparecem. Só depois o backup foi enviado à nuvem.

Se o GitHub Desktop já estiver mostrando outra cópia local do repositório, selecione a pasta final acima para enviar esta entrega. Não é necessário arrastar arquivos no site nem copiar tudo para dentro de `public/`.

### Pelo terminal, como alternativa

Se a pasta ainda não possuir repositório:

```bash
git init -b main
```

Prepare a versão local e confira a seleção antes de enviá-la:

```bash
git add .
git status
git commit -m "Organiza entrega final do Arquivo Corrompido"
```

Se a entrega já tiver um commit inicial, não será necessário criar outro sem mudanças. Se o Git pedir identificação, configure seu nome e email próprios antes do commit. Não use uma identidade inventada.

Depois, substitua o endereço pelo repositório que você criou:

```bash
git remote add origin https://github.com/rpoless/vig.ia-os-escape-room.git
git push -u origin main
```

Se já existir `origin`, confira `git remote -v` antes de alterá-lo. GitHub Desktop também pode publicar a pasta existente. Não selecione a pasta acima desta entrega, pois ela contém arquivos de trabalho e versões anteriores.

**`privado/` está incluída no Git normal, sem forçar arquivos ignorados.** Ela contém narrativa, gabarito, credenciais de interface, históricos e editáveis. Os ZIPs de fontes dentro dela também são versionados. Mantenha o repositório **Private**: se ele se tornar público, qualquer visitante poderá consultar os materiais e o histórico. Nenhum desses arquivos é copiado para `dist/`. Veja [Backup na nuvem](NUVEM.md).

O maior arquivo atual tem menos de 100 MiB, limite individual para Git comum. O PDF do cenário excede o limite de 25 MiB do upload pelo navegador do GitHub: envie por Git ou GitHub Desktop. Git LFS não é necessário para os arquivos atuais. O limite de upload da CLI da Vercel é um fluxo diferente; a implantação planejada usa integração com GitHub.

## 3. Importar na Vercel

1. Entre na sua conta Vercel e escolha **Add New → Project**.
2. Conecte o GitHub, autorize o acesso ao repositório escolhido e selecione **Import**.
3. Selecione **Other** e mantenha **Root Directory = raiz (`.`)**.
4. Confirme **Build Command = `npm run build`**, **Output Directory = `dist`**, **Node = 24.x**. O arquivo `vercel.json` já define build e saída; `package.json` fixa a linha do Node.
5. Não adicione variáveis de ambiente: esta versão não usa nenhuma.
6. Faça o deploy e teste a URL gerada no computador da escola.

As opções disponíveis e cotas dependem da conta. Publicar em uma conta ou criar o repositório não foi executado por esta organização local.

## 4. Conferir a primeira URL

- `/` apresenta a preparação da rodada.
- O primeiro vídeo termina antes de o tempo começar.
- Documentos, áudio, cursores e a reconstituição carregam sem erro.
- Tentar `/README.md`, `/materiais/` ou `/privado/` não fornece os arquivos da entrega local.
- Em **Deployments**, a produção corresponde ao commit esperado. Previews de branches servem para revisão antes de levar mudanças à produção.

O `vercel.json` adiciona headers de revalidação de cache para reduzir versões antigas, tipagem estrita de arquivos e orientação para os buscadores não indexarem o jogo. A orientação de não indexação não restringe acesso; qualquer pessoa com o link pode abrir a página, conforme as opções da conta Vercel.

## Atualizar depois

Edite os arquivos de `public/`, execute testes e build, faça commit e push. A integração dispara uma nova implantação. Não edite `dist/`: ela é descartável e será recriada. Evite renomear arquivos de mídia sem atualizar todas as referências; a hospedagem diferencia letras maiúsculas e minúsculas.

## Solução de problemas

| Sintoma | Conferência |
| --- | --- |
| 404 na página inicial | Root Directory na raiz e Output Directory `dist`; build deve terminar com sucesso. |
| Vídeo ou áudio sem som | Clique real em Iniciar, volume do navegador/Windows, permissões e arquivo completo no Git. |
| Documento funciona no Windows e falha na Vercel | Verifique maiúsculas/minúsculas; execute `npm run check`. |
| Alteração não aparece | Aguarde o deploy concluir, abra a URL do deploy novo e recarregue; evite atualizar durante uma rodada. |
| Configuração voltou ao padrão | Comportamento esperado ao recarregar; prepare a sessão antes de cada grupo. |
| Sem internet na escola | Use a cópia completa de `public/` localmente; visitar uma vez o site não garante cache offline. |
| Guia da equipe não veio no clone | Confira se foi enviado o commit que inclui `privado/` e se a cópia está na branch `main` atualizada. |

## Limite da arquitetura

As validações e os códigos dos controles estão no cliente. Publicar somente `dist/` mantém os documentos da equipe fora do site, mas **não torna o gabarito do JavaScript secreto**. Uma versão com verificação protegida, placar ou progresso entre computadores exigiria um backend e outra arquitetura. Isso não é necessário para hospedar esta versão escolar.
