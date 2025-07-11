import webbrowser
import urllib.parse
import time

def publicar_en_twitter_multiple_con_idiomas(textos_con_idioma):
    print("🔁 Abriendo tweets prellenados para publicación manual...")

    for texto, url_libro, idioma, imagen_url in textos_con_idioma:
        texto_completo = f"{texto} ({idioma}) {url_libro} {imagen_url}"
        url_texto = urllib.parse.quote(texto_completo)
        intent_url = f"https://twitter.com/intent/tweet?text={url_texto}"

        print(f"🔗 Abriendo: {intent_url}")
        webbrowser.open(intent_url)
        time.sleep(1.5)
import os
import webbrowser
from dotenv import load_dotenv

load_dotenv()

CHROME_PROFILE_PATH = os.path.expanduser("~") + "/.config/google-chrome/Default"  # Ajusta según tu SO
CHROME_USER_DATA_DIR = os.path.expanduser("~") + "/.config/google-chrome"


def publicar_en_twitter(texto, idioma="EN"):
    print("🔍 Usando cuenta de Chrome para Twitter")
    # Prepara URL para abrir tweet prellenado (tweet intent)
    tweet_url = f"https://twitter.com/intent/tweet?text={texto}"

    # Abrir Chrome con perfil ya logado en Twitter
    chrome_path = "google-chrome"  # Cambia según tu sistema: "chrome" o ruta absoluta si es Windows
    command = f'{chrome_path} --profile-directory=Default --new-window "{tweet_url}"'

    print(f"🟦 Abriendo navegador con tweet prellenado: {tweet_url}")
    webbrowser.get(command).open(tweet_url)