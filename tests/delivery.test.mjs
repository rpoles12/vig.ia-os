import test from 'node:test';
import assert from 'node:assert/strict';
import fs from 'node:fs';
import path from 'node:path';
import { root, publicDir } from '../scripts/paths.mjs';
import { checkPublic } from '../scripts/check.mjs';
import { createStaticServer } from '../scripts/serve.mjs';

test('referências e estrutura pública estão completas', () => {
  const result = checkPublic();
  assert.equal(result.result, 'passed');
  assert.equal(result.evidence, 25);
  assert.ok(result.references > 100);
  assert.ok(result.files > 100);
});

test('documentação e material de impressão não entram na saída pública', () => {
  assert.equal(fs.existsSync(path.join(publicDir, 'OPERACAO_EQUIPE.md')), false);
  assert.equal(fs.existsSync(path.join(publicDir, 'README.md')), false);
  const ignore = fs.readFileSync(path.join(root, '.gitignore'), 'utf8');
  assert.doesNotMatch(ignore, /^\/acervo\//m);
  const vercelIgnore = fs.readFileSync(path.join(root, '.vercelignore'), 'utf8');
  assert.match(vercelIgnore, /^acervo\//m);
  const manifest = JSON.parse(fs.readFileSync(path.join(root, 'package.json'), 'utf8'));
  assert.equal(manifest.engines.node, '24.x');
  assert.equal(manifest.private, true);
  assert.equal(Object.keys(manifest.dependencies || {}).length, 0);
  for (const name of ['README.md', 'JOGO.md', 'PUBLICACAO.md', 'ARQUITETURA.md', 'CONTEXTO.md', 'TESTES.md']) {
    const file = name === 'README.md' ? path.join(root, name) : path.join(root, 'docs', name);
    assert.ok(fs.statSync(file).size > 1000);
  }
});

test('HTTP serve mídia, HEAD e intervalos, sem expor arquivos de fora da área pública', async () => {
  const server = createStaticServer();
  await new Promise(resolve => server.listen(0, '127.0.0.1', resolve));
  const base = `http://127.0.0.1:${server.address().port}`;
  try {
    const home = await fetch(base);
    assert.equal(home.status, 200);
    assert.match(home.headers.get('content-type'), /^text\/html/);
    assert.match(await home.text(), /VIG\.IA/);
    const video = await fetch(base + '/video/Video_inicial.mp4', { method: 'HEAD' });
    assert.equal(video.status, 200);
    assert.equal(video.headers.get('content-type'), 'video/mp4');
    assert.equal(Number(video.headers.get('content-length')), fs.statSync(path.join(publicDir, 'video/Video_inicial.mp4')).size);
    assert.equal((await video.arrayBuffer()).byteLength, 0);
    const part = await fetch(base + '/video/Video_inicial.mp4', { headers: { range: 'bytes=0-31' } });
    assert.equal(part.status, 206);
    assert.equal((await part.arrayBuffer()).byteLength, 32);
    const suffix = await fetch(base + '/video/Video_inicial.mp4', { headers: { range: 'bytes=-16' } });
    assert.equal(suffix.status, 206);
    assert.equal((await suffix.arrayBuffer()).byteLength, 16);
    const invalid = await fetch(base + '/video/Video_inicial.mp4', { headers: { range: 'bytes=999999999-' } });
    assert.equal(invalid.status, 416);
    for (const url of ['/README.md', '/acervo/README.md', '/materiais/impressao/', '/.git/config', '/%2e%2e%5cREADME.md', '/inexistente.js']) assert.equal((await fetch(base + url)).status, 404);
    assert.equal((await fetch(base, { method: 'POST' })).status, 405);
  } finally { server.closeAllConnections(); await new Promise(resolve => server.close(resolve)); }
});
