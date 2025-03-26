from pymisp import PyMISP

# Defina a URL e a API Key da instância MISP
MISP_URL = "https://misp.example.com"
MISP_API_KEY = "SUA_CHAVE_API"
USE_SSL = False  # Define se a conexão deve utilizar SSL (False se não for seguro)

try:
    misp = PyMISP(MISP_URL, MISP_API_KEY, USE_SSL)
    print("Conexão com MISP estabelecida com sucesso!")
except Exception as e:
    print(f"Erro ao conectar ao MISP: {e}")
