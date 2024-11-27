import socket
from concurrent.futures import ThreadPoolExecutor
from colorama import init, Fore

def socket_validator(host, port):
    socket_ = socket.socket()

    try:
        socket_.connect((host, port))
        socket_.settimeout(0.1)
        return True
    except:
        return False

def valid_port_open(host, port, green_color, red_color, reset_color):

    if socket_validator(host, port):
        print(f"{green_color}[!] {host}:{port} OPEN {reset_color}")
    else:
        print(f"{red_color}[#] {host}:{port} CLOSED {reset_color}", end='\r')

if __name__ == "__main__":

    init()
    GREEN_COLOR = Fore.GREEN
    RESET_COLOR = Fore.RESET
    RED_COLOR = Fore.RED

    HOST = input("HOST: ")
    THREADS = 100

    top_ports = [
    80,    # HTTP
    443,   # HTTPS
    21,    # FTP
    22,    # SSH
    23,    # Telnet
    25,    # SMTP
    53,    # DNS
    110,   # POP3
    135,   # RPC
    139,   # NetBIOS
    143,   # IMAP
    445,   # Microsoft-DS
    3389,  # RDP
    3306,  # MySQL
    8080,  # HTTP alternativo
    5900,  # VNC
    1433,  # SQL Server
    1521,  # Oracle DB
    514    # Syslog
]


    print(f"\n[!]Execute Scanning {HOST} using {THREADS} threads[!]\n")

    with ThreadPoolExecutor(max_workers=THREADS) as executor:
        for port in range(1, 2500):
            executor.submit(valid_port_open, HOST, port, GREEN_COLOR, RED_COLOR, RESET_COLOR)
