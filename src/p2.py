"""Opción 2 · Elegante y premium (estructura inspirada en la referencia Hospic)."""
from datos import *

FONTS = "family=Geist:wght@400;500;600;700&family=Plus+Jakarta+Sans:wght@400;500;600;700"
ARROW = ic("arrow", 16, 2.2)
UP = '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M7 17 17 7M8 7h9v9"/></svg>'
PM = f'<i class="pm">{ic("plus", 16, 2.4)}{ic("minus", 16, 2.4)}</i>'
ECG_BG = ('<svg class="ecg-bg" viewBox="0 0 1200 200" preserveAspectRatio="none" aria-hidden="true"><path d="M0 120h300l30-60 40 120 40-150 40 140 30-50h200l30-40 30 80 30-110 30 100 20-20h330" '
          'fill="none" stroke="currentColor" stroke-width="2"/></svg>')


def chip(t, icon="heart", light=False):
    return f'<span class="chip{" chip-l" if light else ""}">{ic(icon, 14, 2)}{t}</span>'


def btn(t, href="#cita", kind="primary", extra=""):
    return f'<a class="btn btn-{kind}" href="{href}"{extra}><span>{t}</span><i>{ARROW}</i></a>'


def page():
    nav_items = [n for n in NAV if n[0] != "#servicios"]
    dd = "".join(f'<a href="#servicios" data-servicio="{t}">{ic(k, 18)}<span>{t}</span></a>' for k, t, *_ in SERVICIOS)
    nav = (f'<a href="#doctor">El doctor</a><div class="dd"><a href="#servicios" class="dd-t">Servicios '
           f'<svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" aria-hidden="true"><path d="m6 9 6 6 6-6"/></svg></a>'
           f'<div class="dd-p"><p>Consulta y exámenes del corazón</p><div class="dd-g">{dd}</div></div></div>'
           + "".join(f'<a href="{h}">{t}</a>' for h, t in nav_items[1:]))

    POS = {"v-consulta": "50% 75%", "v-ecografo": "50% 55%", "v-esfuerzo": "50% 50%", "v-cuadros": "50% 50%",
           "sala-ecocardiografia": "30% 50%"}

    def scard(i, s):
        k, t, d, u, img = s
        media = (f'<div class="sc-m">{pic(img, ALT[img], pos=POS.get(img))}</div>' if img
                 else f'<div class="sc-m sc-ic">{ic(k, 64, 1.2)}</div>')
        return (f'<article class="scard reveal" style="--i:{i}"><div class="sc-b"><span class="sc-icon">{ic(k, 22)}</span>'
                f'<h3>{t}</h3><p>{d}</p><p class="u"><b>Útil si:</b> {u}</p>'
                f'<a class="link" href="#cita" data-servicio="{t}">Solicitar este servicio {UP}</a></div>{media}</article>')

    servicios = "".join(scard(i, s) for i, s in enumerate(SERVICIOS))
    razones = "".join(
        f'<article class="wcard reveal"><div><h3>{t}</h3><p>{d}</p></div><span class="wc-ic">{ic(k, 26)}</span></article>'
        for k, t, d in RAZONES)
    prev = "".join(
        f'<article class="pv reveal"><span class="pv-ic">{ic(k, 22)}</span><h3>{t}</h3><p>{d}</p></article>'
        for k, t, d in PREVENCION)
    chequeo = "".join(f'<li><i>{ic("check", 14, 2.6)}</i><span><b>{t}</b> {d}</span></li>' for t, d in CHEQUEO)
    pasos = "".join(f'<li><span>{i + 1:02d}</span><div><b>{t}</b><p>{d}</p></div></li>' for i, (t, d) in enumerate(PASOS))
    prep = "".join(
        f'<details class="pq reveal" data-acc="prep"><summary><span class="pq-ic">{ic(k, 20)}</span><h3>{t}</h3>{PM}</summary>'
        '<ul>' + "".join(f"<li>{x}</li>" for x in li) + '</ul></details>' for k, t, li in PREP)
    faq = "".join(
        f'<details class="qa"{" open" if i == 0 else ""} data-acc="faq"><summary><h3>{q}</h3>{PM}</summary><p>{a}</p></details>'
        for i, (q, a) in enumerate(FAQ))
    cred = "".join(f'<div><dt>{a}</dt><dd>{b}</dd></div>' for a, b in CRED)
    hab = "".join(
        f'<figure class="dist">{pic(img, "Distintivo de habilitación " + c)}<figcaption><small>{g} · {t}</small><b>{c}</b></figcaption></figure>'
        for g, t, c, img in HAB)

    return head(2, FONTS, "#12304A") + f"""
<header class="top"><div class="wrap bar">
  <a class="brand" href="#inicio" aria-label="CARDIODUARTE, inicio"><span class="logo"><i class="mark"></i></span><b>CARDIODUARTE</b></a>
  <nav class="main" aria-label="Principal">{nav}</nav>
  <a class="btn btn-primary head-cta" href="#cita"><span>Agendar cita</span><i>{ARROW}</i></a>
  {menu_btn()}
</div>{mnav()}</header>

<main id="contenido">
<section class="hero" id="inicio">
  {pic("sala-ecocardiografia", ALT["sala-ecocardiografia"], "hero-bg", eager=True, pos="35% 50%")}
  <div class="wrap hero-in">
    <div class="hero-copy">
      <span class="eyebrow">{ic("heartecg", 16, 2)}Cardiología y ecocardiografía · El Poblado, Medellín</span>
      <h1>{H1}</h1>
      <p class="lead">{LEAD}</p>
      <div class="ctas">{btn("Agendar una cita")}{btn("Ver servicios", "#servicios", "glass")}</div>
      <div class="avatars"><span class="stack">{pic("dr-duarte", "", "av")}{pic("v-ecografo", "", "av")}{pic("v-esfuerzo", "", "av")}</span>
        <p><b>Atención directa del especialista</b><span>Consulta y exámenes en un solo lugar</span></p></div>
    </div>
    <div class="hero-foot">
      <span class="trust">{ic("shield", 18, 2)}<span><b>Servicios habilitados</b> ante el Ministerio de Salud</span></span>
      <aside class="book" aria-label="Agendar cita">
        <p class="book-t">Agende su cita</p>
        <div class="book-r">{pic("dr-duarte", "", "book-av", pos="50% 15%")}<div><b>{DOCTOR}</b><small>Cardiólogo ecocardiografista</small></div></div>
        <a class="btn btn-white" href="{WA}" target="_blank" rel="noopener"><span>Hablemos por WhatsApp</span><i>{ARROW}</i></a>
      </aside>
    </div>
  </div>
</section>

<section class="sec" id="doctor"><div class="wrap">
  <div class="about-top">
    {chip("Sobre CARDIODUARTE")}
    <p class="statement reveal">En CARDIODUARTE le atiende directamente el especialista. <span>Le explicamos cada examen antes de hacerlo, resolvemos sus dudas con calma y le entregamos resultados que usted pueda entender.</span></p>
    {btn("Conozca al doctor", "#especialista", "dark")}
  </div>
  <div class="about-grid">
    <figure class="ph ph-a reveal">{pic("dr-duarte", ALT["dr-duarte"], pos="50% 20%")}</figure>
    <figure class="ph ph-b reveal">{pic("v-consulta", ALT["v-consulta"], pos="50% 78%")}<figcaption>“{QUOTE}” {tag()}</figcaption></figure>
    <div class="nums">
      <div class="num reveal"><p><span data-count="15">15</span><em>+</em></p><b>Años de trayectoria</b><small>En diagnóstico y tratamiento del corazón</small></div>
      <div class="num reveal"><p><span data-count="8">8</span><em>·</em></p><b>Servicios y exámenes</b><small>Consulta, ecocardiografía, pruebas y monitoreo</small></div>
      <div class="num reveal"><p><span data-count="2">2</span><em>✓</em></p><b>Servicios habilitados</b><small>Cardiología e imágenes no ionizantes</small></div>
    </div>
  </div>
</div></section>

<section class="sec sec-mist" id="servicios"><div class="wrap svc">
  <div class="svc-l">
    {chip("Servicios", "grid")}
    <h2>Consulta y exámenes del corazón en un solo lugar</h2>
    <p class="lead">El médico que le examina es el mismo que interpreta su estudio y le explica el resultado.</p>
    {btn("Pedir orientación", "#cita", "primary", ' data-servicio="No estoy seguro, necesito orientación"')}
  </div>
  <div class="svc-r">{servicios}</div>
</div></section>

<section class="sec" id="por-que"><div class="wrap">
  <div class="head-c">{chip("Por qué elegirnos", "award")}<h2>Lo que encuentra en cada visita</h2>
    <p class="lead">Un consultorio pensado para que usted entienda su corazón y sepa qué hacer después.</p></div>
  <div class="wgrid">{razones}</div>
  <div class="wide">
    <figure class="reveal">{pic("v-recep2", ALT["v-recep2"], pos="50% 45%")}<figcaption><b>Un consultorio tranquilo</b><span>Consultorio 1325 · Torre Médica Metropolitan Salud</span></figcaption></figure>
    <figure class="reveal">{pic("v-letrero", ALT["v-letrero"], pos="50% 72%")}<figcaption><b>CARDIODUARTE</b><span>Cardiología y ecocardiografía · El Poblado, Medellín</span></figcaption></figure>
  </div>
</div></section>

<section class="sec sec-mist" id="prevencion"><div class="wrap">
  <div class="head-split">
    <div>{chip("Prevención", "leaf")}<h2>Pequeños hábitos que cuidan su corazón</h2></div>
    <p class="lead">Recomendaciones generales de salud cardiovascular. No reemplazan la valoración médica ni las indicaciones de su médico tratante. {tag("Ejemplo · validar con el Dr. Duarte")}</p>
  </div>
  <div class="pgrid">{prev}</div>
  <div class="alarm reveal"><span>{ic("alert", 22, 2)}</span><div><h3>Señales de alarma: no espere una cita</h3><p>{ALARMA}</p></div></div>
</div></section>

<section class="band" id="cita-banda">{ECG_BG}<div class="wrap band-in">
  <div class="band-l">
    {chip("Su cita", "cal", True)}
    <h2>Agendar una cita es sencillo</h2>
    <ol class="pasos">{pasos}</ol>
  </div>
  <div class="formcard" id="cita"><h2 class="fc-t">Solicite su cita</h2><p class="fc-s">Déjenos sus datos y le contactamos.</p>
    {form("btn btn-primary btn-submit", f"<i>{ARROW}</i>")}</div>
</div></section>

<section class="sec" id="atencion"><div class="wrap">
  <div class="head-c">{chip("Formas de atención", "id")}<h2>Elija cómo quiere ser atendido</h2>
    <p class="lead">El valor o la cobertura se confirman al agendar, según el servicio y su aseguradora.</p></div>
  <div class="plans">
    <article class="plan reveal"><span class="pl-ic">{ic("user", 22)}</span><h3>Particular</h3>
      <p>Consulta y exámenes sin intermediarios. Para la consulta particular no necesita orden médica.</p>
      <ul><li><i>{ic("check", 14, 2.6)}</i>Le atiende el especialista</li><li><i>{ic("check", 14, 2.6)}</i>Resultado explicado en la cita</li><li><i>{ic("check", 14, 2.6)}</i>Agenda por WhatsApp</li></ul>
      <p class="price">Valor: se informa al agendar</p>{btn("Agendar", "#cita", "dark", ' data-servicio="Consulta de cardiología"')}</article>
    <article class="plan plan-hi reveal" id="chequeo"><span class="pl-badge">Para pacientes particulares</span><span class="pl-ic">{ic("heartecg", 22)}</span><h3>Chequeo Ejecutivo Cardiovascular</h3>
      <p>Una evaluación completa de su corazón en un solo programa, con los resultados explicados por el especialista.</p>
      <ul>{chequeo}</ul>
      <p class="price">Valor: se informa al agendar</p>{btn("Solicitar el chequeo", "#cita", "primary", ' data-servicio="Chequeo Ejecutivo Cardiovascular"')}</article>
    <article class="plan reveal"><span class="pl-ic">{ic("shield", 22)}</span><h3>Póliza o medicina prepagada</h3>
      <p>Atendemos según la cobertura de su aseguradora. Escríbanos con su nombre y le confirmamos cómo puede ser atendido. {tag("Ejemplo · ajustar según convenios")}</p>
      <ul><li><i>{ic("check", 14, 2.6)}</i>Orden médica y autorización si la exige</li><li><i>{ic("check", 14, 2.6)}</i>Le orientamos con el trámite</li><li><i>{ic("check", 14, 2.6)}</i>Mismo especialista, mismo cuidado</li></ul>
      <p class="price">Cobertura: según su aseguradora</p>{btn("Consultar cobertura", "#cita", "dark")}</article>
  </div>
</div></section>

<section class="sec sec-mist" id="especialista"><div class="wrap doc">
  <article class="dcard reveal">{pic("dr-duarte", ALT["dr-duarte"], pos="50% 20%")}
    <div class="dc-b"><b>{DOCTOR}</b><span>Cardiólogo ecocardiografista</span></div><a class="dc-plus" href="#cita" aria-label="Agendar con el doctor">{ic("plus", 18, 2.4)}</a></article>
  <div class="doc-r">
    {chip("Su especialista", "steth")}
    <h2>Formación, experiencia y habilitación</h2>
    <p class="lead">{BIO}</p>
    <dl class="cred">{cred}</dl>
    <div class="hab" id="habilitacion">{hab}</div>
    {btn("Verificar en MinSalud", MINSALUD, "dark", ' target="_blank" rel="noopener"')}
  </div>
</div></section>

<section class="sec" id="preparacion"><div class="wrap prep">
  <div class="prep-l">
    {chip("Preparación", "clip")}
    <h2>Cómo prepararse para su examen</h2>
    <p class="lead">Indicaciones generales. Siga siempre lo que le indique el consultorio al confirmar su cita. No suspenda medicamentos sin orden médica. {tag("Ejemplo · validar con el Dr. Duarte")}</p>
    <figure class="ph ph-prep reveal">{pic("v-esfuerzo", ALT["v-esfuerzo"], pos="50% 50%")}</figure>
  </div>
  <div class="prep-r">{prep}</div>
</div></section>

<section class="sec sec-gray" id="faq"><div class="wrap faq">
  <div class="faq-l">{chip("Preguntas frecuentes", "chat")}<h2>Respuestas a sus preguntas</h2>
    <p class="lead">Lo que más nos preguntan sobre citas, coberturas y cómo llegar.</p>
    <div class="help"><b>¿Necesita ayuda?</b><p>Escríbanos por WhatsApp al {TEL}.</p>{btn("Escríbanos", WA, "primary", ' target="_blank" rel="noopener"')}</div></div>
  <div class="faq-r">{faq}</div>
</div></section>

<section class="sec" id="ubicacion"><div class="wrap visit">
  <figure class="ph ph-torre reveal">{pic("v-torre", ALT["v-torre"], pos="50% 40%")}</figure>
  <div class="visit-r">
    {chip("Ubicación y horario", "pin")}
    <h2>Le esperamos en El Poblado</h2>
    <ul class="ilist">
      <li><i>{ic("pin", 20)}</i><div><b>Dirección</b><span>{DIR1}<br>{DIR2}<br>{DIR3}</span></div></li>
      <li><i>{ic("clock", 20)}</i><div><b>Horario</b><span>Lunes a viernes, 7:00 a. m. a 5:00 p. m. {tag("Validar")}</span></div></li>
      <li><i>{ic("phone", 20)}</i><div><b>WhatsApp y teléfono</b><span><a href="tel:+573187984545">{TEL}</a></span></div></li>
      <li><i>{ic("mail", 20)}</i><div><b>Correo</b><span><a href="mailto:{MAIL}">{MAIL}</a> · {WEB}</span></div></li>
    </ul>
    {btn("Abrir en Google Maps", MAPS, "dark", ' target="_blank" rel="noopener"')}
  </div>
</div></section>

<section class="wrap"><div class="cta reveal">
  {pic("recepcion", ALT["recepcion"], "cta-bg", pos="50% 30%")}
  <div class="cta-in">{chip("Su próximo paso", "heart", True)}<h2>Haga de su corazón una prioridad</h2>
    <p>Ya sea un chequeo o un examen puntual, le ayudamos a planear su cita.</p>
    <div class="ctas">{btn("Agendar una cita")}{btn("Escribir por WhatsApp", WA, "glass", ' target="_blank" rel="noopener"')}</div></div>
</div></section>
</main>

<footer class="foot"><div class="wrap">
  <div class="fcols">
    <div class="fbrand"><a class="brand" href="#inicio"><span class="logo"><i class="mark"></i></span><b>CARDIODUARTE</b></a>
      <p>Cardiología y ecocardiografía. {DOCTOR}, cardiólogo ecocardiografista, en El Poblado, Medellín.</p>
      <p class="hours"><b>Horario</b>Lunes a viernes · 7:00 a. m. a 5:00 p. m. {tag("Validar")}</p></div>
    <div><b>Contacto</b><span>{DIR1}, {DIR2}, Medellín</span><a href="tel:+573187984545">{TEL}</a><a href="mailto:{MAIL}">{MAIL}</a><span>{WEB}</span></div>
    <nav aria-label="Enlaces"><b>Páginas</b>{"".join(f'<a href="{h}">{t}</a>' for h, t in NAV)}<a href="#cita">Agendar cita</a></nav>
    <nav aria-label="Servicios"><b>Servicios</b>{"".join(f'<a href="#servicios">{s[1]}</a>' for s in SERVICIOS[:6])}</nav>
  </div>
  {politica_details()}
  <p class="legal">{LEGAL}</p>
  <p class="giant" aria-hidden="true">CARDIODUARTE</p>
</div></footer>
""" + tail()
