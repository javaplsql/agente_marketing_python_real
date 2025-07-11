from publishers.twitter_publisher import publicar_en_twitter_multiple_con_idiomas
from publishers.linkedin_publisher import publicar_en_linkedin_multiple
from publishers.reddit_publisher import publicar_en_reddit_multiple
from publishers.facebook_publisher import publicar_en_facebook_multiple
from publishers.telegram_publisher import publicar_en_telegram_multiple
from publishers.gumroad_publisher import publicar_en_gumroad_multiple
from publishers.tiktok_publisher import publicar_en_tiktok
from publishers.mastodon_publisher import publicar_en_mastodon_multiple
from publishers.instagram_publisher import publicar_en_instagram_manual
def main():
    print("🚀 Iniciando agente de marketing automático...\n")

    # Nueva imagen del producto en Amazon
    imagen_java = "https://m.media-amazon.com/images/I/61zl7bwTQwL._SY425_.jpg"

    textos_con_idioma = [
        (
            "📘 Curso de Java 2025 en Amazon KDP. ¡Domina Java en entornos profesionales! #Java #AmazonKDP",
            "https://www.amazon.es/dp/B0F9YVY37X",
            "🇪🇸 Español",
            imagen_java
        ),
        (
            "📘 Java Course 2025 on Amazon KDP. Master Java in professional environments! #Java #AmazonKDP",
            "https://www.amazon.co.uk/dp/B0F9YVY37X",
            "🇬🇧 English (UK)",
            imagen_java
        ),
        (
            "📘 Java Kurs 2025 auf Amazon KDP. Beherrsche Java in professionellen Umgebungen! #Java #AmazonKDP",
            "https://www.amazon.de/dp/B0F9YVY37X",
            "🇩🇪 Deutsch",
            imagen_java
        ),
        (
            "📘 Cours Java 2025 sur Amazon KDP. Maîtrisez Java dans des environnements professionnels ! #Java #AmazonKDP",
            "https://www.amazon.fr/dp/B0F9YVY37X",
            "🇫🇷 Français",
            imagen_java
        ),
        (
            "📘 Java Course 2025 on Amazon KDP. Master Java in professional environments! #Java #AmazonKDP",
            "https://www.amazon.in/dp/B0F9YVY37X",
            "🇮🇳 English (India)",
            imagen_java
        ),
        (
            "📘 Corso Java 2025 su Amazon KDP. Padroneggia Java in ambienti professionali! #Java #AmazonKDP",
            "https://www.amazon.it/dp/B0F9YVY37X",
            "🇮🇹 Italiano",
            imagen_java
        ),
    ]
    # Llamadas
    # publicar_en_twitter_multiple_con_idiomas(textos_con_idioma)
    # publicar_en_linkedin_multiple(textos_con_idioma)
    # publicar_en_reddit_multiple(textos_con_idioma)
    # publicar_en_facebook_multiple(textos_con_idioma)
    # publicar_en_telegram_multiple(textos_con_idioma)
    # publicar_en_gumroad_multiple(textos_con_idioma)
    # for t in textos_con_idioma:
    #     publicar_en_tiktok(*t)
    # publicar_en_mastodon_multiple(textos_con_idioma)
    publicar_en_instagram_manual(textos_con_idioma)
    print("\n✅ Proceso completado.")

if __name__ == "__main__":
    main()
