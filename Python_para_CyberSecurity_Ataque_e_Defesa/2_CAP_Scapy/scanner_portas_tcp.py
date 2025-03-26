from scapy.all import IP, TCP, sr1, conf

# Desabilita logs adicionais do Scapy para tornar a saída mais limpa
conf.verb = 0  

def scan_port(ip, port):
    """Verifica se uma porta TCP está aberta ou fechada."""
    
    # Cria um pacote TCP com flag SYN ativada
    packet = IP(dst=ip) / TCP(dport=port, flags='S')
    
    # Envia o pacote e aguarda uma única resposta
    response = sr1(packet, timeout=1)

    # Analisa a resposta recebida
    if response is None:
        print(f"Porta {port} está fechada ou filtrada.")
    elif response.haslayer(TCP) and response.getlayer(TCP).flags == 0x12:
        print(f"Porta {port} está ABERTA.")
        
        # Envia um pacote RST (Reset) para encerrar a conexão
        sr1(IP(dst=ip) / TCP(dport=port, flags='R'), timeout=1)
    else:
        print(f"Porta {port} está fechada ou filtrada.")

if __name__ == "__main__":
    alvo = input("Digite o endereço IP alvo: ")
    portas = [22, 80, 443, 3306, 8080]  # Lista padrão de portas comuns

    for porta in portas:
        scan_port(alvo, porta)
