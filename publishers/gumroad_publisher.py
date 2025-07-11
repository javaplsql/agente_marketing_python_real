import os
import webbrowser
from dotenv import load_dotenv

load_dotenv(".env_template_redes.env")

def publicar_en_gumroad():
    print("🛒 Abriendo Gumroad para publicación manual...")
    webbrowser.open(os.getenv("GUMROAD_PRODUCT_URL"))