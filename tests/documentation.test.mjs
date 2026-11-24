import test from 'node:test';
import assert from 'node:assert/strict';
import fs from 'node:fs';
import path from 'node:path';
import { root, listFiles } from '../scripts/paths.mjs';

test('links locais da documentação vigente apontam para arquivos existentes', () => {
  const markdown = ['README.md', 'CHANGELOG.md', 'LICENCAS.md', ...['docs', 'materiais'].flatMap(dir => listFiles(path.join(root, dir)).filter(file => file.endsWith('.md')).map(file => `${dir}/${file}`))];
  const failures = [];
  for (const relative of markdown) {
    const source = fs.readFileSync(path.join(root, relative), 'utf8');
    const links = [...source.matchAll(/\]\(([^)]+)\)/g)].map(match => match[1]);
    links.push(...[...source.matchAll(/<img[^>]+src="([^"]+)"/g)].map(match => match[1]));
    for (const link of links) {
      if (/^(?:[a-z][a-z\d+.-]*:|#|\/\/)/i.test(link)) continue;
      const target = path.resolve(root, path.dirname(relative), link.split('#')[0]);
      if (!fs.existsSync(target)) failures.push(`${relative} → ${link}`);
    }
  }
  assert.deepEqual(failures, []);
});
