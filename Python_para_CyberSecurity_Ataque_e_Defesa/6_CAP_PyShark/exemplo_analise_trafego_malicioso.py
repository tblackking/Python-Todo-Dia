import pyshark

def analyze_pcap(file_path):
    """Analisa pacotes suspeitos em um arquivo .pcap."""
    print("[+] Analisando pacotes suspeitos no arquivo .pcap...")

    try:
        capture = pyshark.FileCapture(file_path, keep_packets=False)
        
        portas_suspeitas = {'21', '23', '445'}
        
        for packet in capture:
            try:
                if 'TCP' in packet and packet.tcp.dstport in portas_suspeitas:
                    print(f"[ALERTA] Porta suspeita detectada: {packet.tcp.dstport} | IP origem: {packet.ip.src} -> destino: {packet.ip.dst}")
            except AttributeError:
                # Ignora pacotes que não possuem os atributos esperados
                continue
        
        capture.close()

    except Exception as e:
        print(f"[-] Erro durante a análise: {e}")

if __name__ == "__main__":
    arquivo_pcap = input("Digite o caminho do arquivo .pcap: ")
    analyze_pcap(arquivo_pcap)
