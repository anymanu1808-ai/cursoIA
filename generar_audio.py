"""Genera audio/modulo-N.mp3 con una voz femenina neuronal (no robótica).
Uso:  pip install edge-tts   &&   python generar_audio.py
Voz: es-MX-DaliaNeural (neutra latinoamericana). Alternativas: es-CO-SalomeNeural, es-ES-ElviraNeural."""
import asyncio, re, json, edge_tts
VOZ = "es-MX-DaliaNeural"
html = open("index.html", encoding="utf-8").read()
mods = re.findall(r'\{t:"[^"]*",s:"[^"]*",\s*n:"((?:[^"\\]|\\.)*)"', html)
async def main():
    for i, texto in enumerate(mods, 1):
        await edge_tts.Communicate(texto, VOZ, rate="-5%").save(f"audio/modulo-{i}.mp3")
        print("listo", i)
asyncio.run(main())
