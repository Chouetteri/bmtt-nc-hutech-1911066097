from flask import Flask, render_template, request, jsonify
from Cipher.Caesar import CaesarCipher
from Cipher.Vigenere import VigenereCipher
from Cipher.Railfence import RailfenceCipher
from Cipher.Playfair import PlayFairCipher

app = Flask(__name__)   

@app.route("/")
def home():
    return render_template('index.html')

#CAESAR CIPHER
@app.route("/caesar")
def caesar():
    return render_template('caesar.html')

@app.route("/encrypt_caesar", methods=['POST'])
def caesar_encrypt():
    plain_text = request.form['inputPlainText']
    key = int(request.form['inputKeyPlain'])
    Caesar = CaesarCipher()
    encrypted_text = Caesar.encrypt_text(plain_text, key)
    return f"text: {plain_text}<br>key: {key}<br>encrypted text: {encrypted_text}"

@app.route("/decrypt_caesar", methods=['POST'])
def caesar_decrypt():
    cipher_text = request.form['inputCipherText']
    key = int(request.form['inputKeyCipher'])
    Caesar = CaesarCipher()
    decrypted_text = Caesar.decrypt_text(cipher_text, key)
    return f"text: {cipher_text}<br>key: {key}<br>decrypted text: {decrypted_text}" 

#VIGENERE CIPHER
@app.route("/vigenere")
def vigenere():
    return render_template('vigenere.html')

@app.route("/encrypt_vigenere", methods=['POST'])
def vigenere_encrypt():
    plain_text = request.form['inputPlainText']
    key = request.form['inputKeyPlain']
    Vigenere = VigenereCipher()
    encrypted_text = Vigenere.vigenere_encrypt(plain_text, key)
    return f"text: {plain_text}<br>key: {key}<br>encrypted text: {encrypted_text}"

@app.route("/decrypt_vigenere", methods=['POST'])
def vigenere_decrypt():
    cipher_text = request.form['inputCipherText']
    key = request.form['inputKeyCipher']
    Vigenere = VigenereCipher()
    decrypted_text = Vigenere.vigenere_decrypt(cipher_text, key)
    return f"text: {cipher_text}<br>key: {key}<br>decrypted text: {decrypted_text}"

#PLAYFAIR CIPHER
@app.route("/playfair")
def playfair():
    return render_template('playfair.html')

@app.route("/playfair_matrix", methods=['POST'])
def playfair_matrix():
    key = request.form['inputKeyPlain']
    Playfair = PlayFairCipher()
    playfair_matrix = Playfair.create_playfair_matrix(key)
    return f"key: {key}<br>playfair matrix: {playfair_matrix}"

@app.route("/encrypt_playfair", methods=['POST'])
def playfair_encrypt():
    plain_text = request.form['inputPlainText']
    key = request.form['inputKeyPlain']
    Playfair = PlayFairCipher()
    playfair_matrix = Playfair.create_playfair_matrix(key)
    encrypted_text = Playfair.playfair_encrypt(plain_text, playfair_matrix)
    return f"text: {plain_text}<br>key: {key}<br>encrypted text: {encrypted_text}"

@app.route("/decrypt_playfair", methods=['POST'])
def playfair_decrypt():
    cipher_text = request.form['inputCipherText']
    key = request.form['inputKeyCipher']
    Playfair = PlayFairCipher()
    playfair_matrix = Playfair.create_playfair_matrix(key)
    decrypted_text = Playfair.playfair_decrypt(cipher_text, playfair_matrix)
    return f"text: {cipher_text}<br>key: {key}<br>decrypted text: {decrypted_text}"

#RAILFENCE CIPHER
@app.route("/railfence")
def railfence():
    return render_template('railfence.html')

@app.route("/encrypt_railfence", methods=['POST'])
def railfence_encrypt():
    plain_text = request.form['inputPlainText']
    key = int(request.form['inputKeyPlain'])
    Railfence = RailfenceCipher()
    encrypted_text = Railfence.rail_fence_encode(plain_text, key)
    return f"text: {plain_text}<br>key: {key}<br>encrypted text: {encrypted_text}"

@app.route("/decrypt_railfence", methods=['POST'])
def railfence_decrypt():
    cipher_text = request.form['inputCipherText']
    key = int(request.form['inputKeyCipher'])
    Railfence = RailfenceCipher()
    decrypted_text = Railfence.rail_fence_decode(cipher_text, key)
    return f"text: {cipher_text}<br>key: {key}<br>decrypted text: {decrypted_text}"


if __name__ == "__main__":
    app.run(host = "0.0.0.0", port = 5050, debug=True)