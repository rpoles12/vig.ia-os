(()=>{
 'use strict';
 const $=s=>document.querySelector(s),desktop=$('#os-desktop'),host=$('#desktop-shortcuts'),buttons=[...host.querySelectorAll('.desktop-shortcut')];
 const positions=new Map();let drag=null,suppressClickUntil=0,menuTarget=null,returnFocus=null;
 const glyph=id=>VigiaIcons.svg(id);
 function blocked(){return document.body.classList.contains('session-locked')||document.body.classList.contains('final-flow')||document.body.classList.contains('investigation-expired')||!!document.querySelector('dialog:modal')}
 function bounds(){return {width:host.clientWidth,height:host.clientHeight}}
 let grid=null;
 const gridLayer=document.createElement('div');gridLayer.className='desktop-grid';gridLayer.setAttribute('aria-hidden','true');host.prepend(gridLayer);
 const key=cell=>cell.col+':'+cell.row;
 function nearest(cells,point){return cells.reduce((best,cell)=>!best||Math.hypot(cell.col-point.col,cell.row-point.row)<Math.hypot(best.col-point.col,best.row-point.row)?cell:best,null)}
 function paint(){buttons.forEach(button=>{const cell=positions.get(button.dataset.app);if(cell)put(button,{x:grid.margin+cell.col*grid.stepX,y:grid.margin+cell.row*grid.stepY})})}
 function put(button,point){button.style.left=point.x+'px';button.style.top=point.y+'px'}
 function layout(){
  const box=bounds(),first=buttons[0],gap=12,margin=Math.min(20,box.width*.04,box.height*.04);
  buttons.forEach(button=>{button.style.removeProperty('width');button.style.removeProperty('height')});
  let width=first.offsetWidth,height=first.offsetHeight;
  const cols=Math.max(1,Math.floor((box.width-margin*2+gap)/(width+gap)));
  let rows=Math.max(1,Math.floor((box.height-margin*2+gap)/(height+gap)));
  if(cols*rows<buttons.length){rows=Math.ceil(buttons.length/cols);height=Math.max(1,(box.height-margin*2-gap*(rows-1))/rows)}
  width=Math.min(width,Math.max(1,box.width-margin*2));
  buttons.forEach(button=>{button.style.width=width+'px';button.style.height=height+'px'});
  const cells=Array.from({length:cols*rows},(_,i)=>({col:i%cols,row:Math.floor(i/cols)}));
  grid={margin,stepX:width+gap,stepY:height+gap,cols,rows,cells};
  const initialColumns=Math.min(cols,Math.max(2,Math.ceil(buttons.length/rows))),used=new Set(),next=new Map();
  // Reserve valid saved cells before placing icons displaced by a smaller viewport.
  buttons.forEach(button=>{const id=button.dataset.app,cell=positions.get(id);if(cell&&cell.col<cols&&cell.row<rows&&!used.has(key(cell))){next.set(id,cell);used.add(key(cell))}});
  buttons.forEach((button,i)=>{const id=button.dataset.app;if(next.has(id))return;const preferred=positions.get(id)||{col:i%initialColumns,row:Math.floor(i/initialColumns)},cell=nearest(cells.filter(cell=>!used.has(key(cell))),preferred);next.set(id,cell);used.add(key(cell))});
  positions.clear();next.forEach((cell,id)=>positions.set(id,cell));paint();
  gridLayer.replaceChildren(...cells.map(cell=>{const tile=document.createElement('i');tile.style.cssText=`left:${margin+cell.col*grid.stepX}px;top:${margin+cell.row*grid.stepY}px;width:${width}px;height:${height}px`;tile.dataset.cell=key(cell);return tile}))
 }
 function select(button){buttons.forEach(item=>item.classList.toggle('is-selected',item===button))}
 function finish(cancel=false){
  if(!drag)return;const current=drag;drag=null;
  if(current.moved){
   suppressClickUntil=performance.now()+350;
   if(cancel){positions.clear();current.snapshot.forEach((cell,id)=>positions.set(id,cell));paint()}
  }
  current.button.classList.remove('is-icon-dragging');document.body.classList.remove('is-dragging-icon');
  gridLayer.querySelectorAll('.is-grid-target').forEach(tile=>tile.classList.remove('is-grid-target'));
  if(current.button.hasPointerCapture(current.pointerId))current.button.releasePointerCapture(current.pointerId)
 }
 for(const button of buttons){
  button.draggable=false;
  button.addEventListener('dragstart',e=>e.preventDefault());
  button.addEventListener('pointerdown',e=>{
   if(e.button!==0||!e.isPrimary||blocked())return;finish(true);closeMenu();select(button);
   const original={x:parseFloat(button.style.left)||0,y:parseFloat(button.style.top)||0};
   drag={button,id:button.dataset.app,pointerId:e.pointerId,startX:e.clientX,startY:e.clientY,original,snapshot:new Map(positions),moved:false}
  });
  button.addEventListener('lostpointercapture',()=>{if(drag?.button===button)finish(true)})
 }
 document.addEventListener('pointermove',e=>{
  if(!drag||e.pointerId!==drag.pointerId)return;
  if(blocked()){finish(true);return}
  if(!(e.buttons&1)){finish(true);return}
  const dx=e.clientX-drag.startX,dy=e.clientY-drag.startY;
  if(!drag.moved&&Math.hypot(dx,dy)<7)return;
  if(!drag.moved){drag.moved=true;drag.button.setPointerCapture(e.pointerId);drag.button.classList.add('is-icon-dragging');document.body.classList.add('is-dragging-icon')}
  e.preventDefault();
  const cell=nearest(grid.cells,{col:(drag.original.x+dx-grid.margin)/grid.stepX,row:(drag.original.y+dy-grid.margin)/grid.stepY});
  positions.clear();drag.snapshot.forEach((saved,id)=>positions.set(id,saved));
  const occupied=buttons.find(button=>button!==drag.button&&key(positions.get(button.dataset.app))===key(cell));
  if(occupied)positions.set(occupied.dataset.app,drag.snapshot.get(drag.id));
  positions.set(drag.id,cell);paint();
  gridLayer.querySelectorAll('i').forEach(tile=>tile.classList.toggle('is-grid-target',tile.dataset.cell===key(cell)))
 },{passive:false});
 document.addEventListener('pointerup',e=>{if(drag&&e.pointerId===drag.pointerId)finish(false)});
 document.addEventListener('pointercancel',e=>{if(drag&&e.pointerId===drag.pointerId)finish(true)});
 host.addEventListener('click',e=>{if(performance.now()<suppressClickUntil){e.preventDefault();e.stopImmediatePropagation()}},true);
 desktop.addEventListener('pointerdown',e=>{if(!e.target.closest('.desktop-shortcut'))select(null)});
 const menu=document.createElement('div');menu.id='desktop-context-menu';menu.hidden=true;menu.setAttribute('role','menu');menu.setAttribute('aria-label','Opções da área de trabalho');
 menu.innerHTML=`<button role="menuitem" data-context="open">${glyph('folder')}<span id="context-open-label">Abrir Arquivos</span></button><button role="menuitem" data-context="notes">${glyph('file')}<span>Próximos passos.txt</span></button><button role="menuitem" data-context="solve">${glyph('link')}<span>Registrar respostas</span></button><hr><button role="menuitem" data-context="arrange">${glyph('fit')}<span>Organizar ícones</span></button><button role="menuitem" data-context="refresh">${glyph('reset')}<span>Atualizar área de trabalho</span></button><small>Alterações válidas nesta partida</small>`;
 document.body.append(menu);
 function closeMenu(restore=false){menu.hidden=true;if(restore)returnFocus?.focus({preventScroll:true})}
 function showMenu(x,y,target){
  if(blocked())return;finish(true);window.VigiaDesktop?.closeMenus();
  menuTarget=target;returnFocus=target||buttons[0];if(target)select(target);
  $('#context-open-label').textContent='Abrir '+(target?target.textContent:'Arquivos');menu.hidden=false;
  const maxY=bounds().height-menu.offsetHeight-8,maxX=innerWidth-menu.offsetWidth-8;
  menu.style.left=Math.max(8,Math.min(x,maxX))+'px';menu.style.top=Math.max(8,Math.min(y,maxY))+'px';
  menu.querySelector('button').focus({preventScroll:true})
 }
 desktop.addEventListener('contextmenu',e=>{e.preventDefault();showMenu(e.clientX,e.clientY,e.target.closest('.desktop-shortcut'))});
 host.addEventListener('keydown',e=>{if(e.key==='ContextMenu'||e.shiftKey&&e.key==='F10'){e.preventDefault();const target=e.target.closest('.desktop-shortcut'),rect=(target||host).getBoundingClientRect();showMenu(rect.left+20,rect.top+32,target)}});
 menu.addEventListener('click',e=>{
  const item=e.target.closest('[data-context]');if(!item)return;
  const action=item.dataset.context,target=menuTarget?.dataset.app||'files';closeMenu();
  if(action==='arrange'){positions.clear();layout();select(null);window.VigiaDesktop?.remind('Ícones organizados.');return}
  if(action==='refresh'){layout();window.VigiaDesktop?.remind('Área de trabalho atualizada.');return}
  window.VigiaSession?.open(action==='open'?target:action==='notes'?'notes':'solve',true,true)
 });
 menu.addEventListener('keydown',e=>{
  const items=[...menu.querySelectorAll('button')],index=items.indexOf(document.activeElement);
  if(['ArrowDown','ArrowUp','Home','End'].includes(e.key)){e.preventDefault();const next=e.key==='Home'?0:e.key==='End'?items.length-1:(index+(e.key==='ArrowDown'?1:-1)+items.length)%items.length;items[next].focus()}
  if(e.key==='Tab')closeMenu()
 });
 document.addEventListener('pointerdown',e=>{if(!menu.contains(e.target))closeMenu()});
 window.addEventListener('keydown',e=>{if(e.key==='Escape'&&(drag?.moved||!menu.hidden)){e.preventDefault();e.stopImmediatePropagation();if(drag)finish(true);closeMenu(true)}},true);
 window.addEventListener('resize',()=>{finish(true);closeMenu();layout()});
 window.VigiaDesktopInteraction={closeMenu(){finish(true);closeMenu()},reset(){finish(true);closeMenu();positions.clear();select(null);layout()}};
 layout();
})();
