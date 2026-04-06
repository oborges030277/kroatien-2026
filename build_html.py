import json, os

img_dir = r'C:\Users\oborg\Desktop\Urlaub 2026 - Kroatien\extracted_images'
with open(os.path.join(img_dir, 'compressed.json'), 'r') as f:
    imgs = json.load(f)

parts = []

# HEAD + CSS
parts.append("""<!DOCTYPE html>
<html lang="de">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Kroatien 2026 \u2013 Villa Lavanda Macarini</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;700&family=Inter:wght@300;400;500;600&display=swap" rel="stylesheet">
<link rel="stylesheet" href="https://unpkg.com/leaflet@1.9.4/dist/leaflet.css" />
<script src="https://unpkg.com/leaflet@1.9.4/dist/leaflet.js"><\/script>
<style>
:root{--sand:#F5E6D0;--sand-light:#FBF5ED;--terracotta:#C4724E;--terracotta-dark:#A85A3A;--blue:#1B6B93;--blue-dark:#153B50;--blue-light:#E8F4F8;--white:#fff;--gray:#6B7280}
*{margin:0;padding:0;box-sizing:border-box}
html{scroll-behavior:smooth}
body{font-family:'Inter',sans-serif;color:var(--blue-dark);background:var(--sand-light);line-height:1.6}
h1,h2,h3,h4{font-family:'Playfair Display',serif}
nav{position:fixed;top:0;width:100%;background:rgba(21,59,80,0.95);backdrop-filter:blur(10px);z-index:1000}
nav ul{display:flex;list-style:none;max-width:1200px;margin:0 auto;padding:0 1rem;overflow-x:auto}
nav ul::-webkit-scrollbar{display:none}
nav li a{display:block;padding:1rem 0.8rem;color:var(--sand);text-decoration:none;font-size:0.85rem;font-weight:500;white-space:nowrap;transition:color 0.3s}
nav li a:hover{color:var(--terracotta)}
.hero{position:relative;height:100vh;min-height:600px;display:flex;align-items:center;justify-content:center;text-align:center;color:white;overflow:hidden}
.hero-bg{position:absolute;inset:0;background-size:cover;background-position:center;filter:brightness(0.6)}
.hero-content{position:relative;z-index:1;padding:2rem}
.hero h1{font-size:clamp(2.5rem,8vw,5rem);margin-bottom:0.5rem;text-shadow:2px 2px 20px rgba(0,0,0,0.5)}
.hero .subtitle{font-size:clamp(1rem,3vw,1.5rem);font-weight:300;margin-bottom:2rem;opacity:0.9}
.countdown{display:flex;gap:1.5rem;justify-content:center;flex-wrap:wrap;margin-top:1rem}
.countdown-item{background:rgba(255,255,255,0.15);backdrop-filter:blur(10px);border:1px solid rgba(255,255,255,0.3);border-radius:12px;padding:1.2rem 1.5rem;min-width:90px}
.countdown-item .number{font-family:'Playfair Display',serif;font-size:2.5rem;font-weight:700;display:block;line-height:1}
.countdown-item .label{font-size:0.75rem;text-transform:uppercase;letter-spacing:2px;opacity:0.8;margin-top:0.3rem;display:block}
section{padding:5rem 1.5rem;max-width:1200px;margin:0 auto}
.section-full{max-width:100%;background:var(--white);padding-left:0;padding-right:0}
.section-inner{max-width:1200px;margin:0 auto;padding:0 1.5rem}
.section-title{font-size:clamp(1.8rem,4vw,2.5rem);margin-bottom:0.5rem;color:var(--blue-dark)}
.section-subtitle{color:var(--gray);font-size:1.05rem;margin-bottom:2.5rem;font-weight:300}
.card-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(300px,1fr));gap:1.5rem}
.card{background:var(--white);border-radius:16px;overflow:hidden;box-shadow:0 4px 20px rgba(0,0,0,0.08);transition:transform 0.3s,box-shadow 0.3s}
.section-full .card{background:var(--sand-light)}
.card:hover{transform:translateY(-4px);box-shadow:0 8px 30px rgba(0,0,0,0.12)}
.card img{width:100%;height:200px;object-fit:cover}
.card-body{padding:1.5rem}
.card-body h3{font-size:1.2rem;margin-bottom:0.5rem}
.card-body p{color:var(--gray);font-size:0.95rem}
.card-tag{display:inline-block;background:var(--blue-light);color:var(--blue);padding:0.25rem 0.75rem;border-radius:20px;font-size:0.8rem;font-weight:500;margin-top:0.75rem;margin-right:0.25rem}
.card-tag.dog{background:#FEF3C7;color:#92400E}
.icon-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(150px,1fr));gap:1rem;margin:1.5rem 0}
.icon-item{display:flex;align-items:center;gap:0.75rem;padding:0.75rem;background:var(--sand-light);border-radius:10px;font-size:0.9rem}
.section-full .icon-item{background:var(--white)}
.icon-item .emoji{font-size:1.3rem}
.info-box{background:var(--blue-light);border-left:4px solid var(--blue);padding:1.25rem 1.5rem;border-radius:0 10px 10px 0;margin:1.5rem 0}
.info-box.warning{background:#FEF3C7;border-color:#F59E0B}
.info-box.dog{background:#ECFDF5;border-color:#10B981}
.gallery{display:grid;grid-template-columns:repeat(auto-fill,minmax(250px,1fr));gap:1rem;margin:1.5rem 0}
.gallery img{width:100%;height:220px;object-fit:cover;border-radius:12px;transition:transform 0.3s}
.gallery img:hover{transform:scale(1.03)}
.weather-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(200px,1fr));gap:1.5rem;margin:1.5rem 0}
.weather-card{text-align:center;padding:2rem 1.5rem;background:linear-gradient(135deg,var(--blue),var(--blue-dark));color:white;border-radius:16px}
.weather-card .wi{font-size:2.5rem;margin-bottom:0.5rem}
.weather-card .wv{font-family:'Playfair Display',serif;font-size:2rem;font-weight:700}
.weather-card .wl{font-size:0.85rem;opacity:0.8;margin-top:0.25rem}
.btn{display:inline-block;padding:0.8rem 2rem;background:var(--terracotta);color:white;text-decoration:none;border-radius:30px;font-weight:500;transition:background 0.3s,transform 0.3s;font-size:0.95rem}
.btn:hover{background:var(--terracotta-dark);transform:translateY(-2px)}
.rules-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(220px,1fr));gap:1rem;margin:1.5rem 0}
.rule-item{display:flex;align-items:center;gap:0.75rem;padding:1rem;background:var(--sand-light);border-radius:10px}
.rule-item .ri{font-size:1.5rem}
.rooms-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(180px,1fr));gap:1rem;margin:1.5rem 0}
.room-card{padding:1.25rem;background:var(--sand-light);border-radius:12px;text-align:center}
.room-card .ro{font-size:2rem;margin-bottom:0.5rem}
.room-card h4{font-size:1rem;margin-bottom:0.25rem}
.room-card p{font-size:0.85rem;color:var(--gray)}
#map{height:500px;border-radius:16px;margin-top:1.5rem;box-shadow:0 4px 20px rgba(0,0,0,0.1)}
.rl{display:grid;grid-template-columns:repeat(auto-fill,minmax(350px,1fr));gap:1.5rem}
.ri-card{display:flex;gap:1rem;padding:1.5rem;background:var(--sand-light);border-radius:12px;box-shadow:0 2px 10px rgba(0,0,0,0.06)}
.ri-card .ric{font-size:1.5rem;flex-shrink:0;width:50px;height:50px;background:var(--terracotta);color:white;border-radius:12px;display:flex;align-items:center;justify-content:center}
.ri-card h3{font-size:1.05rem;margin-bottom:0.2rem}
.ri-card .rloc{font-size:0.8rem;color:var(--terracotta);font-weight:500}
.ri-card .rdesc{font-size:0.9rem;color:var(--gray);margin-top:0.3rem}
.tip-cards{display:grid;grid-template-columns:repeat(auto-fill,minmax(280px,1fr));gap:1.5rem;margin:1.5rem 0}
.tip-card{padding:1.5rem;background:var(--sand-light);border-radius:12px;border-top:4px solid var(--terracotta)}
.section-full .tip-card{background:var(--white)}
.tip-card h4{margin-bottom:0.5rem}
.tip-card p{font-size:0.9rem;color:var(--gray)}
.sl{list-style:none}
.sl li{padding:1rem 1.25rem;background:var(--sand-light);border-radius:10px;margin-bottom:0.75rem;display:flex;align-items:flex-start;gap:0.75rem}
.sl li .si{font-size:1.3rem;flex-shrink:0;margin-top:2px}
.sl li strong{display:block;margin-bottom:0.2rem}
.sl li span{font-size:0.9rem;color:var(--gray)}
footer{background:var(--blue-dark);color:var(--sand);text-align:center;padding:2rem 1.5rem;font-size:0.85rem}
@media(max-width:768px){
  nav li a{padding:0.8rem 0.6rem;font-size:0.75rem}
  section{padding:3rem 1rem}
  .countdown{gap:0.75rem}
  .countdown-item{padding:0.8rem 1rem;min-width:70px}
  .countdown-item .number{font-size:1.8rem}
  .card-grid,.rl{grid-template-columns:1fr}
  #map{height:350px}
  .gallery{grid-template-columns:1fr}
}
</style>
</head>
<body>
""")

# NAV
parts.append("""
<nav>
  <ul>
    <li><a href="#hero">Start</a></li>
    <li><a href="#unterkunft">Unterkunft</a></li>
    <li><a href="#anreise">Anreise</a></li>
    <li><a href="#wetter">Wetter</a></li>
    <li><a href="#straende">Str\u00e4nde</a></li>
    <li><a href="#ausfluge">Ausfl\u00fcge</a></li>
    <li><a href="#restaurants">Restaurants</a></li>
    <li><a href="#einkaufen">Einkaufen</a></li>
    <li><a href="#karte">Karte</a></li>
  </ul>
</nav>
""")

# HERO
parts.append(f"""
<section class="hero" id="hero">
  <div class="hero-bg" style="background-image:url('{imgs["hero"]}')"></div>
  <div class="hero-content">
    <h1>Kroatien 2026</h1>
    <p class="subtitle">Villa Lavanda Macarini \u00b7 18. Juli \u2013 1. August</p>
    <div class="countdown" id="countdown">
      <div class="countdown-item"><span class="number" id="cd-days">--</span><span class="label">Tage</span></div>
      <div class="countdown-item"><span class="number" id="cd-hours">--</span><span class="label">Stunden</span></div>
      <div class="countdown-item"><span class="number" id="cd-mins">--</span><span class="label">Minuten</span></div>
      <div class="countdown-item"><span class="number" id="cd-secs">--</span><span class="label">Sekunden</span></div>
    </div>
  </div>
</section>
""")

# UNTERKUNFT
parts.append(f"""
<section id="unterkunft">
  <h2 class="section-title">Die Unterkunft</h2>
  <p class="section-subtitle">Villa Lavanda Macarini \u00b7 Brgod, Trget \u00b7 52224 Kroatien</p>
  <div class="gallery">
    <img src="{imgs['hero']}" alt="Villa Lavanda mit Pool">
    <img src="{imgs['villa_entrance']}" alt="Einfahrt zur Villa">
    <img src="{imgs['villa_path']}" alt="Weg zur Villa">
  </div>
  <h3 style="margin:2rem 0 0.5rem">Ausstattung</h3>
  <div class="icon-grid">
    <div class="icon-item"><span class="emoji">\U0001F3CA</span> Beheizter Pool</div>
    <div class="icon-item"><span class="emoji">\U0001F6CF</span> 3 Schlafzimmer</div>
    <div class="icon-item"><span class="emoji">\U0001F6C1</span> 4 Badezimmer</div>
    <div class="icon-item"><span class="emoji">\U0001F4CF</span> 127 m\u00b2</div>
    <div class="icon-item"><span class="emoji">\U0001F373</span> K\u00fcche</div>
    <div class="icon-item"><span class="emoji">\U0001F9F9</span> Waschmaschine</div>
    <div class="icon-item"><span class="emoji">\U0001F32C</span> Trockner</div>
    <div class="icon-item"><span class="emoji">\U0001F4F6</span> Kostenloses WLAN</div>
    <div class="icon-item"><span class="emoji">\U0001F436</span> Haustierfreundlich</div>
    <div class="icon-item"><span class="emoji">\U0001F33B</span> Garten</div>
    <div class="icon-item"><span class="emoji">\u2600\uFE0F</span> Terrasse / Patio</div>
    <div class="icon-item"><span class="emoji">\U0001F3D3</span> Spielbereich</div>
  </div>
  <h3 style="margin:2rem 0 0.5rem">Zimmeraufteilung</h3>
  <div class="rooms-grid">
    <div class="room-card"><div class="ro">\U0001F6CC</div><h4>Schlafzimmer 1</h4><p>1 King-Bett</p></div>
    <div class="room-card"><div class="ro">\U0001F6CC</div><h4>Schlafzimmer 2</h4><p>1 King-Bett</p></div>
    <div class="room-card"><div class="ro">\U0001F6CC</div><h4>Schlafzimmer 3</h4><p>2 Einzelbetten</p></div>
    <div class="room-card"><div class="ro">\U0001F6CB</div><h4>Wohnzimmer</h4><p>1 gro\u00dfes Schlafsofa</p></div>
  </div>
  <h3 style="margin:2rem 0 0.5rem">Hausordnung</h3>
  <div class="rules-grid">
    <div class="rule-item"><span class="ri">\U0001F551</span><div><strong>Check-in</strong> ab 15:00 Uhr</div></div>
    <div class="rule-item"><span class="ri">\U0001F559</span><div><strong>Check-out</strong> vor 10:00 Uhr</div></div>
    <div class="rule-item"><span class="ri">\U0001F436</span><div><strong>Haustiere</strong> Erlaubt (max. 2)</div></div>
    <div class="rule-item"><span class="ri">\U0001F467</span><div><strong>Kinder</strong> 0\u201317 Jahre erlaubt</div></div>
    <div class="rule-item"><span class="ri">\U0001F6AB</span><div><strong>Rauchen</strong> Nicht gestattet</div></div>
    <div class="rule-item"><span class="ri">\U0001F6AB</span><div><strong>Events</strong> Nicht gestattet</div></div>
  </div>
  <div class="info-box" style="margin-top:2rem">
    <strong>\U0001F4F6 WLAN:</strong> Netzwerkname \u201eVilla Lavanda Macarini\u201c
  </div>
  <div style="margin-top:2rem">
    <a href="https://www.airbnb.de/rooms/887083250524888042" target="_blank" class="btn">\U0001F3E0 Auf Airbnb ansehen</a>
  </div>
</section>
""")

# ANREISE
parts.append(f"""
<section id="anreise" class="section-full">
  <div class="section-inner">
    <h2 class="section-title">Anreise</h2>
    <p class="section-subtitle">~1.240 km \u00b7 ca. 12 Stunden Fahrt</p>
    <div class="gallery" style="grid-template-columns:2fr 1fr">
      <img src="{imgs['route_overview']}" alt="Routenplanung" style="height:300px">
      <img src="{imgs['route_istria']}" alt="Route durch Istrien" style="height:300px">
    </div>
    <h3 style="margin:2rem 0 1rem">Maut &amp; Vignetten</h3>
    <div class="tip-cards">
      <div class="tip-card">
        <h4>\U0001F1E6\U0001F1F9 \u00d6sterreich</h4>
        <p>Digitale Vignette \u00fcber <strong>asfinag.at</strong>. 10-Tages-Vignette reicht bei 14 Tagen Urlaub <em>nicht</em> \u2013 besser 2-Monats-Vignette kaufen.</p>
      </div>
      <div class="tip-card">
        <h4>\U0001F1F8\U0001F1EE Slowenien</h4>
        <p>E-Vignette \u00fcber <strong>evinjeta.dars.si</strong>. 7-Tage oder 30-Tage. Wird digital am Kennzeichen registriert.</p>
      </div>
      <div class="tip-card">
        <h4>\U0001F1ED\U0001F1F7 Kroatien</h4>
        <p>Mautstationen auf der Autobahn. Bezahlung mit Karte oder bar. ENC-Transponder f\u00fcr schnellere Durchfahrt optional.</p>
      </div>
    </div>
    <div class="info-box" style="margin-top:1.5rem">
      <strong>\U0001F4A1 Tipp:</strong> M\u00f6gliche Zwischenstopps: M\u00fcnchen, Salzburg oder Ljubljana \u2013 ideal f\u00fcr eine Pause.
    </div>
  </div>
</section>
""")

# WETTER
parts.append("""
<section id="wetter">
  <h2 class="section-title">Wetter im Juli</h2>
  <p class="section-subtitle">Durchschnittswerte f\u00fcr Istrien im Hochsommer</p>
  <div class="weather-grid">
    <div class="weather-card">
      <div class="wi">\u2600\uFE0F</div>
      <div class="wv">27\u201330\u00b0C</div>
      <div class="wl">Lufttemperatur</div>
    </div>
    <div class="weather-card" style="background:linear-gradient(135deg,#0891b2,#164e63)">
      <div class="wi">\U0001F30A</div>
      <div class="wv">24\u201326\u00b0C</div>
      <div class="wl">Wassertemperatur</div>
    </div>
    <div class="weather-card" style="background:linear-gradient(135deg,#d97706,#92400e)">
      <div class="wi">\U0001F31E</div>
      <div class="wv">~11 Std.</div>
      <div class="wl">Sonnenstunden / Tag</div>
    </div>
    <div class="weather-card" style="background:linear-gradient(135deg,#6366f1,#312e81)">
      <div class="wi">\U0001F327\uFE0F</div>
      <div class="wv">~4 Tage</div>
      <div class="wl">Regentage / Monat</div>
    </div>
  </div>
</section>
""")

# STRÄNDE
parts.append(f"""
<section id="straende" class="section-full">
  <div class="section-inner">
    <h2 class="section-title">Str\u00e4nde</h2>
    <p class="section-subtitle">Kiesel, t\u00fcrkises Wasser &amp; hundefreundlich</p>
    <div class="info-box dog">
      <strong>\U0001F436 Gute Nachricht!</strong> In der Region Labin/Rabac sind Hunde grunds\u00e4tzlich an <em>allen</em> Str\u00e4nden willkommen! Bitte Abstand zu anderen Badeg\u00e4sten halten und den Hund anleinen, wenn n\u00f6tig.
    </div>
    <div class="gallery">
      <img src="{imgs['beach_dog']}" alt="Hund am Strand">
      <img src="{imgs['beach_pebble']}" alt="Kieselstrand">
      <img src="{imgs['beach_turquoise']}" alt="T\u00fcrkises Wasser">
    </div>
    <h3 style="margin:2rem 0 1rem">Str\u00e4nde in der N\u00e4he</h3>
    <div class="card-grid">
      <div class="card"><div class="card-body">
        <h3>Strand Get</h3>
        <p>Feinkieselstrand ca. 600m s\u00fcdlich vom Ortszentrum Trget. Sanft abfallend, ideal f\u00fcr Familien und Hunde.</p>
        <span class="card-tag">~2,5 km</span><span class="card-tag dog">\U0001F436 Hundefreundlich</span>
      </div></div>
      <div class="card"><div class="card-body">
        <h3>Strand Biljino</h3>
        <p>Kleiner Strand in Trget mit Bootsanlegern. Ruhige Atmosph\u00e4re, ideal zum Entspannen.</p>
        <span class="card-tag">~2,5 km</span><span class="card-tag dog">\U0001F436 Hundefreundlich</span>
      </div></div>
      <div class="card"><div class="card-body">
        <h3>Strand Rupa</h3>
        <p>Flach abfallender Kieselstrand in Trget. Auch f\u00fcr \u00e4ngstliche Hunde geeignet dank sanftem Einstieg.</p>
        <span class="card-tag">~3 km</span><span class="card-tag dog">\U0001F436 Hundefreundlich</span>
      </div></div>
      <div class="card"><div class="card-body">
        <h3>Pla\u017ea Maslinica (Rabac)</h3>
        <p>\u00dcber 400m langer Kieselstrand \u2013 der Hauptstrand von Rabac. Wei\u00dfe Kiesel, glasklares Wasser.</p>
        <span class="card-tag">~19 Min.</span><span class="card-tag dog">\U0001F436 Hundefreundlich</span>
      </div></div>
      <div class="card"><div class="card-body">
        <h3>Strand Girandella (Rabac)</h3>
        <p>Beliebter Kieselstrand mit guter Infrastruktur. Wundersch\u00f6nes t\u00fcrkises Wasser.</p>
        <span class="card-tag">~21 Min.</span><span class="card-tag dog">\U0001F436 Hundefreundlich</span>
      </div></div>
      <div class="card"><div class="card-body">
        <h3>\u2B50 Hundestrand Ravni</h3>
        <p>Explizit ausgewiesener Hundestrand! Auch bei Windsurfern beliebt. Naturbelassen und ruhig.</p>
        <span class="card-tag">~25 Min.</span><span class="card-tag dog">\U0001F436 Offizieller Hundestrand</span>
      </div></div>
    </div>
  </div>
</section>
""")

# SEHENSWÜRDIGKEITEN
parts.append("""
<section id="ausfluge">
  <h2 class="section-title">Sehensw\u00fcrdigkeiten &amp; Ausfl\u00fcge</h2>
  <p class="section-subtitle">Von Natur \u00fcber Geschichte bis hin zu malerischen St\u00e4dten</p>
  <div class="card-grid">
    <div class="card"><div class="card-body">
      <h3>\U0001F4A7 Wasserfall Sentonina Staza</h3>
      <p>2,4 km Wanderweg zwischen Labin und Rabac. 7 Br\u00fccken, mehrere Wasserf\u00e4lle und ein t\u00fcrkisfarbener See. Dazu Ruinen einer alten M\u00fchle. Der Legende nach lebte hier die Fee Sentona.</p>
      <span class="card-tag">\U0001F697 17 Min.</span>
    </div></div>
    <div class="card"><div class="card-body">
      <h3>\U0001F3DB\uFE0F Altstadt Labin</h3>
      <p>Malerische Kleinstadt auf dem Berg mit Kunstateliers, Volksmuseum und dem Sanfior Gate von 1589. Vom Aussichtspunkt Fortica atemberaubender Blick auf Rabac und die Adria.</p>
      <span class="card-tag">\U0001F697 15 Min.</span>
    </div></div>
    <div class="card"><div class="card-body">
      <h3>\U0001F3DB\uFE0F Pula \u2013 R\u00f6mische Arena</h3>
      <p>Eine der gr\u00f6\u00dften erhaltenen r\u00f6mischen Arenen der Welt! Triumphbogen (Goldenes Tor) und Forum Romanum. Im Sommer Konzerte und Filmfestival.</p>
      <span class="card-tag">\U0001F697 47 Min.</span>
    </div></div>
    <div class="card"><div class="card-body">
      <h3>\u26EA Rovinj</h3>
      <p>Romantische Altstadt mit gewundenen G\u00e4sschen voller Galerien. Von der Kirche der Hl. Euphemia bester Ausblick \u00fcber K\u00fcste und Inseln.</p>
      <span class="card-tag">\U0001F697 ~1,5 Std.</span>
    </div></div>
    <div class="card"><div class="card-body">
      <h3>\U0001F3D6\uFE0F Kap Kamenjak</h3>
      <p>Naturpark an der S\u00fcdspitze Istriens mit Traumstrand Njive. Wilde K\u00fcstenlandschaft, ideal zum Schnorcheln und Klippenspringen.</p>
      <span class="card-tag">\U0001F697 ~1 Std.</span>
    </div></div>
    <div class="card"><div class="card-body">
      <h3>\U0001F682 Pijana Pruga</h3>
      <p>Die \u201ebetrunkenen Gleise\u201c \u2013 historische Bahnlinie von 1951 f\u00fcr den Kohletransport aus Labin. Heute beliebtes Ausflugsziel und Fotomotiv.</p>
      <span class="card-tag">\U0001F697 In der N\u00e4he</span>
    </div></div>
  </div>
</section>
""")

# RESTAURANTS
parts.append("""
<section id="restaurants" class="section-full">
  <div class="section-inner">
    <h2 class="section-title">Restaurants &amp; Essen</h2>
    <p class="section-subtitle">Von Hafenkonoba bis zur besten Pizzeria Kroatiens</p>
    <div class="rl">
      <div class="ri-card">
        <div class="ric">\U0001F963</div>
        <div><h3>Buffet Nando</h3><div class="rloc">Trget \u00b7 Hafen</div><p class="rdesc">Typisch istrisch, direkt am Hafen. Besonders empfohlen: gegrillte Calamari. Ganzj\u00e4hrig ab 12 Uhr.</p></div>
      </div>
      <div class="ri-card">
        <div class="ric">\U0001F41F</div>
        <div><h3>Konoba Martin Pescador</h3><div class="rloc">Trget 11/A</div><p class="rdesc">Fischrestaurant im Fischerdorf. Frischer Fang aus der Adria, ganzj\u00e4hrig ge\u00f6ffnet.</p></div>
      </div>
      <div class="ri-card">
        <div class="ric">\U0001F35D</div>
        <div><h3>Velo Kafe</h3><div class="rloc">Labin \u00b7 Hauptplatz</div><p class="rdesc">Zwei Au\u00dfenterrassen, drei Etagen. Pasta, Gnocchi, Fisch und Tr\u00fcffelgerichte.</p></div>
      </div>
      <div class="ri-card">
        <div class="ric">\U0001F990</div>
        <div><h3>Peteani</h3><div class="rloc">Labin \u00b7 Aldo Negri 9</div><p class="rdesc">Elegantes Restaurant mit ausgezeichneten Meeresfr\u00fcchten. F\u00fcr besondere Anl\u00e4sse.</p></div>
      </div>
      <div class="ri-card">
        <div class="ric">\U0001F355</div>
        <div><h3>\u2B50 Rumore Pizzeria</h3><div class="rloc">Labin \u00b7 San Marco Promenade</div><p class="rdesc">Mehrfach als <strong>beste Pizzeria Kroatiens</strong> ausgezeichnet! Unbedingt reservieren.</p></div>
      </div>
      <div class="ri-card">
        <div class="ric">\U0001F961</div>
        <div><h3>Jest Urban Food</h3><div class="rloc">Labin</div><p class="rdesc">Verstecktes Juwel mit gro\u00dfen Portionen zu fairen Preisen. Istrische Spezialit\u00e4ten und Bao Buns.</p></div>
      </div>
    </div>
  </div>
</section>
""")

# EINKAUFEN
parts.append("""
<section id="einkaufen">
  <h2 class="section-title">Einkaufen</h2>
  <p class="section-subtitle">Superm\u00e4rkte, Markthalle &amp; Shopping</p>
  <ul class="sl">
    <li><span class="si">\U0001F6D2</span><div><strong>STOP SHOP Labin</strong><span>\u0160trmac 303 \u00b7 16+ Gesch\u00e4fte: dm, JYSK, Eurospin, KiK, s.Oliver, TEDi, NKD, Sport Vision u.v.m.</span></div></li>
    <li><span class="si">\U0001F34E</span><div><strong>Markthalle Labin</strong><span>Zentrum von Podlabin \u00b7 T\u00e4glich 7:00\u201312:30 Uhr \u00b7 Frischer Fisch, Fleisch, Obst &amp; Gem\u00fcse nach Saison.</span></div></li>
    <li><span class="si">\U0001F3EA</span><div><strong>Superm\u00e4rkte Podlabin</strong><span>Gr\u00f6\u00dfere Superm\u00e4rkte im unteren Stadtteil von Labin. Ca. 6 km von der Villa.</span></div></li>
  </ul>
  <div class="info-box" style="margin-top:1.5rem">
    <strong>\U0001F4B6 Gut zu wissen:</strong> Kroatien nutzt seit 2023 den <strong>Euro</strong> als W\u00e4hrung. Kartenzahlung ist fast \u00fcberall m\u00f6glich.
  </div>
</section>
""")

# KARTE + FOOTER + JS
parts.append("""
<section id="karte" class="section-full">
  <div class="section-inner">
    <h2 class="section-title">Interaktive Karte</h2>
    <p class="section-subtitle">Alle wichtigen Orte auf einen Blick</p>
    <div id="map"></div>
  </div>
</section>

<footer>
  <p>\U0001F334 Kroatien 2026 \u00b7 Villa Lavanda Macarini \u00b7 18. Juli \u2013 1. August</p>
  <p style="margin-top:0.5rem;opacity:0.6">Erstellt mit \u2764 f\u00fcr den perfekten Urlaub</p>
</footer>

<script>
// Countdown
function updateCountdown(){
  var target=new Date('2026-07-18T15:00:00+02:00');
  var now=new Date();
  var diff=target-now;
  if(diff<=0){document.getElementById('countdown').innerHTML='<p style="font-size:1.5rem">\\U0001F389 Der Urlaub hat begonnen!</p>';return}
  var d=Math.floor(diff/(1000*60*60*24));
  var h=Math.floor((diff%(1000*60*60*24))/(1000*60*60));
  var m=Math.floor((diff%(1000*60*60))/(1000*60));
  var s=Math.floor((diff%(1000*60))/1000);
  document.getElementById('cd-days').textContent=d;
  document.getElementById('cd-hours').textContent=('0'+h).slice(-2);
  document.getElementById('cd-mins').textContent=('0'+m).slice(-2);
  document.getElementById('cd-secs').textContent=('0'+s).slice(-2);
}
updateCountdown();
setInterval(updateCountdown,1000);

// Map
document.addEventListener('DOMContentLoaded',function(){
  var map=L.map('map').setView([45.08,14.10],12);
  L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png',{
    attribution:'\\u00a9 OpenStreetMap contributors',maxZoom:18
  }).addTo(map);

  function mk(color){
    return L.divIcon({className:'',html:'<div style="background:'+color+';width:28px;height:28px;border-radius:50%;border:3px solid white;box-shadow:0 2px 6px rgba(0,0,0,0.3)"><\\/div>',iconSize:[28,28],iconAnchor:[14,14],popupAnchor:[0,-16]});
  }
  var ic={v:mk('#C4724E'),b:mk('#0891b2'),s:mk('#7C3AED'),f:mk('#DC2626'),sh:mk('#059669')};

  L.marker([45.0595,14.0870],{icon:ic.v}).addTo(map).bindPopup('<strong>\\U0001F3E0 Villa Lavanda</strong><br>Unsere Unterkunft');
  L.marker([45.0680,14.0580],{icon:ic.b}).addTo(map).bindPopup('<strong>Strand Get</strong><br>Feinkiesel, ~2,5km');
  L.marker([45.0700,14.0560],{icon:ic.b}).addTo(map).bindPopup('<strong>Strand Biljino</strong><br>Trget');
  L.marker([45.0830,14.1530],{icon:ic.b}).addTo(map).bindPopup('<strong>Pla\\u017ea Maslinica</strong><br>Rabac, 400m');
  L.marker([45.0780,14.1590],{icon:ic.b}).addTo(map).bindPopup('<strong>Strand Girandella</strong><br>Rabac');
  L.marker([45.0550,14.0350],{icon:ic.b}).addTo(map).bindPopup('<strong>\\u2B50 Hundestrand Ravni</strong><br>Offizieller Hundestrand!');
  L.marker([45.0880,14.1250],{icon:ic.s}).addTo(map).bindPopup('<strong>Wasserfall Sentonina</strong><br>2,4km Wanderweg');
  L.marker([45.0890,14.1210],{icon:ic.s}).addTo(map).bindPopup('<strong>Altstadt Labin</strong><br>Fortica, Museum');
  L.marker([45.0690,14.0570],{icon:ic.f}).addTo(map).bindPopup('<strong>Buffet Nando</strong><br>Trget Hafen');
  L.marker([45.0685,14.0575],{icon:ic.f}).addTo(map).bindPopup('<strong>Martin Pescador</strong><br>Fischrestaurant');
  L.marker([45.0895,14.1215],{icon:ic.f}).addTo(map).bindPopup('<strong>\\u2B50 Rumore Pizzeria</strong><br>Beste Pizzeria Kroatiens');
  L.marker([45.0960,14.1120],{icon:ic.sh}).addTo(map).bindPopup('<strong>STOP SHOP Labin</strong><br>16+ Gesch\\u00e4fte');
  L.marker([45.0920,14.1180],{icon:ic.sh}).addTo(map).bindPopup('<strong>Markthalle Labin</strong><br>7:00-12:30');

  var legend=L.control({position:'bottomright'});
  legend.onAdd=function(){
    var d=L.DomUtil.create('div');
    d.style.cssText='background:white;padding:10px 14px;border-radius:8px;box-shadow:0 2px 6px rgba(0,0,0,0.2);font-size:13px;line-height:1.8';
    d.innerHTML='<strong>Legende</strong><br>'+
      '<span style="display:inline-block;width:12px;height:12px;border-radius:50%;background:#C4724E;margin-right:6px;vertical-align:middle"><\\/span>Villa<br>'+
      '<span style="display:inline-block;width:12px;height:12px;border-radius:50%;background:#0891b2;margin-right:6px;vertical-align:middle"><\\/span>Str\\u00e4nde<br>'+
      '<span style="display:inline-block;width:12px;height:12px;border-radius:50%;background:#7C3AED;margin-right:6px;vertical-align:middle"><\\/span>Sehensw\\u00fcrdigkeiten<br>'+
      '<span style="display:inline-block;width:12px;height:12px;border-radius:50%;background:#DC2626;margin-right:6px;vertical-align:middle"><\\/span>Restaurants<br>'+
      '<span style="display:inline-block;width:12px;height:12px;border-radius:50%;background:#059669;margin-right:6px;vertical-align:middle"><\\/span>Einkaufen';
    return d;
  };
  legend.addTo(map);
});

// Smooth scroll
document.querySelectorAll('nav a').forEach(function(a){
  a.addEventListener('click',function(e){
    e.preventDefault();
    var t=document.querySelector(this.getAttribute('href'));
    if(t){window.scrollTo({top:t.getBoundingClientRect().top+window.pageYOffset-50,behavior:'smooth'})}
  });
});
<\/script>
</body>
</html>
""")

# Write
html = ''.join(parts)
outpath = r'C:\Users\oborg\Desktop\Urlaub 2026 - Kroatien\index.html'
with open(outpath, 'w', encoding='utf-8') as f:
    f.write(html)

print(f'Created: {outpath}')
print(f'Size: {os.path.getsize(outpath) / 1024:.0f} KB')
