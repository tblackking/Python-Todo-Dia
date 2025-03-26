from cryptography.hazmat.primitives import hashes

def generate_hash(data):
    """Gera um hash SHA-256 para uma string."""
    digest = hashes.Hash(hashes.SHA256())
    digest.update(data.encode())
    return digest.finalize().hex()

def verify_hash(data, expected_hash):
    """Verifica se um hash gerado corresponde ao valor esperado."""
    generated_hash = generate_hash(data)
    if generated_hash == expected_hash:
        print("[+] O hash é válido!")
    else:
        print("[-] O hash NÃO é válido!")

if __name__ == "__main__":
    mensagem = input("Digite a mensagem para gerar o hash: ")
    hash_gerado = generate_hash(mensagem)
    print(f"\nHash gerado: {hash_gerado}")

    hash_verificacao = input("\nDigite o hash para verificar: ")
    verify_hash(mensagem, hash_verificacao)
