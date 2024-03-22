import time
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
        self.colors = {1: (255, 0, 0), 2: (0, 0, 255), 3: (255, 255, 255)}
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
        self.flag_red_circle = ()
        self.board_clone = []
        self.path = []
        self.moving = False

    def has_path(self, x, y, cur):
        self.board_clone[x][y] = cur
        if y + 1 < self.height:
            if self.board_clone[x][y + 1] == 0 or (self.board_clone[x][y + 1] != -1 and self.board_clone[x][y + 1] > cur):
                self.has_path(x, y + 1, cur + 1)
        if x + 1 < self.width:
            if self.board_clone[x + 1][y] == 0 or (self.board_clone[x + 1][y] != -1 and self.board_clone[x + 1][y] > cur):
                self.has_path(x + 1, y, cur + 1)
        if x - 1 >= 0:
            if self.board_clone[x - 1][y] == 0 or (self.board_clone[x - 1][y] != -1 and self.board_clone[x - 1][y] > cur):
                self.has_path(x - 1, y, cur + 1)
        if y - 1 >= 0:
            if self.board_clone[x][y - 1] == 0 or (self.board_clone[x][y - 1] != -1 and self.board_clone[x][y - 1] > cur):
                self.has_path(x, y - 1, cur + 1)

    def find_path(self, start, x2, y2):
        rows, cols = len(self.board), len(self.board[0])
        queue = deque([(x2, y2)])
        self.path = []
        self.path.append((x2, y2))
        while queue:
            current_cell = queue.popleft()
            cur_val = self.board_clone[current_cell[0]][current_cell[1]]
            if current_cell == start:
                return True

            neighbors = [(1, 0), (-1, 0), (0, 1), (0, -1)]

            for dr, dc in neighbors:
                new_row, new_col = current_cell[0] + dr, current_cell[1] + dc
                if 0 <= new_row < rows and 0 <= new_col < cols and self.board_clone[new_row][new_col] == cur_val - 1:
                    queue.append((new_row, new_col))
                    self.path.append((new_row, new_col))
                    break
        return False

    def on_click(self, mouse_pos):
        self.board_clone = copy.deepcopy(self.board)
        if mouse_pos:
            if self.board[mouse_pos[0]][mouse_pos[1]] == 0:
                if not self.flag_red_circle:
                    self.board[mouse_pos[0]][mouse_pos[1]] = 2
                else:
                    self.board_clone = copy.deepcopy(self.board)
                    for i in range(self.height):
                        for k in range(self.width):
                            if self.board_clone[i][k] == 2:
                                self.board_clone[i][k] = -1
                        self.board_clone[self.flag_red_circle[0]][self.flag_red_circle[1]] = 0
                    self.has_path(*mouse_pos, 1)
                    self.moving = self.find_path(mouse_pos, *self.flag_red_circle)
                    if self.moving:
                        print(self.path)
                        self.flag_red_circle = ()
            elif self.board[mouse_pos[0]][mouse_pos[1]] == 2:
                self.board[mouse_pos[0]][mouse_pos[1]] = 1
                self.flag_red_circle = mouse_pos
            elif self.board[mouse_pos[0]][mouse_pos[1]] == 1:
                self.board[mouse_pos[0]][mouse_pos[1]] = 2
                self.flag_red_circle = ()

    def move(self):
        time.sleep(1)
        if len(self.path) > 1:
            self.board[self.path[1][0]][self.path[1][1]] = 1
            self.board[self.path[0][0]][self.path[0][1]] = 3
            del(self.path[0])
            print(self.path)
        else:
            self.moving = False

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

            if lines.moving:
                lines.move()

            screen.fill((0, 0, 0))
            lines.render(screen)
            pygame.display.flip()

    pygame.display.quit()


if __name__ == "__main__":
    main()
