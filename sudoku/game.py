import sys

import pygame

from gui import GUI
from solve import is_valid_nb_for_cell, solve


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
        self.cursor_coordinate = None
        self.message = ""

    def reset_grid(self) -> None:
        for x in range(9):
            for y in range(9):
                self.grid[x][y] = 0

    def refresh_cursor(self) -> None:
        x, y = pygame.mouse.get_pos()

        if x > 450 or y > 450:
            self.cursor_coordinate = None
        else:
            self.cursor_coordinate = (x // 50, y // 50)

    def place_number(self, nb):
        if not self.cursor_coordinate:
            return

        x = self.cursor_coordinate[0]
        y = self.cursor_coordinate[1]
        if is_valid_nb_for_cell(self.grid, x, y, nb):
            self.grid[x][y] = nb
            self.message = ""
        else:
            self.message = f"{nb} is an invalid value for this cell"

    def loop(self) -> None:
        while True:
            self.gui.draw_grid(self.grid, self.cursor_coordinate, self.message)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.refresh_cursor()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        sys.exit()
                    if event.key == pygame.K_s:
                        solve(self.grid)
                        self.message = "Grid has been solved"
                    if event.key == pygame.K_w:
                        self.reset_grid()
                        self.message = "Grid has been wipped"
                    if event.key == pygame.K_1:
                        self.place_number(1)
                    if event.key == pygame.K_2:
                        self.place_number(2)
                    if event.key == pygame.K_3:
                        self.place_number(3)
                    if event.key == pygame.K_4:
                        self.place_number(4)
                    if event.key == pygame.K_5:
                        self.place_number(5)
                    if event.key == pygame.K_6:
                        self.place_number(6)
                    if event.key == pygame.K_7:
                        self.place_number(7)
                    if event.key == pygame.K_8:
                        self.place_number(8)
                    if event.key == pygame.K_8:
                        self.place_number(8)
                    if event.key == pygame.K_9:
                        self.place_number(9)
