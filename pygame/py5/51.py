import os
import sys
import random

import pygame
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


class Bomb(pygame.sprite.Sprite):
    image = load_image("bomb.png", -1)
    image_boom = load_image("boom.png", -1)
    image = pygame.transform.scale(image, (60, 60))
    image_boom = pygame.transform.scale(image_boom, (60, 60))

    def __init__(self, group):
        # НЕОБХОДИМО вызвать конструктор родительского класса Sprite.
        # Это очень важно !!!
        super().__init__(group)
        self.image = Bomb.image
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(width)
        self.rect.y = random.randrange(height)

    def update(self, *args):
        self.rect = self.rect.move(random.randrange(3) - 1,
                                   random.randrange(3) - 1)
        if args and args[0].type == pygame.MOUSEBUTTONDOWN and \
                self.rect.collidepoint(args[0].pos):
            self.image = self.image_boom





# Изображение не получится загрузить
# без предварительной инициализации pygame

all_sprites = pygame.sprite.Group()
for _ in range(50):
    Bomb(all_sprites)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            all_sprites.update(event)


    screen.fill((255, 255, 255))
    all_sprites.draw(screen)
    all_sprites.update()
    # image = pygame.Surface([100, 100])
    # image.fill(pygame.Color("red"))
    # screen.blit(image, (10, 10))
    # image = load_image("sv.jpg")
    # image3 = load_image("sova.jpg", -1)
    # image4 = pygame.transform.scale(image3, (200, 200))
    # image1 = pygame.transform.scale(image, (200, 100))
    # image2 = pygame.transform.scale(image, (100, 200))
    # screen.blit(image4, (50, 10))
    # screen.blit(image, (10, 10))
    # screen.blit(image1, (20, 10))
    # screen.blit(image2, (130, 10))

    pygame.display.flip()

pygame.display.quit()
