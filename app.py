# -*- coding: utf-8 -*-

from flask import Flask, render_template, request
import random
from collections import Counter

app = Flask(__name__)

def chiffrer(text):
    text = text.lower()  # Convertir tout le texte en minuscules
    tab = list('abcdefghijklmnopqrstuvwxyz .')  # Alphabet en minuscules, y compris espace et point
    sauvgarde = {}
    frequency = Counter(text)

    # Créer le texte chiffré
    encrypted_text = []
    for char in text:
        if char not in sauvgarde:
            rand_alphabet = random.choice(tab)
            while rand_alphabet == char:
                rand_alphabet = random.choice(tab)
            sauvgarde[char] = rand_alphabet
            tab.remove(rand_alphabet)
        encrypted_text.append(sauvgarde[char])

    formatted_frequency = ', '.join(['{}:{}'.format(repr(char), freq) for char, freq in frequency.items()])
    return ''.join(encrypted_text), formatted_frequency

def dechiffrer(ciphertext, frequency):
    # Convertir les fréquences en dictionnaire
    frequency = dict(item.split(':') for item in frequency.split(', '))
    frequency = {eval(char): int(freq) for char, freq in frequency.items()}

    # Calculer les fréquences des caractères dans le texte chiffré
    cipher_frequencies = Counter(ciphertext)
    
    # Créer un mapping du texte chiffré vers le texte original basé sur les fréquences
    sorted_cipher_chars = sorted(cipher_frequencies.items(), key=lambda item: item[1], reverse=True)
    sorted_original_chars = sorted(frequency.items(), key=lambda item: item[1], reverse=True)
    
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
        hashed_password, frequency = chiffrer(password)
        return render_template('encrypt.html', hashed_password=hashed_password, frequency=frequency)
    return render_template('encrypt.html')

@app.route('/decrypt', methods=['GET', 'POST'])
def decrypt():
    if request.method == 'POST':
        hashed_password = request.form['hashed_password']
        frequency = request.form['frequency']
        decrypted_password = dechiffrer(hashed_password, frequency)
        return render_template('decrypt.html', decrypted_password=decrypted_password)
    return render_template('decrypt.html')

if __name__ == '__main__':
    app.run(debug=True)
