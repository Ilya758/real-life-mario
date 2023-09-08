import pygame
from os import listdir
from os.path import isfile, join
from constants import HEIGHT, WIDTH, SCROLL_AREA_WIDTH


class GraphicsService:
    offsetX = 0

    @staticmethod
    def flip(sprites):
        return [pygame.transform.flip(sprite, True, False) for sprite in sprites]

    @staticmethod
    def getBlock(size, isGlass = False):
        path = join('../assets', 'Terrain', 'Terrain.png')
        image = pygame.image.load(path).convert_alpha()
        surface = pygame.Surface((size, size), pygame.SRCALPHA, 32)
        rect = pygame.Rect(0, 0 if isGlass else 128, size, size)
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
                all_sprites[pathToReplace] = sprites

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
    def renderUI(player, window):
        healthbar = pygame.image.load(
            '../assets/ui/health.png').convert_alpha()
        healthbar = pygame.transform.scale(healthbar, (150, 280))
        yCoord = 80 * (3 - player.lifes) if player.lifes > 0 else 80 * 3
        window.blit(healthbar, (20, 20), pygame.Rect(
            0, yCoord, 150, 40))

    @staticmethod
    def draw(window, player, objects):
        bg, image = GraphicsService.getBackground('Blue.png')

        for tile in bg:
            window.blit(image, tuple(tile))

        for obj in objects:
            obj.draw(window, GraphicsService.offsetX)

        player.draw(window, GraphicsService.offsetX)
        GraphicsService.handleBackgroundScrolling(player)
        GraphicsService.renderUI(player, window)
        pygame.display.update()

    @staticmethod
    def handleBackgroundScrolling(player):
        if (player.rect.right - GraphicsService.offsetX >= WIDTH - SCROLL_AREA_WIDTH
                and player.x_vel > 0) or (player.rect.left - GraphicsService.offsetX <= SCROLL_AREA_WIDTH and player.x_vel < 0):
            GraphicsService.offsetX += player.x_vel
