from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];p=ROOT/'output/vigia_os_sistema/VIGIA_OS_LEIA-ME.md'
s=p.read_text(encoding='utf-8');s=s.split('\n## Apresentação antes da rodada')[0]
s+='''

## Fluxo da equipe e dos participantes

1. **Preparação da equipe:** a página abre com Preparar rodada. A engrenagem permite configurar duração, etapas e bônus com as credenciais já usadas pela equipe. As configurações continuam válidas somente nesta sessão, até recarregar a página.
2. **Passar para os participantes:** ao clicar em Abrir tela dos participantes, aparece o vídeo em tela cheia, ainda parado, com o botão Iniciar. O relógio continua parado.
3. **Apresentação:** o botão Iniciar dá play com som, sem outro comando de reprodução. Na primeira exibição, não há avanço, pausa ou botão de pular. Sair do modo de tela cheia do navegador não libera o OS: a apresentação continua cobrindo o sistema.
4. **Investigação:** somente o fim da primeira reprodução abre a área de trabalho e começa a contagem do tempo configurado. O vídeo não consome o tempo da rodada. A narração inicial da investigação segue a opção configurada pela equipe.
5. **Rever o vídeo:** o atalho Vídeo inicial.mp4 abre o player do OS. O vídeo pode ser revisto, pausado, minimizado, maximizado, reaberto pela barra de tarefas ou salvo como MP4. A revisão não pausa nem reinicia o cronômetro. Fechar o player interrompe sua reprodução; o fim do tempo também interrompe o vídeo.
6. **Nova rodada e falhas:** reinicializar pela equipe volta à preparação e exige uma nova exibição completa. Se o arquivo não carregar, o relógio permanece parado; é possível tentar novamente ou voltar à preparação. O ensaio sem tempo também apresenta o vídeo e continua sem contagem após o fim.

Arquivo offline: video/Video_inicial.mp4. Voz Francisca Neural, duração de 1min40.

## Jornais em A3 e reservas

Na pasta 01_PARA_IMPRESSAO do pacote, Jornais_A3_Duas_Copias.pdf contém seis páginas A3 em retrato: jornal 1, jornal 2, manchetes e uma segunda cópia de cada folha, na mesma ordem. Imprimir uma cópia do PDF em papel A3, tamanho real (100%), frente única. As reservas já estão dentro do arquivo. O fundo permanece branco puro e a arte foi ampliada uniformemente, sem distorcer a proporção.
'''
p.write_text(s,encoding='utf-8');print('Documentação atualizada.')
