(()=>{
 'use strict';
 const defaults=Object.freeze({durationSeconds:750,bonusEnabled:true,bonusSeconds:15});
 function normalize(options={}){return {durationSeconds:Number.isInteger(options.durationSeconds)&&options.durationSeconds>=1&&options.durationSeconds<=10859?options.durationSeconds:defaults.durationSeconds,bonusEnabled:typeof options.bonusEnabled==='boolean'?options.bonusEnabled:defaults.bonusEnabled,bonusSeconds:Number.isInteger(options.bonusSeconds)&&options.bonusSeconds>=0&&options.bonusSeconds<=300?options.bonusSeconds:defaults.bonusSeconds}}
 function create(options={}){
  let settings=normalize(options);
  const stages=new Set();let bonus=0,lastSecond=null;
  const remaining=elapsed=>Math.max(0,Math.ceil(settings.durationSeconds+bonus-Math.max(0,elapsed)));
  return {
   remaining,
   award(stage,elapsed){if(!settings.bonusEnabled||settings.bonusSeconds===0||!['identity','access','chronology'].includes(stage)||stages.has(stage)||remaining(elapsed)===0)return null;stages.add(stage);bonus+=settings.bonusSeconds;return {stage,added:settings.bonusSeconds,remaining:remaining(elapsed),totalBonus:bonus}},
   signal(elapsed){
    const left=remaining(elapsed), previous=lastSecond;
    lastSecond=left;
    if(previous!==null&&left>=previous)return null;
    if(left===0)return 'expired';
    if(left<=10)return 'urgent';
    if([15,30,60].some(mark=>left===mark||(previous!==null&&previous>mark&&left<mark)))return 'warning';
    return null;
   },
   reset(){stages.clear();bonus=0;lastSecond=null},
   configure(options){settings=normalize(options);this.reset()},
   totalBonus:()=>bonus
  }
 }
 window.VigiaCountdown={create,defaults};
})();
