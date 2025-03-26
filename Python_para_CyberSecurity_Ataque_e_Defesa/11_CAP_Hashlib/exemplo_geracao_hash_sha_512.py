import hashlib

def generate_sha512(data):
    """Gera um hash SHA-512 a partir de uma string."""
    sha512_hash = hashlib.sha512(data.encode())
    return sha512_hash.hexdigest()

if __name__ == "__main__":
    mensagem = input("Digite a mensagem para gerar o hash SHA-512: ")
    hash_gerado = generate_sha512(mensagem)
    print(f"Hash SHA-512 gerado: {hash_gerado}")
