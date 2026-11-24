import fs from 'node:fs';
import path from 'node:path';
import { root, publicDir, distDir, listFiles } from './paths.mjs';
import { checkPublic } from './check.mjs';

const result = checkPublic();
// O único alvo descartável é <raiz>/dist. Nunca remover a pasta de origem.
if (path.resolve(distDir) !== path.join(root, 'dist') || path.dirname(distDir) !== root) throw new Error('Saída fora da raiz da entrega.');
if (fs.existsSync(distDir) && fs.lstatSync(distDir).isSymbolicLink()) throw new Error('dist não pode ser um link simbólico.');
fs.rmSync(distDir, { recursive: true, force: true });
fs.cpSync(publicDir, distDir, { recursive: true, dereference: false, errorOnExist: true });
if (JSON.stringify(listFiles(publicDir)) !== JSON.stringify(listFiles(distDir))) throw new Error('A saída difere do conteúdo público.');
console.log(`Construção concluída: ${result.files} arquivos, ${(result.bytes / 1024 / 1024).toFixed(1)} MiB. Somente public/ foi copiada para dist/.`);
