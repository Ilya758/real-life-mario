import pygame
from src.entities.environment.abstract import Object
from src.services import GraphicsService


class Block(Object):
    def __init__(self, x, y, size, isGlass = False, isHole=False):
        super().__init__(x, y, size, size)
        block = GraphicsService.getBlock(size, isGlass)
        self.image.blit(block, self.getBody(isHole))
        self.mask = pygame.mask.from_surface(self.image)

    def getBody(self, isHole):
        return (100, 100) if isHole else (0, 0)
