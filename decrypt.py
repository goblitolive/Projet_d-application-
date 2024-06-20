from collections import Counter
import itertools

# Définir les fréquences des caractères en français
french_freq = {
    'e': 14.13, 'a': 7.18, 'i': 6.28, 's': 5.99, 't': 6.17, 'n': 5.52, 'r': 5.05, 'u': 5.20, 'l': 4.81, 'o': 4.18,
    'd': 2.82, 'm': 2.45, 'c': 2.52, 'p': 2.11, 'v': 1.61, 'q': 1.06, 'f': 0.93, 'b': 0.79, 'g': 0.72, 'h': 0.80,
    'j': 0.46, 'x': 0.33, 'y': 0.27, 'z': 0.15, ' ': 17.38, '.': 1.07
}
known_bigrams = {
    'le': 1.5, 'de': 1.3, 'en': 1.2, 're': 1.1, 'on': 1.0, 'te': 0.9, 'se': 0.8, 'er': 0.7, 'an': 0.6, 'ou': 0.5
}

known_trigrams = {
    'les': 0.5, 'des': 0.4, 'ent': 0.3, 'ion': 0.2, 'tio': 0.2, 'est': 0.2, 'que': 0.2, 'pour': 0.1, 'par': 0.1, 'sur': 0.1
}



# def generate_possible_mappings(ciphertext):
#     total_chars = len(ciphertext)
#     cipher_frequencies = Counter(ciphertext)
#     cipher_frequencies_percentage = {char: (freq / total_chars) * 100 for char, freq in cipher_frequencies.items()}

#     sorted_cipher_chars = sorted(cipher_frequencies_percentage.items(), key=lambda item: item[1], reverse=True)
#     sorted_french_chars = sorted(french_freq.items(), key=lambda item: item[1], reverse=True)

#     possible_mappings = []
#     for offset in range(4):
#         char_map = {}
#         for (cipher_char, _), (french_char, _) in zip(sorted_cipher_chars[offset:], sorted_french_chars):
#             char_map[cipher_char] = french_char
#         possible_mappings.append(char_map)

#     return possible_mappings
known_words = ["bienvenu","bonjour", "salut", "comment", "ça", "va", "oui", "non", "merci", "s'il", "vous", "plaît"]
known_words1 = ["viellard","le","bienvenu", "bonjour", "salut", "comment", "ca", "va", "oui", "non", "merci", "sil", "vous", "plait", "homme", "femme", "enfant", "ami", "maison", "ecole", "travail", "nourriture", "eau", "temps", "jour", "nuit", "matin", "soir", "toujours", "jamais", "parfois", "souvent", "ici", "labas", "maintenant", "avant", "apres", "pourquoi", "parce que", "ou", "quand", "qui", "quoi", "moi", "toi", "lui", "elle", "nous", "vous", "eux", "elles", "je", "tu", "il", "elle", "on", "nous", "vous", "ils", "elles", "petit", "grand", "vieux", "jeune", "livre", "chat", "chien", "arbre", "voiture", "ville", "village", "route", "mer", "montagne", "riviere", "soleil", "lune", "etoile", "ciel", "vent", "pluie", "neige", "feu", "terre", "air", "bateau", "avion", "train", "bus", "velo", "fleur", "jardin", "porte", "fenetre", "chaise", "table", "lit", "chambre", "cuisine", "salon", "bain", "manger", "boire", "dormir", "courir", "marcher", "parler", "ecouter", "voir", "regarder", "lire", "ecrire", "jouer", "travailler", "etudier", "aimer", "detester", "acheter", "vendre", "donner", "recevoir", "prendre", "mettre", "enlever", "ouvrir", "fermer", "commencer", "finir", "penser", "croire", "savoir", "connaitre", "comprendre", "apprendre", "enseigner", "trouver", "perdre", "chercher", "gagner", "payer", "demander", "repondre", "monsieur", "madame", "fille", "garcon", "frere", "soeur", "pere", "mere", "oncle", "tante", "cousin", "cousine", "grand-pere", "grand-mere", "bebe", "adulte", "jeune", "vieux", "beau", "joli", "moche", "fort", "faible", "content", "triste", "heureux", "malheureux", "rapide", "lent", "chaud", "froid", "bon", "mauvais", "facile", "difficile", "cher", "bon marche", "leger", "lourd", "proche", "loin", "nouveau", "ancien", "dernier", "premier", "important", "inutile", "necessaire", "interessant", "ennuyeux", "simple", "complexe", "doux", "dur", "sucre", "sale", "amer", "epice", "acide","soixantequinze"]

def decrypt_text(ciphertext, known_frequency):
    total_chars = len(ciphertext)
    cipher_frequencies = Counter(ciphertext)
    cipher_frequencies_percentage = {char: (freq / total_chars) * 100 for char, freq in cipher_frequencies.items()}

    sorted_cipher_chars = sorted(cipher_frequencies_percentage.items(), key=lambda item: item[1], reverse=True)
    sorted_original_chars = sorted(known_frequency.items(), key=lambda item: item[1], reverse=True)

    char_map = {}
    for (cipher_char, _), (original_char, _) in zip(sorted_cipher_chars, sorted_original_chars):
        char_map[cipher_char] = original_char

    decrypted_text = ''.join(char_map.get(char, char) for char in ciphertext)

    return decrypted_text, char_map

# def generate_possible_mappings(ciphertext, known_frequency, known_words, top_n=4):
#     total_chars = len(ciphertext)
#     cipher_frequencies = Counter(ciphertext)
#     cipher_frequencies_percentage = {char: (freq / total_chars) * 100 for char, freq in cipher_frequencies.items()}

#     sorted_cipher_chars = [char for char, _ in sorted(cipher_frequencies_percentage.items(), key=lambda item: item[1], reverse=True)]
#     sorted_french_chars = [char for char, _ in sorted(known_frequency.items(), key=lambda item: item[1], reverse=True)]

#     possible_mappings = []

#     for word in known_words:
#         if len(word) == len(ciphertext):
#             char_map = {cipher_char: word_char for cipher_char, word_char in zip(ciphertext, word)}
#             possible_mappings.append(char_map)

#     if not possible_mappings:
#         for offset in range(4):
#             char_map = {}
#             for i, (cipher_char, french_char) in enumerate(zip(sorted_cipher_chars[offset:], sorted_french_chars)):
#                 char_map[cipher_char] = french_char
#             possible_mappings.append(char_map)

#     scored_mappings = []
#     for mapping in possible_mappings:
#         decrypted_text = decrypt_text(ciphertext, mapping)[0]
#         score = sum(word in decrypted_text for word in known_words)
#         scored_mappings.append((mapping, decrypted_text, score))

#     scored_mappings.sort(key=lambda item: item[2], reverse=True)

#     adjusted_mappings = []
#     for mapping, decrypted_text, score in scored_mappings[:top_n]:
#         adjusted_mapping = mapping.copy()
#         for word in known_words:
#             if word in decrypted_text:
#                 cipher_word = ''.join(mapping.get(char, char) for char in word)
#                 if cipher_word in ciphertext:
#                     for char, cipher_char in zip(word, cipher_word):
#                         adjusted_mapping[cipher_char] = char
#         adjusted_mappings.append(adjusted_mapping)

#     return adjusted_mappings

def calculate_ngram_frequencies(text, n):
    ngrams = [text[i:i+n] for i in range(len(text)-n+1)]
    total_ngrams = len(ngrams)
    ngram_frequencies = Counter(ngrams)
    return {ngram: (freq / total_ngrams) * 100 for ngram, freq in ngram_frequencies.items()}

def generate_possible_mappings(ciphertext, known_frequency, known_words, known_bigrams, known_trigrams, top_n=4):
    total_chars = len(ciphertext)
    cipher_frequencies = Counter(ciphertext)
    cipher_frequencies_percentage = {char: (freq / total_chars) * 100 for char, freq in cipher_frequencies.items()}

    cipher_bigram_frequencies = calculate_ngram_frequencies(ciphertext, 2)
    cipher_trigram_frequencies = calculate_ngram_frequencies(ciphertext, 3)

    sorted_cipher_chars = [char for char, _ in sorted(cipher_frequencies_percentage.items(), key=lambda item: item[1], reverse=True)]
    sorted_french_chars = [char for char, _ in sorted(known_frequency.items(), key=lambda item: item[1], reverse=True)]

    possible_mappings = []

    for word in known_words:
        if len(word) == len(ciphertext):
            char_map = {cipher_char: word_char for cipher_char, word_char in zip(ciphertext, word)}
            possible_mappings.append(char_map)

    if not possible_mappings:
        for offset in range(4):
            char_map = {}
            for i, (cipher_char, french_char) in enumerate(zip(sorted_cipher_chars[offset:], sorted_french_chars)):
                char_map[cipher_char] = french_char
            possible_mappings.append(char_map)

    scored_mappings = []
    for mapping in possible_mappings:
        decrypted_text = decrypt_text(ciphertext, mapping)[0]
        bigram_score = sum(cipher_bigram_frequencies.get(bigram, 0) * known_bigrams.get(bigram, 0) for bigram in cipher_bigram_frequencies)
        trigram_score = sum(cipher_trigram_frequencies.get(trigram, 0) * known_trigrams.get(trigram, 0) for trigram in cipher_trigram_frequencies)
        word_score = sum(word in decrypted_text for word in known_words)
        score = word_score + bigram_score + trigram_score
        scored_mappings.append((mapping, decrypted_text, score))

    scored_mappings.sort(key=lambda item: item[2], reverse=True)

    adjusted_mappings = []
    for mapping, decrypted_text, score in scored_mappings[:top_n]:
        adjusted_mapping = mapping.copy()
        for word in known_words:
            if word in decrypted_text:
                cipher_word = ''.join(mapping.get(char, char) for char in word)
                if cipher_word in ciphertext:
                    for char, cipher_char in zip(word, cipher_word):
                        adjusted_mapping[cipher_char] = char
        adjusted_mappings.append(adjusted_mapping)

    return adjusted_mappings