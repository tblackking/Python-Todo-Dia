import paramiko

def ssh_command(ip, username, password, command):
    """Conecta-se a um host via SSH e executa um comando remoto."""
    try:
        # Inicializa o cliente SSH
        client = paramiko.SSHClient()

        # Permite aceitar automaticamente a chave SSH do host remoto
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        # Estabelece a conexão SSH com o host remoto
        client.connect(ip, username=username, password=password)

        # Executa o comando remoto
        stdin, stdout, stderr = client.exec_command(command)

        # Exibe a saída padrão (stdout) do comando
        print(f"Saída:\n{stdout.read().decode().strip()}")

        # Verifica se houve erro durante a execução
        error = stderr.read().decode().strip()
        if error:
            print(f"Erro:\n{error}")

        # Fecha a conexão SSH
        client.close()

    except Exception as e:
        print(f"[-] Falha na conexão ou execução do comando: {e}")

if __name__ == "__main__":
    ip = input("Digite o endereço IP do servidor: ")
    usuario = input("Digite o nome de usuário: ")
    senha = input("Digite a senha: ")
    comando = input("Digite o comando a ser executado: ")

    ssh_command(ip, usuario, senha, comando)
