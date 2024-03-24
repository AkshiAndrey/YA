import os
import sys
import random

import pygame

# Изображение не получится загрузить
# без предварительной инициализации pygame



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


pygame.init()
size = width, height = 500, 500
screen = pygame.display.set_mode(size)
# image = pygame.Surface([100, 100])
# image.fill(pygame.Color("red"))
# screen.blit(image, (10, 10))
# image = load_image("sv.jpg")
# image1 = pygame.transform.scale(image, (200, 100))
# image2 = pygame.transform.scale(image, (100, 200))
# screen.blit(image, (10, 10))
# screen.blit(image1, (20, 10))
# screen.blit(image2, (130, 10))


# создадим группу, содержащую все спрайты
all_sprites = pygame.sprite.Group()

# создадим спрайт
sprite = pygame.sprite.Sprite()
# определим его вид
sprite.image = pygame.transform.scale(load_image("sova.jpg"), (500, 500))
# и размеры
sprite.rect = sprite.image.get_rect()
# добавим спрайт в группу
all_sprites.add(sprite)

sprite.rect.x = 5
sprite.rect.y = 20

# изображение должно лежать в папке data
bomb_image = load_image("sova.jpg")
image1 = pygame.transform.scale(bomb_image, (40, 40))

for i in range(50):
    # можно сразу создавать спрайты с указанием группы
    bomb = pygame.sprite.Sprite(all_sprites)
    bomb.image = image1
    bomb.rect = bomb.image.get_rect()

    # задаём случайное местоположение бомбочке
    bomb.rect.x = random.randrange(width)
    bomb.rect.y = random.randrange(height)


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((255, 255, 255))
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

    all_sprites.draw(screen)
    pygame.display.flip()

pygame.display.quit()
