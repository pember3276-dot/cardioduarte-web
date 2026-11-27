"""Contenido común de CARDIODUARTE (una sola fuente para las tres propuestas).

Todo lo que aquí aparece sale de la web anterior, del portafolio y de los
distintivos de habilitación. Lo que falta validar va marcado con tag("...").
"""

WA_NUM = "573187984545"
WA = f"https://wa.me/{WA_NUM}?text=Hola%2C%20quisiera%20informaci%C3%B3n%20para%20una%20cita%20en%20CARDIODUARTE"
TEL = "318 798 4545"
MAIL = "conscardioduarte@gmail.com"
WEB = "www.CARDIODUARTE.com"
DIR1 = "Torre Médica Metropolitan Salud"
DIR2 = "Calle 33 n.º 43-85, consultorio 1325"
DIR3 = "Avenida El Poblado antes de San Diego, frente a la estación de Metroplús. Medellín."
# Cómo llegar: MAPS abre la ficha de Google "CARDIODUARTE" (enlace estable por CID).
LAT, LNG = 6.2338043, -75.5699073
_Q = "Torre%20M%C3%A9dica%20Metropolitan%20Salud%2C%20Calle%2033%20%2343-85%2C%20Medell%C3%ADn"
MAPS = "https://maps.google.com/?cid=16402717702183196358"
MAPS_EMBED = f"https://www.google.com/maps?q={_Q}&amp;output=embed&amp;hl=es"
WAZE = f"https://waze.com/ul?ll={LAT},{LNG}&amp;navigate=yes"
LINKEDIN = "https://www.linkedin.com/in/n%C3%A9stor-ricardo-duarte-suarez-62421959/"
MINSALUD = "https://prestadores.minsalud.gov.co/habilitacion/consultadistintivo_dhss.aspx"
DOCTOR = "Dr. Néstor Ricardo Duarte Suárez"
H1 = "Cuidamos su corazón con tiempo, cercanía y un diagnóstico claro."
LEAD = ("En CARDIODUARTE le atiende directamente el especialista. Le explicamos cada examen antes de hacerlo, "
        "resolvemos sus dudas con calma y le entregamos resultados que usted pueda entender.")
BIO = ("Cardiólogo y ecocardiografista con más de 15 años de trayectoria en el diagnóstico y el tratamiento de "
       "enfermedades del corazón. Ha liderado servicios de cardiología y hoy atiende en Medellín a pacientes que "
       "buscan una valoración cuidadosa y cercana.")
QUOTE = "Cada paciente merece entender qué tiene su corazón y qué podemos hacer juntos."


# Modo de generación. Las propuestas (demo) usan R="../" y PROD=False.
# La web publicada (src/sitio.py) cambia estos valores antes de generar cada página.
R = "../"          # prefijo hasta la raíz del sitio
PROD = False       # True: web real (sin barra demo, sin marcas "Ejemplo", formulario vacío)
SITE = "https://www.cardioduarte.com"   # dirección oficial (Hostinger); canonical, sitemap y URLs absolutas
INDEXABLE = True   # False en la copia de muestra de GitHub Pages (noindex para no duplicar contenido)
GTM_ID = "GTM-MGXBRJTH"        # ID de Google Tag Manager (GTM-XXXXXXX) cuando esté disponible
META = {}          # título, descripción, ruta canónica y JSON-LD de la página en curso


def tag(t="Ejemplo"):
    if PROD:
        return ""
    return f'<span class="tag">{t}</span>'


def ic(path, size=24, sw=1.7):
    return (f'<svg width="{size}" height="{size}" viewBox="0 0 24 24" fill="none" stroke="currentColor" '
            f'stroke-width="{sw}" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{I.get(path, path)}</svg>')


I = {
    "heart": '<path d="M12 20s-7-4.4-7-10a4 4 0 0 1 7-2.6A4 4 0 0 1 19 10c0 5.6-7 10-7 10Z"/>',
    "heartecg": '<path d="M12 20s-7-4.4-7-10a4 4 0 0 1 7-2.6A4 4 0 0 1 19 10c0 5.6-7 10-7 10Z"/><path d="M6 11h3l1.5-2.5 2 5 1.5-2.5H18"/>',
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
    "plus": '<path d="M12 5v14M5 12h14"/>',
    "minus": '<path d="M5 12h14"/>',
    "arrow": '<path d="M7 17 17 7M8 7h9v9"/>',
    "cal": '<rect x="3" y="5" width="18" height="16" rx="3"/><path d="M3 10h18M8 3v4M16 3v4"/><path d="M8 14h3v3H8z"/>',
    "star": '<path d="M12 3v18M4.2 7.5l15.6 9M4.2 16.5l15.6-9"/>',
    "phone": '<path d="M5 4h4l2 5-2.5 1.5a11 11 0 0 0 5 5L15 13l5 2v4a2 2 0 0 1-2 2A16 16 0 0 1 3 6a2 2 0 0 1 2-2Z"/>',
    "clock": '<circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/>',
    "mail": '<rect x="3" y="5" width="18" height="14" rx="2"/><path d="m3 7 9 6 9-6"/>',
    "check": '<path d="M5 12.5l4.5 4.5L19 7.5"/>',
    "cap": '<path d="M2 9l10-5 10 5-10 5L2 9Z"/><path d="M6 11v5c3 2.5 9 2.5 12 0v-5"/>',
    "id": '<rect x="3" y="5" width="18" height="14" rx="2"/><circle cx="9" cy="12" r="2.5"/><path d="M14 10h4M14 14h3"/>',
    "clip": '<rect x="5" y="4" width="14" height="17" rx="2"/><path d="M9 4V3h6v1M9 10h6M9 14h4"/>',
    "kit": '<rect x="3" y="7" width="18" height="13" rx="2"/><path d="M9 7V5h6v2M12 11v5M9.5 13.5h5"/>',
    "chat": '<path d="M4 5h16v11H9l-5 4V5Z"/><path d="M8 10h8M8 13h5"/>',
    "doc": '<path d="M6 3h9l4 4v14H6z"/><path d="M14 3v5h5M9 13h7M9 17h5"/>',
}

WA_ICON = ('<svg width="20" height="20" viewBox="0 0 24 24" aria-hidden="true" fill="currentColor"><path d="M12 2a10 10 0 0 0-8.6 15.1L2 22l5-1.3A10 10 0 1 0 12 2Zm0 18.2a8.2 8.2 0 0 1-4.2-1.2l-.3-.2-3 .8.8-2.9-.2-.3A8.2 8.2 0 1 1 12 20.2Zm4.5-6.1c-.2-.1-1.5-.7-1.7-.8s-.4-.1-.6.1-.7.8-.8 1-.3.2-.5.1a6.7 6.7 0 0 1-3.3-2.9c-.2-.4.2-.4.7-1.3.1-.2 0-.3 0-.4l-.8-1.8c-.2-.5-.4-.4-.6-.4h-.5a1 1 0 0 0-.7.3 3 3 0 0 0-.9 2.2 5.2 5.2 0 0 0 1.1 2.8 11.9 11.9 0 0 0 4.6 4c1.7.7 2.3.8 3.2.7a2.7 2.7 0 0 0 1.8-1.3 2.2 2.2 0 0 0 .2-1.3c-.1-.1-.2-.2-.4-.3Z"/></svg>')

# (icono, título, descripción, útil si, foto o None)
SERVICIOS = [
    ("heart", "Consulta de cardiología",
     "Valoración del especialista para síntomas como dolor en el pecho, palpitaciones, presión alta o cansancio, y control de enfermedades del corazón.",
     "tiene síntomas, antecedentes familiares o le remitieron.", "v-consulta"),
    ("echo", "Ecocardiograma transtorácico",
     "Ultrasonido que muestra en tiempo real la forma y el funcionamiento del corazón y sus válvulas. No duele y no usa radiación.",
     "le encontraron un soplo o necesita evaluar la fuerza del corazón.", "v-ecografo"),
    ("run", "Ecocardiograma de estrés con ejercicio",
     "Ecocardiograma antes y después de caminar en banda, para ver cómo responde el corazón al esfuerzo.",
     "se busca descartar enfermedad de las arterias del corazón.", "sala-ecocardiografia"),
    ("pill", "Ecocardiograma de estrés farmacológico",
     "Para quien no puede hacer ejercicio: un medicamento simula el esfuerzo bajo vigilancia continua del especialista.",
     "tiene limitaciones para caminar o correr.", None),
    ("ecg", "Electrocardiograma",
     "Registro de la actividad eléctrica del corazón en pocos minutos. Detecta alteraciones del ritmo y de la conducción.",
     "necesita un chequeo o un requisito prequirúrgico.", "v-cuadros"),
    ("bars", "Prueba de esfuerzo",
     "Electrocardiograma mientras camina en banda, con aumento gradual de la intensidad. Mide su capacidad física y la respuesta del corazón.",
     "va a iniciar deporte o tiene dolor con el esfuerzo.", "v-esfuerzo"),
    ("holter", "Holter de ritmo (24 a 48 h)",
     "Un pequeño equipo registra el ritmo del corazón mientras usted sigue su vida normal.",
     "siente palpitaciones, mareos o ha tenido desmayos.", None),
    ("gauge", "Monitoreo de presión arterial (MAPA)",
     "Mide la presión durante 24 horas en su entorno habitual, para un diagnóstico preciso de la hipertensión.",
     "sus cifras varían mucho o se le sube la presión en consulta.", None),
]

CHEQUEO = [
    ("Consulta especializada de cardiología", "Valoración completa con el especialista."),
    ("Ecocardiograma de estrés", "Con ejercicio o farmacológico, según el caso."),
    ("Holter EKG de 24 horas", "Registro continuo del ritmo del corazón."),
    ("Monitoreo ambulatorio de presión arterial (MAPA)", "La presión durante 24 horas en su rutina."),
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
ALARMA = ("Dolor u opresión en el pecho, falta de aire repentina, desmayo o palpitaciones con malestar requieren "
          "atención inmediata. Acuda al servicio de urgencias más cercano o llame al <strong>123</strong>.")

# Agenda en línea: Doctoralia es la agenda maestra para reservas desde la web para evitar que se crucen citas.
# DOCTORALIA_WIDGET: pegar aquí el código del widget de reserva que da Doctoralia Pro (cuenta del consultorio);
# mientras esté vacío, la web muestra solo el botón al perfil.
DOCTORALIA = "https://www.doctoralia.co/perfil/nestor-ricardo-duarte-suarez"
DOCTORALIA_WIDGET = ""

PASOS = [
    ("Reserve o escríbanos", "Elija día y hora en la agenda en línea, o escríbanos por WhatsApp o con el formulario. Cuéntenos qué necesita y si tiene orden médica."),
    ("Confirmamos con usted", "Le proponemos día y hora, le decimos el valor o la cobertura y le enviamos la preparación del examen."),
    ("Prepárese", "Siga las indicaciones de su examen. Si tiene dudas, escríbanos antes de la cita."),
    ("Le atendemos", "Llegue 15 minutos antes con su documento y exámenes previos. Sale con su resultado explicado."),
]

PREP = [
    ("echo", "Ecocardiograma transtorácico", ["No requiere ayuno.", "Tome sus medicamentos como de costumbre.", "Use ropa cómoda de dos piezas.", "Duración aproximada: 30 a 40 minutos."]),
    ("run", "Ecocardiograma de estrés y prueba de esfuerzo", ["Comida liviana 2 a 3 horas antes.", "Ropa deportiva y tenis.", "Pregunte si debe suspender algún medicamento para el corazón antes del examen.", "Venga acompañado si es estrés farmacológico."]),
    ("ecg", "Electrocardiograma", ["No aplique cremas ni aceites en el pecho ese día.", "Dura unos 10 minutos."]),
    ("holter", "Holter de ritmo", ["Báñese antes de la cita: el equipo no se puede mojar.", "Haga su vida normal y anote en el diario sus síntomas y la hora.", "Regrese al día siguiente (o a las 48 horas) para retirarlo."]),
    ("gauge", "Monitoreo de presión arterial (MAPA)", ["Use una camisa de manga holgada.", "Mantenga el brazo quieto y estirado cada vez que el brazalete infle.", "Anote horas de sueño, comidas y medicamentos."]),
    ("clip", "Qué traer a toda cita", ["Documento de identidad.", "Orden médica y autorización, si su póliza o prepagada la exige.", "Exámenes y lista de medicamentos actuales."]),
]

FAQ = [
    ("¿Cómo pido una cita?", "Puede reservar en línea en la agenda del Dr. Duarte en Doctoralia, escribirnos por WhatsApp al 318 798 4545 o dejar sus datos en el formulario de esta página. Si nos escribe, le proponemos día y hora y le enviamos la preparación del examen."),
    ("¿Atienden pólizas y medicina prepagada?", f"Atendemos pacientes particulares, con póliza o con medicina prepagada, según la cobertura. Escríbanos con el nombre de su aseguradora y le confirmamos cómo puede ser atendido. {tag('Ejemplo · ajustar según convenios')}"),
    ("¿Qué debo llevar el día de la cita?", "Documento de identidad, la orden médica y la autorización si su póliza o prepagada la exige, y sus exámenes y la lista de medicamentos actuales."),
    ("¿Necesito orden médica?", "Para la consulta particular no. Para exámenes cubiertos por su aseguradora, normalmente sí: confírmelo con su póliza o prepagada antes de la cita."),
    ("¿Dónde están ubicados?", f"{DIR1}, {DIR2}. {DIR3}"),
    ("¿Cuál es el horario de atención?", f"Lunes a viernes, de 7:00 a. m. a 5:00 p. m. {tag('Validar')}"),
]

CRED = [
    ("Especialidad", "Cardiología · Ecocardiografía"),
    ("Formación", f"Universidad y año de cada título {tag('Por completar')}"),
    ("Registro médico", f"N.º de registro (ReTHUS) {tag('Por completar')}"),
    ("Experiencia", "Más de 15 años; jefatura de servicio de cardiología"),
    ("Atiende", "Adultos · Pacientes particulares, con póliza o medicina prepagada (según cobertura)"),
]

HAB = [
    ("Consulta externa", "302 · Cardiología", "DHSS0948333", "dist-cardiologia"),
    ("Apoyo diagnóstico", "745 · Imágenes diagnósticas no ionizantes", "DHSS0948334", "dist-imagenes"),
]

# Micrositios de la web publicada: título del servicio -> ruta
SLUG = {
    "Consulta de cardiología": "cardiologo-medellin",
    "Ecocardiograma transtorácico": "ecocardiograma-medellin",
    "Ecocardiograma de estrés con ejercicio": "ecocardiograma-estres-ejercicio-medellin",
    "Ecocardiograma de estrés farmacológico": "ecocardiograma-estres-farmacologico-medellin",
    "Electrocardiograma": "electrocardiograma-medellin",
    "Prueba de esfuerzo": "prueba-de-esfuerzo-medellin",
    "Holter de ritmo (24 a 48 h)": "holter-medellin",
    "Monitoreo de presión arterial (MAPA)": "mapa-presion-arterial-medellin",
    "Chequeo Ejecutivo Cardiovascular": "chequeo-ejecutivo-cardiovascular-medellin",
}
DOC_SLUG = "dr-nestor-ricardo-duarte-suarez"


def slink(t, inner=None):
    """En la web publicada, enlaza el nombre del servicio a su micrositio."""
    inner = inner or t
    return f'<a class="slink" href="{R}{SLUG[t]}/">{inner}</a>' if PROD and t in SLUG else inner


NAV = [("#doctor", "El doctor"), ("#servicios", "Servicios"), ("#prevencion", "Prevención"),
       ("#preparacion", "Preparación"), ("#ubicacion", "Ubicación")]

POLITICA = f"""<p>Néstor Ricardo Duarte Suárez (CARDIODUARTE), como responsable del tratamiento, recoge sus datos personales conforme a la Ley 1581 de 2012 y el Decreto 1377 de 2013 (compilado en el Decreto 1074 de 2015).</p>
      <ul>
        <li><strong>Finalidad:</strong> agendar y confirmar citas, enviarle la preparación de sus exámenes, gestionar autorizaciones con su aseguradora y contactarle sobre su atención.</li>
        <li><strong>Datos sensibles:</strong> la información de salud solo se usa para su atención y se guarda en la historia clínica con la reserva que exige la ley. Usted no está obligado a entregar datos sensibles.</li>
        <li><strong>Sus derechos:</strong> conocer, actualizar, rectificar y suprimir sus datos, revocar la autorización y presentar quejas ante la Superintendencia de Industria y Comercio.</li>
        <li><strong>Cómo ejercerlos:</strong> escriba a {MAIL}. Respondemos consultas en máximo 10 días hábiles y reclamos en máximo 15 días hábiles.</li>
      </ul>"""

LEGAL = ("© 2026 CARDIODUARTE · Prestador habilitado 0500127007 · Esta página no reemplaza la valoración médica. "
         "Ante una urgencia, acuda al servicio de urgencias más cercano o llame al 123.")

OPCIONES = {1: "Clínica moderna y profesional", 2: "Elegante y premium", 3: "Cercana y enfocada en el bienestar"}


def pic(name, alt, cls="", eager=False, pos=None):
    load = 'fetchpriority="high"' if eager else 'loading="lazy" decoding="async"'
    st = f' style="object-position:{pos}"' if pos else ""
    c = f' class="{cls}"' if cls else ""
    return (f'<picture{c}><source srcset="{R}assets/img/{name}.webp" type="image/webp">'
            f'<img src="{R}assets/img/{name}.jpg" alt="{alt}" {load}{st}></picture>')


ALT = {
    "v-consulta": "El Dr. Duarte en su escritorio del consultorio",
    "v-ecografo": "Ecógrafo del consultorio CARDIODUARTE",
    "sala-ecocardiografia": "El Dr. Duarte junto al ecógrafo y la banda de esfuerzo",
    "v-cuadros": "Láminas del corazón en el consultorio",
    "v-esfuerzo": "Sala de prueba de esfuerzo con banda caminadora",
    "v-letrero": "Letrero de CARDIODUARTE en la recepción",
    "recepcion": "Recepción del consultorio CARDIODUARTE",
    "v-recep2": "Recepción de CARDIODUARTE",
    "v-torre": "Entrada de la Torre Médica Metropolitan Salud, Calle 33 n.º 43-85",
    "dr-duarte": "Dr. Néstor Ricardo Duarte Suárez, cardiólogo, con bata blanca",
    "logo-oscuro": "Logotipo de CARDIODUARTE",
}


def demo_bar(n):
    links = " ".join(
        f'<a href="../opcion-{k}/index.html"{" aria-current=" + chr(34) + "page" + chr(34) if k == n else ""}>{k}</a>'
        for k in OPCIONES) + ' <a href="../opcion-a/index.html">4</a>'
    return (f'<div class="demo"><div class="demo-in"><span><strong>Opción {n} · {OPCIONES[n]}.</strong>'
            f'<span class="demo-txt"> Versión demo: lo marcado {tag()} se valida con el consultorio.</span></span>'
            f'<nav class="demo-nav" aria-label="Cambiar de propuesta">Ver opción {links} <a href="../propuestas/">Todas</a></nav></div></div>')


def head(n, fonts, color):
    if PROD:
        return head_prod(n, fonts, color)
    return f"""<!doctype html>
<html lang="es" class="t{n}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<meta name="robots" content="noindex, nofollow">
<title>CARDIODUARTE · Cardiología y ecocardiografía en Medellín (opción {n})</title>
<meta name="description" content="CARDIODUARTE: consulta de cardiología, ecocardiograma, ecocardiograma de estrés, prueba de esfuerzo, Holter y MAPA con el Dr. Néstor Ricardo Duarte Suárez en El Poblado, Medellín.">
<meta name="theme-color" content="{color}">
<link rel="icon" href="../assets/img/logo-corazon.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?{fonts}&display=swap">
<link rel="stylesheet" href="../assets/css/comun.css">
<link rel="stylesheet" href="../assets/css/opcion-{n}.css">
<script type="application/ld+json">{{"@context":"https://schema.org","@type":"MedicalClinic","name":"CARDIODUARTE","medicalSpecialty":"Cardiovascular","url":"https://www.cardioduarte.com","telephone":"+57 318 798 4545","email":"{MAIL}","address":{{"@type":"PostalAddress","streetAddress":"{DIR2}, {DIR1}","addressLocality":"Medellín","addressCountry":"CO"}}}}</script>
</head>
<body>
<a class="skip" href="#contenido">Saltar al contenido</a>
{demo_bar(n)}
"""


def form(btn_class="btn btn-primary", btn_extra="", sel=None):
    sel = sel or (None if PROD else SERVICIOS[1][1])
    opts = "".join(f"<option{' selected' if s[1] == sel else ''}>{s[1]}</option>" for s in SERVICIOS)
    extra = "".join(f"<option{' selected' if o == sel else ''}>{o}</option>" for o in ("Chequeo Ejecutivo Cardiovascular", "No estoy seguro, necesito orientación"))
    v = (lambda x: "") if PROD else (lambda x: f' value="{x}"')
    msg = "" if PROD else "Tengo orden médica para ecocardiograma."
    fine = ("Le respondemos en horario de atención." if PROD
            else "Datos de ejemplo precargados para la demostración. Le respondemos en horario de atención.")
    okp = ("Para terminar, envíe su solicitud por WhatsApp: el mensaje ya va escrito con sus datos y llega directo al consultorio." if PROD
           else "En la web real, esta solicitud llega al consultorio y queda registrada con su origen (web) para el seguimiento. Si prefiere, continúe la conversación por WhatsApp.")
    okb = "Ya casi" if PROD else "Recibimos su solicitud"
    cob = "" if PROD else " selected"
    return f"""<form class="cita" id="form-cita" novalidate>
      <div class="row2">
        <div class="field"><label for="f-nombre">Nombre completo</label><input id="f-nombre" name="nombre" autocomplete="name" {v("María Fernanda Restrepo")} aria-describedby="e-nombre"><span class="err" id="e-nombre" aria-live="polite"></span></div>
        <div class="field"><label for="f-tel">Celular</label><input id="f-tel" name="tel" inputmode="tel" autocomplete="tel" {v("300 123 4567")} placeholder="300 123 4567" aria-describedby="e-tel"><span class="err" id="e-tel" aria-live="polite"></span></div>
      </div>
      <div class="row2">
        <div class="field"><label for="f-servicio">Servicio</label>
          <select id="f-servicio" name="servicio">{opts}{extra}</select></div>
        <div class="field"><label for="f-cobertura">Forma de atención</label>
          <select id="f-cobertura" name="cobertura"><option>Particular</option><option{cob}>Medicina prepagada</option><option>Póliza de salud</option><option>No sé</option></select></div>
      </div>
      <div class="field"><label for="f-franja">¿Cuándo le queda mejor?</label>
        <select id="f-franja" name="franja"><option>Mañana (7 a 12)</option><option>Tarde (1 a 5)</option><option>Cualquier horario</option></select></div>
      <div class="field"><label for="f-msg">Mensaje (opcional)</label><textarea id="f-msg" name="msg" rows="3">{msg}</textarea></div>
      <label class="check" for="f-ok"><input type="checkbox" id="f-ok" name="ok"><span>Autorizo el tratamiento de mis datos personales según la <a href="#politica">política de tratamiento de datos</a>, para gestionar mi cita.</span></label>
      <span class="err" id="e-ok" aria-live="polite"></span>
      <button class="{btn_class}" type="submit">Enviar solicitud{btn_extra}</button>
      <p class="fine">{fine}</p>
      <div class="ok" id="ok" hidden tabindex="-1">
        <b>{okb}, <span id="ok-name"></span>.</b>
        <p>{okp}</p>
        <a class="btn btn-wa" id="ok-wa" href="#" target="_blank" rel="noopener">{WA_ICON}{"Enviar por WhatsApp" if PROD else "Continuar por WhatsApp"}</a>
      </div>
    </form>"""


def menu_btn():
    return ('<button class="menu-btn" type="button" aria-expanded="false" aria-controls="mnav" aria-label="Abrir menú">'
            '<svg width="20" height="20" viewBox="0 0 20 20" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" aria-hidden="true"><path d="M3 6h14M3 10h14M3 14h14"/></svg></button>')


def mnav():
    return '<nav class="mnav" id="mnav" aria-label="Menú móvil" hidden>' + "".join(
        f'<a href="{nav_href(h)}">{t}</a>' for h, t in NAV) + '<a href="#cita" class="mnav-cta">Agendar cita</a></nav>'


def tail():
    return f"""<a class="wa-float" href="{WA}" target="_blank" rel="noopener" aria-label="Escribir por WhatsApp">{WA_ICON}<span>WhatsApp</span></a>
<script src="{R}assets/js/sitio.js" defer></script>
</body>
</html>
"""


def politica_details():
    return f"""<details id="politica" class="politica">
    <summary>Política de tratamiento de datos personales {tag('Ejemplo · revisión jurídica')}</summary>
    <div class="policy">{POLITICA}</div>
  </details>"""


def nav_href(h):
    """Enlaces del menú: anclas en la portada; desde un micrositio, vuelven a la portada."""
    return R + h if PROD and R else h


def head_prod(n, fonts, color):
    """<head> de la web publicada: SEO, Open Graph, datos estructurados y Tag Manager."""
    import json
    m = META
    url = f"{SITE}/{m.get('path', '')}"
    ld = json.dumps(m.get("ld", {}), ensure_ascii=False, separators=(",", ":"))
    gtm = ""
    gtm_body = ""
    if GTM_ID and INDEXABLE:   # la copia de muestra no mide, para no ensuciar Analytics
        gtm = ("<script>(function(w,d,s,l,i){w[l]=w[l]||[];w[l].push({'gtm.start':new Date().getTime(),event:'gtm.js'});"
               "var f=d.getElementsByTagName(s)[0],j=d.createElement(s),dl=l!='dataLayer'?'&l='+l:'';j.async=true;"
               f"j.src='https://www.googletagmanager.com/gtm.js?id='+i+dl;f.parentNode.insertBefore(j,f);}})(window,document,'script','dataLayer','{GTM_ID}');</script>")
        gtm_body = (f'<noscript><iframe src="https://www.googletagmanager.com/ns.html?id={GTM_ID}" height="0" width="0" '
                    'style="display:none;visibility:hidden"></iframe></noscript>')
    return f"""<!doctype html>
<html lang="es-CO" class="t{n}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
{gtm}
<title>{m['title']}</title>
<meta name="description" content="{m['desc']}">
<meta name="robots" content="{'index, follow, max-image-preview:large' if INDEXABLE else 'noindex, nofollow'}">
<link rel="canonical" href="{url}">
<meta name="theme-color" content="{color}">
<meta property="og:type" content="website">
<meta property="og:locale" content="es_CO">
<meta property="og:site_name" content="CARDIODUARTE">
<meta property="og:title" content="{m['title']}">
<meta property="og:description" content="{m['desc']}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{SITE}/assets/img/{m.get('img', 'dr-duarte')}.jpg">
<meta name="twitter:card" content="summary_large_image">
<meta name="geo.region" content="CO-ANT">
<meta name="geo.placename" content="Medellín">
<link rel="icon" href="{R}assets/img/logo-corazon.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?{fonts}&display=swap">
<link rel="stylesheet" href="{R}assets/css/comun.css">
<link rel="stylesheet" href="{R}assets/css/opcion-{n}.css">
<script type="application/ld+json">{ld}</script>
</head>
<body>
{gtm_body}
<a class="skip" href="#contenido">Saltar al contenido</a>
"""


def dir_link(texto):
    """La dirección siempre lleva a Google Maps."""
    return f'<a class="addr-link" href="{MAPS}" target="_blank" rel="noopener" title="Abrir en Google Maps">{texto}</a>'


def como_llegar():
    return (f'<span class="llegar"><a href="{MAPS}" target="_blank" rel="noopener">{ic("pin", 14, 2)}Google Maps</a>'
            f'<a href="{WAZE}" target="_blank" rel="noopener">{ic("arrow", 14, 2)}Waze</a></span>')


def mapa():
    return (f'<figure class="mapa"><iframe src="{MAPS_EMBED}" title="Mapa: {DIR1}, {DIR2}, Medellín" loading="lazy" '
            f'referrerpolicy="no-referrer-when-downgrade" allowfullscreen></iframe>'
            f'<a class="btn btn-white" href="{MAPS}" target="_blank" rel="noopener"><span>Cómo llegar</span><i>{ic("arrow", 14, 2.2)}</i></a></figure>')


def linkedin_link(cls="li-link"):
    if not LINKEDIN:
        return ""
    return (f'<a class="{cls}" href="{LINKEDIN}" target="_blank" rel="noopener me">'
            '<svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M4.98 3.5a2.5 2.5 0 1 1 0 5 2.5 2.5 0 0 1 0-5ZM3 9h4v12H3zM9 9h3.8v1.7h.1c.5-1 1.8-2 3.8-2 4 0 4.8 2.6 4.8 6V21h-4v-5.6c0-1.3 0-3-1.9-3s-2.1 1.4-2.1 2.9V21H9z"/></svg>'
            'LinkedIn del Dr. Duarte</a>')
