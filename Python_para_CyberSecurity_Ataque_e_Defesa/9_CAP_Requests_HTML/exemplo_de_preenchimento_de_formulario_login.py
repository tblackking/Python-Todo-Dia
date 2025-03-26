from requests_html import HTMLSession

def login_automation(url, username, password):
    """Automatiza o preenchimento e envio de um formulário de login."""
    session = HTMLSession()
    response = session.get(url)  # Acessa a página web

    # Localiza o formulário na página
    form = response.html.find("form", first=True)

    if form:
        # Identifica a URL de envio do formulário
        action_url = form.attrs.get("action")
        full_url = url + action_url if "http" not in action_url else action_url

        # Envia os dados de login
        data = {
            "username": username,
            "password": password
        }
        resultado = session.post(full_url, data=data)

        # Verifica se o login foi bem-sucedido
        if "login inválido" in resultado.text.lower():
            print("[-] Login falhou.")
        else:
            print("[+] Login bem-sucedido.")
    else:
        print("[-] Nenhum formulário encontrado na página.")

if __name__ == "__main__":
    url = input("Digite a URL da página de login: ")
    usuario = input("Digite o nome de usuário: ")
    senha = input("Digite a senha: ")

    login_automation(url, usuario, senha)
