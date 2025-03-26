import socket

def client_tcp(host, port):
    """Cliente TCP que se conecta a um servidor e envia uma mensagem."""
    try:
        # Cria um socket TCP
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        # Conecta ao host e porta especificados
        client.connect((host, port))

        # Envia uma mensagem para o servidor
        mensagem = "Olá, servidor!"
        client.send(mensagem.encode())

        # Recebe a resposta do servidor
        resposta = client.recv(1024).decode()
        print(f"Resposta do servidor: {resposta}")
        
        # Fecha a conexão
        client.close()
        
    except Exception as e:
        print(f"Erro na conexão: {e}")

if __name__ == "__main__":
    ip_servidor = input("Digite o IP do servidor: ")
    porta_servidor = int(input("Digite a porta do servidor: "))

    client_tcp(ip_servidor, porta_servidor)
