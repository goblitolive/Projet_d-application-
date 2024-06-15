from flask import Flask, render_template, request, redirect, url_for
from werkzeug.security import check_password_hash
import random
from collections import Counter

app = Flask(__name__)

def chiffrer(text): 
    text = text.lower()  # Convertir tout le texte en minuscules
    L = []
    N = []
    tab = list('abcdefghijklmnopqrstuvwxyz .')  # Alphabet en minuscules
    sauvgarde = {}

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

    return ''.join(N)

FRENCH_LETTER_FREQUENCIES = {
    'e': 14.7, 'a': 7.6, 'i': 7.5, 's': 7.9, 'n': 7.1, 'r': 6.6, 't': 7.0, 'o': 5.8, 'l': 5.5, 'u': 6.3,
    'd': 3.7, 'c': 3.2, 'm': 2.4, 'p': 3.0, 'v': 1.5, 'q': 1.2, 'f': 1.0, 'b': 1.1, 'g': 1.1, 'j': 0.6,
    'x': 0.4, 'y': 0.4, 'z': 0.3, 'h': 1.1, 'k': 0.05, 'w': 0.05, ' ': 18.0, '.': 2.0
}

def dechiffrer(ciphertext):
    # Convertir tout le texte en minuscules pour correspondre à nos fréquences
    ciphertext = ciphertext.lower()

    # Calculer les fréquences des lettres dans le texte chiffré
    letter_counts = Counter(ciphertext)
    total_letters = sum(letter_counts.values())
    
    # Calculer les fréquences en pourcentage
    cipher_frequencies = {char: (count / total_letters) * 100 for char, count in letter_counts.items()}
    
    # Trier les lettres par fréquence dans le texte chiffré
    sorted_cipher_chars = sorted(cipher_frequencies, key=cipher_frequencies.get, reverse=True)
    
    # Trier les lettres par fréquence en français
    sorted_french_chars = sorted(FRENCH_LETTER_FREQUENCIES, key=FRENCH_LETTER_FREQUENCIES.get, reverse=True)
    
    # Créer un mapping du texte chiffré vers le français basé sur les fréquences
    char_map = {}
    for cipher_char, french_char in zip(sorted_cipher_chars, sorted_french_chars):
        char_map[cipher_char] = french_char

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
        hashed_password = chiffrer(password)
        return render_template('encrypt.html', hashed_password=hashed_password)
    return render_template('encrypt.html')

@app.route('/decrypt', methods=['GET', 'POST'])
def decrypt():
    if request.method == 'POST':
        hashed_password = request.form['hashed_password']
        decrypted_password = dechiffrer(hashed_password)
        return render_template('decrypt.html', decrypted_password=decrypted_password)
    return render_template('decrypt.html')

if __name__ == '__main__':
    app.run(debug=True)
