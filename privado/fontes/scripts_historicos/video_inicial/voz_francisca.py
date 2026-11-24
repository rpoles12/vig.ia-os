from pathlib import Path
import asyncio,json,sys,subprocess
ROOT=Path(__file__).resolve().parents[2];sys.path.insert(0,str(ROOT/'tmp/voice_tools'))
import edge_tts
OUT=ROOT/'output/video_inicial/v4_francisca';A=OUT/'audio';A.mkdir(parents=True,exist_ok=True)
FF=ROOT/'tmp/video_inicial/ffmpeg.exe'
async def main():
    scenes=json.loads((ROOT/'output/video_inicial/v3_dinamico/cenas.json').read_text(encoding='utf-8'));semaphore=asyncio.Semaphore(1)
    async def generate(s):
        async with semaphore:
            mp3=A/f'francisca_{s["id"]:02}.mp3';wav=A/f'voz_{s["id"]:02}.wav'
            if mp3.exists() and wav.exists() and wav.stat().st_size>1000:return
            partial=mp3.with_suffix('.partial.mp3')
            for attempt in range(3):
                try:
                    await edge_tts.Communicate(s['voice'],voice='pt-BR-FranciscaNeural',rate='+5%',pitch='-2Hz').save(str(partial))
                    partial.replace(mp3);break
                except Exception:
                    if attempt==2:raise
                    await asyncio.sleep(2+attempt)
            p=subprocess.run([str(FF),'-hide_banner','-y','-i',str(mp3),'-ar','48000','-ac','1','-c:a','pcm_s16le',str(wav)],capture_output=True)
            if p.returncode:raise RuntimeError(p.stderr.decode('utf-8','replace'))
            print('Francisca Neural - cena',s['id'],flush=True)
    await asyncio.gather(*(generate(s) for s in scenes))
    (A/'VOZ.json').write_text(json.dumps({'voice':'pt-BR-FranciscaNeural','rate':'+5%','pitch':'-2Hz','matched_to':'output/vigia_os_sistema/audio/manifesto_integracao.json','note':'Mesma voz e prosódia-base do sistema; sem acrescentar chiado à locução didática.','provider':'Serviço de leitura em voz alta do Microsoft Edge via edge-tts; sem credenciais de cobrança.'},ensure_ascii=False,indent=2),encoding='utf-8')
if __name__=='__main__':asyncio.run(main())
