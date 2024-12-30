import requests
from bs4 import BeautifulSoup

def get_all_hrefs(url):
    
    try:

        response = requests.get(url, timeout=5)
        response.raise_for_status()  
        html_content = response.text

        soup = BeautifulSoup(html_content, 'html.parser')

        hrefs = [a['href'] for a in soup.find_all('a', href=True)]
        return hrefs
    
    except requests.exceptions.RequestException as e:
        print(f"Erro ao acessar a URL: {e}")
        return []
    except Exception as e:
        print(f"Erro ao processar a página: {e}")
        return []

if __name__ == "__main__":
    url = input("[URL] (https): ")
    hrefs = get_all_hrefs(url)

    if hrefs:
        print("\n==========[LINKS ENCONTRADOS]==========\n")
        for href in hrefs:
            if "/" in href[0]:
                print(f'{url}{href}')
            else: 
                print(href)
        
        print("\n==========[LINKS ENCONTRADOS]==========\n")
    else:
        print("[!][ LINKS NOT FOUND ][!]")