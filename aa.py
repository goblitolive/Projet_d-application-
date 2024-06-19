# -*- coding: utf-8 -*-

from collections import Counter
import random

# Fréquences des caractères en français
french_freq = {
    'e': 14.1329, 'n': 5.5238, ' ': 17.3809, 'm': 2.4542, '.': 1.0681, 'c': 2.5202, 'h': 0.7995, 'a': 7.1761, 'r': 5.0508,
    'l': 4.8098, 's': 5.9917, 'f': 0.9320, 'o': 4.1802, 'i': 6.2819, 'b': 0.7901, 'v': 1.6136, 'u': 5.2016, 'y': 0.2741,
    't': 6.1669, 'q': 1.0551, 'd': 2.8247, 'g': 0.7158, 'x': 0.3272, 'z': 0.1533, 'p': 2.1128, 'j': 0.4589, 'k': 0.0021,
    'w': 0.0016
}

# Bigrammes les plus fréquents avec pourcentages
french_bigrams_freq = {
    't ': 2.6225310373599187, 's ': 2.6003129710349944, 'd ': 1.907716702071715, 'e ': 1.7736090931032886, 'l ': 1.748354024906612,
    'es': 1.6852163544149215, 're': 1.595065351485014, 'a ': 1.5632567529335042, 'le': 1.5560638537635647, 'ai': 1.5448748994992145,
    'en': 1.4480105240106966, 'de': 1.4312270926141712, 'it': 1.3867909599643231, 'et': 1.2573187749054133, 'p ': 1.2448510830108517,
    'c ': 1.229825915855867, 'n ': 1.2116039046253537, 's': 1.2053700586780731, 'nt': 1.195779526451487, 'ou': 1.1735614601265631,
    'on': 1.1415930193712767, 'te': 1.047286119143182, 'qu': 1.0439294328638766, 'er': 0.9998129846215816, 'l ': 0.9823901844099505,
    'an': 0.9747177586286817, 'la': 0.9000714494650881, 'm': 0.844925889162219, 'me': 0.8407699918640318, 'il': 0.8375731477885032,
    'r ': 0.8361345679545154, 'ne': 0.8354951991394096, 'ur': 0.812318079591827, 'se': 0.7817882186705285, '. ': 0.7782716901874469,
    'ie': 0.7739559506854833, 'q': 0.7229662876808015, 'is': 0.71497417749198, 'eu': 0.7074615939144876, 'ce': 0.6997891681332189,
    'u ': 0.6588695639664524, 'in': 0.635053075603764, 'ue': 0.6323357581395646, 'i': 0.6225853837092022, 'ns': 0.5946129980483267,
    'ui': 0.5640831371270282, 'el': 0.5589681866061824, 'v': 0.5557713425306537, 'un': 0.5496973387871493, 'i ': 0.5433036506360921,
    'ar': 0.5407461753756692, 'f': 0.5381887001152462, 've': 0.5132533163261228, 't': 0.5127737897147935, 'ra': 0.5114950520845821,
    'pa': 0.5084580502128299, 'co': 0.49886751798624396, 'ta': 0.4919943032238574, 'us': 0.4878384059256701, 'u': 0.48735887931434085,
    'em': 0.4787274003104135, 'll': 0.46785813045361624, 'ma': 0.46785813045361624, 'tr': 0.46418175976675824, 'oi': 0.4601857046723475,
    'au': 0.45762822941192455, 'r': 0.4550707541515016, 'ti': 0.4485172237966679, 'ut': 0.4473983283702329, 'sa': 0.43860700716252915,
    'ch': 0.43349205664168333, 'so': 0.4298156859548254, 'av': 0.4285369483246139, 'ri': 0.4261393152679675, 'n': 0.42470073543397957,
    'va': 0.39544961214289254, 'ir': 0.3893756083993881, 'st': 0.3769079165048264, 'om': 0.3725921770028628, 'vo': 0.3641205402027119,
    'e.': 0.3623622759611711, 'pe': 0.3617229071460654, 'di': 0.3561284300138903, 'j': 0.3439804225268815, 'po': 0.34030405184002355,
    'b': 0.3372670499682713, 'o': 0.33646783894938914, 'ss': 0.33167257283609625, 'ro': 0.3311930462247669, 'as': 0.32463951586993317,
    'ec': 0.3236804626472746, 'to': 0.3220820406095103, 'si': 0.31952456534908735, 'pr': 0.31936472314531095, 'nd': 0.3171269322924409,
    'or': 0.314569457032018, 'da': 0.3104135597338308, 'd ': 0.3100938753262779, 'mo': 0.30258129174878556, 'fa': 0.300503343099692,
    'al': 0.28739628239002457, 'at': 0.2789246455898737, 'he': 0.2787648033860972, 'lu': 0.2635797940273362, 'rt': 0.2624608986009012,
    'mm': 0.25734594808005534, 'ev': 0.2485546268723516, 'ge': 0.2459971516119287, 'nc': 0.2450380983892701, 'vi': 0.23464835514380206,
    'li': 0.22953340462295624, 'ha': 0.22058224121147604, 'ux': 0.2199428723963703, 'h': 0.21978303019259388, 'je': 0.21978303019259388,
    'x ': 0.21131139339244298, 'su': 0.20811454931691434, 'tt': 0.20267991438851565, 'c ': 0.19804449047899914, 'na': 0.1948476464034705,
    'pl': 0.19468780419969406, 'rs': 0.1903720646977304, 'ep': 0.18733506282597817, 'mi': 0.18222011230513238, 'bl': 0.18174058569380308,
    's.': 0.1803020058598152, 'ea': 0.17998232145226234, 'no': 0.1779043728031687, 'ee': 0.1774248461918394, 'am': 0.1748673709314165,
    'ca': 0.17326894889365219, 'ho': 0.17310910668987575, 'io': 0.17294926448609932, 'g': 0.17215005346721718, 'ac': 0.1703917892256764,
    'ei': 0.16703510294637133, 'lo': 0.16591620751993633, 'nn': 0.16559652311238346, 'du': 0.1563256752933504, 'ap': 0.15552646427446823,
    'rd': 0.1547272532555861, 'rr': 0.1483335651045288, 'uv': 0.14705482747431733, 'mp': 0.14593593204788233, 'os': 0.14193987695347154,
    'ol': 0.1403414549157072, 't.': 0.14018161271193078, 'ci': 0.13426745117220282, 'do': 0.13410760896842638, 'ez': 0.130271396077792,
    'ag': 0.1293123428551334, 'bo': 0.1288328162438041, 'ab': 0.12659502539093406, 'br': 0.12547612996449906, 'fi': 0.12339818131540543,
    'ni': 0.12307849690785257, 'ts': 0.12291865470407613, 'fo': 0.1227588125002997, 'ig': 0.11956196842477106, 'ul': 0.11524622892280742,
    'fe': 0.11460686010770169, 'ad': 0.11141001603217303, 'mb': 0.10933206738307942, 'y': 0.1082131719566444, 'cr': 0.1072541187339858,
    'ba': 0.10629506551132722, 'tu': 0.10565569669622149, 'im': 0.10501632788111576, 'ic': 0.1046966434735629, 'ng': 0.10437695906601004
}

def format_substitution_key(substitution_key):
    formatted_key = []
    for char, subst in substitution_key.items():
        formatted_key.append("{0} -> {1}".format(char, subst))
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
    return ''.join(encrypted_text), frequency, substitution_key

def calculate_score(decrypted_text, known_ngrams):
    bigram_frequencies = Counter([decrypted_text[i:i+2] for i in range(len(decrypted_text)-1)])
    score = sum(known_ngrams.get(bigram, 0) for bigram in bigram_frequencies)
    return score

def dechiffrer(ciphertext, known_frequency, known_ngrams):
    # Calculer les fréquences des caractères dans le texte chiffré
    total_chars = len(ciphertext)
    cipher_frequencies = Counter(ciphertext)
    cipher_frequencies_percentage = {char: (freq / total_chars) * 100 for char, freq in cipher_frequencies.items()}

    # Générer plusieurs mappings possibles basés sur les fréquences des caractères
    sorted_cipher_chars = sorted(cipher_frequencies_percentage.items(), key=lambda item: item[1], reverse=True)
    sorted_original_chars = sorted(known_frequency.items(), key=lambda item: item[1], reverse=True)
    
    possible_mappings = []
    for offset in range(4):
        char_map = {}
        for (cipher_char, _), (original_char, _) in zip(sorted_cipher_chars[offset:], sorted_original_chars):
            char_map[cipher_char] = original_char
        possible_mappings.append(char_map)

    # Générer plusieurs textes déchiffrés basés sur les mappings possibles
    possible_decryptions = []
    for char_map in possible_mappings:
        decrypted_text = ''.join(char_map.get(char, char) for char in ciphertext)
        possible_decryptions.append(decrypted_text)

    # Classer les textes déchiffrés par score basé sur les bigrammes
    scored_decryptions = [(decrypted_text, calculate_score(decrypted_text, known_ngrams)) for decrypted_text in possible_decryptions]
    scored_decryptions.sort(key=lambda x: x[1], reverse=True)

    return [decryption for decryption, score in scored_decryptions]

if __name__ == '__main__':
    print("Choisissez une option (1: Chiffrer, 2: Déchiffrer): ")
    choice = input().strip()
    
    if choice == '1':
        print("Entrez le texte à chiffrer: ")
        text = input().strip()
        hashed_password, frequency, substitution_key = chiffrer(text)
        print("Texte chiffré: {0}".format(hashed_password))
        print("Fréquences des caractères: {0}".format(dict(frequency)))
        print("Clé de substitution: {0}".format(substitution_key))
    
    elif choice == '2':
        print("Entrez le texte chiffré: ")
        hashed_password = input().strip()
        decrypted_passwords = dechiffrer(hashed_password, french_freq, french_bigrams_freq)
        for i, decrypted_password in enumerate(decrypted_passwords, start=1):
            print("Texte déchiffré {}: {}".format(i, decrypted_password))
    
    else:
        print("Choix invalide.")
