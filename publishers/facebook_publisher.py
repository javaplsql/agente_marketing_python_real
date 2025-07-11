import webbrowser
import urllib.parse

def publicar_en_facebook_multiple(textos):
    for texto, url, idioma, imagen_url in textos:
        share_url = "https://www.facebook.com/sharer/sharer.php?u=" + urllib.parse.quote_plus(url)
        print(f"🔵 [{idioma}] Compartiendo en Facebook: {texto}")
        webbrowser.open(share_url)
