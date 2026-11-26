/* Conferência opcional em Chrome. Não é dependência da construção na Vercel. */
const fs = require('node:fs');
const path = require('node:path');
const assert = require('node:assert/strict');
const { chromium } = require('playwright');

const root = path.resolve(__dirname, '..');
const out = path.join(root, '.reports', 'browser');
fs.mkdirSync(out, { recursive: true });
let checks = 0;
const eq = (actual, expected) => { assert.deepEqual(actual, expected); checks++; };
const ok = value => { assert.ok(value); checks++; };

(async () => {
  const { createStaticServer } = await import('../scripts/serve.mjs');
  const server = createStaticServer(path.join(root, 'dist'));
  await new Promise(resolve => server.listen(0, '127.0.0.1', resolve));
  const base = `http://127.0.0.1:${server.address().port}`;
  let browser;
  try { browser = await chromium.launch({ channel: 'chrome', headless: true }); }
  catch (error) { await new Promise(resolve => server.close(resolve)); throw error; }
  const errors = [], failedRequests = [];
  const context = await browser.newContext({ viewport: { width: 1440, height: 900 } });
  context.on('page', page => {
    page.on('pageerror', error => errors.push(error.message));
    page.on('response', response => { if (response.status() >= 400 && !response.url().includes('arquivo_inexistente')) failedRequests.push(`${response.status()} ${new URL(response.url()).pathname}`); });
  });
  const page = await context.newPage();
  const timer = async p => (await p.locator('#timer').textContent()).trim();
  async function configure(p, seconds) {
    await p.goto(base);
    await p.locator('#session-settings-open').click();
    await p.locator('#settings-login').fill('admin');
    await p.locator('#settings-password').fill('verset.dev');
    await p.locator('#settings-auth button.primary').click();
    await p.locator('#settings-minutes').fill(String(Math.floor(seconds / 60)));
    await p.locator('#settings-seconds').fill(String(seconds % 60));
    await p.locator('#settings-auto-narration').uncheck();
    await p.locator('#settings-time-warnings').uncheck();
    await p.locator('#settings-form button.primary').click();
  }
  async function finishIntro(p) {
    await p.locator('#start').click();
    eq(await p.locator('#intro-film-player').evaluate(v => v.paused), true);
    await p.locator('#intro-film-start').click();
    await p.waitForFunction(() => document.querySelector('#intro-film-player').currentTime > .2);
    await p.evaluate(() => { document.querySelector('#intro-film-player').playbackRate = 16; });
    await p.waitForFunction(() => VigiaIntroVideo.finished && !VigiaIntroVideo.active, {}, { timeout: 20000 });
  }
  try {
    await configure(page, 120);
    eq(await timer(page), '02:00');
    eq(await page.locator('.desktop-shortcut').count(), 7);
    await page.locator('#start').click();
    eq(await page.locator('#intro-film-player').evaluate(v => v.paused), true);
    await page.waitForTimeout(1100);
    eq(await timer(page), '02:00');
    await page.locator('#intro-film-start').click();
    await page.waitForFunction(() => document.querySelector('#intro-film-player').currentTime > .4);
    eq(await page.locator('#intro-film-player').evaluate(v => ({ muted: v.muted, controls: v.controls, duration: Math.round(v.duration) })), { muted: false, controls: false, duration: 100 });
    await page.keyboard.press('Escape');
    eq(await page.locator('#intro-film').evaluate(d => d.open), true);
    eq(await timer(page), '02:00');
    await page.evaluate(() => { document.querySelector('#intro-film-player').currentTime = 99; });
    await page.waitForTimeout(150);
    ok(await page.locator('#intro-film-player').evaluate(v => v.currentTime < 20));
    await page.screenshot({ path: path.join(out, '01-tutorial.png') });
    await page.evaluate(() => { document.querySelector('#intro-film-player').playbackRate = 16; });
    await page.waitForFunction(() => VigiaIntroVideo.finished && !VigiaIntroVideo.active, {}, { timeout: 20000 });
    eq(await page.locator('body').getAttribute('data-view'), 'desktop');
    await page.waitForTimeout(1200);
    ok((await timer(page)) < '02:00');
    await page.screenshot({ path: path.join(out, '02-desktop.png') });
    const positions = await page.locator('.desktop-shortcut').evaluateAll(xs => xs.map(x => { const r = x.getBoundingClientRect(); return [r.x, r.y].join(':'); }));
    eq(new Set(positions).size, 7);
    await page.locator('.desktop-shortcut[data-app=introvideo]').click();
    await page.waitForFunction(() => document.querySelector('#intro-replay-player').currentTime > .3);
    eq(await page.locator('#intro-replay-player').getAttribute('src'), 'video/Video_inicial.mp4');
    await page.waitForFunction(() => document.querySelector('#ambient-track').dataset.mode === 'ducked');
    const beforeReplay = await timer(page);
    await page.waitForTimeout(1200);
    ok((await timer(page)) < beforeReplay);
    await page.locator('#app-introvideo [data-operation=maximize]').click();
    eq(await page.locator('#app-introvideo').evaluate(x => x.classList.contains('is-maximized')), true);
    await page.locator('#app-introvideo [data-operation=minimize]').click();
    await page.waitForTimeout(250);
    eq(await page.locator('#app-introvideo').isVisible(), false);
    await page.locator('#task-apps [data-task=introvideo]').click();
    eq(await page.locator('#app-introvideo').isVisible(), true);
    await page.locator('#app-introvideo [data-operation=close]').click();
    eq(await page.locator('#intro-replay-player').evaluate(v => v.paused), true);

    // Abrir documentos via interface e enviar respostas com Enter.
    await page.locator('.desktop-shortcut[data-app=files]').click();
    await page.locator('#library [data-evidence=L1]').click();
    eq(await page.locator('#viewer').evaluate(d => d.open), true);
    await page.keyboard.press('Escape');
    await page.locator('#task-apps [data-task=solve]').click();
    await page.locator('#identity input').fill('pessoa sem vínculo');
    await page.locator('#identity input').press('Enter');
    await page.locator('#identity .correlation-help').waitFor();
    checks++;
    const answers = await page.evaluate(() => CASE_DATA.key.answers);
    await page.locator('#identity input').fill(answers.identity[1]);
    await page.locator('#identity input').press('Enter');
    await page.locator('#accessform input[name=fisico]').waitFor({ state: 'visible' });
    eq(await page.locator('#time-bonus').isVisible(), true);
    await page.locator('#accessform input[name=fisico]').fill('Helena Duarte');
    await page.locator('#accessform input[name=digital]').fill('Marcelo Vieira');
    await page.locator('#accessform input[name=digital]').press('Enter');
    await page.locator('#cards li').first().waitFor({ state: 'visible' });
    const correct = await page.evaluate(() => CASE_DATA.key.correct_order);
    const current = await page.locator('#cards li').evaluateAll(xs => xs.map(x => x.dataset.event));
    if (JSON.stringify(current) === JSON.stringify(correct)) {
      await page.locator('#cards li').nth(0).locator('.drag-handle').click();
      await page.locator('#cards li').nth(1).locator('.drag-handle').click();
    }
    await page.locator('#checkorder').click();
    await page.locator('#timeline-work .correlation-help').waitFor();
    checks++;
    for (let i = 0; i < correct.length; i++) {
      const ids = await page.locator('#cards li').evaluateAll(xs => xs.map(x => x.dataset.event));
      if (ids[i] !== correct[i]) {
        await page.locator(`#cards li[data-event="${correct[i]}"] .drag-handle`).click();
        await page.locator('#cards li').nth(i).locator('.drag-handle').click();
      }
    }
    eq(await page.locator('#cards li').evaluateAll(xs => xs.map(x => x.dataset.event)), correct);
    await page.locator('#checkorder').click();
    await page.locator('#finalform input[name=identidade]').waitFor({ state: 'visible' });
    await page.locator('#finalform input[name=identidade]').fill(answers.identity[1]);
    await page.locator('#finalform input[name=credencial]').fill(answers.credential[0]);
    await page.locator('#finalform input[name=horario]').fill(answers.critical_time[0]);
    await page.locator('#finalform input[name=horario]').press('Enter');
    await page.waitForFunction(() => document.querySelector('#code-popup').open);
    eq((await page.locator('#code').textContent()).trim(), answers.generated_protocol);
    eq((await page.locator('#code-countdown').textContent()).trim(), '00:30');
    await page.keyboard.press('Escape');
    eq(await page.locator('#code-popup').evaluate(d => d.open), true);
    const frozen = await timer(page);
    // Conferir a expiração real dos 30s sem sintetizar fechamento.
    await page.waitForFunction(() => !document.querySelector('#code-popup').open, {}, { timeout: 33000 });
    eq((await page.locator('#code').textContent()).trim(), '');
    eq(await timer(page), frozen);
    await page.locator('#recovery-code').fill('XXXX-XXXX-XXXX');
    await page.locator('#recovery-code').press('Enter');
    ok((await page.locator('#recovery-error').textContent()).length > 0);
    await page.locator('#recovery-code').fill(answers.generated_protocol);
    await page.locator('#recovery-code').press('Enter');
    await page.waitForFunction(() => !document.querySelector('#ending-audio').paused);
    const frame = page.frameLocator('#ending-frame');
    await frame.locator('#stage').waitFor({ state: 'visible' });
    await page.screenshot({ path: path.join(out, '03-reconstituicao.png') });
    checks++;
    for (const item of await page.evaluate(() => CASE_DATA.evidence)) eq((await context.request.get(base + '/' + item.file)).status(), 200);

    await page.keyboard.press('Escape');
    await page.keyboard.press('Alt+1');
    eq(await page.locator('#reconstruction').evaluate(d => d.open), true);
    await page.locator('#ending-audio').evaluate(a => { a.currentTime = a.duration - .15; });
    await page.locator('#investigation-complete').waitFor();
    await page.keyboard.press('Escape');
    eq(await page.locator('#investigation-complete').evaluate(d => d.open), true);
    await page.locator('#replay-reconstruction').click();
    await page.waitForFunction(() => document.querySelector('#ending-audio').currentTime > 0);
    ok(await page.locator('#ending-audio').evaluate(a => a.currentTime < 5 && !a.paused));
    await page.locator('#ending-audio').evaluate(a => { a.currentTime = a.duration - .15; });
    await page.locator('#investigation-complete').waitFor();

    // Expiração durante replay e bloqueio de retorno por Esc.
    const expired = await context.newPage();
    await configure(expired, 16);
    await finishIntro(expired);
    await expired.locator('#deadline-popup').waitFor();
    eq((await expired.locator('#deadline-time').textContent()).trim(), '00:15');
    await expired.locator('.desktop-shortcut[data-app=introvideo]').click();
    await expired.evaluate(() => document.querySelector('#intro-replay-player').requestFullscreen());
    await expired.waitForFunction(() => document.querySelector('#deadline-popup').dataset.urgent === 'true', {}, { timeout: 9000 });
    await expired.waitForFunction(() => !document.querySelector('#time-up').hidden, {}, { timeout: 13000 });
    await expired.waitForFunction(() => document.fullscreenElement !== document.querySelector('#intro-replay-player'));
    await expired.keyboard.press('Escape');
    eq(await expired.locator('#time-up').isVisible(), true);
    eq(await expired.locator('#time-up').evaluate(x => getComputedStyle(x).cursor), 'none');
    eq(await expired.locator('#intro-replay-player').evaluate(v => v.paused), true);
    eq(await timer(expired), '00:00');
    await expired.screenshot({ path: path.join(out, '04-expiracao.png') });
    await expired.reload();
    eq(await expired.locator('#time-up').isVisible(), true);
    await expired.close();

    // A aba restaurada mantém o encerramento e oferece a recapitulação.
    await page.reload();
    eq(await page.locator('#investigation-complete').evaluate(d => d.open), true);
    eq(await page.locator('#intro').evaluate(d => d.open), false);
    eq(await page.evaluate(() => VigiaIntroVideo.finished), false);
    eq(errors, []);
    eq(failedRequests.filter(x => !x.endsWith('/favicon.ico')), []);
    const report = { date: new Date().toISOString(), result: 'passed', checks, pageErrors: errors, failedRequests, coverage: ['tutorial antes da contagem', 'replay e janelas', 'Enter e ajuda nos erros', 'ordenação acessível', 'código por 30s e inserção', 'reconstituição automática', '25 documentos por HTTP', 'expiração e Esc', 'reset das configurações'] };
    fs.writeFileSync(path.join(out, 'resultado.json'), JSON.stringify(report, null, 2));
    console.log(JSON.stringify(report, null, 2));
  } catch (error) {
    await page.screenshot({ path: path.join(out, 'FALHA.png') }).catch(() => {});
    throw error;
  } finally {
    await browser.close();
    server.closeAllConnections();
    await new Promise(resolve => server.close(resolve));
  }
})().catch(error => { console.error(error.stack); process.exitCode = 1; });
