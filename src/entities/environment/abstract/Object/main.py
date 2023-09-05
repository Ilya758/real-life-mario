import pygame


class Object(pygame.sprite.Sprite):
    def __init__(self, x, y, w, h, name=None) -> None:
        self.rect = pygame.Rect(x, y, w, h)
        self.image = pygame.Surface((w, h), pygame.SRCALPHA)
        self.width = w
        self.height = h
        self.name = name

    def draw(self, win, offsetX):
        win.blit(self.image, (self.rect.x - offsetX, self.rect.y))
