import hashlib

def generate_sha256(data):
    """Gera um hash SHA-256 a partir de uma string."""
    # Cria um objeto hash SHA-256
    sha256_hash = hashlib.sha256(data.encode())
    
    # Retorna o hash gerado em formato hexadecimal
    return sha256_hash.hexdigest()

if __name__ == "__main__":
    mensagem = input("Digite a mensagem para gerar o hash SHA-256: ")
    hash_gerado = generate_sha256(mensagem)
    print(f"Hash SHA-256 gerado: {hash_gerado}")
