import os
import time
import keyboard as keyboard
from .map import *


def app():
    map = Map(h=12, w=12)
    map.set_random()

    while True:
        map.show_map()
        time.sleep(1)
        if keyboard.is_pressed("alt"):
            break
        map.update()
        os.system('cls')

