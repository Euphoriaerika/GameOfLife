import pygame

from .configuration import *
from .map import Map


def app():
    # Pygame initialization
    pygame.init()
    screen = pygame.display.set_mode(
        (v_cells_number * CELL_SIZE, h_cells_number * CELL_SIZE)
    )
    pygame.display.set_caption("Game of Life")
    clock = pygame.time.Clock()

    # Map initialization
    game_map = Map(h=h_cells_number, w=v_cells_number, live_color=live_color, dead_color=dead_color)

    # Main game of life loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        game_map.update()
        screen.fill((0, 0, 0))  # Очищення екрану
        game_map.draw(screen)
        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()
