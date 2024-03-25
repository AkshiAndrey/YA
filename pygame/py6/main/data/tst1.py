import sys
import pygame

BLUE = (0, 0, 255)

pygame.init()
size = width, height = 500, 500
screen = pygame.display.set_mode(size)


class Hero(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__(all_sprites)
        self.image = pygame.Surface((20, 20))
        self.image.fill(BLUE)
        self.rect = self.image.get_rect()
        self.rect.center = (400, 100)
        self.speed = 0
        self.on_stairs = False

    def update(self):
        stairs_hit_list = pygame.sprite.spritecollide(self, vertical_blocks, False)
        platform_hit_list = pygame.sprite.spritecollide(self, horizontal_blocks, False)
        if stairs_hit_list:
            self.speed = 0
            self.on_stairs = True
        elif platform_hit_list:
            self.on_stairs = False
            for platform in platform_hit_list:
                if self.rect.bottom >= (platform.rect.top - self.speed):
                    self.rect.bottom = platform.rect.top
                    self.speed = 0
        else:
            self.speed = 50

        self.rect.y += self.speed / 60


class Platform(pygame.sprite.Sprite):

    def __init__(self, mouse_pos):
        super().__init__(horizontal_blocks)
        self.width = 50
        self.height = 10
        self.image = pygame.Surface((self.width, self.height))
        self.image.fill((128, 128, 128))
        self.rect = self.image.get_rect()
        self.rect.x = mouse_pos[0]
        self.rect.y = mouse_pos[1]


class Stairs(pygame.sprite.Sprite):

    def __init__(self, mouse_pos):
        super().__init__(vertical_blocks)
        self.width = 10
        self.height = 50
        self.image = pygame.Surface((self.width, self.height))
        self.image.fill((255, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.x = mouse_pos[0]
        self.rect.y = mouse_pos[1]


horizontal_blocks = pygame.sprite.Group()
vertical_blocks = pygame.sprite.Group()
clock = pygame.time.Clock()
all_sprites = pygame.sprite.Group()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:
            if not any(isinstance(sprite, Hero) for sprite in all_sprites):
                hero = Hero()
                hero.rect.topleft = event.pos
                all_sprites.add(hero)
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:
                for sprite in all_sprites:
                    if isinstance(sprite, Hero):
                        sprite.rect.topleft = event.pos

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LCTRL]:
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                Stairs(event.pos)
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            Platform(event.pos)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                hero.rect.x -= 10
            elif event.key == pygame.K_RIGHT:
                hero.rect.x += 10
            elif event.key == pygame.K_UP and hero.on_stairs:
                hero.rect.y -= 10
            elif event.key == pygame.K_DOWN and hero.on_stairs:
                hero.rect.y += 10

    all_sprites.update()
    screen.fill((0, 0, 0))
    horizontal_blocks.draw(screen)
    vertical_blocks.draw(screen)
    all_sprites.draw(screen)

    pygame.display.flip()
    clock.tick(60)
pygame.quit()
sys.exit()
