import test from 'node:test';
import assert from 'node:assert/strict';
import { game } from './helpers.mjs';

test('bônus são únicos e não valem depois da expiração', () => {
  const t = game().VigiaCountdown.create();
  assert.equal(t.remaining(0), 750);
  for (const stage of ['identity', 'access', 'chronology']) {
    assert.equal(t.award(stage, 0).added, 15);
    assert.equal(t.award(stage, 1), null);
  }
  assert.equal(t.award('protocol', 0), null);
  assert.equal(t.totalBonus(), 45);
  assert.equal(t.remaining(794.5), 1);
  assert.equal(t.remaining(795), 0);
  assert.equal(t.award('identity', 795), null);
  t.reset();
  assert.equal(t.totalBonus(), 0);
  assert.equal(t.remaining(0), 750);
});

test('configuração de duração, bônus e limites', () => {
  const create = game().VigiaCountdown.create;
  const custom = create({ durationSeconds: 305, bonusEnabled: true, bonusSeconds: 42 });
  assert.equal(custom.remaining(4.5), 301);
  assert.equal(custom.award('identity', 5).added, 42);
  assert.equal(custom.remaining(5), 342);
  custom.configure({ durationSeconds: 80, bonusEnabled: false, bonusSeconds: 30 });
  assert.equal(custom.award('identity', 0), null);
  assert.equal(custom.remaining(0), 80);
  assert.equal(create({ durationSeconds: 20, bonusSeconds: 0 }).award('identity', 0), null);
  assert.equal(create({ durationSeconds: 1 }).remaining(0), 1);
  assert.equal(create({ durationSeconds: 10859, bonusSeconds: 300 }).award('identity', 0).added, 300);
  for (const durationSeconds of [0, 10860, NaN, 4.5]) assert.equal(create({ durationSeconds }).remaining(0), 750);
  for (const bonusSeconds of [-1, 301, NaN, 2.5]) assert.equal(create({ bonusSeconds }).award('identity', 0).added, 15);
});

test('alertas não se repetem no mesmo segundo', () => {
  const t = game().VigiaCountdown.create();
  assert.equal(t.signal(690), 'warning');
  assert.equal(t.signal(690.5), null);
  assert.equal(t.signal(705), null);
  assert.equal(t.signal(720), 'warning');
  assert.equal(t.signal(730), null);
  assert.equal(t.signal(735), 'warning');
  for (let i = 10; i > 0; i--) assert.equal(t.signal(750 - i), 'urgent');
  assert.equal(t.signal(750), 'expired');
  assert.equal(t.signal(751), null);
});
