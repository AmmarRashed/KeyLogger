import logging
import time

from pynput import keyboard

# time key pressed/released
time_str = time.strftime("%Y-%m-%d--%H-%M-%S")
logging.basicConfig(filename=f"{time_str}.kb.tsv", level=logging.DEBUG, format='%(asctime)s\t%(message)s')


# Keyboard
def on_press(key):
    try:
        logging.info(f'{key.char}\tPressed')
    except AttributeError:
        logging.info(f'{key}\tPressed')


def on_release(key):
    logging.info(f'{key}\tReleased')


if __name__ == "__main__":
    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()
