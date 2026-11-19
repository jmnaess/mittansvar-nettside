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
"""
def page(title, body, desc):
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
<div class="wrap">
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

index = """<h1>Oppgaver, ukepenger og vedlikehold – for hele familien</h1>
<p class="lead">MittAnsvar hjelper familier å fordele oppgaver hjemme, gi barna lønn for jobben de gjør, og huske vedlikeholdet av boligen gjennom året.</p>
<ul class="features">
<li><b>Dagens oppgaver for alle</b>Hver person ser sitt, og barna krysser av selv. Voksne godkjenner det som gir lønn.</li>
<li><b>Lønn for barna</b>Beløp per oppgave og en saldo barnet selv kan følge med på.</li>
<li><b>Årshjul for boligen</b>Forslag til vedlikehold ut fra hvordan dere bor, fra røykvarslere til takrenner.</li>
<li><b>Familieskjerm</b>Et nettbrett på kjøkkenet kan vise dagen for hele familien.</li>
</ul>
<div class="card"><b>Kommer snart</b><br>Appen er under testing og kommer til iPhone og iPad. Vil du vite mer, skriv til <a href="mailto:hei@mittansvar.app">hei@mittansvar.app</a>.</div>
"""
(out/"index.html").write_text(page("MittAnsvar – oppgaver, ukepenger og vedlikehold for familien", index, "Oppgaver, ukepenger og vedlikehold for hele familien."))

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
