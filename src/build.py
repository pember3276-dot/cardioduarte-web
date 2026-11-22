#!/usr/bin/env python3
"""Genera opcion-1/, opcion-2/ y opcion-3/.

- src/datos.py : contenido común (textos, servicios, preguntas, formulario)
- src/p1.py, p2.py, p3.py : estructura de cada propuesta
- assets/css/comun.css + assets/css/opcion-N.css : estilos
Uso: python3 src/build.py
"""
import importlib
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

if __name__ == "__main__":
    for n in (1, 2, 3):
        try:
            mod = importlib.import_module(f"p{n}")
        except ModuleNotFoundError:
            continue
        d = ROOT / f"opcion-{n}"
        d.mkdir(exist_ok=True)
        (d / "index.html").write_text(mod.page(), encoding="utf-8")
        print("ok", d / "index.html")
