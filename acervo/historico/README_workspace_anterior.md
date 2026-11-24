# O Arquivo Corrompido

Materiais da apresentação do escape room investigativo para a feira escolar do SESI. A proposta envolve grupos de 3 a 5 participantes, duração prevista de 15 minutos, documentos físicos e um terminal digital offline.

Esta pasta contém a apresentação, os recursos usados nela e os scripts de produção. O jogo completo, o terminal offline e os áudios não estão incluídos aqui.

## Por onde começar

- **Apresentar o projeto:** abra [o PDF final](output/pdf/O_Arquivo_Corrompido_Apresentacao_SESI.pdf).
- **Alterar textos e composição:** consulte [produção](producao/README.md).
- **Localizar imagens e fontes:** consulte [recursos](assets/README.md).
- **Examinar a revisão existente:** consulte [revisão](revisao/README.md).

## Estrutura

```text
Escape Room/
├── README.md                 Guia geral do projeto
├── .gitignore                Exclusões para eventual controle de versão
├── assets/                   Recursos usados na apresentação
│   ├── fontes/               Arquivos tipográficos
│   └── imagens/
│       ├── capturas/         Telas reais do sistema offline
│       ├── conceitos/        Ilustrações conceituais
│       ├── documentos/       Exemplos de documentos do jogo
│       └── identidade/       Marca visual
├── producao/                 Scripts, dependências e prompts
├── output/pdf/               Apresentação final para compartilhar
└── revisao/pdf/
    ├── previews/             Imagens das nove páginas
    ├── alternativas/         Imagens de revisões anteriores
    └── validacao/            Texto extraído e limites dos textos
```

Cada pasta possui um README que explica seus arquivos e seu uso.

## Fluxo de atualização

1. Edite os textos e a composição em `producao/montar_apresentacao.py` e, quando necessário, os recursos em `assets/`.
2. Siga as instruções em `producao/README.md` para gerar o PDF. A geração usa os recursos locais, sem exigir o pacote original na Área de Trabalho.
3. Confira o PDF e os relatórios em `revisao/pdf/validacao/`.
4. Atualize as imagens de revisão se precisar delas: o gerador do PDF não as recria automaticamente.
5. Compartilhe o arquivo de `output/pdf/`.

## Cuidados

- A geração substitui o PDF final e os dois relatórios de validação. Guarde uma cópia antes de executar se quiser conservar uma versão anterior.
- As imagens de revisão são registros existentes; não há garantia de que correspondam à geração mais recente.
- As ilustrações conceituais não são fotografias de uma aplicação realizada.
- A apresentação foi preparada sem revelar a solução do caso. O script contém verificações básicas de termos sensíveis, que não substituem uma revisão humana.
- Preserve os nomes dos recursos ou atualize as referências nos scripts e nos prompts ao renomeá-los.

## Organização realizada

Os arquivos antes soltos em `assets/` foram separados por função. O antigo conteúdo de `tmp/pdfs/` foi preservado em `revisao/pdf/`. O PDF final permaneceu no mesmo caminho. Os scripts foram ajustados para a nova estrutura.
