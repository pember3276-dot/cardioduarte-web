"""Opción 1 · Clínica moderna y profesional (estructura inspirada en la referencia Clinqora)."""
from datos import *

FONTS = "family=Geist:wght@400;500;600&family=Inter:wght@400;500;600"
PLUS = ic("plus", 16, 2.2)


def chip(t, light=False):
    return f'<span class="chip{" chip-l" if light else ""}">{ic("star", 12, 2)}{t}</span>'


def btn(t, href="#cita", kind="primary", extra=""):
    return f'<a class="btn btn-{kind}" href="{href}"{extra}><span>{t}</span><i>{PLUS}</i></a>'


def page():
    nav = "".join(f'<a href="{h}">{t}</a>' for h, t in NAV)
    big = SERVICIOS[:2]
    small = [SERVICIOS[2], SERVICIOS[5], SERVICIOS[4]]
    rest = [SERVICIOS[3], SERVICIOS[6], SERVICIOS[7]]

    POS = {"v-consulta": "50% 78%", "v-ecografo": "50% 60%", "v-esfuerzo": "50% 55%", "v-cuadros": "50% 50%"}

    def photo_card(s, cls):
        k, t, d, u, img = s
        return (f'<article class="pcard {cls} reveal">{pic(img, ALT[img], pos=POS.get(img))}<div class="glass">'
                f'<div><h3>{t}</h3><p>{d}</p></div><a class="pc-plus" href="#cita" data-servicio="{t}" aria-label="Agendar {t}">{PLUS}</a></div></article>')

    def mini_card(s):
        k, t, d, u, img = s
        return (f'<article class="mcard reveal"><div class="mc-ic">{ic(k)}</div><div><h3>{t}</h3><p>{d}</p>'
                f'<p class="u"><b>Útil si:</b> {u}</p></div></article>')

    razones = "".join(
        f'<article class="vcard reveal"><div class="vtop"><span class="num">{i + 1:02d}</span>{ic("star", 18, 1.8)}</div>'
        f'<h3>{t}</h3><p>{d}</p></article>' for i, (k, t, d) in enumerate(RAZONES))
    prev = "".join(
        f'<article class="tcard{" tcard-hi" if i == 1 else ""} reveal"><span class="q">{ic(k, 20)}</span>'
        f'<h3>{t}</h3><p>{d}</p></article>' for i, (k, t, d) in enumerate(PREVENCION))
    chequeo = "".join(
        f'<article class="gcard reveal"><div class="vtop"><span class="num">{i + 1:02d}</span>{ic("star", 18, 1.8)}</div>'
        f'<h3>{t}</h3><p>{d}</p></article>' for i, (t, d) in enumerate(CHEQUEO))
    pasos = "".join(
        f'<li class="scard{" scard-dark" if i == 3 else ""} reveal"><div class="vtop"><span class="num">{i + 1:02d}</span>{ic("star", 18, 1.8)}</div>'
        f'<h3>{t}</h3><p>{d}</p></li>' for i, (t, d) in enumerate(PASOS))
    prep = "".join(
        f'<article class="bcard reveal"><span class="bchip">{ic(k, 16)}Preparación</span><h3>{t}</h3>'
        f'<details><summary>Ver indicaciones <i>{PLUS}</i></summary><ul>' + "".join(f"<li>{x}</li>" for x in li) +
        '</ul></details></article>' for k, t, li in PREP)
    faq = "".join(
        f'<details class="qa"{" open" if i == 0 else ""} data-acc="faq"><summary><h3>{q}</h3><i>{PLUS}</i></summary><p>{a}</p></details>'
        for i, (q, a) in enumerate(FAQ))
    cred = "".join(f'<div><dt>{a}</dt><dd>{b}</dd></div>' for a, b in CRED)
    hab = "".join(
        f'<figure class="dist reveal">{pic(img, "Distintivo de habilitación " + c)}<figcaption><small>{g}</small><b>{t}</b><span>{c}</span></figcaption></figure>'
        for g, t, c, img in HAB)

    return head(1, FONTS, "#164E78") + f"""
<header class="top"><div class="wrap bar">
  <a class="brand" href="#inicio" aria-label="CARDIODUARTE, inicio"><span class="logo"><i class="mark"></i></span><b>CARDIODUARTE</b></a>
  <nav class="main" aria-label="Principal">{nav}</nav>
  <a class="btn btn-primary head-cta" href="#cita"><span>Agendar cita</span><i>{PLUS}</i></a>
  {menu_btn()}
</div>{mnav()}</header>

<main id="contenido">
<section class="hero" id="inicio"><div class="wrap hero-grid">
  <div class="hero-copy">
    {chip("Atención directa del especialista")}
    <h1>{H1}</h1>
    <p class="lead">{LEAD}</p>
    <div class="ctas">{btn("Agendar una cita")}{btn("Ver servicios", "#servicios", "ghost")}</div>
    <div class="avatars"><span class="stack">{pic("v-consulta", "", "av")}{pic("v-ecografo", "", "av")}{pic("v-esfuerzo", "", "av")}{pic("v-letrero", "", "av")}</span>
      <p>Consulta, ecocardiografía y pruebas del corazón en un solo lugar.</p></div>
  </div>
  <figure class="hero-media">
    {pic("dr-duarte", ALT["dr-duarte"], eager=True, pos="50% 20%")}
    <span class="badge">{ic("shield", 16, 2)}Servicios habilitados ante MinSalud</span>
    <figcaption class="hcard"><span class="hc-ic">{ic("heartecg", 20)}</span><span><b>{DOCTOR}</b><small>Cardiólogo ecocardiografista · El Poblado, Medellín</small></span></figcaption>
  </figure>
</div>
<div class="wrap stats">
  <div class="stat reveal"><p class="n" data-count="15" data-suffix="+">15+</p><h3>Años de trayectoria</h3><p>En diagnóstico y tratamiento del corazón</p></div>
  <div class="stat reveal"><p class="n" data-count="8">8</p><h3>Servicios y exámenes</h3><p>Consulta, ecocardiografía, pruebas y monitoreo</p></div>
  <div class="stat reveal"><p class="n" data-count="2">2</p><h3>Servicios habilitados</h3><p>Cardiología e imágenes no ionizantes</p></div>
</div></section>

<section class="sec" id="doctor"><div class="wrap split">
  <figure class="split-media reveal">{pic("sala-ecocardiografia", ALT["sala-ecocardiografia"], pos="30% 50%")}
    <figcaption class="lime"><b>15+</b><span>Años cuidando corazones en Medellín</span></figcaption></figure>
  <div class="split-copy">
    {chip("El doctor")}
    <h2>{DOCTOR}</h2>
    <p class="lead">{BIO}</p>
    <ul class="checks">
      <li><i>{ic("check", 14, 2.4)}</i>Le atiende directamente el especialista</li>
      <li><i>{ic("check", 14, 2.4)}</i>El mismo médico examina, interpreta y explica</li>
      <li><i>{ic("check", 14, 2.4)}</i>Resultados que usted pueda entender</li>
      <li><i>{ic("check", 14, 2.4)}</i>Particulares, pólizas y medicina prepagada</li>
    </ul>
    <blockquote>“{QUOTE}” {tag()}</blockquote>
  </div>
</div></section>

<section class="sec" id="como"><div class="wrap">
  <div class="head-row">
    <div>{chip("Su cita")}<h2>Agendar una cita es sencillo</h2>
    <p class="lead">Le acompañamos desde el primer mensaje hasta la entrega de su resultado, explicado por el especialista.</p></div>
    {btn("Escribir por WhatsApp", WA, "primary", ' target="_blank" rel="noopener"')}
  </div>
  <ol class="steps">{pasos}</ol>
</div></section>

<section class="sec sec-alt" id="servicios"><div class="wrap">
  <div class="head-split">
    <div>{chip("Servicios")}<h2>Consulta y exámenes del corazón en un solo lugar</h2></div>
    <p class="lead">El médico que le examina es el mismo que interpreta su estudio y le explica el resultado.</p>
  </div>
  <div class="pgrid">{photo_card(big[0], "pc-big")}{photo_card(big[1], "pc-big")}{"".join(photo_card(s, "pc-sm") for s in small)}</div>
  <div class="mgrid">{"".join(mini_card(s) for s in rest)}</div>
  <div class="center">{btn("Pedir orientación", "#cita", "ghost", ' data-servicio="No estoy seguro, necesito orientación"')}</div>
</div></section>

<section class="sec" id="por-que"><div class="wrap">
  <div class="head-center">{chip("Por qué CARDIODUARTE")}<h2>Lo que encuentra en cada visita</h2></div>
  <div class="vgrid">{razones}</div>
</div></section>

<section class="wrap" id="prevencion"><div class="panel">
  <div class="head-center">{chip("Prevención", True)}<h2>Pequeños hábitos que cuidan su corazón</h2>
    <p class="lead">Recomendaciones generales de salud cardiovascular. No reemplazan la valoración médica ni las indicaciones de su médico tratante.</p>
    <span class="pill-note">{ic("alert", 16, 2)}Ejemplo · validar con el Dr. Duarte</span></div>
  <div class="tgrid">{prev}</div>
  <div class="alarm reveal"><span>{ic("alert", 22, 2)}</span><div><h3>Señales de alarma: no espere una cita</h3><p>{ALARMA}</p></div></div>
</div></section>

<section class="sec" id="chequeo"><div class="wrap">
  <div class="diff">
    <div class="diff-l">
      {chip("Para pacientes particulares")}
      <h2>Chequeo Ejecutivo Cardiovascular</h2>
      <p class="lead">Una evaluación completa de su corazón en un solo programa, con los exámenes que su caso necesita y los resultados explicados por el especialista.</p>
      <figure class="diff-media reveal">{pic("v-letrero", ALT["v-letrero"], pos="50% 72%")}</figure>
    </div>
    <div class="ggrid">{chequeo}
      <div class="gcta">{btn("Solicitar el chequeo", "#cita", "primary", ' data-servicio="Chequeo Ejecutivo Cardiovascular"')}</div></div>
  </div>
</div></section>

<section class="sec sec-alt"><div class="wrap">
  <div class="head-row">
    <div>{chip("Su especialista")}<h2>Formación y experiencia</h2>
    <p class="lead">Conozca quién le atiende. Los datos marcados se completan con el consultorio.</p></div>
  </div>
  <div class="team">
    <article class="tm reveal">{pic("v-consulta", ALT["v-consulta"], pos="50% 80%")}<div class="tm-b"><span class="bchip">Cardiología</span><h3>{DOCTOR}</h3><p>Cardiólogo ecocardiografista</p></div></article>
    <dl class="cred reveal">{cred}</dl>
  </div>
</div></section>

<section class="wrap" id="habilitacion"><div class="panel panel-stats">
  <div class="ps-l">{chip("Habilitación", True)}<h2>Servicios habilitados ante el Ministerio de Salud</h2>
    <p>Prestador 0500127007 · {DOCTOR}. Puede verificar cada distintivo en el portal de MinSalud.</p>
    {btn("Verificar en MinSalud", MINSALUD, "lime", ' target="_blank" rel="noopener"')}</div>
  <div class="ps-r">{hab}</div>
</div></section>

<section class="sec" id="preparacion"><div class="wrap">
  <div class="head-row">
    <div>{chip("Preparación")}<h2>Cómo prepararse para su examen</h2>
    <p class="lead">Indicaciones generales. Siga siempre lo que le indique el consultorio al confirmar su cita. No suspenda medicamentos sin orden médica. {tag("Ejemplo · validar con el Dr. Duarte")}</p></div>
  </div>
  <div class="bgrid">{prep}</div>
</div></section>

<section class="sec sec-alt" id="faq"><div class="wrap faq">
  <div class="faq-l">{chip("Preguntas frecuentes")}<h2>Preguntas frecuentes</h2>
    <p class="lead">Respuestas rápidas sobre citas, coberturas y cómo llegar.</p>
    <div class="ask reveal"><h3>¿Tiene otra pregunta?</h3><p>Escríbanos por WhatsApp al {TEL} y le respondemos en horario de atención.</p>
    {btn("Escribir por WhatsApp", WA, "primary", ' target="_blank" rel="noopener"')}</div></div>
  <div class="faq-r">{faq}</div>
</div></section>

<section class="sec" id="ubicacion"><div class="wrap visit">
  <div class="info">
    {chip("Ubicación y horario")}
    <h2>Le esperamos en El Poblado</h2>
    <ul class="ilist">
      <li><i>{ic("pin", 18)}</i><div><b>Dirección</b><span>{DIR1}<br>{DIR2}<br>{DIR3}</span></div></li>
      <li><i>{ic("clock", 18)}</i><div><b>Horario</b><span>Lunes a viernes, 7:00 a. m. a 5:00 p. m. {tag("Validar")}</span></div></li>
      <li><i>{ic("phone", 18)}</i><div><b>WhatsApp y teléfono</b><span><a href="tel:+573187984545">{TEL}</a></span></div></li>
      <li><i>{ic("mail", 18)}</i><div><b>Correo</b><span><a href="mailto:{MAIL}">{MAIL}</a> · {WEB}</span></div></li>
    </ul>
    <figure class="torre reveal">{pic("v-torre", ALT["v-torre"], pos="50% 45%")}<a class="btn btn-white" href="{MAPS}" target="_blank" rel="noopener"><span>Abrir en Google Maps</span><i>{ic("arrow", 14, 2.2)}</i></a></figure>
  </div>
  <div class="formcard" id="cita"><span class="chip">{ic("star", 12, 2)}Solicitud de cita</span><h2>Déjenos sus datos y le contactamos</h2>
    {form("btn btn-primary btn-submit", f"<i>{PLUS}</i>")}</div>
</div></section>

<section class="wrap"><div class="cta reveal">
  <div class="cta-l">{chip("Su próximo paso", True)}<h2>Haga de su corazón una prioridad</h2>
    <p>Ya sea un chequeo o un examen puntual, le ayudamos a planear su cita.</p>
    <div class="ctas">{btn("Agendar una cita", "#cita", "lime")}{btn("Escribir por WhatsApp", WA, "white", ' target="_blank" rel="noopener"')}</div></div>
  <figure class="cta-media">{pic("recepcion", ALT["recepcion"], pos="50% 30%")}</figure>
</div></section>
</main>

<footer class="foot"><div class="wrap">
  <div class="fcols">
    <div class="fbrand"><a class="brand" href="#inicio"><span class="logo"><i class="mark"></i></span><b>CARDIODUARTE</b></a>
      <p>Cardiología y ecocardiografía. {DOCTOR}, cardiólogo ecocardiografista, en El Poblado, Medellín.</p></div>
    <nav aria-label="Enlaces"><b>Enlaces</b>{nav}<a href="#cita">Agendar cita</a></nav>
    <nav aria-label="Servicios"><b>Servicios</b>{"".join(f'<a href="#servicios">{s[1]}</a>' for s in SERVICIOS[:5])}</nav>
    <div><b>Visítenos</b><span>{DIR1}, {DIR2}, Medellín</span><a href="tel:+573187984545">{TEL}</a><a href="mailto:{MAIL}">{MAIL}</a><span>{WEB}</span></div>
  </div>
  {politica_details()}
  <p class="giant" aria-hidden="true">CARDIODUARTE</p>
  <p class="legal">{LEGAL}</p>
</div></footer>
""" + tail()
