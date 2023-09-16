import pygame
from src.constants import PLAYER_VEL
from src.enums import GameEventType, Jump, Y_AxisBoundary, ChannelAction
from src.services import CollisionService, GraphicsService


class Player(pygame.sprite.Sprite):
    GRAVITY = 1
    SPRITES = GraphicsService.loadSpriteSheets(
        'MainCharacters', 'MaskDude', 32, 32, True)
    ANIMATION_DELAY = 3

    def __init__(self, rect, music) -> None:
        self.rect = pygame.Rect(rect)
        self.x_vel = 0
        self.y_vel = 0
        self.mask = None
        self.direction = 'left'
        self.animation_count = 0
        self.fall_count = 0
        self.jumpCount = Jump.Default.value
        self.hit = False
        self.hitCount = 0
        self.music = music
        self.lifes = 3

    def jump(self):
        self.y_vel = -self.GRAVITY * 12
        self.animation_count = 0
        self.jumpCount += 1
        self.music.toggleJumpSound()

        if self.jumpCount == Jump.Single.value:
            self.fall_count = 0

    def move(self, dx, dy):
        self.rect.x += dx
        self.rect.y += dy

    def makeHit(self):
        self.hit = True
        self.hitCount = 0
        self.lifes -= 1

    def moveLeft(self, vel):
        self.x_vel = -vel

        if self.direction != 'left':
            self.direction = 'left'
            self.animation_count = 0

    def moveRight(self, val):
        self.x_vel = +val

        if self.direction != 'right':
            self.direction = 'right'
            self.animation_count = 0

    def land(self):
        self.fall_count = 0
        self.y_vel = 0
        self.jumpCount = Jump.Default.value

    def hitHead(self):
        self.count = 0
        self.y_vel *= -1

    def recoverFromFall(self):
        self.GRAVITY = 1

    def loop(self, fps, objects):
        self.y_vel += min(1, (self.fall_count / fps) * self.GRAVITY)
        self.move(self.x_vel, self.y_vel)
        self.checkTheLowestGameBoundary()

        if self.hit:
            self.hitCount += 1

        if self.hitCount > fps:
            self.hit = False
            self.hitCount = 0

        self.fall_count += 1
        self.updateSprite()
        self.handleMove(objects)

    def checkTheLowestGameBoundary(self):
        if self.rect.y > Y_AxisBoundary.Lowest.value:
            self.music.triggerSoundAction('death', ChannelAction.Play.value)
            self.rect.y = Y_AxisBoundary.Highest.value
            self.y_vel = 0
            self.GRAVITY = 0.1
            self.makeHit()
            pygame.time.set_timer(pygame.event.Event(
                GameEventType.OutOfTheLowestBoundary.value), 1000, loops=1)

    def handleMove(self, objects):
        keys = pygame.key.get_pressed()
        self.x_vel = 0
        collideLeft = CollisionService.collide(
            self, objects, -PLAYER_VEL * 2)
        collideRight = CollisionService.collide(
            self, objects, PLAYER_VEL * 2)

        if keys[pygame.K_a] and not collideLeft:
            self.moveLeft(PLAYER_VEL)
        if keys[pygame.K_d] and not collideRight:
            self.moveRight(PLAYER_VEL)

        CollisionService.handleVerticalCollisions(
            self, objects, self.y_vel)

    def updateSprite(self):
        spriteSheet = 'idle'

        if self.hit:
            spriteSheet = 'hit'
        elif self.y_vel < 0:
            match self.jumpCount:
                case Jump.Single.value:
                    spriteSheet = 'jump'
                case Jump.Double.value:
                    spriteSheet = 'double_jump'
        elif self.y_vel > self.GRAVITY * 2:
            spriteSheet = 'fall'
            self.jumpCount = Jump.Double.value
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
