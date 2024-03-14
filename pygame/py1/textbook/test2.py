import pygame
from PIL import Image, ImageFilter, ImageEnhance


def blit_pil_image(screen, img, position):
    pygame_image = pygame.image.fromstring(img.tobytes(), img.size, 'RGB')
    screen.blit(pygame_image, position)


def images_demo():
    img = Image.open('img/blue_bird.jpg')
    box_size = 400
    img.thumbnail((box_size, box_size))
    blit_pil_image(screen, img, (width // 2 - img.width // 2, 20 + box_size // 2 - img.height // 2))

    small_images = [img for i in range(6)]
    for i in range(len(small_images)):
        small_images[i].thumbnail((150, 150))

    r, g, b = small_images[0].split()
    small_images[0] = Image.merge('RGB', (r.point(lambda x: x // 2), g, b))
    small_images[1] = Image.merge('RGB', (r, g, b.point(lambda x: x // 2)))
    small_images[2] = Image.merge('RGB', (r, g.point(lambda x: x // 2), b))

    small_images[3] = small_images[3].filter(ImageFilter.BLUR)
    small_images[4] = small_images[4].filter(ImageFilter.SHARPEN)

    enhancer = ImageEnhance.Contrast(small_images[5])
    small_images[5] = enhancer.enhance(1.7)


    for i in range(len(small_images)):
        blit_pil_image(screen, small_images[i], (20 + 160 * i, box_size + 40))





if __name__ == '__main__':
    # инициализация Pygame:
    pygame.init()
    # размеры окна:
    size = width, height = 1100, 600
    # screen — холст, на котором нужно рисовать:
    screen = pygame.display.set_mode(size)
    images_demo()

    pygame.display.flip()
    # ожидание закрытия окна:
    while pygame.event.wait().type != pygame.QUIT:
        pass
    # завершение работы:
    pygame.quit()
