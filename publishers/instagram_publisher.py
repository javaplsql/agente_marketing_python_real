from publishers.chrome_mobile_instagram import abrir_instagram_modo_movil  # o donde lo tengas

def publicar_en_instagram_manual(textos):
    print("📸 Abriendo Instagram en modo móvil (Chrome)...")

    for texto, url, idioma, imagen_url in textos:
        print(f"\n🌍 [{idioma}] Prepara esta publicación:")
        print(f"📝 Texto:\n{texto} {url}")
        print(f"🖼 Imagen sugerida: {imagen_url}")
        abrir_instagram_modo_movil()
