import yara
import os

def scan_directory(rule_path, directory_path):
    """Escaneia um diretório inteiro utilizando regras YARA."""
    try:
        # Compila a regra YARA
        rules = yara.compile(filepath=rule_path)

        # Percorre os arquivos do diretório
        for root, _, files in os.walk(directory_path):
            for file in files:
                file_path = os.path.join(root, file)
                matches = rules.match(file_path)
                if matches:
                    print(f"[+] Ameaça detectada no arquivo {file_path}")
                    for match in matches:
                        print(f" - Regra correspondente: {match.rule}")
    except Exception as e:
        print(f"[-] Erro durante a varredura: {e}")

if __name__ == "__main__":
    regra = input("Digite o caminho da regra YARA: ")
    diretorio = input("Digite o caminho do diretório a ser analisado: ")

    scan_directory(regra, diretorio)
