from pathlib import Path
import json, shutil, hashlib, datetime, re

ROOT=Path(__file__).resolve().parents[2]
SOURCE=ROOT/'output/vigia_os_sistema'
PACKAGE=Path(r'C:\Users\SEU_USUARIO\Desktop\Escape_Room_Pacote_Completo').resolve()
BACKUP=ROOT/'tmp/backups/vigia_os_20261119_090842/Escape_Room_Pacote_Completo'
assert str(PACKAGE)==r'C:\Users\SEU_USUARIO\Desktop\Escape_Room_Pacote_Completo'
assert (PACKAGE/'02_SISTEMA_OFFLINE/index.html').is_file()
assert (BACKUP/'02_SISTEMA_OFFLINE/index.html').is_file()
assert '750+bonus' in (SOURCE/'countdown.js').read_text(encoding='utf-8')
def parse_case(p):
    s=p.read_text(encoding='utf-8');return json.loads(s[s.index('=')+1:].strip().rstrip(';'))
original=parse_case(PACKAGE/'02_SISTEMA_OFFLINE/data.js');new=parse_case(SOURCE/'data.js')
assert original['key']==new['key']
assert original['evidence']==new['evidence']
for a,b in zip(original['cards'],new['cards']):
    assert {k:v for k,v in a.items() if k!='image'}=={k:v for k,v in b.items() if k!='image'}
sha=lambda f:hashlib.sha256(f.read_bytes()).hexdigest()
assert sha(PACKAGE/'02_SISTEMA_OFFLINE/engine.js')==sha(SOURCE/'engine.js')
media=[]
for prefix in ['audio','evidencias','encerramento']:
    for file in (PACKAGE/'02_SISTEMA_OFFLINE'/prefix).rglob('*'):
        if file.is_file():
            rel=file.relative_to(PACKAGE/'02_SISTEMA_OFFLINE')
            assert sha(file)==sha(SOURCE/rel),str(rel)
            media.append(str(rel))

update='''## Atualização vigente - VIGIA OS / 19-11-2026

Esta seção substitui descrições antigas de navegação por abas e encerramento roxo de tempo esgotado. A entrada continua em02_SISTEMA_OFFLINE/index.html.

- A navegação principal é uma área de trabalho com5 aplicativos: Arquivos, IA, Registros, Cronologia e Áudios. Barra fixa inclui mini-player, IA e Registros lado a lado, efeitos e relógio real. O painel superior informa o prazo até o apagamento.
- Uma janela principal preserva estado dos aplicativos; minimizar e fechar não apagam rascunhos. O leitor é auxiliar. Em telas largas, IA e documento podem ficar lado a lado.
- Explorador: categorias, busca, lista/ícones, prévia, Enter/duplo clique e arquivos corrompidos com nomes neutros. O catálogo passa por8/23/24/25 evidências. Blocos do desktop e selos de novidade acompanham a recuperação.
- Memória8/34/67/100; validar a cronologia mantém67% e amplia a interpretação temporal. Respostas certas continuam aceitas sem leitura obrigatória. As perguntas finais, chave,25 documentos e sequência oficial foram preservados.
- Bônus de15s para identidade, acessos e cronologia, uma vez cada, com aviso breve de2s sem botão. Prazo de produção750s, orçamento máximo795s. A exposição final da chave tem30s independentes.
- Ao expirar: tela azul VIGIA_DATA_TIMEOUT, chiado de1,2s respeitando silêncio, áudio pausado e interação pública bloqueada. Nada é apagado do Windows. Operação autenticada pode autorizar continuação sem prazo ou reiniciar.
- Conclusões corretas contêm o apagamento; anotar chave por30s, ocultar, digitar e liberar automaticamente o filme continuam obrigatórios. Um fluxo não contorna o outro.
- Novos desktop.js e desktop.css; fundo e ícones em assets/os. app.js adapta apresentação ao motor. engine.js preservado. Os campos image legados dos cartões apontavam para arquivos inexistentes e foram retirados: os6 cartões continuam compostos em HTML, com texto e IDs preservados.
- Conferência:104 testes automatizados de regras e caminhos, efeitos simulados, percurso HTTP com erros/Enter/bônus/arrasto/30s/chave/filme, falha isolada de12s e continuação autorizada. Layouts1280x636,1366x768,1920x1080 e390x844. Abertura file:// bloqueada pela política do navegador de teste: homologação no equipamento do evento e percepção de som continuam pendentes.
- Backup anterior mantido no workspace em tmp/backups/vigia_os_20261119_090842. Consultar VIGIA_OS_LEIA-ME.md e o relatório VERIFICACAO_VIGIA_OS_20261119.json.

'''
for name in ['README.md','LEIA-ME.md','OPERACAO_EQUIPE.md']:
    p=SOURCE/name;p.write_text(update+p.read_text(encoding='utf-8'),encoding='utf-8')
shutil.copytree(SOURCE,PACKAGE/'02_SISTEMA_OFFLINE',dirs_exist_ok=True)
guides=PACKAGE/'05_DOCUMENTACAO/00_GUIA_DE_CONTINUIDADE'
for p in guides.glob('*.md'):
    content=p.read_text(encoding='utf-8')
    p.write_text(content+'\n\n'+update,encoding='utf-8')
p=PACKAGE/'COMECE_AQUI.md';p.write_text(update+p.read_text(encoding='utf-8'),encoding='utf-8')
reports=PACKAGE/'05_DOCUMENTACAO/Registros_de_verificacao';reports.mkdir(exist_ok=True)
checks=json.loads((ROOT/'tmp/vigia_os_impl/motor.json').read_text(encoding='utf-8'))
sound=json.loads((ROOT/'tmp/vigia_os_impl/som.json').read_text(encoding='utf-8'))
report={'version':'VIGIA OS / 2026-11-19','backup':str(BACKUP),'motor':checks,'sound':sound,'canonical_preserved':{'key':True,'engine':True,'evidence':25,'cards':6,'media_files_identical':len(media)},'browser':{'full_path':'passed','wrong_answers_and_docs':'passed','enter_and_fields':'passed','bonus':'passed','close_minimize_restore':'passed','reader_ai_side_by_side':'passed','timeline_pointer_drag':'passed','key_30s_auto_hide':'passed','invalid_and_valid_code':'passed','recap_autoplay':'passed','expiry_blue_12s_copy':'passed','escape_alt2_blocked':'passed','operator_overtime':'passed','reset':'passed','early_key_acknowledgement':'passed','resolutions':['1280x636','1366x768','1920x1080','390x844'],'console':'No error associated with a local source file. One isolated MutationObserver error without URL after the final observation; no local JS uses this API and no associated functional failure observed.'},'limitations':['Direct file:// browser verification blocked by browser URL policy; no bypass attempted.','Validate audio perception, local opening and pilot with group on event computer.'],'assets':{'wallpaper':'Native image_gen PNG','icons':'8 local SVGs','ui':'HTML/CSS/SVG','existing_media':'preserved'}}
(reports/'VERIFICACAO_VIGIA_OS_20261119.json').write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf-8')
shutil.copy2(SOURCE/'VIGIA_OS_LEIA-ME.md',PACKAGE/'05_DOCUMENTACAO/VIGIA_OS_IMPLEMENTADO.md')
for name in ['explorador.png','desktop.png']:
    pic=ROOT/'tmp/vigia_os_impl'/name
    if pic.exists():shutil.copy2(pic,reports/('VIGIA_OS_'+name))
files=[]
for p in sorted(PACKAGE.rglob('*')):
    if p.is_file() and p.name!='INVENTARIO_PACOTE.json':files.append({'arquivo':str(p.relative_to(PACKAGE)),'bytes':p.stat().st_size,'sha256':sha(p)})
manifest={'revisao':'2026-11-19 VIGIA OS','pasta':str(PACKAGE),'quantidade_arquivos':len(files),'total_bytes':sum(x['bytes'] for x in files),'arquivos':files}
(PACKAGE/'INVENTARIO_PACOTE.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2),encoding='utf-8')
for item in files:assert sha(PACKAGE/item['arquivo'])==item['sha256']
local_report=ROOT/'tmp/vigia_os_impl/PUBLICACAO.json';local_report.write_text(json.dumps({'target':str(PACKAGE),'files':len(files),'sha256_verified':True,'backup':str(BACKUP),'entry':str(PACKAGE/'02_SISTEMA_OFFLINE/index.html')},ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps({'files':len(files),'sha256_verified':True,'media_files_preserved':len(media),'entry':str(PACKAGE/'02_SISTEMA_OFFLINE/index.html')},ensure_ascii=False))
