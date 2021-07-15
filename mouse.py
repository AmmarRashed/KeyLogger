import logging
import time

from pynput import mouse

# time key pressed/released
time_str = time.strftime("%Y-%m-%d:%H-%M-%S")
logging.basicConfig(filename=f"{time_str}.tsv", level=logging.DEBUG, format='%(asctime)s\t%(message)s')


# Mouse
def on_move(x, y):
    # logging.info("Mouse moved to ({0}, {1})".format(x, y))
    pass


def on_click(x, y, button, pressed):
    if pressed:
        logging.info(f'{x}\t{y}\tClick\t{button}\tMouse')


def on_scroll(x, y, dx, dy):
    logging.info(f'{x}\t{y}\tScroll\t({dx, dy})\tMouse')


with mouse.Listener(on_move=on_move, on_click=on_click, on_scroll=on_scroll) as listener:
    listener.join()