# Continuidade integral · responsável e manutenção

O ponto de partida é a raiz desta entrega, não `output/vigia_os_sistema` nem o pacote anterior no Desktop. O código mantido agora está em `public/`. A entrega foi consolidada em 24/11/2026 para envio por Git e publicação pela integração GitHub → Vercel.

Leia primeiro `README.md`, `docs/CONTEXTO.md`, `docs/ARQUITETURA.md` e `privado/equipe/GUIA_DA_EQUIPE.md`. O guia da equipe contém a narrativa consolidada, as respostas e as distinções entre invasor, colaborador e responsável pelo empurrão. O catálogo extraído do código acompanha o guia como JSON.

## Conteúdo preservado

- Todos os arquivos do pacote anterior foram copiados para as divisões desta entrega; o inventário local registra a correspondência. Os manuais antigos foram arquivados para evitar instruções conflitantes na documentação vigente.
- Os três PDFs de impressão atuais estão em `materiais/impressao/`. O cartaz final datado está em `materiais/divulgacao/`, com PNG principal e PDF A4.
- Retratos dos nove personagens fictícios, prompts e galeria estão em `fontes/retratos_personagens/`.
- Matrizes individuais, dados internos, documentos complementares, fontes e revisão de fotos estão em `fontes/producao_e_editaveis/`.
- Identidade, telas e cartazes de produção estão em `fontes/identidade_visual/`.
- Scripts históricos estão em `fontes/scripts_historicos/`; podem depender dos caminhos originais do ambiente. O build da Vercel não depende deles.
- A produção do tutorial aprovado está em `fontes/video_inicial/`, incluindo cenas, narração e quadros de storyboard. O MP4 não foi duplicado: a cópia aprovada está em `public/video/Video_inicial.mp4` na raiz da entrega.
- As imagens dos jornais com fundo branco estão junto do PDF final em `materiais/impressao/03_jornais/imagens/`; seus registros de geração ficam em `fontes/jornais/`.
- O planejamento aprovado do OS, suas referências e o PDF de apresentação visual foram preservados em `historico/planejamento_os/`. Eles documentam a concepção; ajustes posteriores estão descritos em `docs/CONTEXTO.md`.
- Documentação anterior e apresentação ficam em `historico/`, com possíveis decisões superadas. Elas são contexto, não especificação vigente.

## Regras para continuar sem regressão

Preservar o tutorial antes do relógio, a chave em exibição temporária antes da inserção e o vídeo narrado de encerramento após o código. Não voltar ao fluxo antigo que exibia direto a inserção, exigia abrir documentos para aceitar respostas ou retornava ao OS com Esc após a expiração.

Preservar a seleção de etapas, as 15 combinações válidas, os bônus únicos e o reset ao recarregar. Não criar persistência permanente de configurações ou de ícones sem uma nova decisão do responsável.

Preservar o nome VIG.IA, o chat progressivo, a mesma trilha ao longo da investigação, o volume reduzido durante áudio/vídeo, os cursores e a identidade roxa. A antiga tela azul e versões com o texto “sinal perdido” foram superadas pela corrupção atual.

O material físico inclui painel, pastas e crachá. O tutorial deve mencioná-los sem entregar soluções. Os jornais finais são três folhas A3 de fundo branco, sem duplicatas. A folha de recortes permanece incluída.

## Produção audiovisual e origem

A voz de narração aprovada é Francisca Neural; o responsável autorizou o envio do roteiro ao serviço da Microsoft durante a produção. O vídeo atual já está em `public/video/Video_inicial.mp4` e dura cerca de 100 segundos. O site não chama serviços de voz em execução. O encerramento usa narração local e cenas da reconstituição por cerca de 255 segundos.

As fontes externas de som e fontes tipográficas estão documentadas em `LICENCAS.md` e `docs/licencas/`. Preservar os avisos e registros ao redistribuir.

## Publicação e limites

Nenhum repositório remoto, push ou deploy é criado pela simples consolidação. Esses passos devem usar as contas do responsável. O destino informado é `https://github.com/rpoless/vig.ia-os-escape-room`. O Git local deve manter `main`, e a visibilidade do repositório precisa ser Private antes do envio da pasta da equipe. A documentação de publicação explica a conexão e a conferência do push.

A arquitetura é totalmente cliente: a pasta da equipe é versionada em GitHub privado e excluída do site, mas o gabarito necessário à validação pode ser inspecionado em JavaScript. Não inserir chaves de API ou senhas pessoais no código. Autenticação de verdade e sigilo das respostas exigiriam um backend futuro.

## Backup

Faça commit e push para guardar código, materiais e `privado/` no repositório privado. Isso inclui as fontes e o histórico, não apenas o inventário. Caches, temporários e `dist/` são regeneráveis e permanecem ignorados. Alterações sem push ainda não estão na nuvem. Não apagar versões anteriores antes de conferir a integridade da entrega e a sincronização com o remoto.

O nome `privado/` é uma divisão do projeto, não um mecanismo de acesso. A privacidade depende da configuração Private do GitHub; a exclusão do site depende de publicar exclusivamente `dist/`, construída de `public/`.
