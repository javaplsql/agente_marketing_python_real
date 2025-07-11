import subprocess
import os


def abrir_instagram_modo_movil():
    # Ruta predeterminada de Chrome en Windows
    chrome_path = "C:/Program Files/Google/Chrome/Application/chrome.exe"

    if not os.path.exists(chrome_path):
        # Si estás en Windows 64 bits y Chrome está instalado para un solo usuario
        chrome_path = os.path.expandvars(r"%LOCALAPPDATA%\Google\Chrome\Application\chrome.exe")

    # URL de Instagram
    url = "https://www.instagram.com/"

    # User-agent móvil real de iPhone
    user_agent = '--user-agent=Mozilla/5.0 (iPhone; CPU iPhone OS 13_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Mobile/15E148 Safari/604.1'

    # Abrir Chrome en modo ventana pequeña y sin perfil (como móvil)
    subprocess.Popen([
        chrome_path,
        url,
        "--new-window",
        "--window-size=400,800",
        user_agent
    ])
