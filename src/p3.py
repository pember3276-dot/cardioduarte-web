"""Opción 3 · Cercana y enfocada en el bienestar (estructura inspirada en la referencia Dr. Alex)."""
from datos import *

FONTS = "family=Fjalla+One&family=Inter:wght@400;500;600;700"
ARROW = ic("arrow", 16, 2.2)
PLUS = ic("plus", 16, 2.4)


def chip(t, light=False):
    return f'<span class="chip{" chip-l" if light else ""}"><i></i>{t}</span>'


def btn(t, href="#cita", kind="teal", extra="", icon=None):
    return f'<a class="btn btn-{kind}" href="{href}"{extra}><span>{t}</span><i>{icon or ARROW}</i></a>'


# dibujos de línea de la portada: (icono, izquierda %, arriba %, tamaño px, giro)
DOODLES = [("steth", 4, 18, 120, -12), ("ecg", 20, 70, 150, 0), ("heart", 82, 14, 110, 10), ("holter", 90, 60, 96, -8),
           ("pill", 8, 62, 80, 30), ("kit", 70, 76, 100, 6), ("drop", 30, 10, 70, 0), ("heartecg", 60, 6, 80, -6),
           ("gauge", 46, 80, 70, 0), ("clip", 96, 34, 70, 12)]


def page():
    nav = "".join(f'<a href="{h}">{t}</a>' for h, t in NAV)
    doodles = "".join(
        f'<span style="left:{x}%;top:{y}%;width:{s}px;height:{s}px;transform:rotate({r}deg)">{ic(k, s, 1)}</span>'
        for k, x, y, s, r in DOODLES)
    POS = {"v-consulta": "50% 75%", "v-ecografo": "50% 55%", "v-esfuerzo": "50% 50%", "sala-ecocardiografia": "30% 50%"}

    def svc(s):
        k, t, d, u, img = s
        return (f'<article class="svc reveal"><div class="svc-h"><span class="svc-ic">{ic(k, 30, 1.4)}</span><h3>{t}</h3></div>'
                f'<figure>{pic(img, ALT[img], pos=POS.get(img))}</figure><p>{d}</p><p class="u"><b>Útil si:</b> {u}</p>'
                f'{btn("Agendar este servicio", "#cita", "teal", f" data-servicio=" + chr(34) + t + chr(34), ic("cal", 16, 2))}</article>')

    def svc_sm(s):
        k, t, d, u, img = s
        return (f'<article class="svs reveal"><span class="svc-ic">{ic(k, 26, 1.4)}</span><h3>{t}</h3><p>{d}</p>'
                f'<a class="more" href="#cita" data-servicio="{t}">Agendar <i>{ARROW}</i></a></article>')

    con_foto = [s for s in SERVICIOS if s[4] and s[4] != "v-cuadros"]
    sin_foto = [s for s in SERVICIOS if s not in con_foto]

    # tablero de "mi forma de trabajar": alterna íconos y textos
    tiles, colors = [], ["t-white", "t-coral", "t-teal"]
    for i, (k, t, d) in enumerate(RAZONES):
        row = i // 2
        icon = f'<div class="tile tile-ic {colors[i % 3]} reveal">{ic(k, 54, 1.2)}</div>'
        text = f'<div class="tile tile-tx reveal"><h3>{t}</h3><p>{d}</p></div>'
        tiles.append(icon + text if row % 2 == 0 else text + icon)
    tablero = "".join(tiles)

    edu = [("steth", "Especialidad", "Cardiología · Ecocardiografía"),
           ("cap", "Formación", f"Universidad y año de cada título {tag('Por completar')}"),
           ("id", "Registro médico", f"N.º de registro (ReTHUS) {tag('Por completar')}"),
           ("award", "Experiencia", "Más de 15 años; jefatura de servicio de cardiología"),
           ("user", "Atiende", "Adultos · Particulares, con póliza o medicina prepagada (según cobertura)")]
    edu_html = "".join(f'<li class="edu reveal"><span class="edu-ic">{ic(k, 24, 1.6)}</span><div><h3>{t}</h3><p>{d}</p></div></li>' for k, t, d in edu)
    hab = "".join(
        f'<li class="edu edu-hab reveal"><span class="edu-img">{pic(img, "Distintivo de habilitación " + c)}</span><div><h3>{t}</h3><p>{g} · Distintivo {c}</p></div></li>'
        for g, t, c, img in HAB)

    pcls = ["p-light", "p-teal", "p-coral"]
    prev = "".join(
        f'<article class="pcard {pcls[i % 3]} reveal"><span class="pc-ic">{ic(k, 22, 1.8)}</span><h3>{t}</h3><p>{d}</p></article>'
        for i, (k, t, d) in enumerate(PREVENCION))
    chequeo = "".join(f'<li><i>{ic("check", 14, 2.6)}</i><span><b>{t}.</b> {d}</span></li>' for t, d in CHEQUEO)
    pasos = "".join(f'<li><span>{i + 1}</span><div><b>{t}</b><p>{d}</p></div></li>' for i, (t, d) in enumerate(PASOS))
    prep = "".join(
        f'<details class="acc" data-acc="prep"><summary><span class="acc-ic">{ic(k, 20, 1.8)}</span><h3>{t}</h3><i class="sq">{PLUS}</i></summary>'
        '<ul>' + "".join(f"<li>{x}</li>" for x in li) + '</ul></details>' for k, t, li in PREP)
    faq = "".join(
        f'<details class="acc"{" open" if i == 0 else ""} data-acc="faq"><summary><h3>{q}</h3><i class="sq">{PLUS}</i></summary><p>{a}</p></details>'
        for i, (q, a) in enumerate(FAQ))

    return head(3, FONTS, "#287C80") + f"""
<header class="top"><div class="wrap"><div class="bar">
  <a class="brand" href="#inicio" aria-label="CARDIODUARTE, inicio"><span class="logo"><i class="mark"></i></span><b>CARDIODUARTE</b></a>
  <nav class="main" aria-label="Principal">{nav}</nav>
  <a class="btn btn-teal head-cta" href="#cita"><span>Agendar cita</span><i>{ic("cal", 16, 2)}</i></a>
  {menu_btn()}
  {mnav()}
</div></div></header>

<main id="contenido">
<section class="hero" id="inicio">
  <div class="doodles" aria-hidden="true">{doodles}</div>
  <div class="wrap hero-grid">
    <div class="hero-l">
      <p class="hi">Hola, soy el <b>{DOCTOR}</b></p>
      <p class="lead">{LEAD}</p>
      <div class="rating"><span class="stack">{pic("v-consulta", "", "av", pos="50% 75%")}{pic("v-ecografo", "", "av")}{pic("v-esfuerzo", "", "av")}</span>
        <p><b>15+ años</b><span>cuidando corazones en Medellín</span></p></div>
    </div>
    <div class="portrait">
      <span class="ring" aria-hidden="true"></span>
      {pic("dr-duarte", ALT["dr-duarte"], "pt-img", eager=True, pos="50% 15%")}
      <span class="orb o1" aria-hidden="true">{ic("heart", 20, 1.8)}</span>
      <span class="orb o2" aria-hidden="true">{ic("ecg", 20, 1.8)}</span>
      <span class="orb o3" aria-hidden="true">{ic("echo", 20, 1.8)}</span>
      <span class="orb o4" aria-hidden="true">{ic("steth", 20, 1.8)}</span>
    </div>
    <div class="hero-r">
      <p>{ic("shield", 18, 2)}<span>Servicios <b>habilitados</b> ante el Ministerio de Salud</span></p>
      <p>{ic("pin", 18, 2)}<span>Torre Médica Metropolitan Salud, <b>El Poblado</b></span></p>
      <div class="ctas">{btn("Agendar una cita", "#cita", "coral", "", ic("cal", 16, 2))}{btn("Ver servicios", "#servicios", "white")}</div>
    </div>
  </div>
  <h1 class="giant-h"><span class="sr">{H1} </span><span aria-hidden="true">Cardiología y</span> <span aria-hidden="true">ecocardiografía</span></h1>
</section>

<section class="sec" id="doctor"><div class="wrap about">
  <figure class="about-ph reveal">{pic("v-consulta", ALT["v-consulta"], pos="50% 78%")}<span class="about-badge"><b>15+</b><small>años de trayectoria</small></span></figure>
  <div class="about-r">
    {chip("Sobre el doctor")}
    <h2>Un cardiólogo que le explica, le escucha y le acompaña</h2>
    <p class="lead">{BIO}</p>
    <div class="goal reveal">{pic("v-cuadros", "", "goal-img")}<div><b>Mi objetivo</b><p>“{QUOTE}” {tag()}</p></div></div>
    {btn("Conozca su formación", "#formacion", "teal")}
  </div>
</div></section>

<section class="sec sec-light" id="servicios"><div class="wrap">
  <div class="head-row">
    <div>{chip("Servicios")}<h2>Lo que hago por su corazón</h2></div>
    {btn("Pedir orientación", "#cita", "teal", ' data-servicio="No estoy seguro, necesito orientación"')}
  </div>
  <div class="svc-grid">{"".join(svc(s) for s in con_foto)}</div>
  <div class="svs-grid">{"".join(svc_sm(s) for s in sin_foto)}</div>
  <div class="chequeo reveal" id="chequeo">
    <div class="ch-l">{chip("Para pacientes particulares", True)}<h2>Chequeo Ejecutivo Cardiovascular</h2>
      <p>Una evaluación completa de su corazón en un solo programa, con los resultados explicados por el especialista.</p>
      {btn("Solicitar el chequeo", "#cita", "white", ' data-servicio="Chequeo Ejecutivo Cardiovascular"', ic("cal", 16, 2))}</div>
    <ul class="ch-r">{chequeo}</ul>
  </div>
</div></section>

<section class="sec" id="por-que"><div class="wrap">
  <div class="head-c">{chip("Mi forma de trabajar")}<h2>Así le atiendo</h2>
    <p class="lead">Lo que encuentra en cada visita a CARDIODUARTE.</p></div>
  <div class="board">{tablero}</div>
</div></section>

<section class="sec sec-light" id="formacion"><div class="wrap edu-wrap">
  <div class="edu-l">
    {chip("Formación y habilitación")}
    <h2>Formación y experiencia</h2>
    <p class="lead">Conozca quién le atiende. Los datos marcados se completan con el consultorio.</p>
    <p class="lead">Prestador 0500127007. Puede verificar cada distintivo en el portal del Ministerio de Salud.</p>
    {btn("Verificar en MinSalud", MINSALUD, "teal", ' target="_blank" rel="noopener"')}
  </div>
  <ul class="edu-list" id="habilitacion">{edu_html}{hab}</ul>
</div></section>

<section class="sec" id="prevencion"><div class="wrap">
  <div class="head-c">{chip("Prevención")}<h2>Pequeños hábitos que cuidan su corazón</h2>
    <p class="lead">Recomendaciones generales de salud cardiovascular. No reemplazan la valoración médica ni las indicaciones de su médico tratante. {tag("Ejemplo · validar con el Dr. Duarte")}</p></div>
  <div class="pgrid">{prev}</div>
  <div class="alarm reveal"><span>{ic("alert", 22, 2)}</span><div><h3>Señales de alarma: no espere una cita</h3><p>{ALARMA}</p></div></div>
</div></section>

<section class="sec sec-light" id="ubicacion"><div class="wrap">
  <div class="head-c">{chip("Su cita")}<h2>Agende su cita</h2>
    <p class="lead">Le acompañamos desde el primer mensaje hasta la entrega de su resultado.</p></div>
  <div class="booking">
    <div class="bk-l">
      <figure class="bk-ph reveal">{pic("recepcion", ALT["recepcion"], pos="50% 30%")}</figure>
      <div class="hours-box"><h3>Horario de atención</h3>
        <p><span>Lunes a viernes</span><b>7:00 a. m. – 5:00 p. m.</b></p>
        {tag("Validar")}</div>
      <a class="phone-box" href="tel:+573187984545"><span>{ic("phone", 22, 1.8)}</span><div><small>WhatsApp y teléfono</small><b>{TEL}</b></div></a>
      <div class="addr"><span>{ic("pin", 20, 1.8)}</span><p><b>{DIR1}</b><br>{DIR2}<br>{DIR3}<br><a href="{MAPS}" target="_blank" rel="noopener">Abrir en Google Maps</a> · <a href="mailto:{MAIL}">{MAIL}</a></p></div>
    </div>
    <div class="bk-r" id="cita">
      <ol class="pasos">{pasos}</ol>
      <h3 class="bk-t">Solicitud de cita</h3>
      {form("btn btn-coral btn-submit", f"<i>{ic('cal', 16, 2)}</i>")}
    </div>
  </div>
</div></section>

<section class="sec" id="preparacion"><div class="wrap qa-wrap">
  <div class="head-c">{chip("Preparación")}<h2>Cómo prepararse para su examen</h2>
    <p class="lead">Indicaciones generales. Siga siempre lo que le indique el consultorio al confirmar su cita. No suspenda medicamentos sin orden médica. {tag("Ejemplo · validar con el Dr. Duarte")}</p></div>
  <div class="accs">{prep}</div>
</div></section>

<section class="sec sec-light" id="faq"><div class="wrap qa-wrap">
  <div class="head-c">{chip("Preguntas frecuentes")}<h2>Preguntas frecuentes</h2></div>
  <div class="accs">{faq}</div>
</div></section>

<section class="wrap"><div class="cta reveal">
  {pic("v-recep2", ALT["v-recep2"], "cta-bg", pos="50% 45%")}
  <div class="cta-in">{chip("Su próximo paso", True)}<h2>Haga de su corazón una prioridad</h2>
    <p>Ya sea un chequeo o un examen puntual, le ayudamos a planear su cita.</p>
    <div class="ctas">{btn("Agendar una cita", "#cita", "coral", "", ic("cal", 16, 2))}{btn("Escribir por WhatsApp", WA, "white", ' target="_blank" rel="noopener"')}</div></div>
</div></section>
</main>

<footer class="foot">
  <div class="fband"><div class="wrap fband-in">
    <div><b>Escríbanos</b><a href="{WA}" target="_blank" rel="noopener">{WA_ICON}WhatsApp {TEL}</a></div>
    <a class="brand fb-brand" href="#inicio"><span class="logo"><i class="mark"></i></span><b>CARDIODUARTE</b></a>
    <div class="fb-r"><b>Horario</b><span>Lunes a viernes · 7:00 a. m. a 5:00 p. m.</span></div>
  </div></div>
  <div class="fmain"><div class="wrap">
    <div class="fcols">
      <div class="fbig"><p class="talk">Hablemos de la salud de su corazón.</p>{btn("Agendar una cita", "#cita", "coral", "", ic("cal", 16, 2))}</div>
      <nav aria-label="Enlaces"><b>Enlaces</b>{nav}<a href="#cita">Agendar cita</a></nav>
      <div><b>Contacto</b><span>{DIR1}, {DIR2}, Medellín</span><a href="tel:+573187984545">{TEL}</a><a href="mailto:{MAIL}">{MAIL}</a><span>{WEB}</span></div>
    </div>
    {politica_details()}
    <p class="legal">{LEGAL}</p>
  </div></div>
</footer>
""" + tail()
