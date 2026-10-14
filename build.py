import json;from data import *
d=json.dumps(dict(R=R,SRC=SRC,HOME=HOME))
open('index.html','w').write('''<!doctype html><html><head><meta charset=utf-8><meta name=viewport content="width=device-width,initial-scale=1"><title>Investor Inputs Tier Map</title><style>
body{margin:0;font-family:system-ui,sans-serif;background:#fff8ee;color:#2b2118}h1{font-size:22px;margin:14px 14px 4px}.sub{margin:0 14px 10px;font-size:13px;color:#7a6650}
.row{margin:10px;border-radius:16px;background:#fff;box-shadow:0 2px 8px #0001;overflow:hidden}.rh{padding:10px 12px;color:#fff;font-weight:700;font-size:16px}.tk{font-size:12px;font-weight:500;opacity:.95;margin-top:3px}
.lad{display:flex;gap:6px;overflow-x:auto;padding:10px}.st{flex:0 0 auto;min-width:92px;border:2px solid #eee;border-radius:12px;padding:8px;font-size:12px;font-weight:600;text-align:center;cursor:pointer;background:#fffdf8}.st b{display:block;font-size:18px}
.st.on{border-color:var(--c);background:var(--c);color:#fff}.st.home{outline:3px dashed #e33;outline-offset:1px}.det{padding:0 12px 12px;font-size:13px;display:none}.det.show{display:block}
.t{border-radius:10px;padding:6px 8px;margin:6px 0}.t h4{margin:0 0 3px;font-size:12px}.t ul{margin:0;padding-left:18px}.S{background:#ffe9a8}.A{background:#d9f2e2}.B{background:#e3ecfb}.F{background:#fde1df}.V{background:#f1e8fb}.C{background:#eee}
.hb{margin:10px;padding:12px;border-radius:16px;background:linear-gradient(135deg,#ffe2c2,#ffd1e0);border:2px solid #e33}.hb h2{margin:0 0 6px;font-size:17px}.hb ol{padding-left:20px;margin:6px 0;font-size:13px}
.src{margin:10px;font-size:11px;color:#6b5a48}.src a{color:#3a5fa0}.leg{display:flex;gap:6px;margin:0 14px;font-size:11px}.leg span{padding:2px 6px;border-radius:6px}
</style></head><body><h1>🗺️ Investor Inputs Tier Map</h1><p class=sub>What investors weigh most at each stage, by business type. Tap a stage. 🔴 dashed = where Sheehan Homestead sits.</p>
<div class=leg><span class=S>S = must-have</span><span class=A>A = strong plus</span><span class=B>B = nice-to-have</span><span class=F>🚩 red flags</span></div>
<a href="lightning.html" style="display:block;margin:10px;padding:12px;border-radius:14px;background:#1b2448;color:#ffd166;font-weight:800;text-decoration:none">🏪⚡ Bodega vs Lightning: valuation mockup + objection playbook →</a><div class=hb><h2>📍 Where Sheehan Homestead sits</h2><div style="font-size:13px">Row 2 (B&M + professionalization) → moving to Row 3 (tech-enabled), at the <b>Angel/Seed</b> stage. Leap Venture Studio Cohort 11 due <b>Sun Oct 18, 11:59 PM PT</b>.</div><b style="font-size:13px">Top 5 inputs to strengthen now:</b><ol id=home></ol></div>
<div id=rows></div><div class=src><b>Sources</b><ul id=src></ul>Qualitative tiers synthesized from these guides; numbers shown only where a source states them. Not investment advice.</div>
<script>const D='''+d+''';
const T=[["S","⭐ S-tier"],["A","A-tier"],["B","B-tier"]];
home.innerHTML=D.HOME.map(x=>"<li>"+x+"</li>").join("");src.innerHTML=D.SRC.map(s=>`<li><a href="${s[1]}" target=_blank>${s[0]}</a> (${s[2]})</li>`).join("");
const L=a=>"<ul>"+a.map(x=>"<li>"+x+"</li>").join("")+"</ul>";
rows.innerHTML=D.R.map((r,i)=>`<div class=row style="--c:${r[3]}"><div class=rh style="background:${r[3]}">${r[1]} ${r[2]}<div class=tk>${r[4]}</div></div><div class=lad>${r[5].map((s,j)=>`<div class="st ${(i==1&&j==1)||(i==2&&j==1)?'home':''}" data-r=${i} data-s=${j}><b>${j+1}</b>${s[0]}</div>`).join("")}</div><div class=det id=d${i}></div></div>`).join("");
function show(i,j){const s=D.R[i][5][j],e=document.getElementById("d"+i);document.querySelectorAll(`.st[data-r="${i}"]`).forEach(x=>x.classList.toggle("on",+x.dataset.s==j));
e.innerHTML=`<h3 style="margin:4px 0">${s[0]}</h3>`+T.map((t,k)=>`<div class="t ${t[0]}"><h4>${t[1]}</h4>${L(s[k+1])}</div>`).join("")+`<div class="t F"><h4>🚩 Red flags</h4>${L(s[4])}</div><div class="t V"><h4>💲 Valuation method</h4>${s[5]}</div><div class="t C"><h4>🏦 Typical check sources</h4>${s[6]}</div>`;e.classList.add("show")}
document.querySelectorAll(".st").forEach(x=>x.onclick=()=>show(+x.dataset.r,+x.dataset.s));D.R.forEach((r,i)=>show(i,i==1||i==2?1:0));
</script></body></html>''')
