import pyshark

def capture_http_dns(interface):
    """Captura pacotes HTTP e DNS para identificar atividades suspeitas."""
    print("[+] Iniciando captura de pacotes HTTP e DNS...")

    try:
        # Captura pacotes HTTP e DNS na interface fornecida
        capture = pyshark.LiveCapture(interface=interface, display_filter='http or dns')
        
        # Exibe pacotes HTTP e DNS encontrados
        for packet in capture:
            if 'HTTP' in packet:
                print(f"[+] Requisição HTTP -> Host: {packet.http.host}")
            elif 'DNS' in packet:
                print(f"[+] Consulta DNS -> Domínio: {packet.dns.qry_name}")
    
    except KeyboardInterrupt:
        print("[-] Captura interrompida pelo usuário.")
    
    except Exception as e:
        print(f"[-] Erro durante a captura: {e}")

if __name__ == "__main__":
    interface = input("Digite a interface de rede (ex: eth0, wlan0): ")
    capture_http_dns(interface)
