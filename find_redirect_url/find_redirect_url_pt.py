import requests 
from colorama import init, Fore


def response_valid_302(url):
    try:
        response = requests.get(url=url, allow_redirects=False, timeout=2)
        response_status_code = response.status_code
        redirected_url = None
        
        if response_status_code == 302:
            redirected_url = response.headers['Location']
            return True, response_status_code, redirected_url
            
        return False, response_status_code, redirected_url
    except requests.ConnectionError as error:
        return f"[ERROR] - {error}"


def redirect_url_execute(url, positive_c, negative_c, reset_c):
    boolean_value, status_code, redirect = response_valid_302(url)

    if boolean_value == True: 
        print(f"{positive_c}[!] FIND REDIRECT URL - {url} | REDIRECT - {redirect}   {reset_c}")
    else:
        print(f"{negative_c}[!] TRY URL - {url}     {reset_c}")


if __name__ == "__main__":
    init()
    GREEN_COLOR = Fore.GREEN
    RESET_COLOR = Fore.RESET
    RED_COLOR = Fore.RED

    URL = input("[$] URL(http/https): ")
    
    redirect_url_execute(URL.lower(), GREEN_COLOR, RED_COLOR, RESET_COLOR)

  