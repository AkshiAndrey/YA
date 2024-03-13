import pygame
import sys


def draw_ellipse(screen, color, rect, ):
    pygame.draw.ellipse(screen, color, rect, width=1)


try:
    n = int(input("Введите целое число n: "))
except ValueError:
    print("Неправильный формат ввода")
    sys.exit()

pygame.init()
screen = pygame.display.set_mode((300, 300))
pygame.display.set_caption("Сфера из эллипсов")

step = 300 / n // 2
for i in range(n):
    draw_ellipse(screen, (255, 255, 255), (0 + i * step, 0, 300 - (i * step * 2), 300))
    draw_ellipse(screen, (255, 255, 255), (0, 0 + i * step, 300, 300 - (i * step * 2)))

pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
