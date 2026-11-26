(()=>{
 'use strict';
 const browserControlKeys=new Set(['KeyL','KeyN','KeyR','KeyS','KeyT','KeyW']);
 const browserActionKeys=new Set(['F5','F11','F12','BrowserBack','BrowserForward','BrowserHome','BrowserRefresh']);

 function blocksBrowser(event){
  const {code,key,ctrlKey,altKey,metaKey,shiftKey}=event;
  if(browserActionKeys.has(key))return true;
  if(altKey&&!ctrlKey&&!metaKey&&['ArrowLeft','ArrowRight','Home','F4'].includes(key))return true;
  if((ctrlKey||metaKey)&&!altKey&&browserControlKeys.has(code))return true;
  if(ctrlKey&&!altKey&&(['Tab','PageUp','PageDown'].includes(key)||/^Digit[1-9]$/.test(code)))return true;
  return (ctrlKey||metaKey)&&!altKey&&shiftKey&&['KeyI','KeyJ','KeyC'].includes(code);
 }

 function appShortcut(event,taskApps){
  const {code,ctrlKey,altKey,metaKey,shiftKey}=event;
  if(ctrlKey||shiftKey||metaKey===altKey)return null;
  if(metaKey&&code==='KeyE')return 'files';
  const digit=/^Digit([1-4])$/.exec(code);
  return digit?taskApps[Number(digit[1])-1]??null:null;
 }

 function operatorShortcut(event){
  return event.ctrlKey&&event.shiftKey&&!event.altKey&&!event.metaKey&&event.code==='KeyO';
 }

 window.VigiaKeyboard={blocksBrowser,appShortcut,operatorShortcut};
})();
