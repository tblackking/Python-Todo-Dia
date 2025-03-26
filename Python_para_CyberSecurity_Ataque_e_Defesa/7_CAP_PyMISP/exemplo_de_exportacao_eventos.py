from pymisp import PyMISP

MISP_URL = "https://misp.example.com"
MISP_API_KEY = "SUA_CHAVE_API"
USE_SSL = False

def exportar_eventos(misp, formato):
    """Exporta eventos da MISP no formato especificado."""
    try:
        eventos = misp.download_last(format=formato)
        nome_arquivo = f"eventos_exportados.{formato}"
        
        with open(nome_arquivo, "wb") as arquivo:
            arquivo.write(eventos)
        
        print(f"[+] Eventos exportados com sucesso para {nome_arquivo}")
    except Exception as e:
        print(f"[-] Falha na exportação de eventos: {e}")

if __name__ == "__main__":
    misp = PyMISP(MISP_URL, MISP_API_KEY, USE_SSL)
    formato = input("Digite o formato de exportação (ex: json, csv, xml): ")
    exportar_eventos(misp, formato)
