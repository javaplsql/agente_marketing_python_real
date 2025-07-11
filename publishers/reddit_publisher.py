import os
import webbrowser
from dotenv import load_dotenv

load_dotenv(".env_template_redes.env")

def publicar_en_reddit():
    print("🔗 Abriendo Reddit para publicación manual...")
    webbrowser.open("https://www.reddit.com/submit")
