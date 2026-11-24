from pathlib import Path
import json, shutil, hashlib, datetime

ROOT = Path(__file__).resolve().parents[2]
SOURCE = ROOT/'output/vigia_os_sistema'
PACKAGE = Path(r'C:\Users\SEU_USUARIO\Desktop\Escape_Room_Pacote_Completo').resolve()
TARGET = PACKAGE/'02_SISTEMA_OFFLINE'
assert str(PACKAGE) == r'C:\Users\SEU_USUARIO\Desktop\Escape_Room_Pacote_Completo'
assert (TARGET/'index.html').is_file()
sha = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
def case(p):
    s=p.read_text(encoding='utf-8')
    return json.loads(s[s.index('=')+1:].strip().rstrip(';'))
old,new=case(TARGET/'data.js'),case(SOURCE/'data.js')
assert old['key']==new['key'] and old['evidence']==new['evidence']
assert old['cards']==new['cards']
assert sha(TARGET/'engine.js')==sha(SOURCE/'engine.js')
media=[]
for folder in ['audio','evidencias','encerramento']:
    for p in (TARGET/folder).rglob('*'):
        if p.is_file():
            rel=p.relative_to(TARGET)
            assert sha(p)==sha(SOURCE/rel),str(rel)
            media.append(str(rel))
assert '750+bonus' in (SOURCE/'countdown.js').read_text(encoding='utf-8')
backup=ROOT/'tmp/backups'/('vigia_os_v2_publicacao_'+datetime.datetime.now().strftime('%Y%m%d_%H%M%S'))/'Escape_Room_Pacote_Completo'
assert backup.resolve().is_relative_to((ROOT/'tmp/backups').resolve())
shutil.copytree(PACKAGE,backup)
update='''## Revisão vigente — VIGIA OS v2 / 19-11-2026

Esta revisão substitui as descrições anteriores da interface. Entrada: 02_SISTEMA_OFFLINE/index.html.

- Desktop somente com atalhos maiores: Arquivos, VIGIA/3, Registros, Áudios, Próximos passos.txt e Lixeira. Retirados os atalhos decorativos de arquivos corrompidos e os painéis de texto.
- Todos os aplicativos na barra de tarefas, com indicador de janela aberta/ativa. Tempo até o apagamento, memória, mini-player, efeitos e relógio ficam na mesma barra. Retirados os botões flutuantes duplicados de IA e respostas.
- Próximos passos.txt atualiza suas orientações conforme identidade, acessos, cronologia e conclusões. Lembretes acompanham a etapa atual e avisos anteriores são descartados na troca de fase.
- Cronologia é uma etapa de Registros. Não existe aplicativo separado. Enter continua enviando respostas e os bônus de15s permanecem.
- Explorador com blocos e prévias dos documentos, navegação com ícones e abertura do documento em janela auxiliar com um clique. Busca e filtros mantidos.
- IA em conversa com histórico, balões opostos, avatares, exemplos e campo de mensagem fixo na parte inferior da janela. Memória e capacidades acessíveis no cabeçalho. As orientações evoluem com a investigação.
- Janelas independentes podem ficar abertas simultaneamente. Barra de tarefas alterna/restaura/minimiza. Posição, tamanho, maximização, conversa e rascunhos são preservados durante a rodada. Arraste pelo título, redimensione pelo canto inferior direito; duplo clique no título maximiza/restaura. Há animações de entrada, saída e minimização, respeitando preferência de movimento reduzido.
- Regras, respostas, documentos, áudios, bônus, tela azul e sequência de anotação por30s → código → filme foram preservados. Reiniciar limpa o estado das janelas e da conversa. Recarregar inicia nova rodada.
- Conferência:105 verificações automatizadas aprovadas; percurso no navegador, envio com Enter, etapas/atualização das notas, prévia e abertura por clique, conversa, minimizar/restaurar/maximizar com rascunho preservado,30s de anotação e código incorreto/correto liberando o filme. Consultar o relatório de verificação v2. Abertura direta local e percepção do som devem ser conferidas no computador do evento; a política do navegador de teste impede file://.

'''
for name in ['README.md','LEIA-ME.md','OPERACAO_EQUIPE.md']:
    p=SOURCE/name
    p.write_text(update+p.read_text(encoding='utf-8'),encoding='utf-8')
shutil.copy2(SOURCE/'desktop.js',ROOT/'producao/vigia_os_impl/desktop_v2.js')
metadata=SOURCE/'assets/os/PRODUCAO.json'
m=json.loads(metadata.read_text(encoding='utf-8'))
m['revision_v2']={'date':'2026-11-19','added_svg':['notes.svg','trash.svg','user.svg'],'method':'SVG local, sem dependências externas','interface':'Janelas independentes e conversa persistente durante a rodada'}
metadata.write_text(json.dumps(m,ensure_ascii=False,indent=2),encoding='utf-8')
shutil.copytree(SOURCE,TARGET,dirs_exist_ok=True)
for p in (PACKAGE/'05_DOCUMENTACAO/00_GUIA_DE_CONTINUIDADE').glob('*.md'):
    p.write_text(update+p.read_text(encoding='utf-8'),encoding='utf-8')
p=PACKAGE/'COMECE_AQUI.md'
p.write_text(update+p.read_text(encoding='utf-8'),encoding='utf-8')
shutil.copy2(SOURCE/'VIGIA_OS_LEIA-ME.md',PACKAGE/'05_DOCUMENTACAO/VIGIA_OS_IMPLEMENTADO.md')
reports=PACKAGE/'05_DOCUMENTACAO/Registros_de_verificacao'
reports.mkdir(exist_ok=True)
report={'version':'VIGIA OS v2','date':'2026-11-19','backup':str(backup),'motor':json.loads((ROOT/'tmp/vigia_os_impl/motor.json').read_text(encoding='utf-8')),'preserved':{'engine_sha256':sha(SOURCE/'engine.js'),'key':True,'evidence':25,'chronology_cards':6,'identical_media_files':len(media)},'browser':{'desktop_shortcuts_only':True,'six_taskbar_apps':True,'status_in_taskbar':True,'file_preview_tiles':True,'one_click_reader':True,'notes_update_per_stage':True,'timeline_inside_records_only':True,'chat_bubbles_avatars_footer':True,'chat_context_refresh':True,'draft_minimize_maximize_restore':True,'enter_answers':True,'bonus':True,'key_30s_auto_hide':True,'wrong_and_correct_key_then_film':True},'limitations':['Navegador de teste bloqueia file://; conferir abertura direta no equipamento do evento.','Validar percepção dos efeitos sonoros e volume no equipamento do evento.']}
(reports/'VERIFICACAO_VIGIA_OS_V2_20261119.json').write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf-8')
for name in ['v2_desktop.png','v2_explorador.png','v2_chat.png']:
    p=ROOT/'tmp/vigia_os_impl'/name
    if p.exists():shutil.copy2(p,reports/('VIGIA_OS_'+name))
for p in SOURCE.rglob('*'):
    if p.is_file():assert sha(p)==sha(TARGET/p.relative_to(SOURCE)),str(p)
files=[{'arquivo':str(p.relative_to(PACKAGE)),'bytes':p.stat().st_size,'sha256':sha(p)} for p in sorted(PACKAGE.rglob('*')) if p.is_file() and p.name!='INVENTARIO_PACOTE.json']
(PACKAGE/'INVENTARIO_PACOTE.json').write_text(json.dumps({'revisao':'2026-11-19 VIGIA OS v2','pasta':str(PACKAGE),'quantidade_arquivos':len(files),'total_bytes':sum(x['bytes'] for x in files),'arquivos':files},ensure_ascii=False,indent=2),encoding='utf-8')
result={'target':str(TARGET),'entry':str(TARGET/'index.html'),'backup':str(backup),'files':len(files),'all_runtime_files_identical':True,'media_preserved':len(media),'checks':report['motor']['checks']}
(ROOT/'tmp/vigia_os_impl/PUBLICACAO_V2.json').write_text(json.dumps(result,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps(result,ensure_ascii=False))
