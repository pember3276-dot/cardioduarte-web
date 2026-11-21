#!/usr/bin/env python3
"""Genera opcion-1/, opcion-2/ y opcion-3/ a partir de un solo contenido.

El contenido (textos, servicios, formulario, política) vive aquí una sola vez.
Cada opción tiene su propio sistema de diseño en assets/css/tema-N.css,
sobre la estructura común de assets/css/base.css.

Uso:  python3 src/build.py
"""
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

OPCIONES = {
    1: {
        "nombre": "Clínica moderna y profesional",
        "fuentes": "family=Manrope:wght@500;600;700;800&family=Inter:wght@400;500;600",
        "color": "#164E78",
    },
    2: {
        "nombre": "Elegante y premium",
        "fuentes": "family=Playfair+Display:ital,wght@0,500;0,600;1,500&family=Jost:wght@400;500;600",
        "color": "#12304A",
    },
    3: {
        "nombre": "Cercana y enfocada en el bienestar",
        "fuentes": "family=Nunito:wght@400;600;700;800",
        "color": "#287C80",
    },
}

WA = "https://wa.me/573187984545?text=Hola%2C%20quisiera%20informaci%C3%B3n%20para%20una%20cita%20en%20CARDIODUARTE"
WA_ICON = '<svg width="20" height="20" viewBox="0 0 24 24" aria-hidden="true" fill="currentColor"><path d="M12 2a10 10 0 0 0-8.6 15.1L2 22l5-1.3A10 10 0 1 0 12 2Zm0 18.2a8.2 8.2 0 0 1-4.2-1.2l-.3-.2-3 .8.8-2.9-.2-.3A8.2 8.2 0 1 1 12 20.2Zm4.5-6.1c-.2-.1-1.5-.7-1.7-.8s-.4-.1-.6.1-.7.8-.8 1-.3.2-.5.1a6.7 6.7 0 0 1-3.3-2.9c-.2-.4.2-.4.7-1.3.1-.2 0-.3 0-.4l-.8-1.8c-.2-.5-.4-.4-.6-.4h-.5a1 1 0 0 0-.7.3 3 3 0 0 0-.9 2.2 5.2 5.2 0 0 0 1.1 2.8 11.9 11.9 0 0 0 4.6 4c1.7.7 2.3.8 3.2.7a2.7 2.7 0 0 0 1.8-1.3 2.2 2.2 0 0 0 .2-1.3c-.1-.1-.2-.2-.4-.3Z"/></svg>'
CHECK = '<svg width="18" height="18" viewBox="0 0 16 16" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M3 8.5l3 3 7-7"/></svg>'


def ic(path, size=24):
    return (f'<svg width="{size}" height="{size}" viewBox="0 0 24 24" fill="none" stroke="currentColor" '
            f'stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{path}</svg>')


I = {
    "heart": '<path d="M12 20s-7-4.4-7-10a4 4 0 0 1 7-2.6A4 4 0 0 1 19 10c0 5.6-7 10-7 10Z"/>',
    "echo": '<path d="M4 18a8 8 0 0 1 16 0"/><path d="M12 18 8 9"/><circle cx="12" cy="18" r="1.5"/>',
    "run": '<circle cx="15" cy="5" r="2"/><path d="M8 21l3-6 3 2v4M6 12l4-3 4 2 3 3"/>',
    "pill": '<rect x="4" y="9" width="16" height="6" rx="3" transform="rotate(-45 12 12)"/><path d="M9.5 9.5l5 5"/>',
    "ecg": '<path d="M2 12h5l2-5 3 10 3-8 2 3h5"/>',
    "bars": '<path d="M4 20V10M10 20V4M16 20v-7M22 20H2"/>',
    "holter": '<rect x="6" y="4" width="12" height="16" rx="3"/><path d="M9 12h1.5l1-2 1.5 4 1-2H15"/>',
    "gauge": '<circle cx="12" cy="13" r="7"/><path d="M12 13l3-3M12 3v3"/>',
    "user": '<circle cx="12" cy="8" r="4"/><path d="M4 21a8 8 0 0 1 16 0"/>',
    "eye": '<path d="M2 12s3.5-7 10-7 10 7 10 7-3.5 7-10 7S2 12 2 12Z"/><circle cx="12" cy="12" r="3"/>',
    "grid": '<rect x="3" y="3" width="7" height="7" rx="2"/><rect x="14" y="3" width="7" height="7" rx="2"/><rect x="3" y="14" width="7" height="7" rx="2"/><rect x="14" y="14" width="7" height="7" rx="2"/>',
    "shield": '<path d="M12 3 4 6v6c0 4.5 3.4 8.3 8 9 4.6-.7 8-4.5 8-9V6l-8-3Z"/><path d="m9 12 2 2 4-4"/>',
    "award": '<circle cx="12" cy="9" r="6"/><path d="M8.5 14 7 22l5-3 5 3-1.5-8"/>',
    "pin": '<path d="M12 22s7-6.2 7-12a7 7 0 0 0-14 0c0 5.8 7 12 7 12Z"/><circle cx="12" cy="10" r="2.5"/>',
    "drop": '<path d="M12 3s6 6.4 6 11a6 6 0 0 1-12 0c0-4.6 6-11 6-11Z"/><path d="M9 14h6M12 11v6"/>',
    "walk": '<circle cx="13" cy="4" r="2"/><path d="m9 20 2.5-6L14 16v5M7 11l3-3h3l3 3"/>',
    "nosmoke": '<path d="M3 14h13v3H3zM19 14v3M21 14v3"/><path d="M4 4l16 16"/>',
    "leaf": '<path d="M5 19c0-8 5-13 15-14-1 10-6 15-14 15"/><path d="M5 19 13 11"/>',
    "moon": '<path d="M20 14.5A8 8 0 1 1 9.5 4a6.5 6.5 0 0 0 10.5 10.5Z"/>',
    "steth": '<path d="M6 3v6a4 4 0 0 0 8 0V3"/><path d="M10 13v3a5 5 0 0 0 10 0v-2"/><circle cx="20" cy="12" r="2"/>',
    "alert": '<path d="M12 3 2 20h20L12 3Z"/><path d="M12 10v4M12 17h.01"/>',
}

SERVICIOS = [
    ("heart", "Consulta de cardiología",
     "Valoración del especialista para síntomas como dolor en el pecho, palpitaciones, presión alta o cansancio, y control de enfermedades del corazón.",
     "tiene síntomas, antecedentes familiares o le remitieron."),
    ("echo", "Ecocardiograma transtorácico",
     "Ultrasonido que muestra en tiempo real la forma y el funcionamiento del corazón y sus válvulas. No duele y no usa radiación.",
     "le encontraron un soplo o necesita evaluar la fuerza del corazón."),
    ("run", "Ecocardiograma de estrés con ejercicio",
     "Ecocardiograma antes y después de caminar en banda, para ver cómo responde el corazón al esfuerzo.",
     "se busca descartar enfermedad de las arterias del corazón."),
    ("pill", "Ecocardiograma de estrés farmacológico",
     "Para quien no puede hacer ejercicio: un medicamento simula el esfuerzo bajo vigilancia continua del especialista.",
     "tiene limitaciones para caminar o correr."),
    ("ecg", "Electrocardiograma",
     "Registro de la actividad eléctrica del corazón en pocos minutos. Detecta alteraciones del ritmo y de la conducción.",
     "necesita un chequeo o un requisito prequirúrgico."),
    ("bars", "Prueba de esfuerzo",
     "Electrocardiograma mientras camina en banda, con aumento gradual de la intensidad. Mide su capacidad física y la respuesta del corazón.",
     "va a iniciar deporte o tiene dolor con el esfuerzo."),
    ("holter", "Holter de ritmo (24 a 48 h)",
     "Un pequeño equipo registra el ritmo del corazón mientras usted sigue su vida normal.",
     "siente palpitaciones, mareos o ha tenido desmayos."),
    ("gauge", "Monitoreo de presión arterial (MAPA)",
     "Mide la presión durante 24 horas en su entorno habitual, para un diagnóstico preciso de la hipertensión.",
     "sus cifras varían mucho o se le sube la presión en consulta."),
]

RAZONES = [
    ("user", "Le atiende el especialista", "Su consulta y sus exámenes los hace directamente el Dr. Duarte, no un intermediario."),
    ("eye", "Un mismo médico de principio a fin", "Quien le examina es quien interpreta el estudio y le explica el resultado."),
    ("grid", "Consulta y exámenes en un solo lugar", "Ecocardiografía, pruebas de esfuerzo, Holter y MAPA sin ir de un sitio a otro."),
    ("shield", "Servicios habilitados", "Cardiología e imágenes no ionizantes habilitadas ante el Ministerio de Salud."),
    ("award", "Más de 15 años de trayectoria", "Experiencia en diagnóstico y tratamiento, incluida la jefatura de un servicio de cardiología."),
    ("pin", "Fácil de llegar", "Torre Médica Metropolitan Salud, en El Poblado, frente a la estación de Metroplús."),
]

PREVENCION = [
    ("drop", "Conozca sus cifras", "Mida su presión arterial y pregunte por su colesterol y su glucosa. Muchas veces no dan síntomas."),
    ("walk", "Muévase cada día", "Caminar a paso rápido suma. Si va a empezar a hacer deporte, consulte antes."),
    ("nosmoke", "No fume", "Dejar el cigarrillo es de las decisiones que más protegen su corazón, a cualquier edad."),
    ("leaf", "Coma con menos sal", "Más frutas, verduras y alimentos frescos; menos sal, azúcar y productos ultraprocesados."),
    ("moon", "Descanse y maneje el estrés", "Dormir bien y darse pausas también es cuidar la presión arterial y el ritmo del corazón."),
    ("steth", "Hágase chequear", "Si tiene antecedentes familiares, hipertensión o diabetes, una valoración a tiempo marca la diferencia."),
]

PREP = [
    [("Ecocardiograma transtorácico", ["No requiere ayuno.", "Tome sus medicamentos como de costumbre.", "Use ropa cómoda de dos piezas.", "Duración aproximada: 30 a 40 minutos."], True),
     ("Ecocardiograma de estrés y prueba de esfuerzo", ["Comida liviana 2 a 3 horas antes.", "Ropa deportiva y tenis.", "Pregunte si debe suspender algún medicamento para el corazón antes del examen.", "Venga acompañado si es estrés farmacológico."], False),
     ("Electrocardiograma", ["No aplique cremas ni aceites en el pecho ese día.", "Dura unos 10 minutos."], False)],
    [("Holter de ritmo", ["Báñese antes de la cita: el equipo no se puede mojar.", "Haga su vida normal y anote en el diario sus síntomas y la hora.", "Regrese al día siguiente (o a las 48 horas) para retirarlo."], False),
     ("Monitoreo de presión arterial (MAPA)", ["Use una camisa de manga holgada.", "Mantenga el brazo quieto y estirado cada vez que el brazalete infle.", "Anote horas de sueño, comidas y medicamentos."], False),
     ("Qué traer a toda cita", ["Documento de identidad.", "Orden médica y autorización, si su póliza o prepagada la exige.", "Exámenes y lista de medicamentos actuales."], False)],
]

NAV = [("#doctor", "El doctor"), ("#servicios", "Servicios"), ("#prevencion", "Prevención"),
       ("#preparacion", "Preparación"), ("#ubicacion", "Ubicación")]

WAVE = ('<svg class="wave" viewBox="0 0 1440 70" preserveAspectRatio="none" aria-hidden="true">'
        '<path d="M0 40c160-30 320-40 480-20s320 50 480 40 320-40 480-40v50H0Z" fill="currentColor"/></svg>')


def picture(name, alt, w, h, cls="", eager=False):
    load = 'fetchpriority="high"' if eager else 'loading="lazy" decoding="async"'
    return (f'<picture{(" class=" + chr(34) + cls + chr(34)) if cls else ""}>'
            f'<source srcset="../assets/img/{name}.webp" type="image/webp">'
            f'<img src="../assets/img/{name}.jpg" alt="{alt}" width="{w}" height="{h}" {load}></picture>')


def page(n):
    o = OPCIONES[n]
    otras = " ".join(
        f'<a href="../opcion-{k}/index.html"{" aria-current=" + chr(34) + "page" + chr(34) if k == n else ""}>{k}</a>'
        for k in OPCIONES)
    nav = "".join(f'<a href="{h}">{t}</a>' for h, t in NAV)

    svc = "".join(
        f'<article class="svc reveal"><span class="n">{i + 1:02d}</span><div class="ic">{ic(I[k])}</div>'
        f'<h3>{t}</h3><p>{d}</p><p class="for"><b>Útil si:</b> {u}</p></article>'
        for i, (k, t, d, u) in enumerate(SERVICIOS))
    razones = "".join(
        f'<li class="reason reveal"><div class="ic">{ic(I[k])}</div><div><h3>{t}</h3><p>{d}</p></div></li>'
        for k, t, d in RAZONES)
    prev = "".join(
        f'<li class="tip reveal"><div class="ic">{ic(I[k])}</div><h3>{t}</h3><p>{d}</p></li>'
        for k, t, d in PREVENCION)

    def col(items):
        return "".join(
            f'<details class="acc"{" open" if op else ""}><summary>{t}</summary><div class="body"><ul>'
            + "".join(f"<li>{x}</li>" for x in li) + "</ul></div></details>"
            for t, li, op in items)

    return f"""<!doctype html>
<html lang="es" class="tema-{n}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<meta name="robots" content="noindex, nofollow">
<title>CARDIODUARTE · Cardiología y ecocardiografía en Medellín (opción {n})</title>
<meta name="description" content="CARDIODUARTE: consulta de cardiología, ecocardiograma, ecocardiograma de estrés, prueba de esfuerzo, Holter y MAPA con el Dr. Néstor Ricardo Duarte Suárez en El Poblado, Medellín.">
<meta name="theme-color" content="{o['color']}">
<link rel="icon" href="../assets/img/logo-corazon.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?{o['fuentes']}&display=swap">
<link rel="stylesheet" href="../assets/css/base.css">
<link rel="stylesheet" href="../assets/css/tema-{n}.css">
<script type="application/ld+json">{{"@context":"https://schema.org","@type":"MedicalClinic","name":"CARDIODUARTE","medicalSpecialty":"Cardiovascular","url":"https://www.cardioduarte.com","telephone":"+57 318 798 4545","email":"conscardioduarte@gmail.com","address":{{"@type":"PostalAddress","streetAddress":"Calle 33 n.º 43-85, consultorio 1325, Torre Médica Metropolitan Salud","addressLocality":"Medellín","addressCountry":"CO"}}}}</script>
</head>
<body>
<a class="skip" href="#contenido">Saltar al contenido</a>

<div class="demo"><div class="wrap"><span><strong>Opción {n} · {o['nombre']}.</strong> <span class="demo-txt">Versión demo: lo marcado <span class="tag">Ejemplo</span> se valida con el consultorio.</span></span>
  <nav class="demo-nav" aria-label="Cambiar de propuesta">Ver opción {otras} <a href="../index.html">Todas</a></nav></div></div>

<header class="top"><div class="wrap bar">
  <a class="brand" href="#inicio" aria-label="CARDIODUARTE, inicio">
    <i class="mark" aria-hidden="true"></i>
    <span class="word"><b>CARDIO<span>DUARTE</span></b><small>Cardiología y ecocardiografía</small></span>
  </a>
  <nav class="main" aria-label="Principal">
    {nav}
  </nav>
  <a class="btn btn-primary btn-sm head-cta" href="#cita">Agendar cita</a>
  <button class="menu-btn" type="button" aria-expanded="false" aria-controls="mnav" aria-label="Abrir menú"><svg width="20" height="20" viewBox="0 0 20 20" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" aria-hidden="true"><path d="M3 6h14M3 10h14M3 14h14"/></svg></button>
</div>
<nav class="mnav" id="mnav" aria-label="Menú móvil" hidden>{nav}<a href="#cita" class="mnav-cta">Agendar cita</a></nav>
</header>

<main id="contenido">
<section class="hero" id="inicio">
  <div class="hero-deco" aria-hidden="true"><span></span><span></span></div>
  <div class="wrap hero-grid">
    <div class="hero-copy">
      <p class="who">Dr. Néstor Ricardo Duarte Suárez · Cardiólogo ecocardiografista</p>
      <h1>Cuidamos su corazón con tiempo, cercanía y un diagnóstico claro.</h1>
      <p class="lead">En CARDIODUARTE le atiende directamente el especialista. Le explicamos cada examen antes de hacerlo, resolvemos sus dudas con calma y le entregamos resultados que usted pueda entender.</p>
      <div class="ctas">
        <a class="btn btn-primary" href="#cita">Agendar una cita</a>
        <a class="btn btn-wa" href="{WA}" target="_blank" rel="noopener">{WA_ICON}Escribir por WhatsApp</a>
      </div>
      <ul class="facts">
        <li>{CHECK}Más de 15 años de trayectoria</li>
        <li>{CHECK}Servicios habilitados ante MinSalud</li>
        <li>{CHECK}El Poblado, Medellín</li>
      </ul>
    </div>
    <figure class="portrait">
      {picture("dr-duarte", "Dr. Néstor Ricardo Duarte Suárez, cardiólogo, con bata blanca", 421, 495, eager=True)}
      <figcaption><b>Dr. Néstor Ricardo Duarte Suárez</b><span>Cardiología y ecocardiografía</span></figcaption>
      <span class="chip" aria-hidden="true">{ic(I["ecg"], 18)}Ecocardiografía</span>
    </figure>
  </div>
  {WAVE}
</section>

<svg class="ecg" viewBox="0 0 1200 28" preserveAspectRatio="none" aria-hidden="true"><path d="M0 14H520l10-8 10 16 12-20 14 24 10-12H1200" fill="none" stroke="currentColor" stroke-width="1.6" vector-effect="non-scaling-stroke"/></svg>

<section class="sec doc" id="doctor"><div class="wrap doc-grid">
  <div class="doc-copy reveal">
    <span class="eyebrow">El doctor</span>
    <h2>Dr. Néstor Ricardo Duarte Suárez</h2>
    <p class="lead">Cardiólogo y ecocardiografista con más de 15 años de trayectoria en el diagnóstico y el tratamiento de enfermedades del corazón. Ha liderado servicios de cardiología y hoy atiende en Medellín a pacientes que buscan una valoración cuidadosa y cercana.</p>
    <blockquote>“Cada paciente merece entender qué tiene su corazón y qué podemos hacer juntos.” <span class="tag">Ejemplo</span></blockquote>
  </div>
  <dl class="cred reveal">
    <div><dt>Especialidad</dt><dd>Cardiología · Ecocardiografía</dd></div>
    <div><dt>Formación</dt><dd>Universidad y año de cada título <span class="tag">Por completar</span></dd></div>
    <div><dt>Registro médico</dt><dd>N.º de registro (ReTHUS) <span class="tag">Por completar</span></dd></div>
    <div><dt>Experiencia</dt><dd>Más de 15 años; jefatura de servicio de cardiología</dd></div>
    <div><dt>Atiende</dt><dd>Adultos · Pacientes particulares, con póliza o medicina prepagada (según cobertura)</dd></div>
  </dl>
</div></section>

<section class="sec svc-sec" id="servicios"><div class="wrap">
  <div class="sec-head">
    <span class="eyebrow">Servicios</span>
    <h2>Consulta y exámenes del corazón en un solo lugar</h2>
    <p class="lead">El médico que le examina es el mismo que interpreta su estudio y le explica el resultado.</p>
  </div>
  <div class="svc-grid">{svc}</div>
  <div class="featured reveal" id="chequeo">
    <div class="feat-copy">
      <span class="eyebrow">Para pacientes particulares</span>
      <h3>Chequeo Ejecutivo Cardiovascular</h3>
      <p>Una evaluación completa de su corazón en un solo programa, con los exámenes que su caso necesita y los resultados explicados por el especialista.</p>
      <a class="btn btn-primary" href="#cita" data-servicio="Chequeo Ejecutivo Cardiovascular">Solicitar el chequeo</a>
    </div>
    <ul class="incl">
      <li>{CHECK}<span><b>Consulta especializada de cardiología</b></span></li>
      <li>{CHECK}<span><b>Ecocardiograma de estrés</b> con ejercicio o farmacológico, según el caso</span></li>
      <li>{CHECK}<span><b>Holter EKG de 24 horas</b></span></li>
      <li>{CHECK}<span><b>Monitoreo ambulatorio de presión arterial (MAPA)</b></span></li>
    </ul>
  </div>
</div></section>

<section class="sec space-sec" aria-label="Nuestro consultorio"><div class="wrap space">
  <figure class="reveal">{picture("sala-ecocardiografia", "El Dr. Duarte en su consultorio junto al ecógrafo y la banda de esfuerzo", 1100, 825)}<figcaption>Sala de ecocardiografía y prueba de esfuerzo</figcaption></figure>
  <figure class="reveal">{picture("recepcion", "Recepción del consultorio CARDIODUARTE", 760, 899)}<figcaption>Recepción · Torre Médica Metropolitan Salud</figcaption></figure>
</div></section>

<section class="sec why" id="por-que"><div class="wrap">
  <div class="sec-head">
    <span class="eyebrow">Por qué CARDIODUARTE</span>
    <h2>Atención especializada, sin prisa y con explicaciones claras</h2>
  </div>
  <ul class="why-grid">{razones}</ul>
</div></section>

<section class="sec prev" id="prevencion"><div class="wrap">
  <div class="sec-head">
    <span class="eyebrow">Prevención</span>
    <h2>Pequeños hábitos que cuidan su corazón <span class="tag">Ejemplo · validar con el Dr. Duarte</span></h2>
    <p class="lead">Recomendaciones generales de salud cardiovascular. No reemplazan la valoración médica ni las indicaciones de su médico tratante.</p>
  </div>
  <ul class="prev-grid">{prev}</ul>
  <div class="alarm reveal" role="note">
    <div class="ic">{ic(I["alert"])}</div>
    <div><h3>Señales de alarma: no espere una cita</h3>
    <p>Dolor u opresión en el pecho, falta de aire repentina, desmayo o palpitaciones con malestar requieren atención inmediata. Acuda al servicio de urgencias más cercano o llame al <strong>123</strong>.</p></div>
  </div>
</div></section>

<section class="sec steps-sec" id="como"><div class="wrap">
  <div class="sec-head"><span class="eyebrow">Su cita</span><h2>Agendar una cita es sencillo</h2></div>
  <ol class="steps">
    <li class="reveal"><h3>Escríbanos</h3><p>Por WhatsApp o con el formulario de esta página. Cuéntenos qué necesita y si tiene orden médica.</p></li>
    <li class="reveal"><h3>Confirmamos con usted</h3><p>Le proponemos día y hora, le decimos el valor o la cobertura y le enviamos la preparación del examen.</p></li>
    <li class="reveal"><h3>Le atendemos</h3><p>Llegue 15 minutos antes con su documento y exámenes previos. Sale con su resultado explicado.</p></li>
  </ol>
</div></section>

<section class="sec prep-sec" id="preparacion"><div class="wrap">
  <div class="sec-head">
    <span class="eyebrow">Preparación</span>
    <h2>Cómo prepararse para su examen <span class="tag">Ejemplo · validar con el Dr. Duarte</span></h2>
    <p class="lead">Indicaciones generales. Siga siempre lo que le indique el consultorio al confirmar su cita. No suspenda medicamentos sin orden médica.</p>
  </div>
  <div class="split">
    <div class="prep">{col(PREP[0])}</div>
    <div class="prep">{col(PREP[1])}</div>
  </div>
  <div class="callout reveal">
    <h3>¿Tiene póliza o medicina prepagada?</h3>
    <p>Escríbanos antes de su cita con el nombre de su aseguradora y le confirmamos cómo puede ser atendido. También atendemos pacientes particulares. <span class="tag">Ejemplo · ajustar según convenios</span></p>
  </div>
</div></section>

<section class="sec hab-sec" id="habilitacion"><div class="wrap">
  <div class="sec-head"><span class="eyebrow">Habilitación</span><h2>Servicios habilitados ante el Ministerio de Salud</h2><p class="lead">Puede verificar cada distintivo en el portal de prestadores del Ministerio de Salud.</p></div>
  <div class="hab">
    <div class="seal reveal"><small>Consulta externa</small><h3>302 · Cardiología</h3><span class="code">DHSS0948333</span><small>Apertura: 24 de septiembre de 2026</small></div>
    <div class="seal reveal"><small>Apoyo diagnóstico</small><h3>745 · Imágenes diagnósticas no ionizantes</h3><span class="code">DHSS0948334</span><small>Apertura: 24 de septiembre de 2026</small></div>
    <div class="seal reveal"><small>Prestador</small><h3>Néstor Ricardo Duarte Suárez</h3><span class="code">0500127007</span><small><a href="https://prestadores.minsalud.gov.co/habilitacion/consultadistintivo_dhss.aspx" target="_blank" rel="noopener">Verificar en MinSalud ↗</a></small></div>
  </div>
</div></section>

<section class="sec visit" id="ubicacion"><div class="wrap visit-grid">
  <div class="info">
    <span class="eyebrow">Ubicación y horario</span>
    <h2>Le esperamos en El Poblado</h2>
    <dl>
      <div><dt>Dirección</dt><dd>Torre Médica Metropolitan Salud<br>Calle 33 n.º 43-85, consultorio 1325<br>Avenida El Poblado antes de San Diego, frente a la estación de Metroplús. Medellín.</dd></div>
      <div><dt>Horario</dt><dd>Lunes a viernes, 7:00 a. m. a 5:00 p. m. <span class="tag">Validar</span></dd></div>
      <div><dt>Contacto</dt><dd>WhatsApp y teléfono: <a href="tel:+573187984545"><strong>318 798 4545</strong></a><br>Correo: <a href="mailto:conscardioduarte@gmail.com"><strong>conscardioduarte@gmail.com</strong></a><br>Web: <strong>www.CARDIODUARTE.com</strong></dd></div>
    </dl>
    <div class="mapcard">
      <svg viewBox="0 0 320 120" role="img" aria-label="Esquema de ubicación: Avenida El Poblado, estación de Metroplús y la torre médica">
        <rect x="0" y="0" width="320" height="120" rx="10" fill="var(--surface)"/>
        <rect x="0" y="52" width="320" height="16" fill="var(--line)"/>
        <text x="10" y="47" font-size="10" fill="var(--muted)" font-family="sans-serif">Av. El Poblado</text>
        <rect x="120" y="74" width="60" height="10" rx="3" fill="var(--accent)"/>
        <text x="120" y="98" font-size="10" fill="var(--muted)" font-family="sans-serif">Metroplús</text>
        <rect x="190" y="14" width="44" height="34" rx="4" fill="var(--brand)"/>
        <text x="240" y="30" font-size="10" fill="var(--ink)" font-family="sans-serif" font-weight="600">Torre Médica</text>
        <text x="240" y="42" font-size="10" fill="var(--muted)" font-family="sans-serif">Calle 33 #43-85</text>
      </svg>
      <a class="btn btn-ghost btn-sm" href="https://www.google.com/maps/search/?api=1&amp;query=Calle%2033%20%2343-85%20Medell%C3%ADn" target="_blank" rel="noopener">Abrir en Google Maps ↗</a>
    </div>
  </div>

  <div id="cita">
    <form class="cita" id="form-cita" novalidate>
      <div><span class="eyebrow">Solicitud de cita</span><h2>Déjenos sus datos y le contactamos</h2></div>
      <div class="row2">
        <div class="field"><label for="f-nombre">Nombre completo</label><input id="f-nombre" name="nombre" autocomplete="name" value="María Fernanda Restrepo" aria-describedby="e-nombre"><span class="err" id="e-nombre" aria-live="polite"></span></div>
        <div class="field"><label for="f-tel">Celular</label><input id="f-tel" name="tel" inputmode="tel" autocomplete="tel" value="300 123 4567" aria-describedby="e-tel"><span class="err" id="e-tel" aria-live="polite"></span></div>
      </div>
      <div class="row2">
        <div class="field"><label for="f-servicio">Servicio</label>
          <select id="f-servicio" name="servicio">
            <option>Consulta de cardiología</option><option selected>Ecocardiograma transtorácico</option><option>Ecocardiograma de estrés con ejercicio</option><option>Ecocardiograma de estrés farmacológico</option><option>Electrocardiograma</option><option>Prueba de esfuerzo</option><option>Holter de ritmo</option><option>Monitoreo de presión arterial (MAPA)</option><option>Chequeo Ejecutivo Cardiovascular</option><option>No estoy seguro, necesito orientación</option>
          </select></div>
        <div class="field"><label for="f-cobertura">Forma de atención</label>
          <select id="f-cobertura" name="cobertura"><option>Particular</option><option selected>Medicina prepagada</option><option>Póliza de salud</option><option>No sé</option></select></div>
      </div>
      <div class="field"><label for="f-franja">¿Cuándo le queda mejor?</label>
        <select id="f-franja" name="franja"><option>Mañana (7 a 12)</option><option>Tarde (1 a 5)</option><option>Cualquier horario</option></select></div>
      <div class="field"><label for="f-msg">Mensaje (opcional)</label><textarea id="f-msg" name="msg" rows="3">Tengo orden médica para ecocardiograma.</textarea></div>
      <label class="check" for="f-ok"><input type="checkbox" id="f-ok" name="ok"><span>Autorizo el tratamiento de mis datos personales según la <a href="#politica">política de tratamiento de datos</a>, para gestionar mi cita.</span></label>
      <span class="err" id="e-ok" aria-live="polite"></span>
      <button class="btn btn-primary" type="submit">Enviar solicitud</button>
      <p class="fine">Datos de ejemplo precargados para la demostración. Le respondemos en horario de atención.</p>
      <div class="ok" id="ok" hidden tabindex="-1">
        <b>Recibimos su solicitud, <span id="ok-name"></span>.</b>
        <p>En la web real, esta solicitud llega al consultorio y queda registrada con su origen (web) para el seguimiento. Si prefiere, continúe la conversación por WhatsApp.</p>
        <a class="btn btn-wa btn-sm" id="ok-wa" href="#" target="_blank" rel="noopener">{WA_ICON}Continuar por WhatsApp</a>
      </div>
    </form>
  </div>
</div></section>
</main>

<footer class="foot">{WAVE}<div class="wrap">
  <div class="foot-brand"><i class="mark" aria-hidden="true"></i><span class="word"><b>CARDIO<span>DUARTE</span></b><small>Cardiología y ecocardiografía</small></span></div>
  <div class="cols">
    <div><b>CARDIODUARTE</b>Cardiología y ecocardiografía<br>Dr. Néstor Ricardo Duarte Suárez</div>
    <div><b>Visítenos</b>Calle 33 n.º 43-85, consultorio 1325<br>Torre Médica Metropolitan Salud, Medellín</div>
    <div><b>Contacto</b><a href="tel:+573187984545">318 798 4545</a><br><a href="mailto:conscardioduarte@gmail.com">conscardioduarte@gmail.com</a><br>www.CARDIODUARTE.com</div>
    <nav aria-label="Enlaces del pie"><b>Enlaces</b>{nav}<a href="#cita">Agendar cita</a></nav>
  </div>
  <details id="politica">
    <summary>Política de tratamiento de datos personales <span class="tag">Ejemplo · revisión jurídica</span></summary>
    <div class="policy">
      <p>Néstor Ricardo Duarte Suárez (CARDIODUARTE), como responsable del tratamiento, recoge sus datos personales conforme a la Ley 1581 de 2012 y el Decreto 1377 de 2013 (compilado en el Decreto 1074 de 2015).</p>
      <ul>
        <li><strong>Finalidad:</strong> agendar y confirmar citas, enviarle la preparación de sus exámenes, gestionar autorizaciones con su aseguradora y contactarle sobre su atención.</li>
        <li><strong>Datos sensibles:</strong> la información de salud solo se usa para su atención y se guarda en la historia clínica con la reserva que exige la ley. Usted no está obligado a entregar datos sensibles.</li>
        <li><strong>Sus derechos:</strong> conocer, actualizar, rectificar y suprimir sus datos, revocar la autorización y presentar quejas ante la Superintendencia de Industria y Comercio.</li>
        <li><strong>Cómo ejercerlos:</strong> escriba a conscardioduarte@gmail.com. Respondemos consultas en máximo 10 días hábiles y reclamos en máximo 15 días hábiles.</li>
      </ul>
    </div>
  </details>
  <p class="legal">© 2026 CARDIODUARTE · Prestador habilitado 0500127007 · Esta página no reemplaza la valoración médica. Ante una urgencia, acuda al servicio de urgencias más cercano o llame al 123.</p>
</div></footer>

<a class="wa-float" href="{WA}" target="_blank" rel="noopener" aria-label="Escribir por WhatsApp">{WA_ICON}<span>WhatsApp</span></a>

<script src="../assets/js/sitio.js" defer></script>
</body>
</html>
"""


if __name__ == "__main__":
    for n in OPCIONES:
        d = ROOT / f"opcion-{n}"
        d.mkdir(exist_ok=True)
        (d / "index.html").write_text(page(n), encoding="utf-8")
        print("ok", d / "index.html")
