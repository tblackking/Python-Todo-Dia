from scapy.all import sniff, IP, ICMP

def packet_callback(packet):
    """Callback para exibir pacotes ICMP capturados."""
    if packet.haslayer(ICMP):
        print(f"ICMP detectado -> Origem: {packet[IP].src} | Destino: {packet[IP].dst}")

print("Iniciando sniffer... Pressione CTRL+C para interromper.")
sniff(filter="icmp", prn=packet_callback, store=0)
