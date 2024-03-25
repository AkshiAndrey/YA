import os
import sys
import pygame


BLUE = (0, 0, 255)


pygame.init()
size = width, height = 500, 500
screen = pygame.display.set_mode(size)


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    # если файл не существует, то выходим
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    if colorkey is not None:
        image = image.convert()
    if colorkey == -1:
        colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    else:
        image = image.convert_alpha()
    return image


class Hero(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__(all_sprites)
        self.image = pygame.Surface((20, 20))
        self.image.fill(BLUE)
        self.rect = self.image.get_rect()
        self.rect.center = (400, 100)
        self.speed = 0

    def update(self):
        platform_hit_list = pygame.sprite.spritecollide(self, horizontal_borders, False)
        if platform_hit_list:
            for platform in platform_hit_list:
                if self.rect.bottom >= (platform.rect.top - self.speed):
                    self.rect.bottom = platform.rect.top
                    self.speed = 0
        else:
            self.speed = 50

        self.rect.y += self.speed / 60


class Platform(pygame.sprite.Sprite):

    def __init__(self, mouse_pos):
        super().__init__(horizontal_borders)
        self.width = 50
        self.height = 10
        self.image = pygame.Surface((self.width, self.height))
        self.image.fill((128, 128, 128))
        self.rect = self.image.get_rect()
        self.rect.x = mouse_pos[0]
        self.rect.y = mouse_pos[1]


horizontal_borders = pygame.sprite.Group()
clock = pygame.time.Clock()
all_sprites = pygame.sprite.Group()
hero = Hero()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            Platform(event.pos)
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                hero.rect.x -= 10
            elif event.key == pygame.K_RIGHT:
                hero.rect.x += 10

    all_sprites.update()
    screen.fill((0, 0, 0))
    horizontal_borders.draw(screen)
    all_sprites.draw(screen)

    pygame.display.flip()
    clock.tick(60)
pygame.quit()
sys.exit()

