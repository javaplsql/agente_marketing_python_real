# publishers/twitter_publisher.py
import webbrowser
import urllib.parse
import time

def publicar_en_twitter_multiple_con_idiomas(textos_con_idioma):
    print("🔁 Abriendo tweets prellenados para publicación manual...")

    for texto, url_libro, idioma, imagen_url in textos_con_idioma:
        texto_completo = f"{texto} ({idioma}) {url_libro} {imagen_url}"
        url_texto = urllib.parse.quote(texto_completo)
        intent_url = f"https://twitter.com/intent/tweet?text={url_texto}"

        print(f"🔗 Abriendo: {intent_url}")
        webbrowser.open(intent_url)
        time.sleep(1.5)
