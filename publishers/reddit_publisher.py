import webbrowser
import urllib.parse

def publicar_en_reddit_multiple(textos):
    for texto, url, idioma, imagen_url in textos:
        titulo = urllib.parse.quote_plus(texto)
        enlace = urllib.parse.quote_plus(url)
        reddit_url = f"https://www.reddit.com/submit?title={titulo}&url={enlace}"
        print(f"🔴 [{idioma}] Compartiendo en Reddit: {texto}")
        webbrowser.open(reddit_url)
