import ecdsa
import os

class ECCCipher:
    def __init__(self):
        self.private_key = None
        self.public_key = None
        self.key_path = r"D:\Study\Code\VScode\bmtt-nc-hutech-1911066097\lab-03\cipher\ecc\keys"
        os.makedirs(self.key_path, exist_ok=True)

    def generate_keys(self):
        self.private_key = ecdsa.SigningKey.generate()
        self.public_key = self.private_key.get_verifying_key()
        self.save_keys()

    def save_keys(self):
        with open(os.path.join(self.key_path, "private_key.pem"), "wb") as priv_file:
            priv_file.write(self.private_key.to_pem())
        
        with open(os.path.join(self.key_path, "public_key.pem"), "wb") as pub_file:
            pub_file.write(self.public_key.to_pem())

    def load_keys(self):
        with open(os.path.join(self.key_path, "private_key.pem"), "rb") as priv_file:
            self.private_key = ecdsa.SigningKey.from_pem(priv_file.read())
        
        with open(os.path.join(self.key_path, "public_key.pem"), "rb") as pub_file:
            self.public_key = ecdsa.VerifyingKey.from_pem(pub_file.read())
        return self.private_key, self.public_key

    def sign(self, message, key):
        return key.sign(message.encode('utf-8'))

    def verify(self, message, signature, key):
        try:
            key.verify(signature, message.encode('utf-8'))
            return True
        except ecdsa.BadSignatureError:
            return False