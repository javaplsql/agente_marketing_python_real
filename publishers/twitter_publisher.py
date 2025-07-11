import webbrowser
import urllib.parse

def publicar_en_twitter(texto, enlace):
    print("⚠️ No se puede publicar automáticamente con el plan gratuito de Twitter.")
    print("🔁 Redirigiendo al navegador para publicación manual...")

    texto_completo = f"{texto} {enlace}"
    url_texto = urllib.parse.quote(texto_completo)
    intent_url = f"https://twitter.com/intent/tweet?text={url_texto}"

    print(f"🔗 Abriendo: {intent_url}")
    webbrowser.open(intent_url)
