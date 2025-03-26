from requests_html import HTMLSession

def extract_links(url):
    """Extrai e exibe links de uma página web."""
    session = HTMLSession()  # Inicia uma nova sessão HTTP
    response = session.get(url)  # Realiza uma requisição GET para a URL fornecida

    print(f"[+] Links encontrados na página {url}:")

    # Coleta e exibe os links encontrados na página
    for link in response.html.absolute_links:
        print(link)

if __name__ == "__main__":
    site = input("Digite a URL da página: ")
    extract_links(site)
