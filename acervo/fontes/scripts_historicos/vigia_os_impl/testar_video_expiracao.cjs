const fs=require('fs'),path=require('path'),assert=require('assert'),{pathToFileURL}=require('url'),{chromium}=require('playwright');
const root=path.resolve(__dirname,'../..');
(async()=>{
 const browser=await chromium.launch({channel:'chrome',headless:true});const page=await browser.newPage({viewport:{width:1440,height:900}});
 try{
 await page.goto(pathToFileURL(path.join(root,'output/vigia_os_sistema/index.html')).href);
 await page.locator('#session-settings-open').click();await page.locator('#settings-login').fill('admin');await page.locator('#settings-password').fill('verset.dev');await page.locator('#settings-auth button.primary').click();await page.locator('#settings-minutes').fill('0');await page.locator('#settings-seconds').fill('3');await page.locator('#settings-auto-narration').uncheck();await page.locator('#settings-time-warnings').uncheck();await page.locator('#settings-form button.primary').click();
 await page.locator('#start').click();await page.locator('#intro-film-start').click();await page.evaluate(()=>document.querySelector('#intro-film-player').playbackRate=16);await page.waitForFunction(()=>VigiaIntroVideo.finished,{},{timeout:20000});
 await page.locator('.desktop-shortcut[data-app=introvideo]').click();await page.evaluate(()=>document.querySelector('#intro-replay-player').requestFullscreen());
 await page.waitForFunction(()=>!document.querySelector('#time-up').hidden,{},{timeout:6000});
 await page.waitForFunction(()=>document.fullscreenElement!==document.querySelector('#intro-replay-player'));
 const result=await page.evaluate(()=>({paused:document.querySelector('#intro-replay-player').paused,timeUp:!document.querySelector('#time-up').hidden,cursor:getComputedStyle(document.querySelector('#time-up')).cursor,timer:document.querySelector('#timer').textContent}));assert.deepStrictEqual(result,{paused:true,timeUp:true,cursor:'none',timer:'00:00'});
 fs.writeFileSync(path.join(root,'tmp/vigia_os_impl/fluxo_video/EXPIRACAO_VIDEO.json'),JSON.stringify(result,null,2));console.log(JSON.stringify(result));
 }finally{await browser.close()}
})().catch(e=>{console.error(e.stack);process.exit(1)});
