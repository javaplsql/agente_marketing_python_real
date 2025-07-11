# env_config.py

# ========================
# URLs y mensajes del libro
# ========================
# URL de la imagen del producto en Amazon.
# Usaremos esta imagen para adjuntar a los tweets.
JAVA_IMAGE_URL = "https://m.media-amazon.com/images/I/61zl7bwTQwL._SY425_.jpg"

# Mensajes para los tweets, organizados por idioma.
MENSAJES_POR_IDIOMA = {
    "es": "📘 *Curso de Java 2025*\n🧑‍💻 Programación Java en entornos profesionales\n📚 Edición en español",
    "fr": "📘 *Cours Java 2025*\n🧑‍💻 Programmation Java en environnements professionnels\n📚 Édition française",
    "de": "📘 *Java-Kurs 2025*\n🧑‍💻 Java-Programmierung in professionellen Umgebungen\n📚 Deutsche Ausgabe",
    "it": "📘 *Corso Java 2025*\n🧑‍💻 Programmazione Java in ambienti professionali\n📚 Edizione italiana",
    "in": "📘 *Java कोर्स 2025*\n🧑‍💻 व्यावसायिक वातावरण में जावा प्रोग्रामिंग\n📚 हिंदी संस्करण",
    "co.uk": "📘 *Java course 2025*\n🧑‍💻 Java programming in professional environments\n📚 English Edition"
}

# URLs de Amazon del libro, organizadas por idioma.
URLS_LIBRO = {
    "es": "https://www.amazon.es/dp/B0F9YVY37X",
    "fr": "https://www.amazon.fr/dp/B0F9YVY37X",
    "de": "https://www.amazon.de/dp/B0F9YVY37X",
    "it": "https://www.amazon.it/dp/B0F9YVY37X",
    "in": "https://www.amazon.in/dp/B0F9YVY37X",
    "co.uk": "https://www.amazon.co.uk/dp/B0F9YVY37X"
}

# Las siguientes credenciales no se usarán directamente en el script de Selenium
# porque el script se basará en la sesión ya iniciada en tu perfil de Chrome.
# Sin embargo, las mantengo aquí por si las necesitas para futuras expansiones.
# ========================
# TWITTER / X
# ========================
CONSUMER_KEY = "ZazzdZEzzRqBbwC2X663sNmFY"
CONSUMER_SECRET = "Wj9eoJUEyk4SZWxytchTqjvsLd0iJXCeSKWYLZVcIr9WOzn2dL"
ACCESS_TOKEN = "1924786809327730688-Yj4Q7VkPggDGKGjAyU7NDoquS8HrHn"
ACCESS_TOKEN_SECRET = "S6LHZTQ32L254iD36WKPhYYaKyMcyJGGTWgo1Ytnp2Yc"

TWITTER_EMAIL = "trendphonedeal@gmail.com"
TWITTER_PASS = "Beayfran2025"
TWITTER_USER = "trendphonedeal"

# ... (puedes mantener el resto de tus configuraciones aquí si lo deseas)