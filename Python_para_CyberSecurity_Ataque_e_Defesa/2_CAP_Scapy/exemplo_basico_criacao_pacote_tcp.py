from scapy.all import IP, TCP

# Cria um pacote com cabeçalho IP e TCP
pacote = IP(dst='192.168.1.1') / TCP(dport=80, flags='S')

# Exibe detalhes técnicos do pacote gerado
pacote.show()
