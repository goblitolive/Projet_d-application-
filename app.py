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
# Bigrammes les plus fréquents avec pourcentages
french_bigrams_freq = {
    'es': 1.6852163544149215, 're': 1.595065351485014, 'le': 1.5560638537635647, 'ai': 1.5448748994992145, 
    'en': 1.4480105240106966, 'de': 1.4312270926141712, 'it': 1.3867909599643231, 'et': 1.2573187749054133, 
    'ou': 1.1735614601265631, 'on': 1.1415930193712767, 'te': 1.047286119143182, 'qu': 1.0439294328638766, 
    'er': 0.9998129846215816, 'an': 0.9747177586286817, 'la': 0.9000714494650881, 'me': 0.8407699918640318, 
    'il': 0.8375731477885032, 'ne': 0.8354951991394096, 'ur': 0.812318079591827, 'se': 0.7817882186705285, 
    'ie': 0.7739559506854833, 'ui': 0.5640831371270282, 'el': 0.5589681866061824, 'un': 0.5496973387871493, 
    'ar': 0.5407461753756692, 've': 0.5132533163261228, 'ra': 0.5114950520845821, 'pa': 0.5084580502128299, 
    'co': 0.49886751798624396, 'ta': 0.4919943032238574, 'us': 0.4878384059256701, 'em': 0.4787274003104135, 
    'ma': 0.46785813045361624, 'tr': 0.46418175976675824, 'oi': 0.4601857046723475, 'au': 0.45762822941192455, 
    'ti': 0.4485172237966679, 'ut': 0.4473983283702329, 'sa': 0.43860700716252915, 'ch': 0.43349205664168333, 
    'so': 0.4298156859548254, 'av': 0.4285369483246139, 'ri': 0.4261393152679675, 'va': 0.39544961214289254, 
    'ir': 0.3893756083993881, 'st': 0.3769079165048264, 'om': 0.3725921770028628, 'vo': 0.3641205402027119, 
    'pe': 0.3617229071460654, 'di': 0.3561284300138903, 'po': 0.34030405184002355, 'ss': 0.33167257283609625, 
    'ro': 0.3311930462247669, 'as': 0.32463951586993317, 'ec': 0.3236804626472746, 'to': 0.3220820406095103, 
    'si': 0.31952456534908735, 'pr': 0.31936472314531095, 'nd': 0.3171269322924409, 'or': 0.314569457032018, 
    'mo': 0.30258129174878556, 'fa': 0.300503343099692, 'al': 0.28739628239002457, 'at': 0.2789246455898737, 
    'he': 0.2787648033860972, 'lu': 0.2635797940273362, 'rt': 0.2624608986009012, 'mm': 0.25734594808005534, 
    'ev': 0.2485546268723516, 'ge': 0.2459971516119287, 'nc': 0.2450380983892701, 'vi': 0.23464835514380206, 
    'li': 0.22953340462295624, 'ha': 0.22058224121147604, 'ux': 0.2199428723963703, 'je': 0.21978303019259388, 
    'su': 0.20811454931691434, 'tt': 0.20267991438851565, 'na': 0.1948476464034705, 'pl': 0.19468780419969406, 
    'rs': 0.1903720646977304, 'ep': 0.18733506282597817, 'mi': 0.18222011230513238, 'bl': 0.18174058569380308, 
    'ea': 0.17998232145226234, 'no': 0.1779043728031687, 'ee': 0.1774248461918394, 'am': 0.1748673709314165, 
    'ca': 0.17326894889365219, 'ho': 0.17310910668987575, 'io': 0.17294926448609932, 'ac': 0.1703917892256764, 
    'ei': 0.16703510294637133, 'lo': 0.16591620751993633, 'nn': 0.16559652311238346, 'du': 0.1563256752933504, 
    'ap': 0.15552646427446823, 'rd': 0.1547272532555861, 'rr': 0.148333565104
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

def dechiffrer(ciphertext, known_frequency, known_ngrams):
    # Déchiffrer en utilisant les bigrammes
    sorted_cipher_bigrams = sorted(known_ngrams.items(), key=lambda item: item[1], reverse=True)
    decrypted_text = ciphertext
    for ngram, freq in sorted_cipher_bigrams:
        decrypted_text = decrypted_text.replace(ngram, ngram.lower())

    # Calculer les fréquences des caractères dans le texte chiffré
    total_chars = len(decrypted_text)
    cipher_frequencies = Counter(decrypted_text)
    cipher_frequencies_percentage = {char: (freq / total_chars) * 100 for char, freq in cipher_frequencies.items()}

    
    # Créer un mapping du texte chiffré vers le texte original basé sur les fréquences
    sorted_cipher_chars = sorted(cipher_frequencies_percentage.items(), key=lambda item: item[1], reverse=True)
    sorted_original_chars = sorted(known_frequency.items(), key=lambda item: item[1], reverse=True)
    
    char_map = {}
    for (cipher_char, _), (original_char, _) in zip(sorted_cipher_chars, sorted_original_chars):
        char_map[cipher_char] = original_char

    # Ajuster le déchiffrage avec les fréquences des caractères
    final_decrypted_text = ''.join(char_map.get(char, char) for char in decrypted_text)
    return final_decrypted_text

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
        decrypted_password =  dechiffrer(hashed_password, french_freq, french_bigrams_freq)
        return render_template('decrypt.html', decrypted_password=decrypted_password)
    return render_template('decrypt.html')

if __name__ == '__main__':
    app.run(debug=True)
