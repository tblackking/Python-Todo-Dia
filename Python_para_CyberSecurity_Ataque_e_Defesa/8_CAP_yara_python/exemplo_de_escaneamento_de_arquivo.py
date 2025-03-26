import yara

def scan_file(rule_path, file_path):
    """Escaneia um arquivo usando uma regra YARA."""
    try:
        # Compila a regra YARA
        rules = yara.compile(filepath=rule_path)
        
        # Realiza a verificação do arquivo
        matches = rules.match(file_path)

        # Exibe o resultado
        if matches:
            print(f"[+] Ameaça detectada no arquivo {file_path}")
            for match in matches:
                print(f" - Regra correspondente: {match.rule}")
        else:
            print(f"[-] Nenhuma ameaça detectada no arquivo {file_path}")
    
    except Exception as e:
        print(f"[-] Erro durante a varredura: {e}")

if __name__ == "__main__":
    regra = input("Digite o caminho da regra YARA: ")
    arquivo = input("Digite o caminho do arquivo a ser analisado: ")

    scan_file(regra, arquivo)
