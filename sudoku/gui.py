import pygame

# Hexadecimal color for drawing
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)


class GUI:
    """GUI to display and interact with sudoku game"""

    def __init__(self) -> None:
        pygame.init()
        pygame.display.set_caption("Sudoku")
        self.window = pygame.display.set_mode((450, 500))
        self.window.fill(WHITE)

    def draw_empty_grid(self) -> None:
        self.window.fill(WHITE)

        for x in range(0, 450, 150):
            for y in range(0, 450, 150):
                pygame.draw.rect(self.window, BLACK, pygame.Rect(x, y, 150, 150), 2)

        for i in range(0, 450, 50):
            pygame.draw.line(self.window, BLACK, (i, 0), (i, 450))
            pygame.draw.line(self.window, BLACK, (0, i), (450, i))

    def draw_grid_footer(self) -> None:
        sysfont = pygame.font.SysFont("Helvetica", 20)
        text = sysfont.render("Press q to quit", True, BLACK)
        self.window.blit(text, (5, 455))
        text = sysfont.render("Press s to solve", True, BLACK)
        self.window.blit(text, (5, 475))

    def fill_grid_with_number(self, grid):
        sysfont = pygame.font.SysFont("Helvetica", 35)
        for x in range(9):
            for y in range(9):
                if grid[x][y] == 0:
                    continue
                text = sysfont.render(str(grid[x][y]), True, BLACK)
                self.window.blit(text, (16 + (50 * x), 12 + (50 * y)))

    def draw_grid(self, grid) -> None:
        self.draw_empty_grid()
        self.draw_grid_footer()
        self.fill_grid_with_number(grid)
        pygame.display.update()
