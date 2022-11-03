import numpy as np
import random


class Map:
    def __init__(self, h=5, w=5, live='#', dead=' '):
        self.char_live = live
        self.char_dead = dead
        self.height = h
        self.width = w
        self.map = np.array([[self.char_dead] * self.width] * self.height)

    def show_map(self):
        print(self.map)

    def set_random(self):
        for i in range(self.height):
            for j in range(self.width):
                if random.randint(0, 1):
                    self.map[i, j] = self.char_live

    def set_cord(self, cord=np.array([0, 0])):
        if not (0 <= cord[0] < self.height):
            return
        if not (0 <= cord[1] < self.width):
            return

        self.map[cord[0]][cord[1]] = self.char_live

    def update(self):
        new_map = self.map.copy()
        for i in range(self.height):  # прохід по мапі
            for j in range(self.width):
                flag = True
                if self.map[i, j] == self.char_live:  # якщо знайдено не пусту ячейку виконуэм для неъ правила
                    flag = False
                count = 0
                for k in range(-1, 2):
                    for l in range(-1, 2):
                        if i + k < 0 or i + k >= self.height:
                            continue
                        if j + l < 0 or j + l >= self.height:
                            continue
                        if self.map[i + k, j + l] == self.char_dead:
                            continue
                        if k == 0 and l == 0:
                            continue
                        count += 1
                if flag:
                    if count == 3:
                        new_map[i, j] = self.char_live
                    continue
                if count < 2 or count > 3:
                    new_map[i, j] = self.char_dead
        self.map = new_map.copy()
