// Quotes app with 'Included only' filter and IMF report number field
const DATA_URL = '../data/appendix.json';

const els = {
  country: document.getElementById('countrySelect'),
  year: document.getElementById('yearSelect'),
  incl: document.getElementById('inclSelect'),
  search: document.getElementById('searchInput'),
  clear: document.getElementById('clearBtn'),
  copyLink: document.getElementById('copyLinkBtn'),
  downloadCsv: document.getElementById('downloadCsvBtn'),
  results: document.getElementById('results'),
  summary: document.getElementById('summary'),
};

let raw = [];
let state = { iso3: '', year: '', q: '', included: '' };

init();

async function init(){
  const res = await fetch(DATA_URL);
  raw = await res.json();

  const p = new URLSearchParams(location.search);
  state.iso3 = p.get('iso3') || '';
  state.year = p.get('year') || '';
  state.q    = p.get('q') || '';
  state.included = p.get('included') || '';

  document.getElementById('searchInput').value = state.q;
  document.getElementById('inclSelect').value = state.included;

  populateFilters();
  bindEvents();
  render();
}

function populateFilters(){
  const countries = Array.from(new Map(raw.map(d => [d.iso3, d.country])).entries())
    .map(([iso3, country]) => ({ iso3, country }))
    .sort((a,b) => a.country.localeCompare(b.country));

  els.country.innerHTML = `<option value=''>All countries</option>` +
    countries.map(c => `<option value='${c.iso3}'>${c.country} (${c.iso3})</option>`).join('');
  els.country.value = state.iso3;

  const yearsSet = new Set(raw.map(d => d.year).filter(Boolean));
  const years = Array.from(yearsSet).sort((a,b) => a-b);
  els.year.innerHTML = `<option value=''>All years</option>` + years.map(y => `<option>${y}</option>`).join('');
  els.year.value = state.year;
}

function bindEvents(){
  els.country.addEventListener('change', () => { state.iso3 = els.country.value; syncURL(); render(); });
  els.year.addEventListener('change', () => { state.year = els.year.value; syncURL(); render(); });
  els.incl.addEventListener('change', () => { state.included = els.incl.value; syncURL(); render(); });
  els.search.addEventListener('input', debounce(() => { state.q = els.search.value.trim(); syncURL(); render(); }, 200));
  els.clear.addEventListener('click', () => {
    state = { iso3:'', year:'', q:'', included:'' };
    els.country.value=''; els.year.value=''; els.search.value=''; els.incl.value='';
    syncURL(); render();
  });
  els.copyLink.addEventListener('click', async () => {
    await navigator.clipboard.writeText(location.href);
    els.copyLink.textContent = 'Copied ✓'; setTimeout(()=> els.copyLink.textContent='Copy Link', 1200);
  });
  els.downloadCsv.addEventListener('click', () => downloadCsv(filterData(raw, state), 'quotes_filtered.csv'));
}

function render(){
  const data = filterData(raw, state);
  els.summary.textContent = `${data.length} result${data.length===1?'':'s'}${summarySuffix(state)}`;
  els.results.innerHTML = data.map(renderCard).join('');
}

function filterData(arr, st){
  const q = (st.q || '').toLowerCase();
  return arr.filter(d =>
    (!st.iso3 || d.iso3 === st.iso3) &&
    (!st.year || String(d.year) === String(st.year)) &&
    (!st.included || String(Boolean(d.included)) === st.included) &&
    (!q || [d.quote, d.source_title, d.motivation, d.imf_report_no || '', (d.tags||[]).join(' ')].join(' ').toLowerCase().includes(q))
  );
}

function renderCard(d){
  const tags = (d.tags||[]).map(t => `<span class="badge">${escapeHtml(t)}</span>`).join('');
  const size = (d.size_pct_gdp != null) ? ` · Size: ${d.size_pct_gdp}% GDP` : '';
  const srcTitle = d.source_title || 'IMF Staff Report';
  const report = d.imf_report_no ? ` • ${escapeHtml(d.imf_report_no)}` : '';
  const page = d.page ? `, ${escapeHtml(d.page)}` : '';
  return `<article class="card">
    <div class="meta"><b>${escapeHtml(d.country)}</b> • ${d.year ?? '—'} • ${(d.action_type||'UNSPEC').toUpperCase()}${size}</div>
    <div class="quote">“${escapeHtml(d.quote)}”</div>
    <div class="badges">
      ${d.included === true ? '<span class="badge">Included ✓</span>' : (d.included === false ? '<span class="badge">Excluded</span>' : '')}
      ${tags}
    </div>
    <div class="meta">Source: ${escapeHtml(srcTitle)}${report}${page}</div>
  </article>`;
}

function summarySuffix(st){
  const parts = [];
  if (st.iso3) parts.push(st.iso3);
  if (st.year) parts.push(st.year);
  if (st.included) parts.push(st.included === 'true' ? 'Included' : 'Excluded');
  if (st.q) parts.push(`“${st.q}”`);
  return parts.length ? ` for ${parts.join(' · ')}` : '';
}

function syncURL(){
  const p = new URLSearchParams();
  if (state.iso3) p.set('iso3', state.iso3);
  if (state.year) p.set('year', state.year);
  if (state.included) p.set('included', state.included);
  if (state.q)    p.set('q', state.q);
  const newUrl = location.pathname + (p.toString()?`?${p.toString()}`:'');
  history.replaceState(null, '', newUrl);
}

function debounce(fn, ms){ let t; return (...a)=>{ clearTimeout(t); t=setTimeout(()=>fn(...a), ms); }; }
function escapeHtml(s){ return String(s==null?'':s).replace(/[&<>"']/g, m => ({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#039;'}[m])); }

function downloadCsv(rows, filename){
  if (!rows.length){ alert('No rows to download.'); return; }
  const headers = Object.keys(rows[0]);
  const csv = [headers.join(',')].concat(rows.map(r => headers.map(h => csvEscape(r[h])).join(','))).join('\n');
  const blob = new Blob([csv], {type:'text/csv;charset=utf-8;'});
  const a = document.createElement('a');
  a.href = URL.createObjectURL(blob); a.download = filename; a.click();
  URL.revokeObjectURL(a.href);
}
function csvEscape(v){
  if (v == null) return '';
  const s = String(v).replace(/"/g,'""');
  return /[",\n]/.test(s) ? `"${s}"` : s;
}
