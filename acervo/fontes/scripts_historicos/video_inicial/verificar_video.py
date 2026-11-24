from pathlib import Path
import subprocess,json,re,hashlib
ROOT=Path(__file__).resolve().parents[2];OUT=ROOT/'output/video_inicial';FF=ROOT/'tmp/video_inicial/ffmpeg.exe';VIDEO=OUT/'VIGIA_OS_Introducao_Tutorial_v2.mp4'
def ff(args):return subprocess.run([str(FF),'-hide_banner']+list(map(str,args)),stdout=subprocess.PIPE,stderr=subprocess.PIPE)
probe=ff(['-i',VIDEO]);info=probe.stderr.decode('utf-8','replace')
duration=re.search(r'Duration: (\d+):(\d+):(\d+\.\d+)',info);assert duration
seconds=int(duration[1])*3600+int(duration[2])*60+float(duration[3]);assert abs(seconds-166)<.1
assert '1920x1080' in info and '30 fps' in info and 'Video: h264' in info and 'Audio: aac' in info
decode=ff(['-v','error','-i',VIDEO,'-f','null','-']);assert decode.returncode==0,decode.stderr.decode('utf-8','replace')
audio=ff(['-i',VIDEO,'-vn','-af','ebur128=peak=true','-f','null','-']);assert audio.returncode==0
aud=audio.stderr.decode('utf-8','replace');(OUT/'audio/analise_volume.txt').write_text(aud[-2400:],encoding='utf-8')
scenes=json.loads((ROOT/'producao/video_inicial/cenas.json').read_text(encoding='utf-8'))
timing=json.loads((OUT/'audio/temporizacao.json').read_text(encoding='utf-8'))
for scene,voice in zip(scenes,timing):
    assert voice['start']>=scene['start'] and voice['end']<scene['start']+scene['duration']
texts='\n'.join(s['voice']+' '+s['title']+' '+s['body'] for s in scenes)+(OUT/'legendas.srt').read_text(encoding='utf-8')
protected=['Bryan','Helena','Marcelo','Carlos','2847','2246','22:46','BA17','B_A_17','NORTHSTAR']
assert not [x for x in protected if x.lower() in texts.lower()]
capture=json.loads((OUT/'capturas/gravao.json').read_text(encoding='utf-8'));assert capture['errors']==[]
for i in range(1,13):assert (OUT/f'storyboard/{i:02}_frame_final.png').exists()
audit=OUT/'capturas/auditoria_conteudo.json'
report={'arquivo':VIDEO.name,'bytes':VIDEO.stat().st_size,'sha256':hashlib.sha256(VIDEO.read_bytes()).hexdigest(),'duration_seconds':seconds,'resolution':[1920,1080],'fps':30,'video_codec':'H.264','audio_codec':'AAC stereo','complete_audio_video_decode':'passed','narration_fits_each_scene':True,'narration_and_captions_protected_content_scan':'passed','browser_recording_errors':capture['errors'],'demo_dom_audit':json.loads(audit.read_text(encoding='utf-8')) if audit.exists() else 'not performed','visual_review':'Quadros da abertura, tutorial e encerramento, folhas de contato e sequência do arrasto inspecionados. A inspeção de imagens é amostragem; não equivale a assistir a cada quadro.','audio_review':'Duração, sobreposição, decodificação, loudness e pico medidos por ferramentas. Narração sintética. Audição humana integral não realizada pelo agente.','sound_analysis_tail':aud[-750:],'scope':'Arquivo independente, não instalado na abertura do sistema.'}
(OUT/'VERIFICACAO.json').write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps({k:report[k] for k in ['arquivo','bytes','duration_seconds','complete_audio_video_decode','narration_fits_each_scene','narration_and_captions_protected_content_scan']},ensure_ascii=False))
