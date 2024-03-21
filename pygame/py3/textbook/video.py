import pygame



WINDOW_SIZE = WINDOW_WIDTH, WINDOW_HEIGHT = 501, 501
FPS = 15
MAP_DIR = 'maps'
TILE_SIZE = 32


class Labyrinth:
    def __init__(self, filename, free_tiles, finish_tile):
        self.map = []
        with open(f"{MAP_DIR}/{filename}") as input_file:
            for line in input_file:
                self.map.append(list(map(int, line.split())))
        self.height = len(self.map)
        self.width = len(self.map[0])
        self.tile_size = TILE_SIZE
        self.free_tiles = free_tiles
        self.finish_tile = finish_tile

    def render(self, screen):
        colors = {0: (0, 0, 0), 1: (120, 120, 120), 2: (50, 50, 50)}
        for y in range(self.height):
            for x in range(self.width):
                rect = pygame.Rect(x * self.tile_size, y * self.tile_size,
                                   self.tile_size, self.tile_size)
                screen.fill(colors[self.map[y][x]], rect)



def main():
    pygame.init()
    screen = pygame.display.set_mode(WINDOW_SIZE)
    clock = pygame.time.Clock()
    lab = Labyrinth("Simple_map.txt", 0, 2)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            screen.fill((0, 0, 0))
            lab.render(screen)
            pygame.display.flip()
            clock.tick(FPS)
    pygame.display.quit()


if __name__ == "__main__":
    main()


