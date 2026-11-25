"""Web publicada de CARDIODUARTE (diseño de la Opción 1).

Genera en la raíz del repositorio:
- index.html                      portada (la Opción 1 en modo publicación)
- <micrositio>/index.html         una página por servicio, el Chequeo Ejecutivo y el doctor
- 404.html, sitemap.xml, robots.txt
"""
from pathlib import Path

import datos
from datos import *
import datos as D
import p1
from p1 import chip, btn, PLUS, FONTS

ROOT = Path(__file__).resolve().parent.parent
HOY = "2026-11-25"

# ---------------------------------------------------------------- palabras clave
# título del servicio -> (H1, <title>, descripción, introducción, foto, posición, preparación)
KW = {
    "Consulta de cardiología": (
        "Cardiólogo en Medellín: consulta de cardiología",
        "Cardiólogo en Medellín · Consulta de cardiología en El Poblado | CARDIODUARTE",
        "Consulta con cardiólogo en Medellín (El Poblado) con el Dr. Néstor Ricardo Duarte Suárez. Valoración del corazón para dolor en el pecho, palpitaciones o presión alta. Particular, póliza y prepagada.",
        "Le atiende directamente el cardiólogo, con tiempo para escucharle, examinarle y explicarle qué tiene su corazón y qué hacer.",
        "v-consulta", "50% 78%", None),
    "Ecocardiograma transtorácico": (
        "Ecocardiograma en Medellín",
        "Ecocardiograma en Medellín · Ecocardiograma transtorácico en El Poblado | CARDIODUARTE",
        "Ecocardiograma transtorácico en Medellín, realizado e interpretado por cardiólogo ecocardiografista. Sin dolor y sin radiación. El Poblado, Torre Médica Metropolitan Salud.",
        "El ecocardiograma lo hace y lo interpreta el mismo cardiólogo ecocardiografista, y le explica el resultado.",
        "v-ecografo", "50% 55%", 0),
    "Ecocardiograma de estrés con ejercicio": (
        "Ecocardiograma de estrés con ejercicio en Medellín",
        "Ecocardiograma de estrés con ejercicio en Medellín | CARDIODUARTE",
        "Ecocardiograma de estrés con ejercicio en Medellín (El Poblado): evalúa cómo responde el corazón al esfuerzo. Realizado por cardiólogo ecocardiografista.",
        "Un ecocardiograma antes y después del ejercicio en banda, con el especialista presente durante todo el examen.",
        "sala-ecocardiografia", "30% 50%", 1),
    "Ecocardiograma de estrés farmacológico": (
        "Ecocardiograma de estrés farmacológico en Medellín",
        "Ecocardiograma de estrés farmacológico en Medellín | CARDIODUARTE",
        "Ecocardiograma de estrés farmacológico en Medellín para pacientes que no pueden hacer ejercicio. Bajo vigilancia continua del cardiólogo, en El Poblado.",
        "Para quien no puede caminar en banda: el esfuerzo se simula con un medicamento, con vigilancia continua del especialista.",
        "sala-ecocardiografia", "60% 50%", 1),
    "Electrocardiograma": (
        "Electrocardiograma en Medellín",
        "Electrocardiograma en Medellín · EKG en El Poblado | CARDIODUARTE",
        "Electrocardiograma (EKG) en Medellín, El Poblado. Registro de la actividad eléctrica del corazón en pocos minutos, interpretado por cardiólogo.",
        "Un examen rápido y sencillo, interpretado por el cardiólogo.",
        "v-cuadros", "50% 50%", 2),
    "Prueba de esfuerzo": (
        "Prueba de esfuerzo en Medellín",
        "Prueba de esfuerzo en Medellín · Ergometría en El Poblado | CARDIODUARTE",
        "Prueba de esfuerzo en Medellín (El Poblado): electrocardiograma mientras camina en banda para medir su capacidad física y la respuesta del corazón.",
        "Mide cómo responde su corazón al ejercicio, con el cardiólogo a su lado durante toda la prueba.",
        "v-esfuerzo", "50% 50%", 1),
    "Holter de ritmo (24 a 48 h)": (
        "Holter en Medellín (24 a 48 horas)",
        "Holter en Medellín · Holter de ritmo 24 a 48 horas | CARDIODUARTE",
        "Holter de ritmo cardíaco de 24 a 48 horas en Medellín (El Poblado), para estudiar palpitaciones, mareos o desmayos. Lectura por cardiólogo.",
        "Estudio del ritmo del corazón durante 24 a 48 horas, con lectura e informe del cardiólogo.",
        "v-consulta", "50% 70%", 3),
    "Monitoreo de presión arterial (MAPA)": (
        "MAPA en Medellín: monitoreo de presión arterial de 24 horas",
        "MAPA en Medellín · Monitoreo de presión arterial 24 horas | CARDIODUARTE",
        "MAPA (monitoreo ambulatorio de presión arterial de 24 horas) en Medellín, El Poblado. Diagnóstico preciso de la hipertensión, con lectura por cardiólogo.",
        "Su presión arterial medida durante 24 horas, en su rutina diaria, para un diagnóstico preciso.",
        "recepcion", "50% 30%", 4),
}
CHQ = "Chequeo Ejecutivo Cardiovascular"


def svc_by_title(t):
    return next(s for s in SERVICIOS if s[1] == t)


# ---------------------------------------------------------------- piezas comunes
def header():
    nav = "".join(f'<a href="{nav_href(h)}">{t}</a>' for h, t in NAV)
    return f"""<header class="top"><div class="wrap bar">
  <a class="brand" href="{D.R or './'}" aria-label="CARDIODUARTE, inicio"><span class="logo"><i class="mark"></i></span><b>CARDIODUARTE</b></a>
  <nav class="main" aria-label="Principal">{nav}</nav>
  <a class="btn btn-primary head-cta" href="#cita"><span>Agendar cita</span><i>{PLUS}</i></a>
  {menu_btn()}
</div>{mnav()}</header>"""


def footer():
    nav = "".join(f'<a href="{nav_href(h)}">{t}</a>' for h, t in NAV)
    svcs = "".join(f'<a href="{D.R}{SLUG[s[1]]}/">{s[1]}</a>' for s in SERVICIOS)
    return f"""<footer class="foot"><div class="wrap">
  <div class="fcols">
    <div class="fbrand"><a class="brand" href="{D.R or './'}"><span class="logo"><i class="mark"></i></span><b>CARDIODUARTE</b></a>
      <p>Cardiología y ecocardiografía. {DOCTOR}, cardiólogo ecocardiografista, en El Poblado, Medellín.</p>{linkedin_link("li-foot")}</div>
    <nav aria-label="Enlaces"><b>Enlaces</b>{nav}<a href="{D.R}{DOC_SLUG}/">{DOCTOR}</a><a href="{D.R}{SLUG[CHQ]}/">Chequeo Ejecutivo</a><a href="#cita">Agendar cita</a></nav>
    <nav aria-label="Servicios"><b>Servicios</b>{svcs}</nav>
    <div><b>Visítenos</b>{dir_link(DIR1 + ", " + DIR2 + ", Medellín")}{como_llegar()}<a href="tel:+573187984545">{TEL}</a><a href="mailto:{MAIL}">{MAIL}</a><span>{WEB}</span></div>
  </div>
  {politica_details()}
  <p class="giant" aria-hidden="true">CARDIODUARTE</p>
  <p class="legal">{LEGAL}</p>
</div></footer>"""


def crumbs(name):
    return (f'<nav class="crumbs wrap" aria-label="Ruta"><a href="{D.R}">Inicio</a><span aria-hidden="true">/</span>'
            f'<span aria-current="page">{name}</span></nav>')


def cita(sel, titulo="Pida su cita"):
    return f"""<section class="sec" id="ubicacion"><div class="wrap visit">
  <div class="info">
    {chip("Ubicación y horario")}
    <h2>{titulo}</h2>
    <ul class="ilist">
      <li><i>{ic("pin", 18)}</i><div><b>Dirección</b><span>{dir_link(DIR1 + "<br>" + DIR2)}<br>{DIR3}</span>{como_llegar()}</div></li>
      <li><i>{ic("clock", 18)}</i><div><b>Horario</b><span>Lunes a viernes, 7:00 a. m. a 5:00 p. m.</span></div></li>
      <li><i>{ic("phone", 18)}</i><div><b>WhatsApp y teléfono</b><span><a href="tel:+573187984545">{TEL}</a></span></div></li>
      <li><i>{ic("mail", 18)}</i><div><b>Correo</b><span><a href="mailto:{MAIL}">{MAIL}</a></span></div></li>
    </ul>
    {mapa()}
  </div>
  <div class="formcard" id="cita"><span class="chip">{ic("star", 12, 2)}Solicitud de cita</span><h2>Déjenos sus datos y le contactamos</h2>
    {form("btn btn-primary btn-submit", f"<i>{PLUS}</i>", sel=sel)}</div>
</div></section>"""


def pasos():
    li = "".join(
        f'<li class="scard{" scard-dark" if i == 3 else ""} reveal"><div class="vtop"><span class="num">{i + 1:02d}</span>{ic("star", 18, 1.8)}</div>'
        f'<h3>{t}</h3><p>{d}</p></li>' for i, (t, d) in enumerate(PASOS))
    return f"""<section class="sec sec-alt"><div class="wrap">
  <div class="head-row"><div>{chip("Su cita")}<h2>Cómo pedir su cita</h2>
    <p class="lead">Le acompañamos desde el primer mensaje hasta la entrega de su resultado, explicado por el especialista.</p></div>
    {btn("Escribir por WhatsApp", WA, "primary", ' target="_blank" rel="noopener"')}</div>
  <ol class="steps">{li}</ol>
</div></section>"""


def faq_sec(items):
    qa = "".join(
        f'<details class="qa"{" open" if i == 0 else ""} data-acc="faq"><summary><h3>{q}</h3><i>{PLUS}</i></summary><p>{a}</p></details>'
        for i, (q, a) in enumerate(items))
    return f"""<section class="sec" id="faq"><div class="wrap faq">
  <div class="faq-l">{chip("Preguntas frecuentes")}<h2>Preguntas frecuentes</h2>
    <div class="ask reveal"><h3>¿Tiene otra pregunta?</h3><p>Escríbanos por WhatsApp al {TEL} y le respondemos en horario de atención.</p>
    {btn("Escribir por WhatsApp", WA, "primary", ' target="_blank" rel="noopener"')}</div></div>
  <div class="faq-r">{qa}</div>
</div></section>"""


def otros(excluir):
    cards = "".join(
        f'<a class="ocard reveal" href="{D.R}{SLUG[s[1]]}/"><span class="mc-ic">{ic(s[0])}</span><span>{s[1]}</span><i>{ic("arrow", 14, 2.2)}</i></a>'
        for s in SERVICIOS if s[1] != excluir)
    if excluir != CHQ:
        cards += f'<a class="ocard reveal" href="{D.R}{SLUG[CHQ]}/"><span class="mc-ic">{ic("heartecg")}</span><span>{CHQ}</span><i>{ic("arrow", 14, 2.2)}</i></a>'
    return f"""<section class="sec sec-alt"><div class="wrap">
  <div class="head-row"><div>{chip("Servicios")}<h2>Otros servicios en CARDIODUARTE</h2></div></div>
  <div class="ogrid">{cards}</div>
</div></section>"""


def hero(chip_t, h1, lead, img, pos, sel, extra=""):
    return f"""<section class="hero" id="inicio"><div class="wrap hero-grid">
  <div class="hero-copy">
    {chip(chip_t)}
    <h1>{h1}</h1>
    <p class="lead">{lead}</p>
    <div class="ctas">{btn("Agendar una cita", "#cita", "primary", f' data-servicio="{sel}"' if sel else "")}{btn("Escribir por WhatsApp", WA, "ghost", ' target="_blank" rel="noopener"')}</div>
    {extra}
  </div>
  <figure class="hero-media">
    {pic(img, ALT[img], eager=True, pos=pos)}
    <span class="badge">{ic("shield", 16, 2)}Servicios habilitados ante MinSalud</span>
    <figcaption class="hcard"><span class="hc-ic">{ic("heartecg", 20)}</span><span><b>{DOCTOR}</b><small>Cardiólogo ecocardiografista · El Poblado, Medellín</small></span></figcaption>
  </figure>
</div></section>"""


def page(body, color="#164E78"):
    return head(1, FONTS, color) + header() + '\n<main id="contenido">\n' + body + "\n</main>\n" + footer() + "\n" + tail()


# ---------------------------------------------------------------- datos estructurados
def org():
    return {
        "@type": "MedicalClinic", "@id": f"{SITE}/#clinica", "name": "CARDIODUARTE",
        "description": "Consultorio de cardiología y ecocardiografía en El Poblado, Medellín.",
        "url": f"{SITE}/", "image": f"{SITE}/assets/img/recepcion.jpg", "logo": f"{SITE}/assets/img/logo-corazon.png",
        "telephone": "+57 318 798 4545", "email": MAIL, "medicalSpecialty": "Cardiovascular",
        "priceRange": "$$", "areaServed": {"@type": "City", "name": "Medellín"},
        "address": {"@type": "PostalAddress", "streetAddress": f"{DIR2}, {DIR1}", "addressLocality": "Medellín",
                    "addressRegion": "Antioquia", "addressCountry": "CO"},
        "hasMap": datos.MAPS.replace("&amp;", "&"),
        "geo": {"@type": "GeoCoordinates", "latitude": datos.LAT, "longitude": datos.LNG},
        "sameAs": ["https://wa.me/573187984545"],
    }


def doctor_ld():
    return {"@type": "Physician", "@id": f"{SITE}/#doctor", "name": "Néstor Ricardo Duarte Suárez",
            "medicalSpecialty": "Cardiovascular", "image": f"{SITE}/assets/img/dr-duarte.jpg",
            "url": f"{SITE}/{DOC_SLUG}/", "worksFor": {"@id": f"{SITE}/#clinica"},
            "address": org()["address"], "telephone": "+57 318 798 4545",
            **({"sameAs": [datos.LINKEDIN]} if datos.LINKEDIN else {})}


def crumbs_ld(name, path):
    return {"@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": 1, "name": "Inicio", "item": f"{SITE}/"},
        {"@type": "ListItem", "position": 2, "name": name, "item": f"{SITE}/{path}"}]}


def faq_ld(items):
    import re
    return {"@type": "FAQPage", "mainEntity": [
        {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": re.sub("<[^>]+>", "", a).strip()}}
        for q, a in items]}


# ---------------------------------------------------------------- páginas
def portada():
    datos.R = ""
    datos.META = {
        "path": "", "img": "dr-duarte",
        "title": "Cardiólogo en Medellín · Ecocardiograma, Holter y MAPA | CARDIODUARTE",
        "desc": ("CARDIODUARTE: cardiólogo ecocardiografista en El Poblado, Medellín. Consulta de cardiología, ecocardiograma, "
                 "eco estrés, prueba de esfuerzo, Holter, MAPA y Chequeo Ejecutivo Cardiovascular con el Dr. Néstor Ricardo Duarte Suárez."),
        "ld": {"@context": "https://schema.org", "@graph": [
            {"@type": "WebSite", "@id": f"{SITE}/#web", "url": f"{SITE}/", "name": "CARDIODUARTE", "inLanguage": "es-CO"},
            org(), doctor_ld(), faq_ld(FAQ)]},
    }
    return p1.page()


def micrositio(t):
    s = svc_by_title(t)
    k, _, d, u, _img = s
    h1, title, desc, intro, img, pos, prep_i = KW[t]
    slug = SLUG[t]
    datos.R = "../"
    datos.META = {
        "path": f"{slug}/", "img": img, "title": title, "desc": desc,
        "ld": {"@context": "https://schema.org", "@graph": [
            org(), doctor_ld(),
            {"@type": "MedicalProcedure" if t == "Consulta de cardiología" else "MedicalTest",
             "name": t, "description": d, "url": f"{SITE}/{slug}/",
             "relevantSpecialty": "Cardiovascular", "provider": {"@id": f"{SITE}/#clinica"}},
            crumbs_ld(t, f"{slug}/"), faq_ld(FAQ[:4])]},
    }
    prep_blocks = [PREP[prep_i]] if prep_i is not None else []
    prep_blocks.append(PREP[5])
    prep = "".join(
        f'<article class="bcard reveal"><span class="bchip">{ic(pk, 16)}Preparación</span><h3>{pt}</h3><ul class="plist">'
        + "".join(f"<li>{x}</li>" for x in li) + '</ul></article>' for pk, pt, li in prep_blocks)
    razones = "".join(
        f'<article class="vcard reveal"><div class="vtop"><span class="num">{i + 1:02d}</span>{ic("star", 18, 1.8)}</div>'
        f'<h3>{rt}</h3><p>{rd}</p></article>' for i, (rk, rt, rd) in enumerate(RAZONES[:3]))
    body = crumbs(t) + hero("Servicio · El Poblado, Medellín", h1, intro, img, pos, t) + f"""
<section class="sec"><div class="wrap split2">
  <div class="about-svc reveal">{chip("En qué consiste")}<h2>{t}</h2><p class="lead">{d}</p>
    <div class="util"><span>{ic(k, 22)}</span><p><b>Es útil si</b> {u}</p></div>
    <p class="fine-note">La indicación de cada examen la define su médico. Esta información es general y no reemplaza la valoración médica.</p></div>
  <div class="bstack">{prep}</div>
</div></section>
{pasos()}
<section class="sec"><div class="wrap">
  <div class="head-center">{chip("Por qué CARDIODUARTE")}<h2>Lo que encuentra en cada visita</h2></div>
  <div class="vgrid">{razones}</div>
</div></section>
{faq_sec(FAQ[:4])}
{cita(t)}
{otros(t)}"""
    return page(body)


def chequeo():
    slug = SLUG[CHQ]
    datos.R = "../"
    desc = ("Chequeo Ejecutivo Cardiovascular en Medellín (El Poblado): consulta de cardiología, ecocardiograma de estrés, "
            "Holter de 24 horas y MAPA en un solo programa, con resultados explicados por el cardiólogo.")
    datos.META = {
        "path": f"{slug}/", "img": "v-letrero", "title": "Chequeo Ejecutivo Cardiovascular en Medellín | CARDIODUARTE", "desc": desc,
        "ld": {"@context": "https://schema.org", "@graph": [
            org(), doctor_ld(),
            {"@type": "MedicalTest", "name": CHQ, "description": desc, "url": f"{SITE}/{slug}/",
             "relevantSpecialty": "Cardiovascular", "provider": {"@id": f"{SITE}/#clinica"}},
            crumbs_ld(CHQ, f"{slug}/")]},
    }
    cards = "".join(
        f'<article class="gcard reveal"><div class="vtop"><span class="num">{i + 1:02d}</span>{ic("star", 18, 1.8)}</div>'
        f'<h3>{t}</h3><p>{d}</p></article>' for i, (t, d) in enumerate(CHEQUEO))
    body = crumbs(CHQ) + hero(
        "Para pacientes particulares", "Chequeo Ejecutivo Cardiovascular en Medellín",
        "Una evaluación completa de su corazón en un solo programa, con los exámenes que su caso necesita y los resultados explicados por el especialista.",
        "v-letrero", "50% 72%", CHQ) + f"""
<section class="sec"><div class="wrap">
  <div class="head-row"><div>{chip("Qué incluye")}<h2>Cuatro estudios, un solo especialista</h2>
    <p class="lead">El mismo cardiólogo hace los exámenes, los interpreta y le explica el resultado en una sola conversación.</p></div></div>
  <div class="ggrid ggrid-4">{cards}</div>
  <div class="center">{btn("Solicitar el chequeo", "#cita", "primary", f' data-servicio="{CHQ}"')}</div>
</div></section>
{pasos()}
{faq_sec(FAQ[:4])}
{cita(CHQ, "Agende su chequeo")}
{otros(CHQ)}"""
    return page(body)


def doctor():
    datos.R = "../"
    desc = ("Dr. Néstor Ricardo Duarte Suárez, cardiólogo ecocardiografista en Medellín con más de 15 años de trayectoria. "
            "Consulta de cardiología y ecocardiografía en El Poblado.")
    datos.META = {
        "path": f"{DOC_SLUG}/", "img": "dr-duarte",
        "title": "Dr. Néstor Ricardo Duarte Suárez · Cardiólogo ecocardiografista en Medellín | CARDIODUARTE", "desc": desc,
        "ld": {"@context": "https://schema.org", "@graph": [org(), doctor_ld(), crumbs_ld(DOCTOR, f"{DOC_SLUG}/")]},
    }
    cred = "".join(f'<div><dt>{a}</dt><dd>{b}</dd></div>' for a, b in CRED if a not in ("Formación", "Registro médico"))
    hab = "".join(
        f'<figure class="dist reveal">{pic(img, "Distintivo de habilitación " + c)}<figcaption><small>{g}</small><b>{t}</b><span>{c}</span></figcaption></figure>'
        for g, t, c, img in HAB)
    svcs = "".join(
        f'<a class="ocard reveal" href="../{SLUG[s[1]]}/"><span class="mc-ic">{ic(s[0])}</span><span>{s[1]}</span><i>{ic("arrow", 14, 2.2)}</i></a>'
        for s in SERVICIOS)
    body = crumbs(DOCTOR) + hero(
        "El doctor", f"{DOCTOR}, cardiólogo en Medellín", BIO, "dr-duarte", "50% 20%", None) + f"""
<section class="sec"><div class="wrap team">
  <article class="tm reveal">{pic("v-consulta", ALT["v-consulta"], pos="50% 80%")}<div class="tm-b"><span class="bchip">Cardiología</span><h2 class="h3">{DOCTOR}</h2><p>Cardiólogo ecocardiografista</p>{linkedin_link()}</div></article>
  <dl class="cred reveal">{cred}</dl>
</div></section>
<section class="wrap" id="habilitacion"><div class="panel panel-stats">
  <div class="ps-l">{chip("Habilitación", True)}<h2>Servicios habilitados ante el Ministerio de Salud</h2>
    <p>Prestador 0500127007 · {DOCTOR}. Puede verificar cada distintivo en el portal de MinSalud.</p>
    {btn("Verificar en MinSalud", MINSALUD, "lime", ' target="_blank" rel="noopener"')}</div>
  <div class="ps-r">{hab}</div>
</div></section>
<section class="sec"><div class="wrap">
  <div class="head-row"><div>{chip("Servicios")}<h2>Lo que hace el doctor por su corazón</h2></div></div>
  <div class="ogrid">{svcs}</div>
</div></section>
{cita(None, "Pida su cita con el doctor")}"""
    return page(body)


def pagina_404():
    datos.R = "/" if datos.INDEXABLE else "/cardioduarte-web/"
    datos.META = {"path": "404.html", "title": "Página no encontrada | CARDIODUARTE",
                  "desc": "La página que busca no existe. Vuelva al inicio de CARDIODUARTE.", "ld": {}}
    html = page(f"""<section class="sec"><div class="wrap head-center nf">{chip("Error 404")}<h1>No encontramos esta página</h1>
  <p class="lead">Puede volver al inicio o escribirnos por WhatsApp y le ayudamos con su cita.</p>
  <div class="ctas">{btn("Volver al inicio", datos.R, "primary")}{btn("Escribir por WhatsApp", WA, "ghost", ' target="_blank" rel="noopener"')}</div></div></section>""")
    return html.replace('content="index, follow, max-image-preview:large"', 'content="noindex"')


def limpiar_datos():
    """En la web publicada no se muestran las marcas de validación de las listas de datos."""
    import re
    quitar = lambda x: re.sub(r'\s*<span class="tag">[^<]*</span>', "", x)
    faq = [(q, quitar(a)) for q, a in datos.FAQ]
    cred = [(a, quitar(b)) for a, b in datos.CRED]
    for mod in (datos, p1, globals()):
        tgt = mod if isinstance(mod, dict) else vars(mod)
        tgt["FAQ"], tgt["CRED"] = faq, cred


HTACCESS = """# CARDIODUARTE · www.cardioduarte.com (Hostinger)
Options -Indexes
DirectoryIndex index.html
ErrorDocument 404 /404.html

<IfModule mod_rewrite.c>
RewriteEngine On
# Siempre https y siempre con www
RewriteCond %{HTTPS} off [OR]
RewriteCond %{HTTP_HOST} !^www\\. [NC]
RewriteRule ^ https://www.cardioduarte.com%{REQUEST_URI} [L,R=301]
</IfModule>

<IfModule mod_headers.c>
Header always set X-Content-Type-Options "nosniff"
Header always set Referrer-Policy "strict-origin-when-cross-origin"
</IfModule>

<IfModule mod_expires.c>
ExpiresActive On
ExpiresByType text/html "access plus 0 seconds"
ExpiresByType text/css "access plus 1 month"
ExpiresByType application/javascript "access plus 1 month"
ExpiresByType image/webp "access plus 6 months"
ExpiresByType image/jpeg "access plus 6 months"
ExpiresByType image/png "access plus 6 months"
</IfModule>

<IfModule mod_deflate.c>
AddOutputFilterByType DEFLATE text/html text/css application/javascript application/json image/svg+xml text/xml application/xml
</IfModule>
"""


def generar(destino):
    """destino "github": copia de muestra en la raíz del repo (noindex).
    destino "hostinger": web oficial indexable en dist/hostinger/, lista para subir a public_html."""
    import re
    import shutil
    oficial = destino == "hostinger"
    base = ROOT / "dist" / "hostinger" if oficial else ROOT
    if oficial and base.exists():
        shutil.rmtree(base)
    datos.PROD = True
    datos.INDEXABLE = oficial
    limpiar_datos()
    out = {"index.html": portada()}
    for t in KW:
        out[f"{SLUG[t]}/index.html"] = micrositio(t)
    out[f"{SLUG[CHQ]}/index.html"] = chequeo()
    out[f"{DOC_SLUG}/index.html"] = doctor()
    out["404.html"] = pagina_404()
    for rel, html in out.items():
        f = base / rel
        f.parent.mkdir(parents=True, exist_ok=True)
        f.write_text(html, encoding="utf-8")
    print(f"ok {destino}: {len(out)} páginas")
    if oficial:
        urls = [""] + [p[:-len("index.html")] for p in out if p.endswith("/index.html")]
        sm = "".join(f"<url><loc>{SITE}/{u}</loc><lastmod>{HOY}</lastmod><priority>{'1.0' if not u else '0.8'}</priority></url>\n" for u in urls)
        (base / "sitemap.xml").write_text(
            f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n{sm}</urlset>\n', encoding="utf-8")
        (base / "robots.txt").write_text(f"User-agent: *\nAllow: /\n\nSitemap: {SITE}/sitemap.xml\n", encoding="utf-8")
        (base / ".htaccess").write_text(HTACCESS, encoding="utf-8")
        # solo los recursos que usa la web oficial
        usados = set()
        for html in out.values():
            usados |= set(re.findall(r'assets/img/([\w.-]+)', html))
        for c in ("comun.css", "opcion-1.css"):
            usados |= set(re.findall(r"img/([\w.-]+)", (ROOT / "assets/css" / c).read_text()))
        for rel in ["assets/css/comun.css", "assets/css/opcion-1.css", "assets/js/sitio.js"] + [f"assets/img/{n}" for n in sorted(usados)]:
            (base / rel).parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(ROOT / rel, base / rel)
    datos.PROD = False
    datos.INDEXABLE = True
    datos.R = "../"


def main():
    generar("github")
    generar("hostinger")
