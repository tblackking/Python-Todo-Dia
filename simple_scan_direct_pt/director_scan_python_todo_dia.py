import requests 
from concurrent.futures import ThreadPoolExecutor
from colorama import init, Fore


def request_validator(direct, host):
    try:
        response = requests.get(f"https://{host}/{direct}", timeout=1.5)
        status_code_ = response.status_code

        if status_code_ == 200: 
            return True, status_code_ 
        else: 
            return False, status_code_ 

    except Exception as error:
        return f'[ERROR] - {error}'


def execute_direct_scan(direct, host, positive_color, negative_color, reset_color):

    request_validator_, status_code_ = request_validator(direct, host)

    if request_validator_:
        print(f"{positive_color}[!!] https://{host}/{direct} | [{status_code_}]     {reset_color}")
    else:
        print(f"{negative_color}[//]  https://{host}/{direct} | [{status_code_}]    {reset_color}", end="\r")


if __name__ == "__main__":
    init()
    GREEN_COLOR = Fore.GREEN
    RESET_COLOR = Fore.RESET
    RED_COLOR = Fore.RED

    HOST = input("[$] HOST: ")
    LIST_DIRECT = input("[$] LIST_DIRECT: ")
    THREADS = input("[$] THREADS: ")

    list_to_read = open(fr"{LIST_DIRECT}", 'r', 
                        encoding='utf-8').read().splitlines()
    
    print(f"\n[#] EXECUTING DIRECTORY SCAN -> {HOST} USING {THREADS} THREADS [#] \n")

    with ThreadPoolExecutor(max_workers=int(THREADS)) as executor:
        for dct in list_to_read:
            executor.submit(execute_direct_scan, 
                            dct, HOST,
                            GREEN_COLOR, RED_COLOR, RESET_COLOR)