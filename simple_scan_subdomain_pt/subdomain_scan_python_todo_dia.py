import requests 
from concurrent.futures import ThreadPoolExecutor
from colorama import init, Fore


def request_validator(subdomain, host):
    try:
        requests.get(f"http://{subdomain}.{host}")
    except requests.ConnectionError:
        return False 
    else:
        return True


def execute_subdomain_scan(subdomain, host, positive_color, negative_color, reset_color):
    if request_validator(subdomain, host):
        print(f"{positive_color}[!!] {subdomain}.{host}      {reset_color}")
    else:
        print(f"{negative_color}[//] {subdomain}.{host}     {reset_color}", end="\r")


if __name__ == "__main__":
    init()
    GREEN_COLOR = Fore.GREEN
    RESET_COLOR = Fore.RESET
    RED_COLOR = Fore.RED

    HOST = input("[$] HOST: ")
    LIST_SUB = input("[$] LIST_SUB: ")
    THREADS = input("[$] THREADS: ")

    list_to_read = open(fr"{LIST_SUB}", 'r', 
                        encoding='utf-8').read().splitlines()
    
    print(f"\n[#] EXECUTING SUBDOMAIN SCAN -> {HOST} USING {THREADS} THREADS [#] \n")

    with ThreadPoolExecutor(max_workers=int(THREADS)) as executor:
        for subd in list_to_read:
            executor.submit(execute_subdomain_scan, 
                            subd, HOST,
                            GREEN_COLOR, RED_COLOR, RESET_COLOR)