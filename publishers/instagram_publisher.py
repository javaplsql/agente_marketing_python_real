import os
from dotenv import load_dotenv

load_dotenv(".env_template_redes.env")

def instrucciones_para_instagram():
    print("\ud83d\udcf8 Abre Instagram y publica manualmente con este mensaje:")
    print("Caption sugerido:")
    print("Learn Java professionally in 2025! \ud83d\udcd8 Kindle Edition now on Amazon.")
    print("Link: " + os.getenv("BOOK_URL_ES"))
    print("Imagen: " + os.getenv("JAVA_IMAGE_URL"))

# publisher_linkedin.py
import os
import webbrowser
from urllib.parse import quote
from dotenv import load_dotenv

load_dotenv(".env_template_redes.env")

def publicar_en_linkedin():
    url = quote(os.getenv("BOOK_URL_ES"))
    share_url = f"https://www.linkedin.com/sharing/share-offsite/?url={url}"
    print("\ud83d\udd17 Abriendo publicación en LinkedIn:", share_url)
    webbrowser.open(share_url)