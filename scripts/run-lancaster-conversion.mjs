import fs from 'node:fs';
import path from 'node:path';
import { spawnSync } from 'node:child_process';

const root=process.cwd();
const python=spawnSync('python3',[path.join(root,'scripts/lancaster-conversion-pass.py'),root],{stdio:'inherit'});
if(python.status===0)process.exit(0);

const publicDir=path.join(root,'public');
const files=[];
function walk(dir){for(const entry of fs.readdirSync(dir,{withFileTypes:true})){const file=path.join(dir,entry.name);if(entry.isDirectory())walk(file);else if(file.endsWith('.html'))files.push(file);}}
walk(publicDir);
const map='https://www.google.com/maps?q=101%20N%20Queen%20St%2C%20Suite%20400%2C%20Lancaster%2C%20PA%2017603&output=embed';
for(const file of files){
  let html=fs.readFileSync(file,'utf8');
  html=html.replace(/<a[^>]*href=["']tel:[^"']*555[^"']*["'][^>]*>.*?<\/a>/gis,'');
  html=html.replace(/(?:\+?1[\s.-]?)?\(?555\)?[\s.-]?555[\s.-]?\d{4}/g,'').replaceAll('—','-').replaceAll('–','-');
  html=html.replace(/class="hp-field"/g,'class="rr-hp-field"').replace(/class="form-status"/g,'class="rr-form-status"');
  html=html.replace(/"telephone"\s*:\s*""\s*,?/g,'');
  if(!html.includes('data-lancaster-css'))html=html.replace('</head>','<link rel="stylesheet" href="/lancaster-conversion.css" data-lancaster-css="true"/><script src="/lancaster-conversion.js" data-lancaster-js="true" defer></script></head>');
  html=html.replace(/(<div[^>]*class=["'][^"']*rr-footer-map[^"']*["'][^>]*>)[\s\S]*?(<\/div>)/g,`$1<iframe title="Commercial Roofing Contractors of Lancaster office map" src="${map}" loading="lazy" referrerpolicy="no-referrer-when-downgrade" allowfullscreen></iframe>$2`);
  if(file.endsWith('/contact.html')&&!html.includes('name="roofNeed"')){
    const field='<label class="rr-contact-field rr-contact-field--full rr-lc-roof-need">What does the roof need?<select name="roofNeed" required><option value="">Choose the closest match</option><option>Emergency Roof Repair</option><option>Commercial Roof Repair</option><option>Flat Roof Replacement Inspection</option><option>Roof Coating</option><option>Commercial Roof Replacement</option><option>Roof Service Agreement</option><option>Not Sure Yet</option></select></label>';
    html=html.replace(/(<label[^>]*>Timeline)/,field+'$1');
  }
  if((file.endsWith('/home.html')||file.endsWith('/index.html'))&&html.includes('class="rr-lc-main"'))html=html.replace(/<h1[^>]*>[\s\S]*?<\/h1>/,'<h1>Commercial Roof Help for Lancaster Buildings</h1>');
  fs.writeFileSync(file,html);
}
console.log(`Lancaster Node protection pass: ${files.length} pages`);
