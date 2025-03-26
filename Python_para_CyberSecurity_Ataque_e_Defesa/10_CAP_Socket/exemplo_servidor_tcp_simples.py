import socket

def server_tcp(host, port):
    """Servidor TCP que aceita conexões e responde às mensagens."""
    try:
        # Cria um socket TCP
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        # Liga o servidor ao IP e porta especificados
        server.bind((host, port))
        
        # Permite até 5 conexões simultâneas
        server.listen(5)
        print(f"Servidor iniciado em {host}:{port}")

        # Loop para aceitar conexões indefinidamente
        while True:
            client, addr = server.accept()
            print(f"Conexão recebida de {addr[0]}:{addr[1]}")

            # Recebe mensagem do cliente
            mensagem = client.recv(1024).decode()
            print(f"Mensagem recebida: {mensagem}")

            # Envia uma resposta para o cliente
            resposta = "Mensagem recebida com sucesso."
            client.send(resposta.encode())

            # Fecha a conexão com o cliente
            client.close()
    except Exception as e:
        print(f"Erro no servidor: {e}")

if __name__ == "__main__":
    ip = "0.0.0.0"
    porta = int(input("Digite a porta para o servidor: "))

    server_tcp(ip, porta)
