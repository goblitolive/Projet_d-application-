from difflib import SequenceMatcher

def find_most_similar_known_words(cipher_word, known_words, top_n=4):
    """
    Cette fonction prend un mot chiffré, calcule sa longueur, et cherche dans known_words les mots
    de même longueur en les classant par ordre de similarité décroissante.

    :param cipher_word: Le mot chiffré.
    :param known_words: Une liste de mots connus.
    :param top_n: Le nombre de mots les plus similaires à retourner (par défaut 4).
    :return: Une liste des top_n mots connus les plus similaires.
    """
    cipher_word_length = len(cipher_word)
    same_length_words = [word for word in known_words if len(word) == cipher_word_length]
    
    def similarity(a, b):
        return SequenceMatcher(None, a, b).ratio()
    
    scored_words = [(word, similarity(cipher_word, word)) for word in same_length_words]
    scored_words.sort(key=lambda item: item[1], reverse=True)
    
    return [word for word, score in scored_words[:top_n]]

# Exemple d'utilisation
cipher_word = "exemple"
known_words = ["exemple", "sample", "temple", "example", "simple","eaample","exenple,exmlpe"]
similar_words = find_most_similar_known_words(cipher_word, known_words)
print(similar_words)