import socket
import os


HOST = '0.0.0.0'    
PORT = 5000         
BUFFER_SIZE = 4096  
SAVE_DIR = 'recebidos/'  

if not os.path.exists(SAVE_DIR):
    os.makedirs(SAVE_DIR)


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
    server_socket.bind((HOST, PORT))
    server_socket.listen(5)
    print(f"Servidor aguardando conexão na porta {PORT}...")

    conn, addr = server_socket.accept()
    with conn:
        print(f"Conexão estabelecida com {addr}")

        while True:
            
            filename = conn.recv(BUFFER_SIZE).decode('utf-8')
            if filename == 'EXIT':
                print("Cliente encerrou a conexão.")
                break
            
            conn.sendall(b'FILENAME_RECEIVED')  
            
            
            file_size = int(conn.recv(BUFFER_SIZE).decode('utf-8'))
            conn.sendall(b'SIZE_RECEIVED')  
            

            filepath = os.path.join(SAVE_DIR, filename)
            with open(filepath, 'wb') as file:
                bytes_received = 0
                while bytes_received < file_size:
                    chunk = conn.recv(min(BUFFER_SIZE, file_size - bytes_received))
                    if not chunk:
                        break
                    file.write(chunk)
                    bytes_received += len(chunk)

            print(f"Arquivo {filename} recebido e salvo em {filepath}")
