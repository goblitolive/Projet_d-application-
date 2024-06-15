from flask import Flask, render_template, request, redirect, url_for
from werkzeug.security import generate_password_hash, check_password_hash
import random
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/encrypt', methods=['GET', 'POST'])
def encrypt():
    if request.method == 'POST':
        password = request.form['password']
        hashed_password = generate_password_hash(password)
        return render_template('encrypt.html', hashed_password=hashed_password)
    return render_template('encrypt.html')

def cheffre(): 
    text = input("ktb text dyalk  : ").lower()  # Convertir tout le texte en minuscules
    L = []
    N = []
    tab = list('abcdefghijklmnopqrstuvwxyz .')  # Alphabet en minuscules
    sauvgarde = {}

    # Ajouter chaque caractère du texte dans le tableau L
    for i in text:
        L.append(i)
    print("L =", L)

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

    print("N =", N)

cheffre()



@app.route('/decrypt', methods=['GET', 'POST'])
def decrypt():
    if request.method == 'POST':
        password = request.form['password']
        hashed_password = request.form['hashed_password']
        password_match = check_password_hash(hashed_password, password)
        return render_template('decrypt.html', password_match=password_match)
    return render_template('decrypt.html')

if __name__ == '__main__':
    app.run(debug=True)
