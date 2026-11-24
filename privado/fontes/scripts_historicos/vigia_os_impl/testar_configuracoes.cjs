const fs=require('fs'),vm=require('vm'),assert=require('assert'),path=require('path');
const root=path.resolve(__dirname,'../..'),box={window:{}};vm.createContext(box);vm.runInContext(fs.readFileSync(path.join(root,'output/vigia_os_sistema/countdown.js'),'utf8'),box);
let checks=0;function eq(actual,expected){assert.deepStrictEqual(actual,expected);checks++}
const create=box.window.VigiaCountdown.create;
const custom=create({durationSeconds:305,bonusEnabled:true,bonusSeconds:42});
eq(custom.remaining(0),305);eq(custom.remaining(4.5),301);eq(custom.award('identity',5).added,42);eq(custom.remaining(5),342);eq(custom.award('identity',6),null);eq(custom.award('protocol',6),null);eq(custom.award('access',10).added,42);eq(custom.award('chronology',10).added,42);eq(custom.totalBonus(),126);eq(custom.remaining(431),0);eq(custom.award('access',431),null);
custom.reset();eq(custom.remaining(0),305);eq(custom.totalBonus(),0);eq(custom.award('identity',0).added,42);
custom.configure({durationSeconds:80,bonusEnabled:false,bonusSeconds:30});eq(custom.remaining(0),80);eq(custom.award('identity',0),null);eq(custom.totalBonus(),0);eq(custom.signal(20),'warning');eq(custom.signal(70),'urgent');eq(custom.signal(80),'expired');eq(custom.signal(81),null);
const zero=create({durationSeconds:20,bonusEnabled:true,bonusSeconds:0});eq(zero.award('identity',0),null);eq(zero.remaining(0),20);eq(zero.totalBonus(),0);
const minimum=create({durationSeconds:1,bonusEnabled:false});eq(minimum.remaining(0),1);eq(minimum.signal(0),'urgent');eq(minimum.signal(1),'expired');eq(minimum.award('identity',1),null);
const maximum=create({durationSeconds:10859,bonusSeconds:300});eq(maximum.remaining(0),10859);eq(maximum.award('identity',0).added,300);
for(const options of [{durationSeconds:0,bonusSeconds:-1},{durationSeconds:10860,bonusSeconds:301},{durationSeconds:NaN,bonusSeconds:NaN},{durationSeconds:4.5,bonusSeconds:2.5}]){const timer=create(options);eq(timer.remaining(0),750);eq(timer.award('identity',0).added,15)}
const report={date:'2026-11-19',result:'passed',checks,coverage:['Duração e bônus personalizados','Bônus desativado e zero','Acerto único por etapa e expiração','Limites e valores inválidos','Reinício mantém configuração e limpa bônus']};fs.writeFileSync(path.join(root,'tmp/vigia_os_impl/configuracoes.json'),JSON.stringify(report,null,2));console.log(JSON.stringify(report));
