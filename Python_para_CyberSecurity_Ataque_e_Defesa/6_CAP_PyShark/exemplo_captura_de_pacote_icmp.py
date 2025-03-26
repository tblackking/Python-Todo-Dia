import pyshark

def capture_icmp(interface):
    """Captura pacotes ICMP (Ping) em tempo real."""
    print("[+] Iniciando captura de pacotes ICMP...")
    
    try:
        # Captura pacotes ICMP em tempo real
        capture = pyshark.LiveCapture(interface=interface, display_filter='icmp')
        
        # Exibe cada pacote ICMP detectado
        for packet in capture:
            print(f"[+] ICMP detectado - Origem: {packet.ip.src} | Destino: {packet.ip.dst}")
    
    except KeyboardInterrupt:
        print("[-] Captura interrompida pelo usuário.")
    
    except Exception as e:
        print(f"[-] Erro durante a captura: {e}")

if __name__ == "__main__":
    interface = input("Digite a interface de rede (ex: eth0, wlan0): ")
    capture_icmp(interface)
