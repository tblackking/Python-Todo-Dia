from requests_html import HTMLSession

def scrape_dynamic_content(url):
    """Coleta conteúdo gerado dinamicamente por JavaScript."""
    session = HTMLSession()
    response = session.get(url)

    # Renderiza o JavaScript da página
    response.html.render(timeout=20)

    print(f"[+] Conteúdo dinâmico extraído:\n{response.html.text}")

if __name__ == "__main__":
    url = input("Digite a URL da página que utiliza JavaScript: ")
    scrape_dynamic_content(url)
