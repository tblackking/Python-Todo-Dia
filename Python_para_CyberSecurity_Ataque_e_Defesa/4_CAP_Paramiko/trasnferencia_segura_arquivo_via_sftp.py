import paramiko

def sftp_transfer(ip, username, password, local_file, remote_file):
    """Realiza uma transferência segura de arquivos via SFTP."""
    try:
        # Inicializa uma conexão segura via SFTP
        transport = paramiko.Transport((ip, 22))
        transport.connect(username=username, password=password)

        # Inicializa o cliente SFTP
        sftp = paramiko.SFTPClient.from_transport(transport)

        # Envia o arquivo local para o destino remoto
        sftp.put(local_file, remote_file)

        print(f"[+] Arquivo '{local_file}' enviado com sucesso para '{remote_file}'.")

        # Fecha as conexões SFTP e SSH
        sftp.close()
        transport.close()

    except Exception as e:
        print(f"[-] Falha na transferência de arquivos: {e}")

if __name__ == "__main__":
    ip = input("Digite o endereço IP do servidor: ")
    usuario = input("Digite o nome de usuário: ")
    senha = input("Digite a senha: ")
    arquivo_local = input("Digite o caminho do arquivo local: ")
    arquivo_remoto = input("Digite o caminho do arquivo remoto: ")

    sftp_transfer(ip, usuario, senha, arquivo_local, arquivo_remoto)
