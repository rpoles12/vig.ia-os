# Reconstituição do incidente

Esta página é aberta pelo terminal VIG.IA assim que o protocolo final correto é confirmado. A narração começa automaticamente e percorre os 26 quadros em sequência, com transições, movimentos, textos explicativos e legendas. É um filme montado em HTML/CSS/JavaScript; não existe um MP4 separado.

O áudio contínuo é `../../audio/final_completo.wav`. O terminal pai controla a reprodução e sincroniza as cenas/legendas pelo tempo do áudio. No modal integrado, a janela se adapta à tela, não deve criar rolagem interna e pode ser fechada pelo botão ou por Esc; fechar retorna à aba Respostas. A barra compacta integrada oferece progresso, reproduzir/pausar, tempo, legendas e som. O salto de capítulo, o controle deslizante de volume e tela cheia estão ocultos nessa apresentação integrada. Se o navegador bloquear o início automático, aparece **Reproduzir reconstituição**.

Tudo é executado localmente, sem internet. Preserve `encerramento/filme/` junto com `audio/final_completo.wav`, ambos dentro da pasta `02_SISTEMA_OFFLINE`. As imagens de fundo, evidências e fontes usadas pelo filme pertencem às subpastas `assets/`. Não renomeie nem mova esses arquivos isoladamente.
