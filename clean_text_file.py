# -*- coding: utf-8 -*-

import re
import codecs
from unidecode import unidecode

def clean_text(text):
    # Utilise unidecode pour convertir les accents
    text = unidecode(text)
    
    # Supprime les apostrophes et les virgules
    text = text.replace("'", " ").replace(",", " ")

    # Supprime les doubles tirets et les underscores
    text = text.replace("--", " ").replace("_", " ")

    # Supprime les autres signes de ponctuation complexes
    text = re.sub(r'[;:!?"“”]', ' ', text)

    return text

def main():
    input_path = "C:/Users/elhar/OneDrive/Desktop/projet_app/text.txt"
    output_path = "C:/Users/elhar/OneDrive/Desktop/projet_app/text_cleaned.txt"

    # Lecture du texte original
    with codecs.open(input_path, "r", "utf-8") as f:
        raw_text = f.read()

    # Nettoyage du texte
    cleaned_text = clean_text(raw_text)

    # Enregistrement du texte nettoyé
    with codecs.open(output_path, "w", "utf-8") as f:
        f.write(cleaned_text)

    print("Le texte nettoyé a été sauvegardé avec succès dans text_cleaned.txt.")

if __name__ == "__main__":
    main()
