import random
import time

import pygame

WINDOW_SIZE = WINDOW_WIDTH, WINDOW_HEIGHT = 501, 501


class MovingCircle:
    def __init__(self):
        self.color = (255, 0, 0)
        self.radius = 20
        self.x = WINDOW_WIDTH // 2
        self.y = WINDOW_HEIGHT // 2
        self.target_x = self.x
        self.target_y = self.y
        self.speed = 5
        self.moving = False

    def render(self, screen):
        pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), self.radius)

    def check_click(self, pos):
        if not self.moving:
            self.target_x, self.target_y = pos
            self.moving = True

    def move(self):
        dx = self.target_x - self.x
        dy = self.target_y - self.y

        time.sleep(0.05)

        if dx:
            self.x += min(self.speed, dx) if dx >= 0 else max(-self.speed, dx)
        if dy:
            self.y += min(self.speed, dy) if dy >= 0 else max(-self.speed, dy)
        if dx == 0 and dy == 0:
            self.moving = False

    def move_faster(self):
        self.speed += 1

    def speed_set(self):
        self.speed = random.randint(2, 10)


def main():
    pygame.init()
    screen = pygame.display.set_mode(WINDOW_SIZE)
    circle_ = MovingCircle()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                circle_.check_click(event.pos)

            if circle_.moving:
                circle_.speed_set()
                while circle_.moving:
                    circle_.move()
                    screen.fill((0, 0, 0))
                    circle_.render(screen)
                    pygame.display.flip()

            screen.fill((0, 0, 0))
            circle_.render(screen)
            pygame.display.flip()

    pygame.display.quit()


if __name__ == "__main__":
    main()
