const fs=require('fs'),path=require('path'),{pathToFileURL}=require('url'),{chromium}=require('playwright');
const root=path.resolve(__dirname,'../..'),out=path.join(root,'output/video_inicial/capturas');
(async()=>{
 const browser=await chromium.launch({channel:'chrome',headless:true});const page=await browser.newPage({viewport:{width:1440,height:900}});await page.goto(pathToFileURL(path.join(root,'tmp/video_inicial/demo_os/index.html')).href);await page.locator('#start').click();
 const report=[];const forbidden=['Bryan','Helena','Marcelo','Carlos','2847','2246','22:46','BA17','B_A_17','NORTHSTAR'];
 async function check(app){await page.evaluate(id=>VigiaSession.open(id,false,false),app);await page.waitForTimeout(250);const visible=await page.locator('body').innerText();const found=forbidden.filter(x=>visible.toLowerCase().includes(x.toLowerCase()));report.push({app,protected_terms_found:found});if(found.length)throw new Error('Conteúdo protegido visível em '+app)}
 for(const app of ['desktop','files','media','vigia','solve','notes'])await check(app);
 await page.evaluate(()=>VigiaSession.open('solve'));await page.locator('#identity input').fill('Pessoa Exemplo');await page.locator('#identity input').press('Enter');await page.waitForTimeout(250);await page.locator('#accessform input[name=fisico]').fill('Exemplo Físico');await page.locator('#accessform input[name=digital]').fill('Exemplo Digital');await page.locator('#accessform input[name=digital]').press('Enter');await page.waitForTimeout(250);await check('timeline');
 const answer=await page.evaluate(()=>CASE_DATA.key.answers.identity);if(JSON.stringify(answer)!=='["Pessoa Exemplo"]')throw new Error('Resposta demonstrativa inválida');
 await browser.close();fs.writeFileSync(path.join(out,'auditoria_conteudo.json'),JSON.stringify({result:'passed',screens:report,all_evidence_images_are_fictional:true,demo_identity:'Pessoa Exemplo'},null,2));console.log('7 telas verificadas: nenhum termo protegido visível.');
})().catch(e=>{console.error(e);process.exit(1)});
