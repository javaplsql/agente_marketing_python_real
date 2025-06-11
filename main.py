from generators.content_generator import generar_contenido
from publishers.twitter_publisher import publicar_en_twitter
from publishers.reddit_publisher import publicar_en_reddit
from publishers.linkedin_publisher import publicar_en_linkedin
from publishers.blogger_publisher import publicar_en_blogger
from publishers.facebook_publisher import publicar_en_facebook
from publishers.instagram_publisher import publicar_en_instagram
# from publishers.video_generator import publicar_en_tiktok  # opcional

if __name__ == "__main__":
    post = generar_contenido()
    publicar_en_twitter(post)
    publicar_en_reddit(post)
    publicar_en_linkedin(post)
    publicar_en_blogger(post)
    publicar_en_facebook(post)
    publicar_en_instagram(post)
    # publicar_en_tiktok(post)