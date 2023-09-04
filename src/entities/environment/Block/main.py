import pygame

from entities.environment.Object import Object
from services.GraphicsService import GraphicsService


class Block(Object):
    def __init__(self, x, y, size):
        super().__init__(x, y, size, size)
        block = GraphicsService.getBlock(size)
        self.image.blit(block, (0, 0))
        self.mask = pygame.mask.from_surface(self.image)
