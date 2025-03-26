from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
import os

def encrypt_message(key, plaintext):
    """Criptografa uma mensagem usando AES."""
    
    # Gera um IV (Vetor de Inicialização) aleatório
    iv = os.urandom(16)
    
    # Cria uma instância do algoritmo AES no modo CFB
    cipher = Cipher(algorithms.AES(key), modes.CFB(iv), backend=default_backend())
    encryptor = cipher.encryptor()

    # Criptografa a mensagem e concatena com o IV
    ciphertext = encryptor.update(plaintext.encode()) + encryptor.finalize()
    return iv + ciphertext

def decrypt_message(key, encrypted_data):
    """Descriptografa uma mensagem criptografada com AES."""
    
    # Extrai o IV dos primeiros 16 bytes
    iv = encrypted_data[:16]
    ciphertext = encrypted_data[16:]
    
    # Inicializa o algoritmo AES para descriptografar
    cipher = Cipher(algorithms.AES(key), modes.CFB(iv), backend=default_backend())
    decryptor = cipher.decryptor()

    # Descriptografa a mensagem e retorna como texto
    plaintext = decryptor.update(ciphertext) + decryptor.finalize()
    return plaintext.decode()

if __name__ == "__main__":
    # Gera uma chave AES de 256 bits
    key = os.urandom(32)

    mensagem = input("Digite a mensagem para criptografar: ")
    encrypted_data = encrypt_message(key, mensagem)
    print(f"\nMensagem criptografada: {encrypted_data.hex()}")

    decrypted_data = decrypt_message(key, encrypted_data)
    print(f"\nMensagem descriptografada: {decrypted_data}")
