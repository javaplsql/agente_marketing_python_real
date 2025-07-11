import os
import requests
from dotenv import load_dotenv

load_dotenv(".env_template_redes.env")

def publicar_en_telegram():
    token = os.getenv("TELEGRAM_BOT_TOKEN")
    chat_id = os.getenv("TELEGRAM_CHAT_ID")
    if not token or not chat_id:
        print("\u26a0\ufe0f Faltan credenciales de Telegram")
        return

    mensaje = (
        "\ud83d\udcd8 Java Course 2025 disponible en Kindle:\n"
        + os.getenv("BOOK_URL_ES")
    )
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    response = requests.post(url, data={"chat_id": chat_id, "text": mensaje})

    if response.ok:
        print("\u2705 Mensaje enviado a Telegram.")
    else:
        print("\u274c Error al enviar mensaje:", response.text)