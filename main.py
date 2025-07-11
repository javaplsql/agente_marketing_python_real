from publishers.twitter_publisher import publicar_en_twitter

def main():
    print("🚀 Iniciando agente de marketing automático...\n")

    mensaje = "📘 Curso Java 2025 en Amazon KDP. ¡Domina Java en entornos profesionales! #Java #AmazonKDP"
    enlace = "https://www.amazon.com/dp/B0D2W9F79C?tag=trendphonedea-21"  # ← incluye tu tag de afiliado

    publicar_en_twitter(mensaje, enlace)

    print("\n✅ Proceso completado.")

if __name__ == "__main__":
    main()
