import os
import requests
from dotenv import load_dotenv

load_dotenv(".env_template_redes.env")

def publicar_en_mastodon():
    access_token = os.getenv("MASTODON_ACCESS_TOKEN")
    base_url = os.getenv("MASTODON_API_BASE_URL")
    if not access_token or not base_url:
        print("\u26a0\ufe0f Faltan credenciales de Mastodon")
        return

    mensaje = "\ud83d\udcd8 Aprende Java profesionalmente con 'Java Course 2025':\n" + os.getenv("BOOK_URL_ES")
    response = requests.post(
        f"{base_url}/api/v1/statuses",
        headers={"Authorization": f"Bearer {access_token}"},
        data={"status": mensaje}
    )

    if response.ok:
        print("\u2705 Publicado en Mastodon")
    else:
        print("\u274c Error en Mastodon:", response.text)