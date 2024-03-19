import pygame
from new import Board as br


WINDOW_SIZE = WINDOW_WIDTH, WINDOW_HEIGHT = 501, 501
FPS = 15


def main():
    pygame.init()
    screen = pygame.display.set_mode(WINDOW_SIZE)
    clock = pygame.time.Clock()
    board = br(4, 5)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                board.get_click(event.pos)

            board.render(screen)

            screen.fill((0, 0, 0))
            board.render(screen)
            pygame.display.flip()
            clock.tick(FPS)
    pygame.display.quit()


if __name__ == "__main__":
    main()