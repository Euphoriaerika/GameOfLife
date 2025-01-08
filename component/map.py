import pygame
import numpy as np

from .configuration import *


class Map:
    def __init__(self, h=25, w=25, live_color=(0, 255, 0), dead_color=(0, 0, 0)):
        self.live_color = live_color
        self.dead_color = dead_color
        self.height = h
        self.width = w
        self.map = self._set_random(h, w)  # Map as matrix of booleans

    def _set_random(self, h, w):
        """
        Set random initial state of the map.
        """
        return np.random.choice([True, False], size=(h, w), p=[0.3, 0.7])

    def update(self):
        """
        Update the map according to the rules of the game of life.
        """
        new_map = self.map.copy()
        for i in range(self.height):
            for j in range(self.width):
                count = (
                    np.sum(
                        self.map[
                            max(0, i - 1) : min(self.height, i + 2),
                            max(0, j - 1) : min(self.width, j + 2),
                        ]
                    )
                    - self.map[i, j]
                )
                if self.map[i, j]:
                    new_map[i, j] = count in [2, 3]
                else:
                    new_map[i, j] = count == 3
        self.map = new_map

    def draw(self, screen):
        """
        Draw the map on the screen.
        """
        for i in range(self.height):
            for j in range(self.width):
                color = self.live_color if self.map[i, j] else self.dead_color
                pygame.draw.rect(
                    screen, color, (j * CELL_SIZE, i * CELL_SIZE, CELL_SIZE, CELL_SIZE)
                )
