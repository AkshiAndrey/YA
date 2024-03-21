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

    def get_title_id(self, position):
        return self.map[position[1]][position[0]]

    def is_free(self, position):
        return self.get_title_id(position) in self.free_tiles


class Game:
    def __init__(self, labyrinth, hero):
        self.labyrinth = labyrinth
        self.hero = hero

    def render(self, screen):
        self.labyrinth.render(screen)
        self.hero.render(screen)

    def update_hero(self):
        next_x, next_y = self.hero.get_position()
        if pygame.key.get_pressed()[pygame.K_LEFT]:
            next_x -= 1
        if pygame.key.get_pressed()[pygame.K_RIGHT]:
            next_x += 1
        if pygame.key.get_pressed()[pygame.K_DOWN]:
            next_y += 1
        if pygame.key.get_pressed()[pygame.K_UP]:
            next_y -= 1
        if self.labyrinth.is_free((next_x, next_y)):
            self.hero.set_position((next_x, next_y))


class Hero:
    def __init__(self, position):
        self.x = position[0]
        self.y = position[1]

    def get_position(self):
        return self.x, self.y

    def set_position(self, position):
        self.x, self.y = position

    def render(self, screen):
        center = self.x * TILE_SIZE + TILE_SIZE // 2, self.y * TILE_SIZE + TILE_SIZE // 2
        pygame.draw.circle(screen, (255, 255, 255), center, TILE_SIZE // 2)


def main():
    pygame.init()
    screen = pygame.display.set_mode(WINDOW_SIZE)
    clock = pygame.time.Clock()
    lab = Labyrinth("Simple_map.txt", [0, 2], 2)
    hero = Hero((7, 7))
    game = Game(lab, hero)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            game.update_hero()
            screen.fill((0, 0, 0))

            game.render(screen)
            pygame.display.flip()
            clock.tick(FPS)
    pygame.display.quit()


if __name__ == "__main__":
    main()
