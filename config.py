import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

def get_gemini_client():
    """
    Initialise et retourne le client Gemini en utilisant la clé d'API.
    """
    api_key = os.getenv("GEMINI_API_KEY")
    
    if not api_key:
        raise ValueError("Erreur : La clé GEMINI_API_KEY est manquante dans le fichier .env")
        
    # On initialise le client officiel avec la nouvelle norme
    return genai.Client(api_key=api_key)