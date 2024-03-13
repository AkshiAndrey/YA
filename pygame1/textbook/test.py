import pygame


# def draw(screen):
#     screen.fill((0, 0, 0))
#     font = pygame.font.Font(None, 50)
#     text = font.render("Hello, Pygame!", True, (100, 255, 100))
#     text_x = width // 2 - text.get_width() // 2
#     text_y = height // 2 - text.get_height() // 2
#     text_w = text.get_width()
#     text_h = text.get_height()
#     screen.blit(text, (text_x, text_y))
#     pygame.draw.rect(screen, (0, 255, 0), (text_x - 10, text_y - 10,
#                                            text_w + 20, text_h + 20), 1)

def draw_square(screen):
    color = pygame.Color(50, 150, 50)
    # рисуем "тень"
    pygame.draw.rect(screen, color,
                     (20, 20, 100, 100), 0)
    hsv = color.hsva
    # увеличиваем параметр Value, который влияет на яркость
    color.hsva = (hsv[0], hsv[1], hsv[2] + 30, hsv[3])
    # рисуем сам объект
    pygame.draw.rect(screen, color, (10, 10, 100, 100), 0)


def show_text(font, fontname, position):
    font_color = (50, 50, 50)
    text = font.render(f'hello ({fontname})', 1, font_color)
    screen.blit(text, position)


def fonts_demo():
    screen.fill((200, 200, 200))
    font_size = 24
    font = pygame.font.Font(None, font_size)
    show_text(font, 'default', (40, 40))

    print(pygame.font.get_fonts())
    font_names = ['arial', 'calibri', 'corbel', 'ebrima']
    for i, name in enumerate(font_names):
        font = pygame.font.SysFont(name, font_size)
        show_text(font, name, (40, 80 + 60 * i))
        font = pygame.font.SysFont(name, font_size, bold=True)
        show_text(font, name, (340, 80 + 60 * i))
        font = pygame.font.SysFont(name, font_size, italic=True)
        show_text(font, name, (740, 80 + 60 * i))

    font = pygame.font.Font('fonts/SAIBA-45-Regular-(v1.1).otf', font_size)
    show_text(font, 'Saiba', (40, 400))




if __name__ == '__main__':
    # инициализация Pygame:
    pygame.init()
    # размеры окна:
    size = width, height = 1100, 600
    # screen — холст, на котором нужно рисовать:
    screen = pygame.display.set_mode(size)

    fonts_demo()
    pygame.display.flip()
    # ожидание закрытия окна:
    while pygame.event.wait().type != pygame.QUIT:
        pass
    # завершение работы:
    pygame.quit()
