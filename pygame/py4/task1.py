from collections import deque

import pygame
import copy

WINDOW_SIZE = WINDOW_WIDTH, WINDOW_HEIGHT = 501, 501


class Board:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = [[0 for i in range(width)] for _ in range(height)]
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


class Lines(Board):

    def __init__(self, width, height):
        super().__init__(width, height)
        self.flag_red_circle = []
        self.board_clone = []





    # def has_path(self, x1, y1, x2, y2):
    #     self.board_clone[x2][y2] = 1
    #     if (x2, y2) == (x1, y1):
    #         return True
    #     if self.exist_sell(x2 + 1, y2):
    #         if self.board_clone[x2 + 1][y2] == 0:
    #             # self.board_clone[x2 + 1][y2] = 1
    #             return self.has_path(x1, y1, x2 + 1, y2)
    #     if self.exist_sell(x2, y2 + 1):
    #         if self.board_clone[x2][y2 + 1] == 0:
    #             # self.board_clone[x2][y2 + 1] = 1
    #             return self.has_path(x1, y1, x2, y2 + 1)
    #     if self.exist_sell(x2 - 1, y2):
    #         if self.board_clone[x2 - 1][y2] == 0:
    #             # self.board_clone[x2 - 1][y2] = 1
    #             return self.has_path(x1, y1, x2 - 1, y2)
    #     if self.exist_sell(x2, y2 - 1):
    #         if self.board_clone[x2][y2 - 1] == 0:
    #             # self.board_clone[x2][y2 - 1] = 1
    #             return self.has_path(x1, y1, x2, y2 - 1)
    #     return False


    def has_path(self, x1, y1, x2, y2):
        rows, cols = len(self.board), len(self.board[0])

        queue = deque([(x2, y2)])
        visited = set()
        visited.add((x2, y2))

        while queue:
            current_cell = queue.popleft()
            if current_cell == (x1, y1):
                self.viz = list(visited)
                return True

            neighbors = [(1, 0), (-1, 0), (0, 1), (0, -1)]  # Possible movements: down, up, right, left

            for dr, dc in neighbors:
                new_row, new_col = current_cell[0] + dr, current_cell[1] + dc

                if 0 <= new_row < rows and 0 <= new_col < cols and self.board[new_row][new_col] == 2 and (
                        new_row, new_col) not in visited:
                    visited.add((new_row, new_col))

                elif 0 <= new_row < rows and 0 <= new_col < cols and self.board[new_row][new_col] == 0 and (
                        new_row, new_col) not in visited:
                    queue.append((new_row, new_col))
                    visited.add((new_row, new_col))
        return False

    def on_click(self, mouse_pos):
        self.board_clone = copy.deepcopy(self.board)
        if mouse_pos:
            if self.board[mouse_pos[0]][mouse_pos[1]] == 0:
                if not self.flag_red_circle:
                    self.board[mouse_pos[0]][mouse_pos[1]] = 2
                else:
                    if self.has_path(*mouse_pos, *self.flag_red_circle):
                        self.board[mouse_pos[0]][mouse_pos[1]] = 2
                        self.board[self.flag_red_circle[0]][self.flag_red_circle[1]] = 0
                        self.flag_red_circle = []
            elif self.board[mouse_pos[0]][mouse_pos[1]] == 2:
                self.board[mouse_pos[0]][mouse_pos[1]] = 1
                self.flag_red_circle = mouse_pos
            elif self.board[mouse_pos[0]][mouse_pos[1]] == 1:
                self.board[mouse_pos[0]][mouse_pos[1]] = 2
                self.flag_red_circle = []

    def exist_sell(self, x, y):
        ex = False
        try:
            ex = self.board_clone[x][y]
            if ex == 0:
                return True
        except Exception:
            pass
        return ex

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
                                           self.cell_size / 2 - 5)
                    else:
                        if color == 2:
                            pygame.draw.circle(screen, self.colors[color],
                                               (self.top + self.cell_size * j + self.cell_size / 2,
                                                self.left + self.cell_size * i + self.cell_size / 2),
                                               self.cell_size / 2 - 5)


def main():
    pygame.init()
    screen = pygame.display.set_mode(WINDOW_SIZE)
    lines = Lines(5, 5)
    # lines.set_view(2, 2, 80)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                lines.get_click(event.pos)
        screen.fill((0, 0, 0))
        lines.render(screen)
        pygame.display.flip()

    pygame.display.quit()


if __name__ == "__main__":
    main()
