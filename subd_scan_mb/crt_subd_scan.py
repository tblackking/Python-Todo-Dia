import requests


def crt_sub(host):

    try:
        response = requests.get(f"https://crt.sh/?q={host}", timeout=4)

        HTML = response.text
        DOMAINS = []

        for line in HTML.splitlines():
                if '<TD>' in line and not ('<A' in line):
                    new_line = line.replace('<TD>', '').replace('</TD>', '').replace('<BR>', '\n').strip()

                    if not new_line in DOMAINS:
                        DOMAINS.append(new_line)
        
        return DOMAINS

    except Exception as e:
        return f"[ERROR] - {e}\n[//] Verify your input please\nExample - google.com"

if __name__ == "__main__":

    HOST = input("[$] HOST: ")

    print("\n[!] Executindo search in crt.sh [!]\n[!!] If anything data return, please consult again [!!]\n")

    RESULT = crt_sub(host=HOST)

    for host in RESULT:
        print(host)