from cryptography.hazmat.primitives.asymmetric import dh
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
import os

def generate_client_key_pair(parameters):
    private_key = parameters.generate_private_key()
    public_key = private_key.public_key()
    return private_key, public_key

def derive_shared_secret(private_key, server_public_key):
    shared_key = private_key.exchange(server_public_key)
    return shared_key

def main():
    file_path = r"D:\Study\Code\VScode\bmtt-nc-hutech-1911066097\lab-04\dh_key_pair\server_public_key.pem"

    if not os.path.exists(file_path):
        print("Không tìm thấy tệp server_public_key.pem")
        return

    with open(file_path, "rb") as f:
        server_public_key = serialization.load_pem_public_key(f.read())
    
    parameters = server_public_key.parameters()
    private_key, public_key = generate_client_key_pair(parameters)

    shared_secret = derive_shared_secret(private_key, server_public_key)

    print("Shared Secret:", shared_secret.hex())

if __name__ == "__main__":
    main()
