import os
import webbrowser
from dotenv import load_dotenv

load_dotenv(".env_template_redes.env")

def publicar_en_blogger():
    print("✍️ Abriendo Blogger para publicación manual...")
    webbrowser.open("https://www.blogger.com")