// main script for index.html (and shared functions)
let DATA = [];
let CURRENT_COUNTRY = '';
const CART_KEY = 'cart';

function fetchDataAndInit(){
  fetch('data.json')
    .then(r=>r.json())
    .then(j=>{
      DATA = j.countries;
      initCountryTabs();
      // select first non-empty country
      const first = DATA.find(c=>c.foods && c.foods.length>0);
      if(first) selectCountry(first.name);
      updateCartCount();
    })
    .catch(err=>{
      console.error('Failed to load data.json', err);
      document.getElementById('foodCards').innerHTML = '<p>Failed to load data.</p>';
    });
}

function initCountryTabs(){
  const tab = document.getElementById('countryTabs');
  tab.innerHTML = DATA.map(c=>`<button onclick="selectCountry('${c.name}')">${c.name}</button>`).join('');
}

function selectCountry(name){
  CURRENT_COUNTRY = name;
  const country = DATA.find(c=>c.name===name);
  if(!country) return;
  renderFoods(country.foods);
}

function renderFoods(list){
  const deleted = JSON.parse(localStorage.getItem('deleted')||'[]');
  const ratings = JSON.parse(localStorage.getItem('ratings')||'{}');
  const container = document.getElementById('foodCards');
  if(!list || list.length===0){ container.innerHTML = '<p>No foods available.</p>'; return; }
  const filtered = list.filter(f=>!deleted.includes(f.id));
  container.innerHTML = filtered.map(f=>{
    const extra = ratings[f.id] ? ` (${( (ratings[f.id].reduce((a,b)=>a+b,0)/ratings[f.id].length)).toFixed(1)})` : '';
    return `
      <div class="card">
        <img src="${f.image}" alt="${f.name}">
        <div class="card-body">
          <h3>${f.name}</h3>
          <p class="meta">⭐ ${f.rating}${extra}</p>
          <p class="meta">Ingredients: ${f.ingredients.join(', ')}</p>
          <div class="card-actions">
            <button onclick="viewDetail('${f.id}')">Details</button>
            <button onclick="addToCart('${f.id}')">Add to cart</button>
            <button style="background:#e74c3c" onclick="deleteLocal('${f.id}')">Delete</button>
          </div>
        </div>
      </div>
    `;
  }).join('');
}

// navigation helpers
function viewDetail(id){
  localStorage.setItem('selectedFood', id);
  location.href = 'detail.html';
}

function addToCart(id){
  let cart = JSON.parse(localStorage.getItem(CART_KEY)||'[]');
  if(!cart.includes(id)) cart.push(id);
  localStorage.setItem(CART_KEY, JSON.stringify(cart));
  updateCartCount();
  alert('Added to cart');
}

function updateCartCount(){
  const c = JSON.parse(localStorage.getItem(CART_KEY)||'[]').length;
  const el = document.getElementById('cartCount');
  if(el) el.innerText = c;
}

// delete locally (does not modify data.json): mark id as deleted
function deleteLocal(id){
  if(!confirm('Remove this item locally? (will hide from lists)')) return;
  const deleted = JSON.parse(localStorage.getItem('deleted')||'[]');
  if(!deleted.includes(id)) deleted.push(id);
  localStorage.setItem('deleted', JSON.stringify(deleted));
  // re-render current country
  const c = DATA.find(x=>x.name===CURRENT_COUNTRY);
  if(c) renderFoods(c.foods);
}

// search
const searchInput = document.getElementById('searchInput');
if(searchInput){
  searchInput.addEventListener('input', (e)=>{
    const q = e.target.value.trim().toLowerCase();
    const country = DATA.find(c=>c.name===CURRENT_COUNTRY);
    if(!country) return;
    if(!q) return renderFoods(country.foods);
    const filtered = country.foods.filter(f=> {
      return f.name.toLowerCase().includes(q) || f.ingredients.join(' ').toLowerCase().includes(q);
    });
    renderFoods(filtered);
  });
}

// init
fetchDataAndInit();
