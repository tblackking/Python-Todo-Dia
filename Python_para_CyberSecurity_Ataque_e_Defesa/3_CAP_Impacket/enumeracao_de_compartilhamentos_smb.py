from impacket.smbconnection import SMBConnection

def smb_enum(ip, username, password, domain=''):
    """Enumera os compartilhamentos SMB disponíveis em um sistema remoto."""
    try:
        # Estabelece uma conexão SMB com a máquina alvo
        conn = SMBConnection(ip, ip)
        conn.login(username, password, domain)

        print(f"[+] Compartilhamentos disponíveis em {ip}:")
        for share in conn.listShares():
            print(f"  - {share['shi1_netname'].decode().strip()}")
        conn.close()

    except Exception as e:
        print(f"[-] Falha na conexão SMB: {e}")

if __name__ == "__main__":
    ip = input("Digite o endereço IP do servidor SMB: ")
    usuario = input("Digite o nome de usuário: ")
    senha = input("Digite a senha: ")

    smb_enum(ip, usuario, senha)
