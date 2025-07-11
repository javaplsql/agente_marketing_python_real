import webbrowser

def publicar_en_tiktok(texto, url, idioma, imagen_url):
    perfil = "https://www.tiktok.com/upload"
    print(f"🎵 [{idioma}] Abriendo subida en TikTok para que añadas: {texto} {url}")
    webbrowser.open(perfil)
