from requests_html import HTMLSession
from urllib.parse import urljoin

def web_crawler(url, depth=2):
    """Crawleia links internos de uma página web para mapear estruturas ocultas."""
    session = HTMLSession()  # Inicia uma sessão HTTP
    visited = set()  # Conjunto para armazenar links já visitados

    def crawl(url, current_depth):
        """Função recursiva para mapear páginas internas."""
        if current_depth > depth or url in visited:
            return
        visited.add(url)
        print(f"[+] Visitando: {url}")
        
        response = session.get(url)
        for link in response.html.absolute_links:
            if url in link:  # Apenas links internos
                crawl(link, current_depth + 1)

    crawl(url, 1)

if __name__ == "__main__":
    site = input("Digite a URL inicial para o crawler: ")
    profundidade = int(input("Digite a profundidade máxima (padrão: 2): "))

    web_crawler(site, profundidade)
