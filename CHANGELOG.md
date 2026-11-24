# Histórico da entrega

## Ajuste de armazenamento na nuvem · 24/11/2026

- Inclusão de `privado/`, fontes, editáveis, histórico e ZIPs de produção no versionamento, para armazenar o projeto completo em GitHub privado.
- Manutenção da publicação exclusiva de `public/` via `dist/`; os materiais da equipe não entram no site.
- Atualização dos guias e preservação de relatórios de verificação em `privado/verificacao/`.
- Destino informado pelo responsável: `rpoless/vig.ia-os-escape-room`. A visibilidade deve ser **Private** antes do envio.

## 1.0.0 · 24/11/2026

- Consolidação do sistema atual em `public/`, sem substituir o motor nem a interface aprovados.
- Organização dos PDFs finais: cenário A4 horizontal, seis documentos A4 verticais e três jornais A3 sem duplicatas.
- Inclusão do cartaz final com data/horário em PNG e PDF A4.
- Separação de equipe, soluções, editáveis e históricos em `privado/`, fora do Git e do build.
- Reescrita da documentação atual, preservando os manuais antigos como histórico local.
- Inclusão de comandos Node sem dependências de execução, servidor de conferência, testes, workflow e configuração da Vercel.
- Preparação para GitHub → Vercel com saída estática `dist/` e verificação de referências para hospedagem com caminhos sensíveis a maiúsculas/minúsculas.

As versões anteriores dos documentos tinham atualizações acumuladas e instruções superadas. Elas permanecem arquivadas em `privado/historico/`; não são a referência vigente.
