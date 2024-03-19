from random import randint

import pygame
import pickle

WINDOW_SIZE = WINDOW_WIDTH, WINDOW_HEIGHT = 600, 600
TIMER_EVENT_TYPE = 30
DATA_DIR = 'data'


class ClickMee():
    def __init__(self):
        self.width = 200
        self.height = 60
        self.x = randint(0, WINDOW_WIDTH - self.width)
        self.y = randint(0, WINDOW_HEIGHT - self.height)
        self.delay = 1000
        pygame.time.set_timer(TIMER_EVENT_TYPE, self.delay)
        self.score = 0
        self.is_paused = False

    def render(self, screen):
        font = pygame.font.Font(None, 24)
        text = font.render(f"Попаданий: {self.score}", 1, (50, 70, 0))
        pygame.draw.rect(screen, (200, 150, 50), (self.x, self.y, self.width, self.height), 0)
        screen.blit(text, (self.x + (self.width - text.get_width()) // 2,
                           self.y + (self.height - text.get_height()) // 2))

    def move(self):
        self.x = randint(0, WINDOW_WIDTH - self.width)
        self.y = randint(0, WINDOW_HEIGHT - self.height)

    def check_click(self, pos):
        if self.x <= pos[0] <= self.x + self.width and self.y <= pos[1] <= self.y + self.height:
            self.move()
            self.delay = max(self.delay - 50, 50)
            pygame.time.set_timer(TIMER_EVENT_TYPE, self.delay)
            self.score += 1

    def switch_pause(self):
        self.is_paused = not self.is_paused
        pygame.time.set_timer(TIMER_EVENT_TYPE, self.delay if not self.is_paused else 0)


def main():
    pygame.init()
    screen = pygame.display.set_mode(WINDOW_SIZE)

    clickme = ClickMee()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == TIMER_EVENT_TYPE:
                clickme.move()
            if event.type == pygame.MOUSEBUTTONDOWN:
                clickme.check_click(event.pos)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    clickme.switch_pause()
                if event.key == pygame.K_s:
                    with open(f'{DATA_DIR}/save.dat', 'wb') as file:
                        pickle.dump(clickme, file)
                if event.key == pygame.K_l:
                    with open(f'{DATA_DIR}/save.dat', 'rb') as file:
                        clickme = pickle.load(file)

        screen.fill((0, 0, 0))
        clickme.render(screen)
        pygame.display.flip()

    pygame.display.quit()


if __name__ == "__main__":
    main()