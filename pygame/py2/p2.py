import random

import pygame
import math

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
        self.target_x, self.target_y = pos
        self.moving = True

    def move(self):
        dx = self.target_x - self.x
        dy = self.target_y - self.y
        distance = math.hypot(dx, dy)
        if distance > 5:
            angle = math.atan2(dy, dx)
            self.x += math.cos(angle) * min(self.speed, distance)
            self.y += math.sin(angle) * min(self.speed, distance)
        else:
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
        circle_.speed_set()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                circle_.check_click(event.pos)

            screen.fill((0, 0, 0))

            if circle_.moving:
                circle_.move()
                circle_.move_faster()

            circle_.render(screen)
            pygame.display.flip()

    pygame.display.quit()


if __name__ == "__main__":
    main()
