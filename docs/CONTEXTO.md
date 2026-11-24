# Contexto e continuidade do projeto

**Referência vigente: entrega consolidada de 24/11/2026.** Este documento descreve o projeto sem revelar as soluções. A narrativa integral, as credenciais de interface e o gabarito estão em `privado/`, incluída no repositório **privado** e excluída da saída do site.

## Objetivo

Projeto escolar de escape room com investigação presencial e digital. O participante usa um computador fictício para relacionar vestígios físicos e registros, em vez de apenas preencher um questionário. A identidade visual combina roxo, preto, branco, linguagem de computador e falhas de transmissão. A marca de produção é 7set.dev, e a assistente se chama **VIG.IA**.

O evento informado para a divulgação é **03/12, das 7h às 15h**. Nenhum ano foi acrescentado ao cartaz. O nome da escola aparece em materiais históricos de apresentação; a documentação técnica não presume sala, endereço ou URL ainda não fornecidos.

## Decisões vigentes

- Navegação principal como área de trabalho de computador, com atalhos, lixeira, menu iniciar, menu de contexto, janelas e barra de tarefas.
- A cronologia é uma etapa do app Registros. Orientações da próxima correlação ficam em um arquivo de anotações que evolui com o progresso.
- Explorador com blocos de prévia e abertura de documentos em janela; chat com mensagens dos dois lados e indicador de digitação.
- Ícones maiores, barra de tarefas com ícones sem títulos, relógio e memória na própria barra. Posições de atalhos duram somente a sessão, com grade invisível e sem sobreposição.
- VIG.IA local mais capaz conforme a memória, com caminhos para evidências e orientação ligada à etapa. Acertar sem abrir documentos continua válido.
- Duração e bônus configuráveis antes do início; seleção de uma ou mais etapas para adaptar o público. Valores voltam ao padrão ao recarregar.
- Primeiro vídeo obrigatório antes do relógio; replay acessível como MP4 no OS. O vídeo menciona o painel, as pastas e o crachá, sem antecipar soluções.
- Voz aprovada: Francisca Neural. Tutorial mais curto e com movimento; versão atual de aproximadamente 1min40s.
- Uma mesma música de suspense em toda a investigação, com redução durante áudio/vídeo. Efeitos de falha contínuos no fim do tempo.
- Falha final com corrupção, trincas, binários e cursor invisível. Não usar a antiga tela azul nem o título “sinal perdido”.
- Chave final exibida uma vez por até 30s para copiar no papel; depois, terminal de inserção e reconstituição automática.
- Seis documentos complementares impressos e jornais com fundo branco. PDF final dos jornais: **três folhas A3, sem cópias extras**. A folha de manchetes permanece entre as três: não houve instrução posterior para removê-la.
- Cartaz de divulgação final em PNG, com PDF A4 como versão para impressão.

## Evolução resumida

| Fase | Resultado |
| --- | --- |
| Investigação inicial | Definição do caso, personagens, pistas físicas e validações digitais. |
| Aprimoramento do enigma | Pistas de horário interpretativas, ajuda após erros, código de recuperação e encerramento narrado. |
| Acessibilidade da condução | Bônus, Enter nos formulários, orientações e seleção de etapas. |
| Reestruturação aprovada | Troca da página de navegação por área de trabalho e aplicativos do VIG.IA OS. |
| Som e interação | Cursores próprios, trilha ambiente, janelas, menu iniciar, grade e expiração com corrupção. |
| Tutorial e impressos | Tutorial com voz aprovada e jornais gerados como imagens com fundo branco em PDF A3. |
| Fluxo final do participante | Preparação da equipe → boas-vindas → vídeo → OS com contagem → código → reconstituição. |
| Entrega de 24/11/2026 | Pasta autônoma, documentação reescrita, testes, build estático e configuração GitHub/Vercel. |

## Fontes de verdade

1. As instruções atuais do responsável pelo projeto orientam novas alterações.
2. O comportamento entregue pode ser conferido em `public/` e nos testes.
3. README, `docs/` e o novo guia da equipe descrevem a versão consolidada.
4. `privado/historico/` conserva versões anteriores para rastreabilidade. Elas contêm decisões superadas e não devem orientar implementação sem comparação com os itens acima.

Não concatenar novas regras ao fim de um manual antigo mantendo instruções conflitantes no início. Reescreva as seções afetadas e registre a mudança no changelog.

## Continuidade por outra pessoa ou ferramenta

Comece pelo README, pelo guia do jogo e pela arquitetura. Para alterar o enigma, leia o guia da equipe em `privado/`. Um clone atualizado do repositório privado inclui gabarito documentado, históricos e matrizes de impressão. Apenas pessoas com acesso ao repositório devem consultar esses materiais. Preserve a relação entre narrativa, documentos, horários e reconstituição. O relatório de inventário local registra os arquivos de origem e as novas divisões.

## Pendências externas à entrega local

- Enviar os commits ao repositório informado pelo responsável, confirmando primeiro a visibilidade Private: `rpoless/vig.ia-os-escape-room`.
- Importar na Vercel e conferir a primeira URL de produção, inclusive permissões da conta.
- Fazer uma rodada completa no computador da escola e conferir volume, impressão, montagem da sala e tempo real de troca entre grupos.
- Informar sala/endereço ou instruções adicionais se forem desejados em uma futura edição do cartaz.

O repositório de destino é `https://github.com/rpoless/vig.ia-os-escape-room`. A URL de produção depende da importação na Vercel. O estado de sincronização deve ser conferido no Git, não presumido a partir desta documentação. Evoluções como placar, sincronização entre computadores e respostas protegidas por servidor são novas funcionalidades, fora da arquitetura estática atual.
