import sys

import pygame

from gui import GUI
from solve import solve


class Game:
    def __init__(self) -> None:
        self.grid = [
            [0, 0, 4, 0, 5, 0, 0, 0, 0],
            [9, 0, 0, 7, 3, 4, 6, 0, 0],
            [0, 0, 3, 0, 2, 1, 0, 4, 9],
            [0, 3, 5, 0, 9, 0, 4, 8, 0],
            [0, 9, 0, 0, 0, 0, 0, 3, 0],
            [0, 7, 6, 0, 1, 0, 9, 2, 0],
            [3, 1, 0, 9, 7, 0, 2, 0, 0],
            [0, 0, 9, 1, 8, 2, 0, 0, 3],
            [0, 0, 0, 0, 6, 0, 1, 0, 0],
        ]
        self.gui = GUI()

    def reset_grid(self):
        for x in range(9):
            for y in range(9):
                self.grid[x][y] = 0

    def loop(self) -> None:
        while True:
            self.gui.draw_grid(self.grid)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        sys.exit()
                    if event.key == pygame.K_s:
                        solve(self.grid)
                    if event.key == pygame.K_w:
                        self.reset_grid()
