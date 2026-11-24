import fs from 'node:fs';
import path from 'node:path';
import vm from 'node:vm';
import { pathToFileURL } from 'node:url';
import { root, publicDir, listFiles } from './paths.mjs';

export function checkPublic(directory = publicDir) {
  const files = listFiles(directory);
  const exact = new Set(files);
  const folded = new Map();
  const issues = [];
  let references = 0;
  let bytes = 0;
  const ignore = /^(?:[a-z][a-z\d+.-]*:|\/\/|#)/i;
  const reference = (from, raw) => {
    const value = raw.trim().replaceAll('&amp;', '&');
    if (!value || ignore.test(value) || value.includes('${')) return;
    const clean = value.split(/[?#]/)[0];
    if (!clean) return;
    let decoded;
    try { decoded = decodeURIComponent(clean); } catch { issues.push(`URL inválida em ${from}: ${raw}`); return; }
    const resolved = path.posix.normalize(decoded.startsWith('/') ? decoded.slice(1) : path.posix.join(path.posix.dirname(from), decoded));
    references++;
    if (resolved.startsWith('../') || resolved === '..') {
      issues.push(`Referência fora da área pública: ${from} → ${raw}`);
    } else if (!exact.has(resolved) && !exact.has(resolved.replace(/\/$/, '') + '/index.html')) {
      const same = files.find(file => file.toLowerCase() === resolved.toLowerCase());
      issues.push(same ? `Capitalização: ${from} → ${resolved}; arquivo: ${same}` : `Referência ausente: ${from} → ${resolved}`);
    }
  };
  for (const file of files) {
    const low = file.toLowerCase();
    if (folded.has(low)) issues.push(`Colisão de nomes: ${folded.get(low)} / ${file}`);
    folded.set(low, file);
    const target = path.join(directory, file);
    const size = fs.statSync(target).size;
    bytes += size;
    if (!size) issues.push(`Arquivo vazio: ${file}`);
    if (size >= 100 * 1024 * 1024) issues.push(`Arquivo excede o limite do GitHub: ${file}`);
    if (/(?:^|\/)(?:acervo|privado|node_modules|\.git|\.env)(?:\/|$)/i.test(file) || /(?:OPERACAO_EQUIPE|GABARITO|INVENTARIO_ORIGEM)/i.test(file)) issues.push(`Arquivo da equipe na área pública: ${file}`);
    if (/\.(html|css|js)$/.test(file)) {
      const source = fs.readFileSync(target, 'utf8');
      if (file.endsWith('.html')) {
        for (const match of source.matchAll(/\b(?:src|href|poster)\s*=\s*["']([^"']+)["']/gi)) reference(file, match[1]);
      }
      if (file.endsWith('.css')) {
        for (const match of source.matchAll(/url\(\s*(["']?)([^)'"\s]+)\1\s*\)/gi)) reference(file, match[2]);
      }
      if (file.endsWith('.js')) {
        for (const match of source.matchAll(/["']((?:(?:\.\.\/)+)?(?:assets|audio|video|evidencias|encerramento)\/[^"'\n]*\.(?:png|jpg|jpeg|svg|woff2|wav|mp3|mp4|html)(?:\?[^"'\n]*)?)["']/gi)) reference(file, match[1]);
      }
    }
  }
  const box = { window: {} };
  vm.createContext(box);
  vm.runInContext(fs.readFileSync(path.join(directory, 'data.js'), 'utf8'), box, { timeout: 1000 });
  const data = box.window.CASE_DATA;
  for (const item of data.evidence) reference('index.html', item.file);
  for (const card of data.cards) if (card.image) reference('index.html', card.image);
  for (const file of ['video/Video_inicial.mp4', 'audio/audio01.wav', 'audio/audio02.wav', 'audio/audio03.wav', 'audio/final_completo.wav', 'audio/trilha/long-note-one.mp3', 'encerramento/filme/index.html']) reference('index.html', file);
  const config = JSON.parse(fs.readFileSync(path.join(root, 'vercel.json'), 'utf8'));
  if (config.framework !== null || config.outputDirectory !== 'dist' || config.buildCommand !== 'npm run build') issues.push('Configuração da Vercel incompatível com esta entrega.');
  if (issues.length) throw new Error(issues.join('\n'));
  return { result: 'passed', files: files.length, references, bytes, evidence: data.evidence.length };
}

if (process.argv[1] && import.meta.url === pathToFileURL(path.resolve(process.argv[1])).href) {
  try { console.log(JSON.stringify(checkPublic(), null, 2)); }
  catch (error) { console.error(error.message); process.exitCode = 1; }
}
