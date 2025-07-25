import keyboard
from keyboards_use import keys, block_keyboard, wait_for_press
from block_mouse import block_mouse_for_time
import threading

wait_keys_press_ = False  

wait_press_thread = threading.Thread(target=wait_for_press, args=(keyboard, wait_keys_press_))
wait_press_thread.start()

for k in keys:
    block_keyboard(keyboard, k)
    if wait_keys_press_:
        break

while not wait_keys_press_:
    block_mouse_for_time()
    if keyboard.is_pressed('esc+shift'):
        break
  

wait_press_thread.join()


