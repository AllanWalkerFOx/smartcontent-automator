from config import get_gemini_client
from google.genai.errors import APIError

def generate_social_content(text_input):
    try:
        # Initialisation du client
        client = get_gemini_client()
        
        print("\n[1/2] Analyse du contenu et génération du post LinkedIn...")
        prompt_linkedin = f"Analyse ce texte et fais-en un post LinkedIn percutant :\n{text_input}"
        
        response_linkedin = client.models.generate_content(
            model='gemini-2.5-flash',
            contents=prompt_linkedin,
        )
        
        print("[2/2] Génération du script vidéo Short/TikTok (9:16)...")
        prompt_video = f"Crée un script vidéo court (Hook, Corps, CTA) basé sur :\n{text_input}"
        
        response_video = client.models.generate_content(
            model='gemini-2.5-flash',
            contents=prompt_video,
        )
        
        # Sauvegarde sécurisée
        with open("output_linkedin.txt", "w", encoding="utf-8") as f:
            f.write(response_linkedin.text)
            
        with open("output_video.txt", "w", encoding="utf-8") as f:
            f.write(response_video.text)
            
        print("\n Terminé ! Fichiers créés avec succès.")

    except APIError as e:
        print(f"\n Erreur API Gemini : {e}")
    except ConnectionError:
        print("\n Erreur de connexion : Impossible de joindre les serveurs.")
    except Exception as e:
        print(f"\n Une erreur imprévue est survenue : {e}")

# LE BLOC D'EXÉCUTION À AJOUTER :
if __name__ == "__main__":
    print("--- BIENVENUE SUR SMARTCONTENT-AUTOMATOR ---")
    user_text = input("Colle le texte ou l'article à transformer :\n> ")
    if user_text.strip():
        generate_social_content(user_text)
    else:
        print("Erreur : Le texte fourni est vide.")