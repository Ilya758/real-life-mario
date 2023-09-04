import pygame
from os import listdir
from os.path import isfile, join
from constants import HEIGHT, WIDTH


class GraphicsService:
    @staticmethod
    def flip(sprites):
        return [pygame.transform.flip(sprite, True, False) for sprite in sprites]

    @staticmethod
    def getBlock(size):
        path = join('../assets', 'Terrain', 'Terrain.png')
        image = pygame.image.load(path).convert_alpha()
        surface = pygame.Surface((size, size), pygame.SRCALPHA, 32)
        rect = pygame.Rect(96, 0, size, size)
        surface.blit(image, (0, 0), rect)

        return pygame.transform.scale2x(surface)

    @staticmethod
    def loadSpriteSheets(dir1, dir2, w, h, direction=False):
        pygame.display.set_mode((WIDTH, HEIGHT))
        path = join("../assets", dir1, dir2)
        images = [f for f in listdir(path) if isfile(join(path, f))]

        all_sprites = {}

        for image in images:
            spriteSheet = pygame.image.load(join(path, image)).convert_alpha()
            sprites = []

            for i in range(spriteSheet.get_width() // w):
                surface = pygame.Surface((w, h), pygame.SRCALPHA, 32)
                rect = pygame.Rect(i * w, 0, w, h)
                surface.blit(spriteSheet, (0, 0), rect)
                sprites.append(pygame.transform.scale2x(surface))

            pathToReplace = image.replace(".png", "")

            if direction:
                all_sprites[pathToReplace + "_right"] = sprites
                all_sprites[pathToReplace +
                            "_left"] = GraphicsService.flip(sprites)
            else:
                all_sprites[image.replace(".png", "")] = sprites

        return all_sprites

    @staticmethod
    def getBackground(name):
        image = pygame.image.load(join(
            '../assets', 'bg', name
        ))
        _, _, width, height = image.get_rect()
        tiles = []

        for i in range(WIDTH // width + 1):
            for j in range(HEIGHT // height + 1):
                pos = [i * width, j * height]
                tiles.append(pos)

        return tiles, image

    @staticmethod
    def draw(window, bg, bg_image, player, objects, offsetX):
        for tile in bg:
            window.blit(bg_image, tuple(tile))

        for obj in objects:
            obj.draw(window, offsetX)

        player.draw(window, offsetX)
        pygame.display.update()
