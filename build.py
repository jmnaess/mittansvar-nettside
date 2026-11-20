import markdown, pathlib, sys
src = pathlib.Path(sys.argv[1]); out = pathlib.Path(sys.argv[2]); out.mkdir(exist_ok=True)
CSS = """
:root{--bg:#FFFDF7;--surface:#FFFFFF;--text:#2B2118;--muted:#6B5E52;--border:#F1EBE1;--primary:#0E6E6E;--tint:#E3F3F1}
@media (prefers-color-scheme:dark){:root{--bg:#1C1712;--surface:#28211A;--text:#F4EDE3;--muted:#B8AB9C;--border:#3A3128;--primary:#7CC4BD;--tint:#173230}}
*{box-sizing:border-box}
body{margin:0;background:var(--bg);color:var(--text);font:17px/1.6 -apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,"Helvetica Neue",Arial,sans-serif}
.wrap{max-width:720px;margin:0 auto;padding:24px 20px 48px}
header{display:flex;align-items:center;gap:12px;padding:8px 0 24px}
header a.brand{display:flex;align-items:center;gap:10px;color:var(--text);text-decoration:none;font-weight:800;font-size:20px}
header img{width:40px;height:40px;border-radius:10px}
nav{margin-left:auto;display:flex;gap:16px;font-size:15px}
a{color:var(--primary)}
h1{font-size:34px;line-height:1.2;margin:8px 0 12px}
h2{font-size:22px;margin:36px 0 8px}
.lead{font-size:20px;color:var(--muted)}
.card{background:var(--surface);border:1px solid var(--border);border-radius:16px;padding:20px;margin:20px 0}
table{width:100%;border-collapse:collapse;font-size:15px;margin:12px 0;display:block;overflow-x:auto}
th,td{text-align:left;vertical-align:top;padding:8px 10px;border-bottom:1px solid var(--border)}
th{color:var(--muted);font-weight:700}
.meta{color:var(--muted);font-size:15px}
footer{margin-top:48px;padding-top:16px;border-top:1px solid var(--border);color:var(--muted);font-size:14px}
ul.features{padding-left:0;list-style:none}
ul.features li{background:var(--surface);border:1px solid var(--border);border-radius:14px;padding:14px 16px;margin:10px 0}
ul.features b{display:block}

.hero{background:#FFF4D1;border-radius:28px;padding:36px 24px 0;margin:0 -4px;overflow:hidden;position:relative}
@media (prefers-color-scheme:dark){.hero{background:#2A231B}}
.hero-grid{display:grid;grid-template-columns:1fr;gap:28px;align-items:end}
@media (min-width:760px){.hero-grid{grid-template-columns:1.1fr 1fr}.wrap.wide{max-width:980px}.hero{padding:56px 48px 0}}
.fox{width:84px;height:84px;border-radius:22px;overflow:hidden;box-shadow:0 6px 18px rgba(43,33,24,.15)}
.hero h1{font-family:ui-rounded,"SF Pro Rounded",system-ui,sans-serif;font-size:44px;line-height:1.05;margin:20px 0 12px;letter-spacing:-.5px}
.hero h1 em{font-style:normal;color:var(--primary)}
.hero p{font-size:19px;color:var(--muted);margin:0 0 20px;max-width:30ch}
.badge{display:inline-block;background:var(--text);color:var(--bg);border-radius:999px;padding:10px 18px;font-weight:700;font-size:15px;margin-bottom:36px}
.phone{justify-self:center;width:280px;background:#1C1712;border-radius:40px 40px 0 0;padding:12px 12px 0;box-shadow:0 20px 50px rgba(43,33,24,.25)}
.screen{line-height:1.3;background:#FFFDF7;border-radius:30px 30px 0 0;padding:20px 14px 18px;color:#2B2118;height:330px;overflow:hidden}
.screen h3{font-family:ui-rounded,system-ui,sans-serif;margin:0 0 12px;font-size:22px}
.pcard{background:#fff;border-radius:16px;box-shadow:0 1px 4px rgba(43,33,24,.08);padding:10px 12px;margin-bottom:10px}
.phead{display:flex;align-items:center;gap:8px;font-weight:800;font-size:15px;margin-bottom:6px}
.av{width:26px;height:26px;border-radius:13px;display:inline-flex;align-items:center;justify-content:center;font-size:12px;font-weight:800;border:2px solid}
.tally{margin-left:auto;font-size:12px;color:#6B5E52;font-weight:700}
.trow{display:flex;align-items:center;gap:8px;font-size:14px;padding:5px 0}
.tick{width:20px;height:20px;border-radius:10px;border:2px solid #CFC5B6;flex:none}
.tick.on{background:#0E6E6E;border-color:#0E6E6E;position:relative}
.tick.on:after{content:"";position:absolute;left:5px;top:2px;width:5px;height:9px;border:solid #fff;border-width:0 2px 2px 0;transform:rotate(45deg)}
.done{text-decoration:line-through;color:#9A8E80}
.kr{white-space:nowrap;margin-left:auto;background:#FFF1C2;color:#6E4D00;font-size:11px;font-weight:800;padding:2px 7px;border-radius:9px}
.tiles{display:grid;grid-template-columns:1fr;gap:12px;margin:28px 0}
@media (min-width:760px){.tiles{grid-template-columns:repeat(3,1fr)}}
.tile{background:var(--surface);border:1px solid var(--border);border-radius:20px;padding:20px}
.tile .ic{width:44px;height:44px;border-radius:12px;background:var(--tint);color:var(--primary);display:flex;align-items:center;justify-content:center;margin-bottom:12px}
.tile b{display:block;font-size:18px;margin-bottom:4px}
.tile span{color:var(--muted);font-size:15px}
"""
def page(title, body, desc, wide=False):
    return f"""<!doctype html>
<html lang="nb">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="icon" href="icon.png">
<style>{CSS}</style>
</head>
<body>
<div class="wrap{' wide' if wide else ''}">
<header><a class="brand" href="./"><img src="icon.png" alt="">MittAnsvar</a>
<nav><a href="personvern.html">Personvern</a><a href="support.html">Support</a></nav></header>
<main>
{body}
</main>
<footer>MittAnsvar er laget av John Martin Næss, som en privat app. Den er ikke tilknyttet noen offentlig etat.<br>
<a href="mailto:hei@mittansvar.app">hei@mittansvar.app</a> · <a href="personvern.html">Personvern</a> · <a href="support.html">Support</a></footer>
</div>
</body>
</html>
"""
md = (src/"personvern.md").read_text()
body = markdown.markdown(md, extensions=["tables","toc"])
body = body.replace("<p>Sist oppdatert:", '<p class="meta">Sist oppdatert:',1)
(out/"personvern.html").write_text(page("Personvern – MittAnsvar", body, "Hvordan MittAnsvar behandler opplysninger om familien din."))

# Forsiden (index.html) redigeres direkte som egen fil – den bygges ikke her.

support = """<h1>Support</h1>
<p class="lead">Trenger du hjelp, har du funnet en feil, eller har du et forslag? Skriv til <a href="mailto:hei@mittansvar.app">hei@mittansvar.app</a>. Vi svarer så fort vi kan, vanligvis innen et par dager.</p>
<h2>Vanlige spørsmål</h2>
<div class="card"><b>Hvordan sletter jeg kontoen min?</b><br>Åpne appen og gå til <i>Innstillinger</i> → <i>Slett konto</i>. Er du den siste voksne i husstanden, slettes hele husstanden. Les mer i <a href="personvern.html#hvor-lenge-vi-lagrer-og-sletting">personvernerklæringen</a>.</div>
<div class="card"><b>Hvordan kommer barna inn i appen?</b><br>Barna trenger ikke e-post. En voksen legger inn barnet og kobler barnets enhet med en QR-kode eller en kode på 8 tegn.</div>
<div class="card"><b>Fikk du ikke innloggingskoden?</b><br>Sjekk søppelposten. Koden kommer fra noreply@mittansvar.app.</div>
<div class="card"><b>Personvern</b><br>Spørsmål om personvern sender du til <a href="mailto:personvern@mittansvar.app">personvern@mittansvar.app</a>.</div>
"""
(out/"support.html").write_text(page("Support – MittAnsvar", support, "Hjelp og kontakt for MittAnsvar."))
(out/"CNAME").write_text("mittansvar.app\n")
(out/".nojekyll").write_text("")
