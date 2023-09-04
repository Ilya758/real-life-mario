import pygame

from services.GraphicsService import GraphicsService


class Player(pygame.sprite.Sprite):
    GRAVITY = 1
    SPRITES = GraphicsService.loadSpriteSheets(
        'MainCharacters', 'MaskDude', 32, 32, True)
    ANIMATION_DELAY = 3

    def __init__(self, x, y, w, h) -> None:
        self.rect = pygame.Rect(x, y, w, h)
        self.x_vel = 0
        self.y_vel = 0
        self.mask = None
        self.direction = 'left'
        self.animation_count = 0
        self.fall_count = 0
        self.jump_count = 0
        self.hit = False
        self.hitCount = 0

    def jump(self):
        self.y_vel = -self.GRAVITY * 8
        self.animation_count = 0
        self.jump_count += 1

        if self.jump_count == 1:
            self.fall_count = 0

    def move(self, dx, dy):
        self.rect.x += dx
        self.rect.y += dy

    def makeHit(self):
        self.hit = True
        self.hitCount = 0

    def move_left(self, vel):
        self.x_vel = -vel

        if self.direction != 'left':
            self.direction = 'left'
            self.animation_count = 0

    def move_right(self, val):
        self.x_vel = +val

        if self.direction != 'right':
            self.direction = 'right'
            self.animation_count = 0

    def landed(self):
        self.fall_count = 0
        self.y_vel = 0
        self.jump_count = 0

    def hitHead(self):
        self.count = 0
        self.y_vel *= -1

    def loop(self, fps):
        self.y_vel += min(1, (self.fall_count / fps) * self.GRAVITY)
        self.move(self.x_vel, self.y_vel)

        if self.hit:
            self.hitCount += 1

        if self.hitCount > fps * 2:
            self.hit = False
            self.hitCount = 0

        self.fall_count += 1
        self.updateSprite()

    def updateSprite(self):
        spriteSheet = 'idle'

        if self.hit:
            spriteSheet = 'hit'
        elif self.y_vel < 0:
            if self.jump_count == 1:
                spriteSheet = 'jump'
            elif self.jump_count == 2:
                spriteSheet = 'double_jump'
        elif self.y_vel > self.GRAVITY * 2:
            spriteSheet = 'fall'
        elif self.x_vel != 0:
            spriteSheet = 'run'

        spriteSheetName = spriteSheet + '_' + self.direction
        sprites = self.SPRITES[spriteSheetName]
        spriteIndex = (self.animation_count //
                       self.ANIMATION_DELAY) % len(sprites)
        self.sprite = sprites[spriteIndex]
        self.animation_count += 1
        self.update()

    def update(self):
        self.rect = self.sprite.get_rect(topleft=(self.rect.x, self.rect.y))
        self.mask = pygame.mask.from_surface(self.sprite)

    def draw(self, win, offsetX):
        win.blit(self.sprite, (self.rect.x - offsetX, self.rect.y))
