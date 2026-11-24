from pathlib import Path
import shutil,datetime
ROOT=Path(__file__).resolve().parents[2];S=ROOT/'output/vigia_os_sistema'
B=ROOT/'tmp/backups'/('fluxo_video_'+datetime.datetime.now().strftime('%Y%m%d_%H%M%S'));B.mkdir(parents=True)
for n in ['app.js','desktop.js','index.html','VIGIA_OS_LEIA-ME.md']:shutil.copy2(S/n,B/n)
app=(S/'app.js').read_text(encoding='utf-8')
assert 'VigiaIntroVideo.begin' not in app
app=app.replace("if(timeExpired||$('#code-popup').open)return;","if(timeExpired||$('#code-popup').open||VigiaIntroVideo.active)return;")
app=app.replace("'notes','trash'","'notes','trash','introvideo'")
app=app.replace("document.body.dataset.view=id;VigiaDesktop.open(id);renderAiPresence();","document.body.dataset.view=id;VigiaDesktop.open(id);renderAiPresence();if(id==='introvideo'){player.pause();VigiaIntroVideo.replay()}")
a=app.index(' function start(isDemo=false)');b=app.index("$('#start').onclick",a)
app=app[:a]+''' function start(isDemo=false){
  if(started||VigiaIntroVideo.active)return;
  VigiaFeedback.prime();if($('#intro').open)$('#intro').close();
  const beginRound=()=>{VigiaAmbient.start();started=true;demo=isDemo;running=!demo;elapsed=0;last=Date.now();updateAnalysisClock();notice('ANÁLISE INICIADA · '+E.perfilIA().next);tab('desktop');VigiaDesktop.welcome();if(VigiaSettings.current().autoNarration&&!E.estado().skippedStages.length)play('audio01')};
  VigiaIntroVideo.begin(beginRound,()=>$('#intro').showModal());
 }
 '''+app[b:]
app=app.replace('timeExpired=true;running=false;','VigiaIntroVideo.stopReplay();timeExpired=true;running=false;')
app=app.replace('VigiaAmbient.reset();E.reiniciar();','VigiaIntroVideo.reset();VigiaAmbient.reset();E.reiniciar();')
(S/'app.js').write_text(app,encoding='utf-8')
desktop=(S/'desktop.js').read_text(encoding='utf-8').replace("trash:'Lixeira'","trash:'Lixeira',introvideo:'Vídeo inicial.mp4'")
desktop=desktop.replace('function hideWindow(win,close=false){','function hideWindow(win,close=false){if(close&&win.id===\'introvideo\')VigiaIntroVideo.stopReplay();')
(S/'desktop.js').write_text(desktop,encoding='utf-8')
html=(S/'index.html').read_text(encoding='utf-8')
html=html.replace('</head>','<link rel="stylesheet" href="intro-video.css?v=1"></head>')
html=html.replace('<script src="desktop.js','<script src="intro-video.js?v=1"></script><script src="desktop.js')
html=html.replace('desktop.js?v=20261119-stages','desktop.js?v=20261124-intro-video').replace('app.js?v=20261119-stages','app.js?v=20261124-intro-video')
html=html.replace('<h2 id="intro-title">Reconstruir o incidente.</h2><p>Carlos Mendes morreu após um confronto na sala técnica. Um lote de projetos foi copiado e os registros foram comprometidos.</p>','<h2 id="intro-title">Preparar rodada.</h2><p>Área da equipe: use a engrenagem para ajustar o tempo, as etapas e os bônus antes de receber os participantes.</p>')
html=html.replace('Iniciar investigação<i data-icon="arrow">','Iniciar apresentação<i data-icon="arrow">')
html=html.replace('A VIG.IA é sua IA de apoio. Peçam dicas, documentos e caminhos a qualquer momento. Ela recupera novas relações conforme vocês recuperam a memória.','Ao iniciar, o vídeo será reproduzido automaticamente em tela cheia. A investigação e o cronômetro começam somente depois do fim da apresentação.')
(S/'index.html').write_text(html,encoding='utf-8')
(S/'video').mkdir(exist_ok=True)
shutil.copy2(ROOT/'output/video_inicial/v4_francisca/VIGIA_OS_Tutorial_Francisca_v4.mp4',S/'video/Video_inicial.mp4')
guide='''

## Apresentação antes da rodada

1. A equipe prepara tempo, etapas e bônus na engrenagem da tela inicial. As configurações continuam válidas somente até recarregar a página.
2. O botão Iniciar apresentação abre o vídeo local em tela cheia, com reprodução automática e som. Não há botão adicional de play nem controle de avanço nessa primeira exibição.
3. O cronômetro permanece parado durante toda a apresentação. Só o fim da primeira reprodução libera a área de trabalho e inicia a contagem configurada. Se o navegador sair de tela cheia com Esc, a apresentação continua cobrindo o sistema.
4. Depois disso, o atalho Vídeo inicial.mp4 abre o arquivo no player do OS; pode ser minimizado, maximizado, reaberto pela barra de tarefas e salvo como MP4. Rever o vídeo não reinicia nem pausa o relógio. Fechar o player interrompe sua reprodução; o fim do tempo também interrompe o vídeo.
5. Reinicializar a rodada pela equipe exige assistir à apresentação novamente. Uma falha ao carregar o vídeo mantém o relógio parado e permite tentar novamente ou voltar à preparação.

Arquivo offline: video/Video_inicial.mp4. Voz Francisca Neural, duração de 1min40. O ensaio sem tempo também apresenta o vídeo e mantém o cronômetro parado ao terminar.
'''
with (S/'VIGIA_OS_LEIA-ME.md').open('a',encoding='utf-8') as f:f.write(guide)
print('Fluxo aplicado na cópia de preparação. Backup:',B)
