import path from 'node:path';
import { fileURLToPath } from 'node:url';
import fs from 'node:fs';

export const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..');
export const publicDir = path.join(root, 'public');
export const distDir = path.join(root, 'dist');

export function listFiles(directory, base = directory) {
  return fs.readdirSync(directory, { withFileTypes: true }).flatMap(entry => {
    const target = path.join(directory, entry.name);
    if (entry.isSymbolicLink()) throw new Error(`Link simbólico não permitido: ${target}`);
    return entry.isDirectory() ? listFiles(target, base) : [path.relative(base, target).split(path.sep).join('/')];
  }).sort();
}
