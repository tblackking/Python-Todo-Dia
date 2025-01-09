import socket
import os


HOST = '127.0.0.1'  
PORT = 5000         
BUFFER_SIZE = 4096  
MAX_FILE_SIZE = 100 * 1024 * 1024  

def send_file(client_socket, filename):
    if not os.path.isfile(filename):
        print(f"Arquivo não encontrado: {filename}")
        return

    file_size = os.path.getsize(filename)
    if file_size > MAX_FILE_SIZE:
        print(f"O arquivo {filename} é muito grande (tamanho: {file_size} bytes).")
        return

   
    client_socket.sendall(os.path.basename(filename).encode('utf-8'))
    client_socket.recv(BUFFER_SIZE)  

    client_socket.sendall(str(file_size).encode('utf-8'))
    client_socket.recv(BUFFER_SIZE)  


    with open(filename, 'rb') as file:
        while chunk := file.read(BUFFER_SIZE):
            client_socket.sendall(chunk)
    
    print(f"Arquivo {filename} enviado com sucesso.")

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
    client_socket.connect((HOST, PORT))
    print("Conectado ao servidor.")

    while True:
        command = input("\nDigite o caminho do arquivo para enviar ou 'sair' para encerrar: ")
        if command.lower() == 'sair':
            client_socket.sendall(b'EXIT')
            print("Conexão encerrada.")
            break
        elif os.path.isfile(command):
            send_file(client_socket, command)
        else:
            print("Arquivo inválido ou não encontrado.")
