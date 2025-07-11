README - Agente Marketing Automático Redes Sociales
Descripción
Este proyecto automatiza la publicación de un mensaje promocional con enlace a un libro Amazon KDP en varias redes sociales mediante apertura de navegador con sesión iniciada manualmente.
Ideal para cuentas con acceso limitado API o planes free.

Requisitos
Python 3.8+

Google Chrome con perfil activo y sesión iniciada para trendphonedeal@gmail.com

Paquetes Python: selenium, python-dotenv, tweepy

Archivo .env_template_redes configurado con credenciales y URLs

Instalación
Clona o descarga el repositorio.

Crea un entorno virtual y actívalo:

bash
Copiar
Editar
python -m venv .venv
source .venv/bin/activate  # Linux/Mac
.\.venv\Scripts\activate   # Windows
Instala dependencias:

bash
Copiar
Editar
pip install -r requirements.txt
Renombra .env_template_redes a .env y verifica que contiene:

Credenciales para redes sociales

URLs de producto Amazon KDP

Usuario y contraseña para apertura manual de sesión

Uso
Inicia sesión manual en Chrome con el perfil trendphonedeal@gmail.com antes de ejecutar el script.

Ejecuta el agente:

bash
Copiar
Editar
python main.py
Se abrirán pestañas en Chrome para cada red social con el mensaje y enlace prellenado para publicar.

Notas
Para Twitter API free, se usa OAuth pero con acceso limitado. Por eso se prioriza abrir navegador con sesión iniciada para Facebook, LinkedIn, Mastodon, etc.

Instagram y TikTok requieren publicación manual por restricciones API.

Telegram utiliza bot con token para envío directo.

Estructura
main.py — Lanza todas las publicaciones.

publishers/ — Scripts específicos por red social (twitter, facebook, linkedin, etc).

.env — Variables de entorno con credenciales y URLs.