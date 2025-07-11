import webbrowser

def publicar_en_linkedin_multiple(textos):
    for texto, url, idioma, imagen_url in textos:
        texto_formateado = f"{texto}\n🔗 {url}"
        share_url = f"https://www.linkedin.com/sharing/share-offsite/?url={url}"
        print(f"🟦 [{idioma}] Compartiendo en LinkedIn: {texto_formateado}")
        webbrowser.open(share_url)
