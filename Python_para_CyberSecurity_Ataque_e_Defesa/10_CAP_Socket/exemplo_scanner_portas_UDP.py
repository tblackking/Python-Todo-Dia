import socket

def scan_udp(ip, port):
    """Verifica se uma porta UDP está aberta."""
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.settimeout(1)

    try:
        sock.sendto(b"Teste", (ip, port))
        data, _ = sock.recvfrom(1024)
        print(f"[+] Porta UDP {port} está aberta.")
    except socket.timeout:
        print(f"[-] Porta UDP {port} fechada ou filtrada.")
    finally:
        sock.close()

if __name__ == "__main__":
    alvo = input("Digite o endereço IP alvo: ")
    porta = int(input("Digite a porta UDP a ser verificada: "))

    scan_udp(alvo, porta)
