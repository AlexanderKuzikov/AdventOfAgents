
const el = id => document.getElementById(id);

// переключение колонок EN / RU
for (const side of ['en', 'ru']) {
  const box = el('tgl-' + side);
  if (!box) continue;
  box.addEventListener('change', e =>
    document.body.classList.toggle('hide-' + side, !e.target.checked));
}

// печать
const printBtn = el('btn-print');
if (printBtn) printBtn.addEventListener('click', () => window.print());

// подсветка мест, где распознавание субтитров соврало
const markBtn = el('btn-mark');
if (markBtn) {
  markBtn.addEventListener('click', () => {
    const on = !document.body.classList.contains('show-fixes');
    document.body.classList.toggle('show-fixes', on);
    markBtn.textContent = on ? 'Скрыть исправления' : 'Показать исправления';
  });
}

// фильтр дней по тегу
const filters = el('filters');
if (filters) {
  const days = [...document.querySelectorAll('[data-tags]')];
  filters.addEventListener('click', e => {
    const btn = e.target.closest('button[data-tag]');
    if (!btn) return;
    const tag = btn.dataset.tag.toLowerCase();
    filters.querySelectorAll('button').forEach(b => b.classList.remove('on'));
    btn.classList.add('on');
    if (!tag) { days.forEach(d => d.classList.remove('hidden')); return; }
    days.forEach(d => d.classList.toggle('hidden', !d.dataset.tags.split('||').includes(tag)));
  });
}
