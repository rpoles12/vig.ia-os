from pathlib import Path
import json,subprocess,hashlib,re
ROOT=Path(__file__).resolve().parents[2];OUT=ROOT/'output/video_inicial/v3_dinamico';FF=ROOT/'tmp/video_inicial/ffmpeg.exe';video=OUT/'VIGIA_OS_Tutorial_Curto_v3.mp4'
def run(args):return subprocess.run([str(FF),'-hide_banner']+list(map(str,args)),capture_output=True)
probe=run(['-i',video]).stderr.decode('utf-8','replace');assert '00:01:40.00' in probe and '1920x1080' in probe and '30 fps' in probe
decode=run(['-v','error','-i',video,'-f','null','-']);assert decode.returncode==0,decode.stderr
scenes=json.loads((OUT/'cenas.json').read_text(encoding='utf-8'));timing=json.loads((OUT/'audio/temporizacao.json').read_text(encoding='utf-8'))
assert len(scenes)==len(timing)==12
for s,t in zip(scenes,timing):assert t['start']>=s['start'] and t['end']<=s['start']+s['duration']
text=' '.join(s['voice'] for s in scenes)+(OUT/'legendas.srt').read_text(encoding='utf-8')
assert not any(x.lower() in text.lower() for x in ['Bryan','Helena','Marcelo','2847','22:46','BA17','B_A_17'])
audio=run(['-i',video,'-vn','-af','ebur128=peak=true','-f','null','-']);assert audio.returncode==0
(OUT/'audio/volume_final.txt').write_text(audio.stderr.decode('utf-8','replace')[-1500:],encoding='utf-8')
result={'video':video.name,'sha256':hashlib.sha256(video.read_bytes()).hexdigest(),'seconds':100,'previous_seconds':166,'reduction_seconds':66,'size':[1920,1080],'fps':30,'full_decode':'passed','voice_fits_scenes':True,'no_protected_content_in_voice_and_captions':True,'visual_review':'Quadros de aplicativos e sequência de movimento amostrados; textos dos jornais e renderizações do PDF inspecionados visualmente. Não representa uma revisão humana integral do vídeo.','audio_review':'Síntese local; redução de pausas e mixagem com música reduzida sob voz. Duração, decodificação e loudness verificados por ferramenta; sem audição humana integral pelo agente.','preserved':'A investigação física, todos os aplicativos e controles, tempo e memória, bônus configurável, resposta por Enter, orientações dos erros, cronologia e anotação da chave foram mantidos.'}
(OUT/'VERIFICACAO.json').write_text(json.dumps(result,ensure_ascii=False,indent=2),encoding='utf-8');print(json.dumps(result,ensure_ascii=False))
