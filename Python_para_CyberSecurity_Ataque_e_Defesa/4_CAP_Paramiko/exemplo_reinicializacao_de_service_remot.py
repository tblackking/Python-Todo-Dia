import paramiko

def restart_service(ip, username, password, service_name):
    """Reinicia um serviço remoto via SSH."""
    try:
        # Inicializa o cliente SSH
        client = paramiko.SSHClient()
        
        # Permite aceitar automaticamente a chave SSH do host remoto
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        # Estabelece a conexão SSH com o host remoto
        client.connect(ip, username=username, password=password)

        # Comando remoto para reiniciar o serviço
        command = f"sudo systemctl restart {service_name}"

        # Executa o comando no servidor remoto
        stdin, stdout, stderr = client.exec_command(command)

        # Exibe a saída padrão (stdout) do comando
        output = stdout.read().decode().strip()
        erro = stderr.read().decode().strip()

        if output:
            print(f"[+] Saída: {output}")
        if erro:
            print(f"[-] Erro: {erro}")
        else:
            print(f"[+] O serviço '{service_name}' foi reiniciado com sucesso.")
        
        # Fecha a conexão SSH
        client.close()

    except Exception as e:
        print(f"[-] Falha ao reiniciar o serviço: {e}")

if __name__ == "__main__":
    ip = input("Digite o endereço IP do servidor: ")
    usuario = input("Digite o nome de usuário: ")
    senha = input("Digite a senha: ")
    servico = input("Digite o nome do serviço a ser reiniciado (ex: apache2, nginx, mysql): ")

    restart_service(ip, usuario, senha, servico)
