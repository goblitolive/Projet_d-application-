from flask import Flask, jsonify, render_template, request
import random
from collections import Counter
from decrypt import decrypt_text, generate_possible_mappings  # Importer les fonctions de decrypt.py

app = Flask(__name__)

# Définir les fréquences des caractères en français
french_freq = {
    'e': 14.13, 'a': 7.18, 'i': 6.28, 's': 5.99, 't': 6.17, 'n': 5.52, 'r': 5.05, 'u': 5.20, 'l': 4.81, 'o': 4.18,
    'd': 2.82, 'm': 2.45, 'c': 2.52, 'p': 2.11, 'v': 1.61, 'q': 1.06, 'f': 0.93, 'b': 0.79, 'g': 0.72, 'h': 0.80,
    'j': 0.46, 'x': 0.33, 'y': 0.27, 'z': 0.15, ' ': 17.38, '.': 1.07
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
        decrypted_password = decrypt_text(hashed_password, french_freq)  # Utiliser la fonction de déchiffrement correcte
        return render_template('decrypt.html', decrypted_password=decrypted_password)
    return render_template('decrypt.html')

@app.route('/get_options', methods=['POST'])
def get_options():
    data = request.get_json()
    word = data['word']
    
    # Générer quatre propositions basées sur le mot cliqué
    possible_mappings = generate_possible_mappings(word)
    options = []
    for char_map in possible_mappings:
        decrypted_text = ''.join(char_map.get(char, char) for char in word)
        options.append(decrypted_text)
    
    return jsonify({'options': options})

if __name__ == '__main__':
    app.run(debug=True)
