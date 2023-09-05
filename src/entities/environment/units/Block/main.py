import pygame

from entities.environment.abstract import Object
from services import GraphicsService


class Block(Object):
    def __init__(self, x, y, size, isHole=False):
        super().__init__(x, y, size, size)
        block = GraphicsService.getBlock(size)
        self.image.blit(block, self.getBody(isHole))
        self.mask = pygame.mask.from_surface(self.image)

    def getBody(self, isHole):
        return (100, 100) if isHole else (0, 0)
