import yara
import psutil  # Biblioteca para manipulação de processos

def scan_memory(rule_path):
    """Escaneia processos em execução utilizando regras YARA."""
    try:
        # Compila a regra YARA
        rules = yara.compile(filepath=rule_path)

        # Percorre processos em execução
        for process in psutil.process_iter(['pid', 'name']):
            try:
                with open(f"/proc/{process.info['pid']}/mem", 'rb') as mem_file:
                    matches = rules.match(data=mem_file.read())
                    if matches:
                        print(f"[+] Processo suspeito encontrado: {process.info['name']} (PID: {process.info['pid']})")
            except (PermissionError, FileNotFoundError):
                continue
    except Exception as e:
        print(f"[-] Erro durante a análise de memória: {e}")

if __name__ == "__main__":
    regra = input("Digite o caminho da regra YARA: ")
    scan_memory(regra)
