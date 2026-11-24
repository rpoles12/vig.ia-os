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

## 2. Enviar pelo GitHub Desktop

O destino é o repositório público de portfólio [rpoless/vig.ia-os-escape-room](https://github.com/rpoless/vig.ia-os-escape-room). Os materiais de produção são públicos e o acervo contém spoilers do jogo.

1. Selecione a cópia local `vig.ia-os-escape-room` em Documents/GitHub no GitHub Desktop.
2. Revise as alterações, crie o commit e use **Push origin**.
3. Confira no GitHub se aparecem o README, os prints, os vídeos e a pasta `acervo/`.

Não é necessário tornar o repositório privado. A pasta `acervo/` e os ZIPs de fontes são versionados normalmente; apenas caches, temporários, saídas geradas e credenciais reais ficam ignorados. A pasta do Desktop anteriormente usada foi movida pelo responsável para esta cópia local; use o repositório atual.

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
- Tentar `/README.md`, `/materiais/` ou `/acervo/` não fornece os arquivos da entrega local.
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
| Guia da equipe não veio no clone | Confira se foi enviado o commit que inclui `acervo/` e se a cópia está na branch `main` atualizada. |

## Limite da arquitetura

As validações e os códigos dos controles estão no cliente. Publicar somente `dist/` mantém os documentos da equipe fora do site, mas **não torna o gabarito do JavaScript secreto**. Uma versão com verificação protegida, placar ou progresso entre computadores exigiria um backend e outra arquitetura. Isso não é necessário para hospedar esta versão escolar.
