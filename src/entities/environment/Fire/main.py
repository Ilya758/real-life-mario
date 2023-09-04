import pygame

from entities.environment.Object import Object
from services.GraphicsService import GraphicsService


class Fire(Object):
    ANIMATION_DELAY = 3

    def __init__(self, x, y, w, h):
        super().__init__(x, y, w, h, 'fire')
        self.fire = GraphicsService.loadSpriteSheets('Traps', 'Fire', w, h)
        self.image = self.fire['off'][0]
        self.mask = pygame.mask.from_surface(self.image)
        self.animation_count = 0
        self.animation_name = 'off'

    def on(self):
        self.animation_name = 'on'

    def off(self):
        self.animation_name = 'off'

    def loop(self):
        sprites = self.fire[self.animation_name]
        spriteIndex = (self.animation_count //
                       self.ANIMATION_DELAY) % len(sprites)

        self.image = sprites[spriteIndex]
        self.animation_count += 1
        self.rect = self.image .get_rect(topleft=(self.rect.x, self.rect.y))
        self.mask = pygame.mask.from_surface(self.image)

        if self.animation_count // self.ANIMATION_DELAY > len(sprites):
            self.animation_count = 0
