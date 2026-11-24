import test from 'node:test';
import assert from 'node:assert/strict';
import { game, submit } from './helpers.mjs';

test('progressão completa aceita respostas sem leitura prévia e mantém o catálogo esperado', () => {
  const b = game(), data = b.CASE_DATA, e = b.VigiaEngine.criarVigia(data.vigia, data.key);
  const available = () => data.evidence.filter(x => x.stage === 0 || x.stage === 1 && e.estado().identityConfirmed || x.stage === 2 && e.estado().accessesConfirmed || x.stage === 3 && e.estado().chronologyOrdered).length;
  assert.equal(data.evidence.length, 25);
  assert.equal(e.estado().memory, 8);
  assert.equal(available(), 8);
  assert.equal(submit(e, 'access', data).ok, false);
  assert.equal(submit(e, 'chronology', data).ok, false);
  assert.equal(submit(e, 'protocol', data).ok, false);
  for (const [i, id] of ['identity', 'access', 'chronology', 'protocol'].entries()) {
    assert.equal(submit(e, id, data, false).ok, false);
    assert.equal(submit(e, id, data).ok, true);
    assert.equal(e.estado().memory, [34, 67, 67, 100][i]);
    assert.equal(available(), [23, 24, 25, 25][i]);
    assert.equal(e.estado().evidenceSeen.length, 0);
  }
  assert.equal(e.estado().protocolConfirmed, true);
  e.reiniciar();
  assert.equal(e.estado().memory, 8);
  assert.equal(e.estado().protocolConfirmed, false);
});

for (let mask = 1; mask < 16; mask++) {
  test(`seleção de etapas: combinação ${mask}/15`, () => {
    const b = game(), data = b.CASE_DATA, defs = Array.from(b.VigiaEngine.stages);
    const selected = defs.filter((_, i) => mask & (1 << i)).map(stage => stage.id);
    const e = b.VigiaEngine.criarVigia(data.vigia, data.key, { stages: selected });
    let previous = 8;
    assert.equal(e.estado().memory, 8);
    for (const stage of defs.filter(stage => !selected.includes(stage.id))) assert.equal(submit(e, stage.id, data).ok, false);
    for (const [i, id] of selected.entries()) {
      if (selected[i + 1]) assert.equal(submit(e, selected[i + 1], data).ok, false);
      assert.equal(submit(e, id, data, false).ok, false);
      assert.equal(submit(e, id, data).ok, true);
      const state = e.estado();
      assert.ok(state.memory >= previous);
      assert.equal(e.perfilIA().memory, state.memory);
      assert.equal(e.orientar('qual é a próxima etapa?').memory, state.memory);
      assert.equal(state.evidenceSeen.length, 0);
      previous = state.memory;
    }
    assert.equal(e.estado().memory, 100);
    assert.equal(e.estado().protocolConfirmed, true);
    e.reiniciar();
    assert.equal(e.estado().memory, 8);
    assert.equal(e.estado().protocolConfirmed, false);
  });
}

test('etapas inválidas são recusadas', () => {
  const b = game(), d = b.CASE_DATA;
  for (const stages of [[], ['inexistente'], null]) assert.throws(() => b.VigiaEngine.criarVigia(d.vigia, d.key, { stages }));
});

test('assistente aponta caminhos locais e acompanha a memória', () => {
  const b = game(), d = b.CASE_DATA, e = b.VigiaEngine.criarVigia(d.vigia, d.key);
  for (const query of ['onde encontro os documentos?', 'onde registro minha resposta?', 'quanto tempo temos?', 'como mover os cartões?', 'nao entendi o horario', 'qual documento comparar?']) {
    const response = e.orientar(query);
    assert.ok(response.text.length > 20);
    assert.equal(response.memory, 8);
    assert.equal(response.text.includes(d.key.answers.generated_protocol), false);
  }
  submit(e, 'identity', d);
  assert.equal(e.perfilIA().memory, 34);
  submit(e, 'access', d);
  assert.equal(e.perfilIA().memory, 67);
});
