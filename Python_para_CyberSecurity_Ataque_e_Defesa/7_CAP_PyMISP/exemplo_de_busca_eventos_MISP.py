from pymisp import PyMISP

MISP_URL = "https://misp.example.com"
MISP_API_KEY = "SUA_CHAVE_API"
USE_SSL = False

def buscar_evento(misp, termo_busca):
    """Busca eventos na MISP relacionados a um termo específico."""
    try:
        resultado = misp.search(controller='events', value=termo_busca)
        if resultado:
            print(f"[+] {len(resultado)} eventos encontrados para: {termo_busca}")
            for evento in resultado:
                print(f"  - Evento ID: {evento['Event']['id']} | Descrição: {evento['Event']['info']}")
        else:
            print("[-] Nenhum evento encontrado para este termo.")
    except Exception as e:
        print(f"[-] Falha na busca: {e}")

if __name__ == "__main__":
    misp = PyMISP(MISP_URL, MISP_API_KEY, USE_SSL)
    termo = input("Digite o termo de busca: ")
    buscar_evento(misp, termo)
