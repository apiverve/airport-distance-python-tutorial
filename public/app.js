import { api, busy, esc, showError, stats } from './ui.js';

const ROUTES = [
  ['JFK', 'LAX'],
  ['LHR', 'JFK'],
  ['SFO', 'NRT'],
  ['DXB', 'SIN'],
  ['SYD', 'LAX']
];

const form = document.getElementById('form');
const from = document.getElementById('from');
const to = document.getElementById('to');
const go = document.getElementById('go');
const result = document.getElementById('result');

const num = (n, digits = 0) => Number(n).toLocaleString(undefined, { maximumFractionDigits: digits });

document.getElementById('routes').innerHTML = ROUTES
  .map(([a, b]) => `<button type="button" data-a="${a}" data-b="${b}">${a} → ${b}</button>`)
  .join('');

document.getElementById('routes').addEventListener('click', (e) => {
  const chip = e.target.closest('button');
  if (!chip) return;
  from.value = chip.dataset.a;
  to.value = chip.dataset.b;
  form.requestSubmit();
});

document.getElementById('swap').addEventListener('click', () => {
  [from.value, to.value] = [to.value, from.value];
});

function place(airport) {
  const where = [airport.city, airport.state, airport.country].filter(Boolean).join(', ');
  return `<li><span>${esc(airport.iata)}</span>${esc(airport.name)} · ${esc(where)}</li>`;
}

// Some fields are for paid plans and come back empty on the free plan, so
// each one is optional here: the rows without a value are left out.
function hours(diff) {
  if (typeof diff !== 'number') return null;
  if (!diff) return 'Same time zone';
  const n = Math.abs(diff);
  return `${n} hour${n === 1 ? '' : 's'} ${diff > 0 ? 'ahead' : 'behind'}`;
}

form.addEventListener('submit', (e) => {
  e.preventDefault();
  const query = new URLSearchParams({ from: from.value.trim(), to: to.value.trim() });
  busy(go, 'Calculating…', async () => {
    try {
      const d = await api(`/api/distance?${query}`);
      result.innerHTML = `
        <div class="figure">
          <div class="big">${num(d.distanceMiles)} mi</div>
          <div class="sub">${num(d.distanceKm)} km${d.distanceNauticalMiles ? ` · ${num(d.distanceNauticalMiles)} nautical miles` : ''}</div>
        </div>
        ${stats([
          ['Flight time', d.estimatedFlightTime],
          ['Time difference', hours(d.timezoneDiffHours)],
          ['Heading', d.direction && `${d.direction} (${d.bearing}°)`],
          ['Route', typeof d.isInternational === 'boolean' ? (d.isInternational ? 'International' : 'Domestic') : null],
          ['CO₂ per passenger', d.carbonEstimateKg && `about ${num(d.carbonEstimateKg)} kg`]
        ])}
        ${d.airport1 && d.airport2 ? `<h2>Airports</h2><ul class="list">${place(d.airport1)}${place(d.airport2)}</ul>` : ''}`;
    } catch (err) {
      showError(result, err);
    }
  });
});
