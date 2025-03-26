import socket
import threading

def scan_port(ip, port):
    """Verifica se uma porta TCP está aberta."""
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)
    
    resultado = sock.connect_ex((ip, port))

    if resultado == 0:
        print(f"[+] Porta {port} aberta.")
    sock.close()

if __name__ == "__main__":
    alvo = input("Digite o endereço IP alvo: ")
    portas = range(1, 1025)

    for porta in portas:
        thread = threading.Thread(target=scan_port, args=(alvo, porta))
        thread.start()
