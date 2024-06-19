# -*- coding: utf-8 -*-

import re
import codecs
from unidecode import unidecode
import os

def clean_text(text):
    # Utilise unidecode pour convertir les accents en leur équivalent non accentué
    text = unidecode(text)
    
    # Remplace les apostrophes par des espaces pour ne pas coller les mots
    text = text.replace("'", " ")
    
    # Supprime les caractères non alphabétiques, sauf les points et les virgules
    text = re.sub(r'[^a-zA-Z .,]', '', text)
    
    # Remplace les espaces multiples par un seul espace
    text = re.sub(r'\s+', ' ', text)
    
    return text.strip()  # Supprime les espaces de début et de fin

def main():
    input_path = r"C:\Users\pc\appli\Projet_d-application-\text.txt"
    output_path = r"C:\Users\pc\appli\Projet_d-application-\text_cleaned.txt"
    if not os.path.exists(input_path):
        print(f"Erreur: Le fichier d'entrée '{input_path}' n'existe pas.")
        return

    try:
        # Lecture du texte original
        with codecs.open(input_path, "r", "utf-8") as f:
            raw_text = f.read()

        # Nettoyage du texte
        cleaned_text = clean_text(raw_text)

        # Enregistrement du texte nettoyé
        with codecs.open(output_path, "w", "utf-8") as f:
            f.write(cleaned_text)

        print("Le texte nettoyé a été sauvegardé avec succès dans text_cleaned.txt.")
    
    except FileNotFoundError as e:
        print(f"Erreur: Fichier non trouvé - {e}")
    except Exception as e:
        print(f"Une erreur est survenue: {e}")

if __name__ == "__main__":
    main()
