import hashlib
import os
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import hashes

def get_sha256_hash(text): 
    data = text.encode('utf-8')
    sha256 = hashlib.sha256()
    sha256.update(data)
    return sha256.hexdigest()

def aes_encrypt(key, plaintext): 
    nonce = os.urandom(12)
    cipher = Cipher(algorithms.AES(key), modes.GCM(nonce))
    encryptor = cipher.encryptor()
    ciphertext = encryptor.update(plaintext.encode('utf-8')) + encryptor.finalize()
    return nonce, ciphertext, encryptor.tag

def aes_decrypt(key, nonce, ciphertext, tag):
    cipher = Cipher(algorithms.AES(key), modes.GCM(nonce, tag))
    decryptor = cipher.decryptor()
    try:
        decrypted_data = decryptor.update(ciphertext) + decryptor.finalize()
        return decrypted_data.decode('utf-8')
    except Exception:
        return "Помилка розшифрування!"

def generate_rsa_keys():
    private_key = rsa.generate_private_key(public_exponent=65537, key_size=2048)
    return private_key, private_key.public_key()

def sign_message(message, private_key): 
    return private_key.sign(
        message.encode('utf-8'),
        padding.PSS(mgf=padding.MGF1(hashes.SHA256()), salt_length=padding.PSS.MAX_LENGTH),
        hashes.SHA256()
    )

def verify_signature(message, signature, public_key): 
    try:
        public_key.verify(
            signature,
            message.encode('utf-8'),
            padding.PSS(mgf=padding.MGF1(hashes.SHA256()), salt_length=padding.PSS.MAX_LENGTH),
            hashes.SHA256()
        )
        return True
    except Exception:
        return False

if __name__ == "__main__":
    msg = "Секретне повідомлення 2026"
    print(f"Оригінал: {msg}\n")

    print(f"SHA-256: {get_sha256_hash(msg)}")
    
    aes_key = os.urandom(32)
    n, ct, tag = aes_encrypt(aes_key, msg)
    print(f"AES Encrypted: {ct.hex()}")
    print(f"AES Decrypted: {aes_decrypt(aes_key, n, ct, tag)}")

    priv_key, pub_key = generate_rsa_keys()
    sig = sign_message(msg, priv_key)
    print(f"RSA Signature valid: {verify_signature(msg, sig, pub_key)}")