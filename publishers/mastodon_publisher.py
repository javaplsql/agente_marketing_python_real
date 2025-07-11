import webbrowser
import urllib.parse

def publicar_en_mastodon_multiple(textos):
    for texto, url, idioma, imagen_url in textos:
        status = f"{texto} {url}"
        share_url = "https://mastodon.social/share?text=" + urllib.parse.quote_plus(status)
        print(f"🐘 [{idioma}] Compartiendo en Mastodon: {texto}")
        webbrowser.open(share_url)
