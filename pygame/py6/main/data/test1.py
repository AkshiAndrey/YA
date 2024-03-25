import pygame
import sys

# Инициализация Pygame
pygame.init()

# Цвета
BLUE = (0, 0, 255)


class Hero(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((10, 10))
        self.image.fill(BLUE)
        self.rect = self.image.get_rect()

        # Начальная позиция
        self.rect.center = (400, 100)

        # Скорость перемещения вниз в пикселях в секунду
        self.speed = 50

    def update(self):
        # Перемещение вниз
        self.rect.y += self.speed / 60  # 60 FPS


class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((800, 600))
        self.clock = pygame.time.Clock()
        self.hero = Hero()
        self.all_sprites = pygame.sprite.Group(self.hero)

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        self.hero.rect.x -= 10
                    elif event.key == pygame.K_RIGHT:
                        self.hero.rect.x += 10

            self.all_sprites.update()

            self.screen.fill((255, 255, 255))
            self.all_sprites.draw(self.screen)
            pygame.display.flip()

            self.clock.tick(60)  # FPS

        pygame.quit()
        sys.exit()


if __name__ == "__main__":
    game = Game()
    game.run()