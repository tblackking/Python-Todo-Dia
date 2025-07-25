keys = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
    '0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
    '`', '~', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '-', '=', '+',
    '[', '{', ']', '}', '\\', '|',
    ';', ':', "'", '"',
    ',', '<', '.', '>', '/',
    ' ',  # Barra de espaço
    '\t',  # Tabulação
    '\n',  # Nova linha
    'f1', 'f2', 'f3', 'f4', 'f5', 'f6', 'f7', 'f8', 'f9', 'f10', 'f11', 'f12',
    'insert', 'delete', 'home', 'end', 'page up', 'page down',
    'up', 'down', 'left', 'right',
    'backspace', 'enter', 'return', 'space',
    'tab', 'caps lock', 'num lock', 'scroll lock',
    'print screen', 'pause',
    'menu', 'windows', 'command', 'option', 'alt', 'ctrl', 'control',
]


def block_keyboard(keyboard, tecla):
    def on_key_event(e):
        #global wait_keys_press
        if keyboard.is_pressed('esc+shift'):
            print("[!] Desbloqueando todas as teclas...")
            keyboard.unhook_all()  # Desbloqueia todas as teclas
            #wait_keys_press = True

    keyboard.hook(on_key_event)

    # Bloqueia a tecla inicialmente
    keyboard.block_key(tecla)
    print(f"[!] KEYBOARD BLOCK - {tecla}")
    
def wait_for_press(keyboard, variable_to_acess):
    variable_to_acess
    keyboard.wait('esc+shift')
    variable_to_acess = True
    
