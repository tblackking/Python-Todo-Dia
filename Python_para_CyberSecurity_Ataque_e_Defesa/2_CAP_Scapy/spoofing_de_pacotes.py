from scapy.all import IP, ICMP, send

def spoof_packet(target_ip, spoof_ip):
    """Envia um pacote ICMP falsificado."""
    packet = IP(src=spoof_ip, dst=target_ip) / ICMP()
    send(packet)
    print(f"Pacote ICMP enviado de {spoof_ip} para {target_ip}")

if __name__ == "__main__":
    alvo = input("Digite o endereço IP alvo: ")
    ip_falso = input("Digite o endereço IP falso (spoof): ")
    spoof_packet(alvo, ip_falso)
