from flask import Flask, render_template, request, jsonify
from Cipher.Caesar import CaesarCipher

app = Flask(__name__)   

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/caesar")
def caesar():
    return render_template('caesar.html')

@app.route("/encrypt", methods=['POST'])
def caesar_encrypt():
    plain_text = request.form['inputPlainText']
    key = int(request.form['inputKeyPlain'])
    Caesar = CaesarCipher()
    encrypted_text = Caesar.encrypt_text(plain_text, key)
    return f"text: {plain_text}<br>key: {key}<br>encrypted text: {encrypted_text}"

@app.route("/decrypt", methods=['POST'])
def caesar_decrypt():
    cipher_text = request.form['inputCipherText']
    key = int(request.form['inputKeyCipher'])
    Caesar = CaesarCipher()
    decrypted_text = Caesar.decrypt_text(cipher_text, key)
    return f"text: {cipher_text}<br>key: {key}<br>decrypted text: {decrypted_text}" 

if __name__ == "__main__":
    app.run(host = "0.0.0.0", port = 5050, debug=True)