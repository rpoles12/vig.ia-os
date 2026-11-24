import fs from 'node:fs';
import path from 'node:path';
import vm from 'node:vm';
import { publicDir } from '../scripts/paths.mjs';

export function game() {
  const box = {};
  box.window = box;
  vm.createContext(box);
  for (const file of ['data.js', 'vigia.js', 'engine.js', 'countdown.js']) vm.runInContext(fs.readFileSync(path.join(publicDir, file), 'utf8'), box);
  return box;
}

export function submit(engine, id, data, valid = true) {
  if (id === 'identity') return engine.validarIdentidade(valid ? data.key.answers.identity[1] : 'pessoa sem vínculo');
  if (id === 'access') return engine.validarAcessos({ fisico: valid ? 'Helena Duarte' : 'Marcelo', digital: 'Marcelo Vieira' });
  if (id === 'chronology') return engine.validarCronologia(valid ? data.key.correct_order : [...data.key.correct_order].reverse());
  return engine.validarProtocolo({ identidade: data.key.answers.identity[0], credencial: data.key.answers.credential[0], horario: valid ? data.key.answers.critical_time[0] : '00:00' });
}
