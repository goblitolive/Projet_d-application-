from collections import Counter

# Définir les fréquences des caractères en français
french_freq = {
    'e': 14.13, 'a': 7.18, 'i': 6.28, 's': 5.99, 't': 6.17, 'n': 5.52, 'r': 5.05, 'u': 5.20, 'l': 4.81, 'o': 4.18,
    'd': 2.82, 'm': 2.45, 'c': 2.52, 'p': 2.11, 'v': 1.61, 'q': 1.06, 'f': 0.93, 'b': 0.79, 'g': 0.72, 'h': 0.80,
    'j': 0.46, 'x': 0.33, 'y': 0.27, 'z': 0.15, ' ': 17.38, '.': 1.07
}

def decrypt_text(ciphertext, known_frequency):
    # Calculer les fréquences des caractères dans le texte chiffré
    total_chars = len(ciphertext)
    cipher_frequencies = Counter(ciphertext)
    cipher_frequencies_percentage = {char: (freq / total_chars) * 100 for char, freq in cipher_frequencies.items()}

    # Créer un mapping du texte chiffré vers le texte original basé sur les fréquences des caractères
    sorted_cipher_chars = sorted(cipher_frequencies_percentage.items(), key=lambda item: item[1], reverse=True)
    sorted_original_chars = sorted(known_frequency.items(), key=lambda item: item[1], reverse=True)

    char_map = {}
    for (cipher_char, _), (original_char, _) in zip(sorted_cipher_chars, sorted_original_chars):
        char_map[cipher_char] = original_char

    # Déchiffrer le texte avec le mapping
    decrypted_text = ''.join(char_map.get(char, char) for char in ciphertext)

    return decrypted_text

def generate_possible_mappings(ciphertext):
    total_chars = len(ciphertext)
    cipher_frequencies = Counter(ciphertext)
    cipher_frequencies_percentage = {char: (freq / total_chars) * 100 for char, freq in cipher_frequencies.items()}

    sorted_cipher_chars = sorted(cipher_frequencies_percentage.items(), key=lambda item: item[1], reverse=True)
    sorted_french_chars = sorted(french_freq.items(), key=lambda item: item[1], reverse=True)

    possible_mappings = []
    for offset in range(4):
        char_map = {}
        for (cipher_char, _), (french_char, _) in zip(sorted_cipher_chars[offset:], sorted_french_chars):
            char_map[cipher_char] = french_char
        possible_mappings.append(char_map)

    return possible_mappings
