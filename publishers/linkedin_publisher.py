# publisher_linkedin.py
import os
import webbrowser
from urllib.parse import quote
from dotenv import load_dotenv

load_dotenv(".env_template_redes.env")

def publicar_en_linkedin():
    url = quote(os.getenv("BOOK_URL_ES"))
    share_url = f"https://www.linkedin.com/sharing/share-offsite/?url={url}"
    print("🔗 Abriendo publicación en LinkedIn:", share_url)
    webbrowser.open(share_url)
