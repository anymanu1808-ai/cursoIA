# Curso básico de Inteligencia Artificial

Curso web (HTML puro, sin dependencias) con 7 módulos, narración en voz femenina y evaluación final.

## Publicar en GitHub Pages
1. Crea un repositorio y sube estos archivos.
2. *Settings → Pages → Deploy from a branch → main / (root)*.
3. Tu curso quedará en `https://TU-USUARIO.github.io/NOMBRE-REPO/`.

## Voz natural (recomendado)
Por defecto el navegador usa su mejor voz femenina en español. Para una voz neuronal, estable en todos los dispositivos:
```
pip install edge-tts
python generar_audio.py
```
Sube la carpeta `audio/` generada: el curso usa los `.mp3` automáticamente.

## Evaluación
- 10 preguntas; se aprueba con más de 80 % (9 o más aciertos).
- 3 intentos de evaluación. Por pregunta: 3 oportunidades; a la tercera falla se muestra la respuesta y continúa.
- Constantes `PASS`, `MAX_EXAM`, `MAX_Q` al inicio del script en `index.html`.
- El progreso se guarda en `localStorage` (es del navegador: se puede borrar; no es un control antifraude).
