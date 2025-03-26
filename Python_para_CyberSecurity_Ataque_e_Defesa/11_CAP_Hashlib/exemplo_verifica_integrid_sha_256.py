import hashlib

def file_hash(file_path):
    """Gera um hash SHA-256 para um arquivo."""
    sha256_hash = hashlib.sha256()

    # Lê o arquivo em blocos para evitar sobrecarga de memória
    with open(file_path, "rb") as file:
        while chunk := file.read(4096):
            sha256_hash.update(chunk)

    # Retorna o hash gerado em formato hexadecimal
    return sha256_hash.hexdigest()

def verify_integrity(file_path, expected_hash):
    """Verifica se um arquivo corresponde ao hash esperado."""
    file_hash_value = file_hash(file_path)
    if file_hash_value == expected_hash:
        print("[+] O arquivo é legítimo e não foi alterado.")
    else:
        print("[-] O arquivo foi modificado ou corrompido.")

if __name__ == "__main__":
    caminho_arquivo = input("Digite o caminho do arquivo a ser verificado: ")
    hash_esperado = input("Digite o hash esperado para validação: ")

    verify_integrity(caminho_arquivo, hash_esperado)
