import pyautogui


def block_mouse_for_time():
    pyautogui.FAILSAFE = False

    try: 
        largura_tela, altura_tela = pyautogui.size()

        x = largura_tela // 2  
        y = altura_tela     
            
        pyautogui.moveTo(x, y)
    except pyautogui.FailSafeException:
        pass
    finally:
        pyautogui.FAILSAFE = True
