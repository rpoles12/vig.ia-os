(()=>{
 'use strict';
 const screen=document.querySelector('#time-up');
 screen.innerHTML=`<h2 id="timeup-title" class="sr-only" tabindex="-1">Falha crítica do computador.</h2><p id="timeup-copy" class="sr-only">O prazo terminou. A tela está corrompida e a sessão permanece bloqueada. Chamem a equipe responsável.</p><strong id="timeup-memory" class="sr-only">08%</strong><canvas class="failure-raster" aria-hidden="true"></canvas><div class="failure-errors" aria-hidden="true"></div><div class="failure-lcd-bleed" aria-hidden="true"></div><div class="failure-lcd-stripes" aria-hidden="true"></div><div class="failure-glass" aria-hidden="true"><img src="assets/os/failure/cracked-glass-v1.png" alt="" draggable="false"></div><div class="failure-scanlines" aria-hidden="true"></div>`;
 const canvas=screen.querySelector('canvas'),ctx=canvas.getContext('2d',{alpha:false}),host=screen.querySelector('.failure-errors');
 const motion=matchMedia('(prefers-reduced-motion: reduce)');
 const faults=['TRANSMISSION_ERROR','CRC_MISMATCH','SECTOR_UNREADABLE','PACKET_DROPPED','BUS_FAILURE','BUFFER_OVERFLOW','FRAME_CORRUPTED','MEMORY_ACCESS_FAULT','DISK_IO_ERROR','RX_STREAM_ABORT','UNRECOVERABLE_BLOCK','CHECKSUM_INVALID'];
 const hex=()=>Math.floor(Math.random()*0xffffffff).toString(16).toUpperCase().padStart(8,'0');
 const binary=length=>Array.from({length},()=>Math.random()>.5?'1':'0').join('');
 const panels=Array.from({length:32},(_,i)=>{const block=document.createElement('pre');block.style.cssText=`left:${i%4*25-4+(i*7%12)}%;top:${Math.floor(i/4)*13-3}%;font-size:${10+i%4*2}px;--i:${i};`;host.append(block);return block});
 let timer=null,tick=0,width=0,height=0;
 const noise=document.createElement('canvas');noise.width=160;noise.height=90;const nctx=noise.getContext('2d'),pixels=nctx.createImageData(160,90);
 function resize(){width=Math.max(1,screen.clientWidth);height=Math.max(1,screen.clientHeight);const ratio=Math.min(devicePixelRatio||1,1.25);canvas.width=Math.round(width*ratio);canvas.height=Math.round(height*ratio);ctx.setTransform(ratio,0,0,ratio,0,0)}
 function updatePanels(){for(let i=0;i<panels.length;i++){if(tick>1&&(i+tick)%4!==0)continue;panels[i].textContent=`[${faults[(i+tick)%faults.length]}] 0x${hex()}\n${binary(34)}\nrecv:${hex()} → ▓▓▓ ░░ / ERR\n${i%2?'retry() = -1; stream.abort();':hex()+' '+hex()+' ?????'}`;panels[i].style.transform=motion.matches?'none':`translate(${Math.floor(Math.random()*28)-14}px,${Math.floor(Math.random()*10)-5}px)`}}
 function draw(){
  tick++;ctx.fillStyle='#030508';ctx.fillRect(0,0,width,height);
  const colors=['#74c9b6','#a37cda','#d582a2','#5f9883','#809fa1'];ctx.font='12px Consolas,monospace';
  for(let col=0;col<Math.ceil(width/24);col++){const x=col*24,y=(tick*(col%3+1)*5+col*47)%(height+160)-160;ctx.fillStyle=colors[col%colors.length];ctx.globalAlpha=.25+col%4*.08;for(let row=0;row<12;row++)ctx.fillText(binary(3),x,y+row*15)}
  ctx.globalAlpha=1;
  for(let i=0;i<10;i++){const y=(i*137+tick*3)%height,h=i%3===0?24:3;ctx.fillStyle=i%2?'#9163b41f':'#49e5ca20';ctx.fillRect(0,y,width,h);ctx.fillStyle='#c4d4e326';ctx.fillRect((i*191+tick*29)%width,y,60+i*11,h)}
  for(let i=0;i<16;i++){const x=(i*173+tick*11)%width,y=(i*97+Math.floor(tick/5)*19)%height;ctx.fillStyle=['#010207','#a1335755','#45579b60','#32ae9a3d'][i%4];ctx.fillRect(x,y,20+i%5*27,4+i%4*8)}
  for(let i=0;i<pixels.data.length;i+=4){const value=Math.random()*255;pixels.data[i]=value*.8;pixels.data[i+1]=value*.9;pixels.data[i+2]=value;pixels.data[i+3]=255}nctx.putImageData(pixels,0,0);ctx.globalAlpha=.18;ctx.imageSmoothingEnabled=false;ctx.drawImage(noise,0,0,width,height);ctx.globalAlpha=1;
  if(!motion.matches&&tick%4===0){const y=(tick*43)%height,h=8+tick%41;ctx.drawImage(canvas,0,y*canvas.height/height,canvas.width,h*canvas.height/height,tick%8===0?-45:32,y,width,h)}
  updatePanels();
 }
 function sync(){clearInterval(timer);timer=null;if(screen.hidden){VigiaFeedback.stopDeadline();return}if(document.hidden)return;resize();tick=0;draw();timer=setInterval(draw,motion.matches?500:120)}
 new MutationObserver(sync).observe(screen,{attributes:true,attributeFilter:['hidden']});
 window.addEventListener('resize',()=>{if(!screen.hidden)resize()});document.addEventListener('visibilitychange',sync);motion.addEventListener('change',sync);sync();
})();
