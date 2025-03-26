import hmac
import hashlib

def generate_signature(message, secret_key):
    """Gera uma assinatura digital utilizando HMAC-SHA256."""
    signature = hmac.new(secret_key.encode(), message.encode(), hashlib.sha256).hexdigest()
    return signature

def verify_signature(message, secret_key, expected_signature):
    """Verifica se a assinatura digital corresponde ao esperado."""
    generated_signature = generate_signature(message, secret_key)
    if generated_signature == expected_signature:
        print("[+] Assinatura válida e mensagem autêntica.")
    else:
        print("[-] Assinatura inválida ou mensagem adulterada.")

if __name__ == "__main__":
    mensagem = input("Digite a mensagem original: ")
    chave_secreta = input("Digite a chave secreta: ")

    assinatura = generate_signature(mensagem, chave_secreta)
    print(f"Assinatura digital gerada: {assinatura}")

    assinatura_verificacao = input("Digite a assinatura para verificação: ")
    verify_signature(mensagem, chave_secreta, assinatura_verificacao)
