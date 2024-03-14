from random import randint

import pygame

WINDOW_SIZE = WINDOW_WIDTH, WINDOW_HEIGHT = 600, 600
TIMER_EVENT_TYPE = 30



class ClickMee():
    def __init__(self):
        self.width = 200
        self.height = 60
        self.x = randint(0, WINDOW_WIDTH - self.width)
        self.y = randint(0, WINDOW_HEIGHT - self.height)
        self.delay = 1000
        pygame.time.set_timer(TIMER_EVENT_TYPE, self.delay)

    def render(self, screen):
        font = pygame.font.Font(None, 50)
        text = font.render("Click me", 1, (50, 70, 0))
        pygame.draw.rect(screen, (200, 150, 50), (self.x, self.y, self.width, self.height), 0)
        screen.blit(text, (self.x + (self.width - text.get_width()) // 2,
                           self.y + (self.height - text.get_height()) // 2))


    def move(self):
        self.x = randint(0, WINDOW_WIDTH - self.width)
        self.y = randint(0, WINDOW_HEIGHT - self.height)


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

        screen.fill((0, 0, 0))
        clickme.render(screen)
        pygame.display.flip()

    pygame.display.quit()


if __name__ == "__main__":
    main()
