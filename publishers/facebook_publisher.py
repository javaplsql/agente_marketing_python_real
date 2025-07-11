import os
import webbrowser
from dotenv import load_dotenv

load_dotenv(".env_template_redes.env")

def publicar_en_facebook():
    url = os.getenv("BOOK_URL_ES")
    share_url = os.getenv("FACEBOOK_SHARE_URL_TEMPLATE").format(url=url)
    print("\ud83d\udd17 Abriendo Facebook Share:", share_url)
    webbrowser.open(share_url)