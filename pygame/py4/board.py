import pygame

WINDOW_SIZE = WINDOW_WIDTH, WINDOW_HEIGHT = 501, 501


class Board:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = [[0] * width for _ in range(height)]
        self.board_color = [[0] * width for _ in range(height)]
        self.color = (255, 255, 255)
        self.left = 10
        self.top = 10
        self.colors = {1: (255, 0, 0), 2: (0, 0, 255)}
        self.cell_size = 30
        self.turn_status = 1

    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size

    def render(self, screen):

        for i in range(self.height):
            for j in range(self.width):
                pygame.draw.rect(screen, self.color,
                                 (self.top + self.cell_size * j, self.left + self.cell_size * i,
                                  self.cell_size, self.cell_size), 1)
                if color := self.board[i][j]:
                    if color == 1:
                        pygame.draw.circle(screen, self.colors[color],
                                           (self.top + self.cell_size * j + self.cell_size / 2,
                                            self.left + self.cell_size * i + self.cell_size / 2),
                                           self.cell_size / 2 - 5, 1)
                    else:
                        pygame.draw.line(screen, self.colors[color],
                                         (self.top + self.cell_size * j + 2,
                                          self.left + self.cell_size * i + 2),
                                         (self.top + self.cell_size * j - 2 + self.cell_size,
                                          self.left + self.cell_size * i - 2 + self.cell_size), 1)
                        pygame.draw.line(screen, self.colors[color],
                                         (self.top + self.cell_size * j + self.cell_size - 2,
                                          self.left + self.cell_size * i + 2),
                                         (self.top + self.cell_size * j + 2,
                                          self.left + self.cell_size * i - 2 + self.cell_size), 1)

    def get_click(self, mouse_pos):
        cell = self.get_cell(mouse_pos)
        self.on_click(cell)

    def get_cell(self, mouse_pos):
        for i, value in enumerate(self.board):
            for j, value_ in enumerate(value):
                height = self.cell_size * (i + 1) + self.top
                width = self.cell_size * (j + 1) + self.left
                width_min = width - self.cell_size
                height_min = height - self.cell_size
                if width_min < mouse_pos[0] < width and height_min < mouse_pos[1] < height:
                    return i, j
        return None

    def on_click(self, mouse_pos):
        if mouse_pos:
            if not self.board[mouse_pos[0]][mouse_pos[1]]:
                self.board[mouse_pos[0]][mouse_pos[1]] = self.turn_status
                self.turn_status = 1 if self.turn_status == 2 else 2


def main():
    pygame.init()
    screen = pygame.display.set_mode(WINDOW_SIZE)
    board = Board(10, 10)
    # board.set_view(5, 5, 80)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                board.get_click(event.pos)
        screen.fill((0, 0, 0))
        board.render(screen)
        pygame.display.flip()

    pygame.display.quit()


if __name__ == "__main__":
    main()
