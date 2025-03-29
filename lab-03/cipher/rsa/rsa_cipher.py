import rsa
import os

class RSACipher:
    def __init__(self):
        self.private_key = None
        self.public_key = None
        self.key_path = r"D:\Study\Code\VScode\bmtt-nc-hutech-1911066097\lab-03\cipher\rsa\keys"
        os.makedirs(self.key_path, exist_ok=True)

    def generate_keys(self):
        self.public_key, self.private_key = rsa.newkeys(2048)
        self.save_keys()

    def save_keys(self):
        with open(os.path.join(self.key_path, "private_key.pem"), "wb") as priv_file:
            priv_file.write(self.private_key.save_pkcs1("PEM"))
        
        with open(os.path.join(self.key_path, "public_key.pem"), "wb") as pub_file:
            pub_file.write(self.public_key.save_pkcs1("PEM"))

    def load_keys(self):
        with open(os.path.join(self.key_path, "private_key.pem"), "rb") as priv_file:
            self.private_key = rsa.PrivateKey.load_pkcs1(priv_file.read())
        
        with open(os.path.join(self.key_path, "public_key.pem"), "rb") as pub_file:
            self.public_key = rsa.PublicKey.load_pkcs1(pub_file.read())
        return self.private_key, self.public_key

    def encrypt(self, message, key):
        return rsa.encrypt(message.encode(), key)

    def decrypt(self, ciphertext, key):
        return rsa.decrypt(ciphertext, key).decode()

    def sign(self, message, key):
        return rsa.sign(message.encode(), key, "SHA-256")

    def verify(self, message, signature, key):
        try:
            rsa.verify(message.encode(), signature, key)
            return True
        except rsa.VerificationError:
            return False