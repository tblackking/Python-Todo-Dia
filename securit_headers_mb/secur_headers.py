import requests

def validate_security_headers(url):

    required_headers = {
        "Strict-Transport-Security": "Forçar HTTPS",
        "Content-Security-Policy": "Previne ataques de XSS e de injeção",
        "X-Content-Type-Options": "Contra ataques de MIME sniffing",
        "X-Frame-Options": "Prevenção de iframes não autorizados",
        "X-XSS-Protection": "Contra XSS no navegador",
        "Referrer-Policy": "Controla as informações enviadas no cabeçalho Referer",
        "Permissions-Policy": "Restringe o uso de APIs sensíveis"
    }

    results = {}
    try:

        response = requests.head(url, allow_redirects=False, timeout=10)
        headers = response.headers

        for header, description in required_headers.items():
            if header in headers:
                results[header] = {"status": "[!!] PRESENT", "value": headers[header]}
            else:
                results[header] = {"status": "[//] NOT PRESENT", "description": description}
        
        return results

    except requests.exceptions.RequestException as e:
        return f"[ERROR] - {e}\n[//] Verify your input please\nExample - https://google.com"
    


if __name__ == "__main__":

    URL = input("[$] URL: ")

    security_results = validate_security_headers(URL)

    print("\n[!] Executindo search in crt.sh [!]\n[!!] If anything data return, please consult again [!!]\n")

    print("====================================================")

    for header, info in security_results.items():
        if "status" in info:
            print(f"{header}: {info['status']}")
        else:
            print(f"{header}: {info}")
    
    print("====================================================")