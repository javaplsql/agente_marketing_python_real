import webbrowser
import urllib.parse

def publicar_en_gumroad_multiple(textos):
    for texto, url, idioma, imagen_url in textos:
        share_text = f"{texto}\n{url}"
        encoded = urllib.parse.quote_plus(share_text)
        share_url = f"https://gumroad.com/share?share_key={encoded}"
        print(f"💰 [{idioma}] Compartiendo en Gumroad: {texto}")
        webbrowser.open(share_url)
