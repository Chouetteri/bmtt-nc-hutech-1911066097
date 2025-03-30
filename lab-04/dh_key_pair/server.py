from cryptography.hazmat.primitives.asymmetric import dh
from cryptography.hazmat.primitives import serialization
import os

def generate_dh_parameters():
    parameters = dh.generate_parameters(generator=2, key_size=2048)
    return parameters

def generate_server_key_pair(parameters):
    private_key = parameters.generate_private_key()
    public_key = private_key.public_key()
    return private_key, public_key

def main():
    parameters = generate_dh_parameters()
    private_key, public_key = generate_server_key_pair(parameters)

    save_path = r"D:\Study\Code\VScode\bmtt-nc-hutech-1911066097\lab-04\dh_key_pair"
    
    os.makedirs(save_path, exist_ok=True)
    
    with open(os.path.join(save_path, "server_public_key.pem"), "wb") as f:
        f.write(public_key.public_bytes(encoding=serialization.Encoding.PEM,format=serialization.PublicFormat.SubjectPublicKeyInfo))

if __name__ == "__main__":
    main()

