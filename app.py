# -*- coding: utf-8 -*-

from flask import Flask, render_template, request
import random
from collections import Counter

app = Flask(__name__)

# Fréquences des caractères en français
french_freq = {
    'e': 14.1329, 'n': 5.5238, ' ': 17.3809, 'm': 2.4542, '.': 1.0681, 'c': 2.5202, 'h': 0.7995, 'a': 7.1761, 'r': 5.0508,
    'l': 4.8098, 's': 5.9917, 'f': 0.9320, 'o': 4.1802, 'i': 6.2819, 'b': 0.7901, 'v': 1.6136, 'u': 5.2016, 'y': 0.2741,
    't': 6.1669, 'q': 1.0551, 'd': 2.8247, 'g': 0.7158, 'x': 0.3272, 'z': 0.1533, 'p': 2.1128, 'j': 0.4589, 'k': 0.0021,
    'w': 0.0016
}

def format_substitution_key(substitution_key):
    formatted_key = []
    for char, subst in substitution_key.items():
        formatted_key.append(f"{char} -> {subst}")
    return ', '.join(formatted_key)

def chiffrer(text):
    text = text.lower()  # Convertir tout le texte en minuscules
    tab = list('abcdefghijklmnopqrstuvwxyz .')  # Alphabet en minuscules, y compris espace et point
    sauvegarde = {}
    total_chars = len(text)  # Nombre total de caractères

    # Calculer les fréquences des caractères en pourcentage
    frequency = Counter(text)
    frequency_percentage = {char: (freq / total_chars) * 100 for char, freq in frequency.items()}

    # Créer le texte chiffré
    encrypted_text = []
    for char in text:
        if char not in sauvegarde:
            rand_alphabet = random.choice(tab)
            while rand_alphabet == char:
                rand_alphabet = random.choice(tab)
            sauvegarde[char] = rand_alphabet
            tab.remove(rand_alphabet)
        encrypted_text.append(sauvegarde[char])

    substitution_key = format_substitution_key(sauvegarde)
    return ''.join(encrypted_text), frequency_percentage, substitution_key

def dechiffrer(ciphertext, known_frequency):
    # Calculer les fréquences des caractères dans le texte chiffré
    total_chars = len(ciphertext)
    cipher_frequencies = Counter(ciphertext)
    cipher_frequencies_percentage = {char: (freq / total_chars) * 100 for char, freq in cipher_frequencies.items()}

    # Créer un mapping du texte chiffré vers le texte original basé sur les fréquences
    sorted_cipher_chars = sorted(cipher_frequencies_percentage.items(), key=lambda item: item[1], reverse=True)
    sorted_original_chars = sorted(known_frequency.items(), key=lambda item: item[1], reverse=True)
    
    char_map = {}
    for (cipher_char, _), (original_char, _) in zip(sorted_cipher_chars, sorted_original_chars):
        char_map[cipher_char] = original_char

    # Déchiffrer le texte
    decrypted_text = ''.join(char_map.get(char, char) for char in ciphertext)

    return decrypted_text

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/encrypt', methods=['GET', 'POST'])
def encrypt():
    if request.method == 'POST':
        password = request.form['password']
        hashed_password, frequency, substitution_key = chiffrer(password)
        return render_template('encrypt.html', hashed_password=hashed_password, frequency=frequency, substitution_key=substitution_key)
    return render_template('encrypt.html')

@app.route('/decrypt', methods=['GET', 'POST'])
def decrypt():
    if request.method == 'POST':
        hashed_password = request.form['hashed_password']
        decrypted_password = dechiffrer(hashed_password, french_freq)
        return render_template('decrypt.html', decrypted_password=decrypted_password)
    return render_template('decrypt.html')

if __name__ == '__main__':
    app.run(debug=True)
