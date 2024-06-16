# -*- coding: utf-8 -*-

from flask import Flask, render_template, request
import random
from collections import Counter

app = Flask(__name__)

def chiffrer(text): 
    text = text.lower()  # Convertir tout le texte en minuscules
    L = []
    N = []
    tab = list('abcdefghijklmnopqrstuvwxyz .')  # Alphabet en minuscules
    sauvgarde = {}
    frequency = Counter(text)

    # Ajouter chaque caractère du texte dans le tableau L
    for i in text:
        L.append(i)

    # Remplacer chaque caractère de L par un caractère aléatoire de tab
    for j in range(len(L)):
        if L[j] not in sauvgarde:
            # Choisir un caractère aléatoire de tab
            rand_alphabet = random.choice(tab)
            while rand_alphabet == L[j]:
                rand_alphabet = random.choice(tab)
            
            # Ajouter la substitution au dictionnaire et retirer de tab
            sauvgarde[L[j]] = rand_alphabet
            tab.remove(rand_alphabet)  # Assurer que le caractère n'est pas réutilisé
            N.append(rand_alphabet)
        else:
            N.append(sauvgarde[L[j]])

    formatted_frequency = ', '.join(['{}:{}'.format(char, freq) for char, freq in frequency.items()])
    return ''.join(N), formatted_frequency

def dechiffrer(ciphertext, frequency):
    # Convertir tout le texte en minuscules pour correspondre à nos fréquences
    ciphertext = ciphertext.lower()

    # Convertir les fréquences en dictionnaire
    frequency = dict(item.split(':') for item in frequency.split(','))
    frequency = {char: int(freq) for char, freq in frequency.items()}

    # Trier les lettres par fréquence dans le texte chiffré
    sorted_cipher_chars = sorted(frequency, key=frequency.get, reverse=True)
    
    # Trier les lettres par fréquence dans le texte chiffré
    sorted_original_chars = sorted(frequency, key=frequency.get, reverse=True)

    # Créer un mapping du texte chiffré vers le texte original basé sur les fréquences
    char_map = {}
    for cipher_char, original_char in zip(sorted_cipher_chars, sorted_original_chars):
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
        return render_template('decrypt.html', decrypted_password=decrypted_password, frequency=frequency)
    return render_template('decrypt.html')

if __name__ == '__main__':
    app.run(debug=True)
