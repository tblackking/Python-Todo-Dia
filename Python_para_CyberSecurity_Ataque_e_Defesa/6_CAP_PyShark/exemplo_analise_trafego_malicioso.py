import pyshark

def analyze_pcap(file_path):
    """Analisa pacotes suspeitos em um arquivo .pcap."""
    print("[+] Analisando pacotes suspeitos no arquivo .pcap...")

    try:
        capture = pyshark.FileCapture(file_path)
        
        # Detecta pacotes suspeitos utilizando portas comuns de ataque
        for packet in capture:
            if hasattr(packet, 'tcp') and packet.tcp.dstport in ['21', '23', '445']:
                print(f"[ALERTA] Porta suspeita detectada: {packet.tcp.dstport}")
    
    except Exception as e:
        print(f"[-] Erro durante a análise: {e}")

if __name__ == "__main__":
    arquivo_pcap = input("Digite o caminho do arquivo .pcap: ")
    analyze_pcap(arquivo_pcap)
