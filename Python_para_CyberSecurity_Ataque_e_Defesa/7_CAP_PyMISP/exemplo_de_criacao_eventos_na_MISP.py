from pymisp import PyMISP, MISPEvent

MISP_URL = "https://misp.example.com"
MISP_API_KEY = "SUA_CHAVE_API"
USE_SSL = False

def criar_evento(misp, categoria, info, atributo, tipo):
    """Cria um evento na MISP com um IoC associado."""
    
    # Cria um novo evento na plataforma MISP
    evento = MISPEvent()
    evento.info = info
    evento.add_attribute(atributo, tipo=tipo, category=categoria)

    try:
        resultado = misp.add_event(evento)
        print(f"[+] Evento criado com sucesso. ID do evento: {resultado['Event']['id']}")
    except Exception as e:
        print(f"[-] Falha ao criar o evento: {e}")

if __name__ == "__main__":
    misp = PyMISP(MISP_URL, MISP_API_KEY, USE_SSL)
    categoria = "Network activity"
    informacao = "Atividade suspeita detectada na rede"
    atributo = "192.168.1.100"
    tipo = "ip-dst"

    criar_evento(misp, categoria, informacao, atributo, tipo)
