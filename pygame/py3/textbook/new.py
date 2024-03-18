import pygame
WINDOW_SIZE = WINDOW_WIDTH, WINDOW_HEIGHT = 501, 501


class Board:
    # создание поля
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = [[0] * width for _ in range(height)]
        # значения по умолчанию
        self.left = 10
        self.top = 10
        self.color = (255, 255, 255)
        self.cell_size = 30

    # настройка внешнего вида
    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size

    def render(self, screen):
        for i in range(self.width):
            for j in range(self.height):
                pygame.draw.rect(screen, self.color,
                                 (self.left + self.cell_size * i,
                                  self.top + self.cell_size * j,
                                  self.cell_size, self.cell_size), 1)

    def set_view(self, left, top, size):
        self.top = top
        self.left = left
        self.cell_size = size


def main():
    pygame.init()
    screen = pygame.display.set_mode(WINDOW_SIZE)
    # поле 5 на 7
    board = Board(4, 3)
    board.set_view(100, 100, 50)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.fill((0, 0, 0))
        board.render(screen)
        pygame.display.flip()

    pygame.display.quit()


if __name__ == "__main__":
    main()
