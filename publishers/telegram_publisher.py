import webbrowser
import urllib.parse

def publicar_en_telegram_multiple(textos):
    for texto, url, idioma, imagen_url in textos:
        mensaje = f"{texto}\n{url}"
        tg_url = "https://t.me/share/url?url=" + urllib.parse.quote_plus(url) + "&text=" + urllib.parse.quote_plus(texto)
        print(f"📘 [{idioma}] Compartiendo en Telegram: {texto}")
        webbrowser.open(tg_url)
