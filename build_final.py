import json, os

img_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'extracted_images')
with open(os.path.join(img_dir, 'compressed.json'), 'r') as f:
    imgs = json.load(f)
with open(os.path.join(img_dir, 'web_images.json'), 'r') as f:
    web = json.load(f)

# Beach photos from beach_fotos/
beach_fotos_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'beach_fotos', 'beach_images.json')
with open(beach_fotos_path, 'r') as f:
    beach_imgs = json.load(f)

def beach_img(folder, idx=0):
    """Get base64 data URI for a beach photo by folder name and index."""
    if folder in beach_imgs and idx < len(beach_imgs[folder]):
        return beach_imgs[folder][idx]['data']
    return ''

print(f"PDF: {len(imgs)}, Web: {len(web)}, Beach folders: {len(beach_imgs)}")

def img(key, source='web'):
    d = web if source == 'web' else imgs
    return d.get(key, '')

CSS = """
:root{--sand:#F5E6D0;--sand-light:#FBF5ED;--tc:#C4724E;--tc-d:#A85A3A;--bl:#1B6B93;--bl-d:#153B50;--bl-l:#E8F4F8;--wh:#fff;--gr:#6B7280}
*{margin:0;padding:0;box-sizing:border-box}html{scroll-behavior:smooth}
body{font-family:'Inter',sans-serif;color:var(--bl-d);background:var(--sand-light);line-height:1.6}
h1,h2,h3,h4{font-family:'Playfair Display',serif}
a{color:var(--bl);transition:color .2s}a:hover{color:var(--tc)}
nav{position:fixed;top:0;width:100%;background:rgba(21,59,80,.95);backdrop-filter:blur(10px);z-index:1000}
nav ul{display:flex;list-style:none;max-width:1200px;margin:0 auto;padding:0 1rem;overflow-x:auto}
nav ul::-webkit-scrollbar{display:none}
nav li a{display:block;padding:1rem .8rem;color:var(--sand);text-decoration:none;font-size:.85rem;font-weight:500;white-space:nowrap}
nav li a:hover{color:var(--tc)}
.hero{position:relative;height:100vh;min-height:600px;display:flex;align-items:center;justify-content:center;text-align:center;color:#fff;overflow:hidden}
.hero-bg{position:absolute;inset:0;background-size:cover;background-position:center;filter:brightness(.5)}
.hero-content{position:relative;z-index:1;padding:2rem}
.hero h1{font-size:clamp(2.5rem,8vw,5rem);margin-bottom:.5rem;text-shadow:2px 2px 20px rgba(0,0,0,.5)}
.hero .sub{font-size:clamp(1rem,3vw,1.5rem);font-weight:300;margin-bottom:2rem;opacity:.9}
.cd{display:flex;gap:1.5rem;justify-content:center;flex-wrap:wrap;margin-top:1rem}
.cd-i{background:rgba(255,255,255,.15);backdrop-filter:blur(10px);border:1px solid rgba(255,255,255,.3);border-radius:12px;padding:1.2rem 1.5rem;min-width:90px}
.cd-i .n{font-family:'Playfair Display',serif;font-size:2.5rem;font-weight:700;display:block;line-height:1}
.cd-i .l{font-size:.75rem;text-transform:uppercase;letter-spacing:2px;opacity:.8;margin-top:.3rem;display:block}
sec,section{padding:5rem 1.5rem;max-width:1200px;margin:0 auto}
.sf{max-width:100%;background:var(--wh);padding-left:0;padding-right:0}
.si{max-width:1200px;margin:0 auto;padding:0 1.5rem}
.st{font-size:clamp(1.8rem,4vw,2.5rem);margin-bottom:.5rem}
.ss{color:var(--gr);font-size:1.05rem;margin-bottom:2.5rem;font-weight:300}
.cg{display:grid;grid-template-columns:repeat(auto-fill,minmax(300px,1fr));gap:1.5rem}
.card{background:var(--wh);border-radius:16px;overflow:hidden;box-shadow:0 4px 20px rgba(0,0,0,.08);transition:transform .3s,box-shadow .3s}
.sf .card{background:var(--sand-light)}.card:hover{transform:translateY(-4px);box-shadow:0 8px 30px rgba(0,0,0,.12)}
.card img{width:100%;height:200px;object-fit:cover}.cb{padding:1.5rem}.cb h3{font-size:1.15rem;margin-bottom:.5rem}.cb p{color:var(--gr);font-size:.93rem}
.cb a.more{display:inline-block;margin-top:.5rem;font-size:.85rem;font-weight:500;color:var(--bl);text-decoration:none}
.cb a.more:hover{color:var(--tc);text-decoration:underline}
.tag{display:inline-block;background:var(--bl-l);color:var(--bl);padding:.2rem .7rem;border-radius:20px;font-size:.8rem;font-weight:500;margin-top:.6rem;margin-right:.2rem}
.tag.dog{background:#FEF3C7;color:#92400E}
.ig{display:grid;grid-template-columns:repeat(auto-fill,minmax(150px,1fr));gap:1rem;margin:1.5rem 0}
.ii{display:flex;align-items:center;gap:.7rem;padding:.7rem;background:var(--sand-light);border-radius:10px;font-size:.9rem}
.sf .ii{background:var(--wh)}.ii .em{font-size:1.3rem}
.ib{background:var(--bl-l);border-left:4px solid var(--bl);padding:1.2rem 1.5rem;border-radius:0 10px 10px 0;margin:1.5rem 0}
.ib.dog{background:#ECFDF5;border-color:#10B981}
.gal{display:grid;grid-template-columns:repeat(auto-fill,minmax(220px,1fr));gap:1rem;margin:1.5rem 0}
.gal img{width:100%;height:200px;object-fit:cover;border-radius:12px;transition:transform .3s}.gal img:hover{transform:scale(1.03)}
.wg{display:grid;grid-template-columns:repeat(auto-fill,minmax(200px,1fr));gap:1.5rem;margin:1.5rem 0}
.wc{text-align:center;padding:2rem 1.5rem;background:linear-gradient(135deg,var(--bl),var(--bl-d));color:#fff;border-radius:16px}
.wc .wi{font-size:2.5rem;margin-bottom:.5rem}.wc .wv{font-family:'Playfair Display',serif;font-size:2rem;font-weight:700}.wc .wl{font-size:.85rem;opacity:.8;margin-top:.25rem}
.rg{display:grid;grid-template-columns:repeat(auto-fill,minmax(220px,1fr));gap:1rem;margin:1.5rem 0}
.ri{display:flex;align-items:center;gap:.7rem;padding:1rem;background:var(--sand-light);border-radius:10px}.ri .ric{font-size:1.5rem}
.rmg{display:grid;grid-template-columns:repeat(auto-fill,minmax(180px,1fr));gap:1rem;margin:1.5rem 0}
.rmc{padding:1.2rem;background:var(--sand-light);border-radius:12px;text-align:center}.rmc .ro{font-size:2rem;margin-bottom:.5rem}.rmc h4{font-size:1rem;margin-bottom:.2rem}.rmc p{font-size:.85rem;color:var(--gr)}
.rl{display:grid;grid-template-columns:repeat(auto-fill,minmax(350px,1fr));gap:1.5rem}
.rc{display:flex;gap:1rem;padding:1.5rem;background:var(--sand-light);border-radius:12px;box-shadow:0 2px 10px rgba(0,0,0,.06)}
.rc .rci{font-size:1.5rem;flex-shrink:0;width:50px;height:50px;background:var(--tc);color:#fff;border-radius:12px;display:flex;align-items:center;justify-content:center}
.rc h3{font-size:1.05rem;margin-bottom:.2rem}.rc .rloc{font-size:.8rem;color:var(--tc);font-weight:500}.rc .rdesc{font-size:.9rem;color:var(--gr);margin-top:.3rem}
.rc a.more{font-size:.8rem;color:var(--bl);text-decoration:none;margin-top:.3rem;display:inline-block}
.rc a.more:hover{text-decoration:underline}
.tc{display:grid;grid-template-columns:repeat(auto-fill,minmax(280px,1fr));gap:1.5rem;margin:1.5rem 0}
.tip{padding:1.5rem;background:var(--sand-light);border-radius:12px;border-top:4px solid var(--tc)}.sf .tip{background:var(--wh)}
.tip h4{margin-bottom:.5rem}.tip p{font-size:.9rem;color:var(--gr)}
.rst{display:grid;grid-template-columns:repeat(auto-fill,minmax(280px,1fr));gap:1.5rem;margin:1.5rem 0}
.rs{padding:1.5rem;border-radius:12px;background:#FEF2F2;border-left:4px solid #DC2626}.sf .rs{background:#FEF2F2}
.rs h4{margin-bottom:.3rem;font-size:1rem}.rs .rsl{font-size:.8rem;color:#DC2626;font-weight:500;margin-bottom:.5rem}.rs p{font-size:.9rem;color:var(--gr)}
.rs a.rslink{display:inline-block;margin-top:.5rem;font-size:.82rem;color:#DC2626;font-weight:500;text-decoration:none}.rs a.rslink:hover{text-decoration:underline}
.sl{list-style:none}.sl li{padding:1rem 1.2rem;background:var(--sand-light);border-radius:10px;margin-bottom:.7rem;display:flex;align-items:flex-start;gap:.7rem}
.sl li .sli{font-size:1.3rem;flex-shrink:0;margin-top:2px}.sl li strong{display:block;margin-bottom:.2rem}.sl li span{font-size:.9rem;color:var(--gr)}
.sl li a{font-size:.8rem;display:inline-block;margin-top:.3rem}
.map-img{width:100%;border-radius:16px;box-shadow:0 4px 20px rgba(0,0,0,.1);margin-top:1.5rem}
/* Lightbox */
.lb-overlay{display:none;position:fixed;inset:0;background:rgba(0,0,0,.92);z-index:2000;cursor:pointer;align-items:center;justify-content:center}
.lb-overlay.active{display:flex}
.lb-overlay img{max-width:92vw;max-height:90vh;border-radius:8px;box-shadow:0 8px 40px rgba(0,0,0,.5)}
.lb-close{position:fixed;top:1rem;right:1.5rem;color:#fff;font-size:2.5rem;cursor:pointer;z-index:2001;line-height:1}
.gal img,.rmc.clickable{cursor:pointer}
/* Rest stop images */
.rs img{width:100%;height:120px;object-fit:cover;border-radius:8px;margin-bottom:.8rem}
footer{background:var(--bl-d);color:var(--sand);text-align:center;padding:2rem 1.5rem;font-size:.85rem}
@media(max-width:768px){nav li a{padding:.8rem .6rem;font-size:.75rem}section{padding:3rem 1rem}.cd{gap:.7rem}.cd-i{padding:.8rem 1rem;min-width:70px}.cd-i .n{font-size:1.8rem}.cg,.rl{grid-template-columns:1fr}.gal{grid-template-columns:1fr 1fr}}
"""

JS = r"""
function uc(){var t=new Date('2026-07-18T15:00:00+02:00'),n=new Date(),d=t-n;if(d<=0){document.getElementById('cd').innerHTML='<p style="font-size:1.5rem">\ud83c\udf89 Der Urlaub hat begonnen!</p>';return}var dd=Math.floor(d/864e5),hh=Math.floor(d%864e5/36e5),mm=Math.floor(d%36e5/6e4),ss=Math.floor(d%6e4/1e3);document.getElementById('cd-d').textContent=dd;document.getElementById('cd-h').textContent=('0'+hh).slice(-2);document.getElementById('cd-m').textContent=('0'+mm).slice(-2);document.getElementById('cd-s').textContent=('0'+ss).slice(-2)}uc();setInterval(uc,1e3);
document.querySelectorAll('nav a').forEach(function(a){a.addEventListener('click',function(e){e.preventDefault();var t=document.querySelector(this.getAttribute('href'));if(t)window.scrollTo({top:t.getBoundingClientRect().top+window.pageYOffset-50,behavior:'smooth'})})});
// Lightbox
var lb=document.getElementById('lightbox'),lbImg=document.getElementById('lb-img');
document.querySelectorAll('.gal img, img.zoomable').forEach(function(img){
  img.style.cursor='pointer';
  img.addEventListener('click',function(){lbImg.src=this.src;lb.classList.add('active')});
});
document.querySelectorAll('.rmc.clickable').forEach(function(el){
  el.addEventListener('click',function(){var s=this.dataset.img;if(s){lbImg.src=s;lb.classList.add('active')}});
});
lb.addEventListener('click',function(){lb.classList.remove('active')});
document.addEventListener('keydown',function(e){if(e.key==='Escape')lb.classList.remove('active')});
"""

html = f"""<!DOCTYPE html>
<html lang="de">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Kroatien 2026 \u2013 Villa Lavanda Macarini</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;700&family=Inter:wght@300;400;500;600&display=swap" rel="stylesheet">
<style>{CSS}</style>
</head>
<body>

<nav><ul>
<li><a href="#hero">Start</a></li>
<li><a href="#villa">Unterkunft</a></li>
<li><a href="#anreise">Anreise</a></li>
<li><a href="#wetter">Wetter</a></li>
<li><a href="#straende">Str\u00e4nde</a></li>
<li><a href="#ausfluge">Ausfl\u00fcge</a></li>
<li><a href="#restaurants">Restaurants</a></li>
<li><a href="#einkaufen">Einkaufen</a></li>
<li><a href="#karte">Karte</a></li>
</ul></nav>

<section class="hero" id="hero">
<div class="hero-bg" style="background-image:url('{img("villa_foto_06")}')"></div>
<div class="hero-content">
<h1>Kroatien 2026</h1>
<p class="sub">Villa Lavanda Macarini \u00b7 18. Juli \u2013 1. August</p>
<div class="cd" id="cd">
<div class="cd-i"><span class="n" id="cd-d">--</span><span class="l">Tage</span></div>
<div class="cd-i"><span class="n" id="cd-h">--</span><span class="l">Stunden</span></div>
<div class="cd-i"><span class="n" id="cd-m">--</span><span class="l">Minuten</span></div>
<div class="cd-i"><span class="n" id="cd-s">--</span><span class="l">Sekunden</span></div>
</div></div>
</section>

<!-- UNTERKUNFT -->
<section id="villa">
<h2 class="st">Die Unterkunft</h2>
<p class="ss">Villa Lavanda Macarini \u00b7 Brgod, Trget \u00b7 52224 Kroatien \u00b7 <a href="https://www.fewo-direkt.de/ferienwohnung-ferienhaus/p5360164?dateless=true" target="_blank">\U0001F4F7 Alle Fotos &amp; Details auf FeWo-direkt</a> \u00b7 <a href="https://www.google.com/maps/place/45.037297,14.074107" target="_blank">\U0001F4CD Google Maps</a></p>

<div class="gal" style="grid-template-columns:repeat(auto-fill,minmax(220px,1fr))">
{"".join(f'<img src="{img("villa_foto_" + str(i).zfill(2))}" alt="Villa Foto {i}">' for i in range(1, 27))}
</div>

<h3 style="margin:2rem 0 .5rem">Ausstattung</h3>
<div class="ig">
<div class="ii"><span class="em">\U0001F3CA</span> Beheizter Pool</div>
<div class="ii"><span class="em">\U0001F6CF</span> 3 Schlafzimmer</div>
<div class="ii"><span class="em">\U0001F6C1</span> 4 Badezimmer</div>
<div class="ii"><span class="em">\U0001F4CF</span> 127 m\u00b2</div>
<div class="ii"><span class="em">\U0001F373</span> K\u00fcche</div>
<div class="ii"><span class="em">\U0001F9F9</span> Waschmaschine</div>
<div class="ii"><span class="em">\U0001F32C</span> Trockner</div>
<div class="ii"><span class="em">\U0001F4F6</span> Kostenloses WLAN</div>
<div class="ii"><span class="em">\U0001F436</span> Haustierfreundlich</div>
<div class="ii"><span class="em">\U0001F33B</span> Garten (600m\u00b2)</div>
<div class="ii"><span class="em">\u2600\uFE0F</span> Terrasse / Patio</div>
<div class="ii"><span class="em">\U0001F3D3</span> Spielbereich / Tischtennis</div>
</div>

<h3 style="margin:2rem 0 .5rem">Zimmeraufteilung</h3>
<div class="rmg">
<div class="rmc clickable" data-img="{img('villa_foto_10')}" title="Klick f\u00fcr Foto"><div class="ro">\U0001F6CC</div><h4>Schlafzimmer 1</h4><p>1 King-Bett \U0001F4F7</p></div>
<div class="rmc clickable" data-img="{img('villa_foto_21')}" title="Klick f\u00fcr Foto"><div class="ro">\U0001F6CC</div><h4>Schlafzimmer 2</h4><p>1 King-Bett \U0001F4F7</p></div>
<div class="rmc clickable" data-img="{img('villa_foto_22')}" title="Klick f\u00fcr Foto"><div class="ro">\U0001F6CC</div><h4>Schlafzimmer 3</h4><p>2 Einzelbetten \U0001F4F7</p></div>
<div class="rmc clickable" data-img="{img('villa_foto_13')}" title="Klick f\u00fcr Foto"><div class="ro">\U0001F6CB</div><h4>Wohnzimmer</h4><p>1 gro\u00dfes Schlafsofa \U0001F4F7</p></div>
</div>

<h3 style="margin:2rem 0 .5rem">Hausordnung</h3>
<div class="rg">
<div class="ri"><span class="ric">\U0001F551</span><div><strong>Check-in</strong> ab 15:00 Uhr</div></div>
<div class="ri"><span class="ric">\U0001F559</span><div><strong>Check-out</strong> vor 10:00 Uhr</div></div>
<div class="ri"><span class="ric">\U0001F436</span><div><strong>Haustiere</strong> Erlaubt (max. 2)</div></div>
</div>
<div class="ib" style="margin-top:2rem"><strong>\U0001F4F6 WLAN:</strong> Netzwerkname \u201eVilla Lavanda Macarini\u201c</div>
</section>

<!-- ANREISE -->
<section id="anreise" class="sf"><div class="si">
<h2 class="st">Anreise</h2>
<p class="ss">~1.240 km \u00b7 ca. 12 Stunden Fahrt \u00b7 <a href="https://www.google.com/maps/dir/Am+M%C3%BChlenbach+18,+48308+Senden,+Deutschland/45.037297,14.074107" target="_blank">\U0001F697 Komplette Route auf Google Maps</a></p>
<div class="gal" style="grid-template-columns:2fr 1fr">
<img src="{imgs['route_overview']}" alt="Route" style="height:300px">
<img src="{imgs['route_istria']}" alt="Route Istrien" style="height:300px">
</div>

<h3 style="margin:2rem 0 1rem">Maut &amp; Vignetten</h3>
<div class="tc">
<div class="tip"><h4>\U0001F1E6\U0001F1F9 \u00d6sterreich</h4><p>Digitale Vignette \u00fcber <a href="https://www.asfinag.at" target="_blank">asfinag.at</a>. 10-Tages-Vignette reicht bei 14 Tagen <em>nicht</em> \u2013 besser 2-Monats-Vignette.</p></div>
<div class="tip"><h4>\U0001F1F8\U0001F1EE Slowenien</h4><p>E-Vignette \u00fcber <a href="https://evinjeta.dars.si" target="_blank">evinjeta.dars.si</a>. 7 oder 30 Tage. Digital am Kennzeichen registriert.</p></div>
<div class="tip"><h4>\U0001F1ED\U0001F1F7 Kroatien</h4><p>Mautstationen auf der Autobahn. Bezahlung mit Karte oder bar. ENC-Transponder optional.</p></div>
</div>

<h3 style="margin:2rem 0 1rem">\U0001F6D1 Empfohlene Rastst\u00e4tten</h3>
<div class="rst">
<div class="rs"><img src="{img('rs_steigerwald')}" alt="Steigerwald"><h4>\U0001F3C6 Steigerwald S\u00fcd</h4><div class="rsl">A3 \u00b7 Wachenroth (~3h)</div><p>ADAC \u201egut\u201c. Saubere Anlagen, gutes Essen, Kinderspielplatz, Coffee Fellows.</p><a class="rslink" href="https://www.serways.de/standorte/steigerwald-sued/" target="_blank">\u2192 Website</a> \u00b7 <a class="rslink" href="https://www.google.com/maps/dir/Am+M%C3%BChlenbach+18,+48308+Senden/Rastst%C3%A4tte+Steigerwald+S%C3%BCd,+Wachenroth" target="_blank">\U0001F4CD Route</a></div>
<div class="rs"><img src="{img('rs_dasing')}" alt="Bauernmarkt Dasing"><h4>\U0001F33E Bauernmarkt Dasing</h4><div class="rsl">A8 \u00b7 Ausfahrt Dasing (~5h)</div><p>Kein Rasthof \u2013 ein Erlebnis! Hofladen, B\u00e4ckerei, Metzgerei, Biergarten. T\u00e4gl. 8\u201318 Uhr.</p><a class="rslink" href="https://bauernmarkt-dasing.de/" target="_blank">\u2192 Website</a> \u00b7 <a class="rslink" href="https://www.google.com/maps/dir/Am+M%C3%BChlenbach+18,+48308+Senden/Bauernmarkt+Dasing,+An+der+Brandleiten+6,+86453+Dasing" target="_blank">\U0001F4CD Route</a></div>
<div class="rs"><img src="{img('rs_irschenberg')}" alt="Irschenberg"><h4>\U0001F3D4 Irschenberg S\u00fcd</h4><div class="rsl">A8 \u00b7 bei Rosenheim (~6h)</div><p>H\u00f6chstgelegene Rastst\u00e4tte Deutschlands. Panorama-Terrasse mit Alpenblick.</p><a class="rslink" href="https://www.serways.de/standorte/irschenberg-sued/" target="_blank">\u2192 Website</a> \u00b7 <a class="rslink" href="https://www.google.com/maps/dir/Am+M%C3%BChlenbach+18,+48308+Senden/Rastst%C3%A4tte+Irschenberg+S%C3%BCd" target="_blank">\U0001F4CD Route</a></div>
<div class="rs"><h4>\U0001F3DE Hochfelln Nord</h4><div class="rsl">A8 \u00b7 Chiemsee (~6,5h)</div><p>Atemberaubender Blick auf den Chiemsee. Regionale K\u00fcche, E-Ladestationen.</p><a class="rslink" href="https://www.google.com/maps/dir/Am+M%C3%BChlenbach+18,+48308+Senden/Rastst%C3%A4tte+Hochfelln+Nord,+A8" target="_blank">\U0001F4CD Route</a></div>
<div class="rs"><img src="{img('rs_tauernalm')}" alt="Tauernalm"><h4>\u2B50 Landzeit Tauernalm</h4><div class="rsl">A10 \u00b7 Flachau, \u00d6sterreich (~8h)</div><p>Top 10 Europas! Salatbar, Pasta, Grillstation, frische S\u00e4fte. Hotel (DZ ab 105\u20ac).</p><a class="rslink" href="https://landzeit.at/en/tauernalm" target="_blank">\u2192 Website &amp; Hotel</a> \u00b7 <a class="rslink" href="https://www.google.com/maps/dir/Am+M%C3%BChlenbach+18,+48308+Senden/Landzeit+Tauernalm,+Flachau" target="_blank">\U0001F4CD Route</a></div>
<div class="rs"><h4>\U0001F6E3 Karawankentunnel</h4><div class="rsl">A11 \u00b7 AT/SLO Grenze (~9,5h)</div><p><strong>Achtung:</strong> Samstags im Juli/August 1\u20132h Stau! Fr\u00fch oder sp\u00e4t fahren.</p><a class="rslink" href="https://www.google.com/maps/dir/Am+M%C3%BChlenbach+18,+48308+Senden/Karawankentunnel" target="_blank">\U0001F4CD Route</a></div>
<div class="rs"><h4>\u26FD Po\u010divali\u0161\u010de Lom</h4><div class="rsl">A1 \u00b7 Logatec, Slowenien (~10,5h)</div><p>Petrol-Tankstelle in Waldlage. Ruhig und entspannt.</p><a class="rslink" href="https://www.google.com/maps/dir/Am+M%C3%BChlenbach+18,+48308+Senden/Po%C4%8Divali%C5%A1%C4%8De+Lom,+Logatec" target="_blank">\U0001F4CD Route</a></div>
</div>

</div></section>

<!-- WETTER -->
<section id="wetter">
<h2 class="st">Wetter im Juli</h2>
<p class="ss">Durchschnittswerte f\u00fcr Istrien im Hochsommer</p>
<div class="wg">
<div class="wc"><div class="wi">\u2600\uFE0F</div><div class="wv">27\u201330\u00b0C</div><div class="wl">Lufttemperatur</div></div>
<div class="wc" style="background:linear-gradient(135deg,#0891b2,#164e63)"><div class="wi">\U0001F30A</div><div class="wv">24\u201326\u00b0C</div><div class="wl">Wassertemperatur</div></div>
<div class="wc" style="background:linear-gradient(135deg,#d97706,#92400e)"><div class="wi">\U0001F31E</div><div class="wv">~11 Std.</div><div class="wl">Sonnenstunden / Tag</div></div>
<div class="wc" style="background:linear-gradient(135deg,#6366f1,#312e81)"><div class="wi">\U0001F327\uFE0F</div><div class="wv">~4 Tage</div><div class="wl">Regentage / Monat</div></div>
</div>
</section>

<!-- STRÄNDE -->
<section id="straende" class="sf"><div class="si">
<h2 class="st">Str\u00e4nde</h2>
<p class="ss">Kiesel, t\u00fcrkises Wasser &amp; hundefreundlich</p>
<div class="ib dog"><strong>\U0001F436 Gute Nachricht!</strong> In der Region Labin/Rabac sind Hunde an <em>allen</em> Str\u00e4nden willkommen!</div>
<div class="gal">
<img src="{imgs['beach_dog']}" alt="Hund am Strand">
<img src="{imgs['beach_pebble']}" alt="Kieselstrand">
<img src="{imgs['beach_turquoise']}" alt="T\u00fcrkises Wasser">
</div>
<h3 style="margin:2rem 0 1rem">Str\u00e4nde in der N\u00e4he</h3>
<div class="cg">
<div class="card"><img src="{img('trget_coast')}" alt="Trget"><div class="cb"><h3>Strand Get</h3><p>Feinkieselstrand 600m s\u00fcdlich von Trget. Sanft abfallend, ideal f\u00fcr Familien und Hunde.</p><a class="more" href="https://www.google.com/maps/dir/45.037297,14.074107/Strand+Get,+Trget,+Croatia" target="_blank">\U0001F697 Route (2,5 km)</a><br><span class="tag dog">\U0001F436 Hundefreundlich</span></div></div>
<div class="card"><img src="{beach_img('Strand Biljina')}" alt="Strand Biljina"><div class="cb"><h3>Strand Biljina</h3><p>Kieselstrand direkt am Hafen von Trget, umgeben von alten Fischerhäusern und Bootsanlegern. Authentisches Fischerdorf-Flair, ruhig und wenig besucht.</p><a class="more" href="https://www.google.com/maps/dir/45.037297,14.074107/45.020383,14.056371" target="_blank">\U0001F697 Route (2,5 km)</a><br><span class="tag dog">\U0001F436 Hundefreundlich</span></div></div>
<div class="card"><img src="{beach_img('Plaža Rupa')}" alt="Plaža Rupa"><div class="cb"><h3>Plaža Rupa</h3><p>Versteckte Kieselbucht südlich von Strand Get. Flach abfallend, kristallklares Wasser \u2013 ideal für Familien und ängstliche Hunde.</p><a class="more" href="https://www.google.com/maps/dir/45.037297,14.074107/45.022,14.055" target="_blank">\U0001F697 Route (~3 km)</a><br><span class="tag dog">\U0001F436 Hundefreundlich</span></div></div>
<div class="card"><img src="{img('rabac_beach')}" alt="Rabac"><div class="cb"><h3>Pla\u017ea Maslinica</h3><p>400m Kieselstrand \u2013 Rabacs Hauptstrand. Wei\u00dfe Kiesel, glasklares Wasser, Blue Flag.</p><a class="more" href="https://www.google.com/maps/dir/45.037297,14.074107/Maslinica+Beach,+Rabac,+Croatia" target="_blank">\U0001F697 Route (19 Min.)</a> \u00b7 <a class="more" href="https://www.tripadvisor.com/Attraction_Review-g303832-d15083674-Reviews-Maslinica_Beach-Rabac_Istria.html" target="_blank">Fotos</a><br><span class="tag dog">\U0001F436 Hundefreundlich</span></div></div>
<div class="card"><img src="{img('girandella')}" alt="Girandella"><div class="cb"><h3>Strand Girandella</h3><p>Blue-Flag-Strand umgeben von Pinien. Kristallklares Wasser, Strandbar, Wassersport.</p><a class="more" href="https://www.google.com/maps/dir/45.037297,14.074107/Girandella+Beach,+Rabac,+Croatia" target="_blank">\U0001F697 Route (21 Min.)</a> \u00b7 <a class="more" href="https://croatia.hr/en-gb/beaches/girandella-beach" target="_blank">Fotos</a><br><span class="tag dog">\U0001F436 Hundefreundlich</span></div></div>
<div class="card"><div class="cb"><h3>\u2B50 Hundestrand Ravni</h3><p>Offizieller Hundestrand! 210m Kiesel, auch bei Windsurfern beliebt. Parkplatz, WC, Restaurant.</p><a class="more" href="https://www.google.com/maps/dir/45.037297,14.074107/Ravni+Beach,+Croatia" target="_blank">\U0001F697 Route (25 Min.)</a> \u00b7 <a class="more" href="https://www.istriasun.com/istria/ravni-beach" target="_blank">Infos</a><br><span class="tag dog">\U0001F436 Offizieller Hundestrand</span></div></div>
<div class="card"><img src="{beach_img('Plaža Prtlog')}" alt="Plaža Prtlog"><div class="cb"><h3>Plaža Prtlog</h3><p>Naturbelassener Fels- und Kiesstrand auf der Halbinsel Duga Luka. Windgeschützte Bucht mit kristallklarem Wasser, fast menschenleer. Keine Infrastruktur \u2013 pure Natur!</p><a class="more" href="https://www.google.com/maps/dir/45.037297,14.074107/45.0546,14.1432" target="_blank">\U0001F697 Route (~15 Min.)</a><br><span class="tag">Geheimtipp</span></div></div>
<div class="card"><img src="{beach_img('beach Drenje')}" alt="Beach Drenje"><div class="cb"><h3>Strand Drenje</h3><p>Ruhiger, abgeschiedener Kiesstrand nahe dem Naturpark Učka. Kaum besucht, perfekt für Ruhe und schöne Sonnenuntergänge. Keine Einrichtungen vor Ort.</p><a class="more" href="https://www.google.com/maps/dir/45.037297,14.074107/45.0207899,14.1586863" target="_blank">\U0001F697 Route (~20 Min.)</a><br><span class="tag">Ruhige Lage</span></div></div>
</div>
</div></section>

<!-- SEHENSWÜRDIGKEITEN -->
<section id="ausfluge">
<h2 class="st">Sehensw\u00fcrdigkeiten &amp; Ausfl\u00fcge</h2>
<p class="ss">Von Natur \u00fcber Geschichte bis hin zu malerischen St\u00e4dten</p>
<div class="cg">
<div class="card"><img src="{img('sentonina')}" alt="Sentonina"><div class="cb"><h3>\U0001F4A7 Wasserfall Sentonina Staza</h3><p>2,4 km Wanderweg: 7 Br\u00fccken, Wasserf\u00e4lle, t\u00fcrkisfarbener See und M\u00fchlenruine. Der Legende nach lebte hier die Fee Sentona.</p><a class="more" href="https://www.alltrails.com/de/route/croatia/istra/804-sentonina-staza" target="_blank">\u2192 AllTrails</a> \u00b7 <a class="more" href="https://www.google.com/maps/dir/45.037297,14.074107/Sentonina+staza,+Labin,+Croatia" target="_blank">\U0001F697 Route</a><br><span class="tag">\U0001F697 17 Min.</span></div></div>
<div class="card"><img src="{img('labin_altstadt')}" alt="Labin"><div class="cb"><h3>\U0001F3DB\uFE0F Altstadt Labin</h3><p>Kunstateliers, Volksmuseum, Sanfior Gate (1589). Vom Aussichtspunkt Fortica atemberaubender Adria-Blick.</p><a class="more" href="https://worldonabudget.de/labin-kroatien-istrien/" target="_blank">\u2192 Reisef\u00fchrer</a> \u00b7 <a class="more" href="https://www.google.com/maps/dir/45.037297,14.074107/Labin+Old+Town,+Croatia" target="_blank">\U0001F697 Route</a><br><span class="tag">\U0001F697 15 Min.</span></div></div>
<div class="card"><img src="{img('pula_arena')}" alt="Pula Arena"><div class="cb"><h3>\U0001F3DB\uFE0F Pula \u2013 R\u00f6mische Arena</h3><p>Eine der gr\u00f6\u00dften erhaltenen r\u00f6mischen Arenen! Goldenes Tor, Forum Romanum. Konzerte &amp; Filmfestival im Sommer.</p><a class="more" href="https://en.wikipedia.org/wiki/Pula_Arena" target="_blank">\u2192 Wikipedia</a> \u00b7 <a class="more" href="https://www.google.com/maps/dir/45.037297,14.074107/Pula+Arena,+Croatia" target="_blank">\U0001F697 Route</a><br><span class="tag">\U0001F697 47 Min.</span></div></div>
<div class="card"><img src="{img('rovinj')}" alt="Rovinj"><div class="cb"><h3>\u26EA Rovinj</h3><p>Romantische Altstadt mit G\u00e4sschen voller Galerien. Von der Kirche der Hl. Euphemia bester K\u00fcstenblick.</p><a class="more" href="https://abenteuerglobus.com/rovinj-tipps/" target="_blank">\u2192 Reisef\u00fchrer</a> \u00b7 <a class="more" href="https://www.google.com/maps/dir/45.037297,14.074107/Rovinj+Old+Town,+Croatia" target="_blank">\U0001F697 Route</a><br><span class="tag">\U0001F697 ~1,5 Std.</span></div></div>
<div class="card"><img src="{img('kap_kamenjak')}" alt="Kamenjak"><div class="cb"><h3>\U0001F3D6\uFE0F Kap Kamenjak</h3><p>Naturpark an der S\u00fcdspitze Istriens. Wilde K\u00fcste, Traumstrand Njive, Schnorcheln und Klippenspringen.</p><a class="more" href="https://www.placesofjuma.com/de/schoenste-straende-istrien/" target="_blank">\u2192 Str\u00e4nde</a> \u00b7 <a class="more" href="https://www.google.com/maps/dir/45.037297,14.074107/Cape+Kamenjak,+Croatia" target="_blank">\U0001F697 Route</a><br><span class="tag">\U0001F697 ~1 Std.</span></div></div>
<div class="card"><div class="cb"><h3>\U0001F682 Pijana Pruga</h3><p>Die \u201ebetrunkenen Gleise\u201c \u2013 historische Bahnlinie von 1951. Heute beliebtes Ausflugsziel und Fotomotiv.</p><span class="tag">\U0001F697 In der N\u00e4he</span></div></div>
</div>
</section>

<!-- RESTAURANTS -->
<section id="restaurants" class="sf"><div class="si">
<h2 class="st">Restaurants &amp; Essen</h2>
<p class="ss">Von Hafenkonoba bis zur besten Pizzeria Kroatiens</p>
<div class="rl">
<div class="rc"><div class="rci">\U0001F963</div><div><h3>Konoba Nando</h3><div class="rloc">Trget \u00b7 Hafen</div><p class="rdesc">Direkt am Hafen, Blick aufs Meer. Frischer Fisch, gegrillte Calamari. Ganzj\u00e4hrig.</p><a class="more" href="https://www.tripadvisor.com/Restaurant_Review-g12938286-d2236361-Reviews-Konoba_Nando-Trget_Istria.html" target="_blank">\u2192 Tripadvisor</a> \u00b7 <a class="more" href="https://www.google.com/maps/dir/45.037297,14.074107/Konoba+Nando,+Trget,+Croatia" target="_blank">\U0001F697 Route</a></div></div>
<div class="rc"><div class="rci">\U0001F41F</div><div><h3>Martin Pescador</h3><div class="rloc">Trget 20</div><p class="rdesc">Fischertaverne mit Boot-Bar. Frischer Fang, Meeresfr\u00fcchte, Hummer. Haus-Wein: Malvasia.</p><a class="more" href="https://www.tripadvisor.com/Restaurant_Review-g12938286-d2332333-Reviews-Martin_Pescador-Trget_Istria.html" target="_blank">\u2192 Tripadvisor</a> \u00b7 <a class="more" href="https://www.google.com/maps/dir/45.037297,14.074107/Martin+Pescador,+Trget,+Croatia" target="_blank">\U0001F697 Route</a></div></div>
<div class="rc"><div class="rci">\U0001F35D</div><div><h3>Velo Kafe</h3><div class="rloc">Labin \u00b7 Titov trg 12</div><p class="rdesc">3 Etagen: Taverne mit Kamin, Caf\u00e9, Restaurant. Pasta, Tr\u00fcffel, Fisch. Mo\u2013So 11\u201323 Uhr.</p><a class="more" href="https://velokafe.com/" target="_blank">\u2192 Website</a> \u00b7 <a class="more" href="https://www.google.com/maps/dir/45.037297,14.074107/Velo+Kafe,+Titov+trg+12,+Labin,+Croatia" target="_blank">\U0001F697 Route</a></div></div>
<div class="rc"><div class="rci">\U0001F990</div><div><h3>Peteani</h3><div class="rloc">Labin \u00b7 Aldo Negri 9</div><p class="rdesc">#1 in Labin! Gault&amp;Millau-ausgezeichnet. Saisonale istrische K\u00fcche, erstklassige Weine.</p><a class="more" href="https://www.tripadvisor.com/Restaurant_Review-g1077176-d12957137-Reviews-Restaurant_Peteani-Labin_Istria.html" target="_blank">\u2192 Tripadvisor</a> \u00b7 <a class="more" href="https://www.google.com/maps/dir/45.037297,14.074107/Restaurant+Peteani,+Aldo+Negri+9,+Labin,+Croatia" target="_blank">\U0001F697 Route</a></div></div>
<div class="rc"><div class="rci">\U0001F355</div><div><h3>\u2B50 Rumore Pizzeria</h3><div class="rloc">Labin \u00b7 \u0160etali\u0161te San Marco 2</div><p class="rdesc">Erste AVPN-zertifizierte Pizzeria Kroatiens! Neapolitanische Pizza aus dem Holzofen. Reservieren!</p><a class="more" href="https://pizzeriarumore.com/en/" target="_blank">\u2192 Website</a> \u00b7 <a class="more" href="https://www.google.com/maps/dir/45.037297,14.074107/Pizzeria+Rumore,+Labin,+Croatia" target="_blank">\U0001F697 Route</a></div></div>
<div class="rc"><div class="rci">\U0001F961</div><div><h3>Jest Urban Food</h3><div class="rloc">Labin \u00b7 Ul. Mate Bla\u017eine 3</div><p class="rdesc">5.0 auf Tripadvisor! Kreative Bao Buns, BBQ, Brunch. Gro\u00dfe Portionen, faire Preise.</p><a class="more" href="https://www.tripadvisor.com/Restaurant_Review-g1077176-d28001447-Reviews-Jest_Urban_Food-Labin_Istria.html" target="_blank">\u2192 Tripadvisor</a> \u00b7 <a class="more" href="https://www.google.com/maps/dir/45.037297,14.074107/Jest+Urban+Food,+Labin,+Croatia" target="_blank">\U0001F697 Route</a></div></div>
</div>
</div></section>

<!-- EINKAUFEN -->
<section id="einkaufen">
<h2 class="st">Einkaufen</h2>
<p class="ss">Superm\u00e4rkte, Markthalle &amp; Shopping</p>
<ul class="sl">
<li><span class="sli">\U0001F6D2</span><div><strong>STOP SHOP Labin</strong><span>\u0160trmac 303 \u00b7 16+ Gesch\u00e4fte: dm, JYSK, Eurospin, KiK, s.Oliver, TEDi, NKD, Sport Vision u.v.m.</span><br><a href="https://cpi-europe.com/en/retail/stop-shop-labin" target="_blank">\u2192 Gesch\u00e4fte &amp; Infos</a></div></li>
<li><span class="sli">\U0001F34E</span><div><strong>Markthalle Labin</strong><span>Zentrum von Podlabin \u00b7 T\u00e4glich 7:00\u201312:30 \u00b7 Frischer Fisch, Fleisch, Obst &amp; Gem\u00fcse.</span></div></li>
<li><span class="sli">\U0001F3EA</span><div><strong>Superm\u00e4rkte Podlabin</strong><span>Gr\u00f6\u00dfere Superm\u00e4rkte im unteren Stadtteil. Ca. 6 km von der Villa.</span></div></li>
</ul>
<div class="ib" style="margin-top:1.5rem"><strong>\U0001F4B6 Gut zu wissen:</strong> Kroatien nutzt seit 2023 den <strong>Euro</strong>. Kartenzahlung fast \u00fcberall m\u00f6glich.</div>
</section>

<!-- KARTE -->
<section id="karte" class="sf"><div class="si">
<h2 class="st">\u00dcbersichtskarte</h2>
<p class="ss">Alle wichtigen Orte auf einen Blick</p>
<img src="{img('static_map')}" alt="\u00dcbersichtskarte Istrien" class="map-img">
<p style="margin-top:.5rem;font-size:.8rem;color:var(--gr)">\u00a9 OpenStreetMap contributors \u00b7 V=Villa, S=Strand, H=Hundestrand, A=Attraktion, L=Labin, R=Restaurant, E=Einkaufen</p>
</div></section>

<!-- Lightbox overlay -->
<div class="lb-overlay" id="lightbox">
<span class="lb-close">&times;</span>
<img id="lb-img" src="" alt="Vollbild">
</div>

<footer>
<p>\U0001F334 Kroatien 2026 \u00b7 Villa Lavanda Macarini \u00b7 18. Juli \u2013 1. August</p>
<p style="margin-top:.5rem;opacity:.6">Erstellt mit \u2764 f\u00fcr den perfekten Urlaub</p>
</footer>

<script>{JS}</script>
</body></html>"""

outpath = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'index.html')
with open(outpath, 'w', encoding='utf-8') as f:
    f.write(html)
print(f"Created: {outpath}")
print(f"Size: {os.path.getsize(outpath) / 1024:.0f} KB")
