import pyshark

def capture_ftp_attempts(interface):
    """Monitora tentativas de login FTP para detectar atividades suspeitas."""
    print("[+] Iniciando monitoramento de tentativas de login FTP...")

    try:
        capture = pyshark.LiveCapture(interface=interface, display_filter='ftp')
        
        for packet in capture:
            try:
                if hasattr(packet, 'ftp') and hasattr(packet.ftp, 'request_command') and packet.ftp.request_command == 'USER':
                    print(f"[+] Tentativa de login FTP - Usuário: {packet.ftp.request_arg}")
            except AttributeError:
                continue  # Pula pacotes FTP que não contêm o campo esperado

    except KeyboardInterrupt:
        print("[-] Captura interrompida pelo usuário.")

    except Exception as e:
        print(f"[-] Erro durante a captura: {e}")

if __name__ == "__main__":
    interface = input("Digite a interface de rede (ex: eth0, wlan0): ")
    capture_ftp_attempts(interface)
