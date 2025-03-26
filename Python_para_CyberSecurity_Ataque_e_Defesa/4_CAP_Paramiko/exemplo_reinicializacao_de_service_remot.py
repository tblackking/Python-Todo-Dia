import paramiko

def restart_service(ip, username, password, service_name):
    """Reinicia um serviço remotamente via SSH."""
    command = f"sudo systemctl restart {service_name}"
    ssh_command(ip, username, password, command)

if __name__ == "__main__":
    ip = input("Digite o endereço IP do servidor: ")
    usuario = input("Digite o nome de usuário: ")
    senha = input("Digite a senha: ")
    servico = input("Digite o nome do serviço a ser reiniciado: ")

    restart_service(ip, usuario, senha, servico)
