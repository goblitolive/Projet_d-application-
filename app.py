from flask import Flask, render_template, request, redirect, url_for
from werkzeug.security import generate_password_hash, check_password_hash

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
