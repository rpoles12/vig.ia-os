(()=>{
 'use strict';
 const screen=document.querySelector('#time-up');
 screen.innerHTML=`<div class="failure-noise" aria-hidden="true"></div><div class="failure-streams" aria-hidden="true"></div><div class="failure-slices" aria-hidden="true"><i></i><i></i><i></i></div><header class="failure-header"><span>VIG.IA / RECOVERY TERMINAL</span><span class="failure-offline">● CONEXÃO INTERROMPIDA</span></header><div class="failure-panel"><div class="failure-label"><span class="failure-led"></span> TRANSMISSÃO COMPROMETIDA <span>[ ERR_0x00 ]</span></div><div class="failure-counter" aria-hidden="true">00:00<span>TIMEOUT / NO RESPONSE</span></div><h2 id="timeup-title" tabindex="-1" data-text="SINAL PERDIDO">SINAL PERDIDO</h2><div class="failure-rule"></div><p id="timeup-copy">O tempo acabou. A transmissão foi interrompida e os dados deste computador ficaram indisponíveis.</p><div class="failure-diagnostics" aria-hidden="true"><span>DISK I/O</span><b>READ FAILURE</b><span>PACKETS</span><b>░░ LOST ░░</b><span>CHECKSUM</span><b>INVALID</b></div><div class="failure-memory"><span>MEMÓRIA RECUPERADA <strong id="timeup-memory">08%</strong></span><span>SESSÃO BLOQUEADA</span></div><p class="failure-team">Chamem a equipe responsável.</p></div><footer class="failure-footer"><span>TRANSMISSION_ABORTED // VIGIA_DATA_TIMEOUT</span><span>RECONEXÃO AUTOMÁTICA INDISPONÍVEL</span></footer>`;
 const host=screen.querySelector('.failure-streams');
 const lines=Array.from({length:38},(_,i)=>{const line=document.createElement('span');line.className=i%4===0?'failure-log':'failure-binary';line.style.cssText=`left:${(i*31)%96}%;top:${(i*17)%100}%;--delay:${-(i%9)}s;--duration:${9+i%7}s;--shift:${i%2?1:-1};font-size:${10+i%5*3}px`;host.append(line);return line});
 const errors=['0xBA17 // SECTOR UNREADABLE','recv() → NULL / PACKET LOST','FATAL: journal.recover [DENIED]','0101 ░░░ 1100 / CRC_MISMATCH','/dev/memory : I/O ERROR','BUFFER OVERRUN ▓▓▓','0x2246 :: CONNECTION RESET','[ sync ] FAILED / RETRY ABORTED','FRAGMENT_??? // NOT FOUND'];
 let interval=null,tick=0;
 function scramble(){tick++;for(let i=0;i<lines.length;i++){if(tick>1&&(i+tick)%3!==0)continue;lines[i].textContent=i%4===0?errors[(i+tick)%errors.length]:Array.from({length:22+i%5*7},()=>Math.random()>.5?'1':'0').join(' ')}}
 function sync(){clearInterval(interval);interval=null;if(!screen.hidden&&!document.hidden){tick=0;scramble();interval=setInterval(scramble,240)}}
 new MutationObserver(sync).observe(screen,{attributes:true,attributeFilter:['hidden']});
 document.addEventListener('visibilitychange',sync);sync();
})();
