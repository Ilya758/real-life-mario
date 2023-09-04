import pygame

from entities.Player import Player
from entities.environment.Fire import Fire
from entities.environment.Block import Block
from constants import FPS, HEIGHT, WIDTH, BLOCK_SIZE, SCROLL_AREA_WIDTH
from services.MovementService import MovementService
from services.GraphicsService import GraphicsService


class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption('REAL-TIME-MARIO')
        self.window = pygame.display.set_mode((WIDTH, HEIGHT))
        self.offsetX = 0
        self.handleGameLoop()

    def handleGameLoop(self):
        clock = pygame.time.Clock()
        bg, image = GraphicsService.getBackground('Blue.png')
        run = True
        player = Player(100, 100, 50, 50)
        fire = Fire(100, HEIGHT - BLOCK_SIZE - 64, 16, 32)
        fire.on()
        floor = [Block(i * BLOCK_SIZE, HEIGHT - BLOCK_SIZE, BLOCK_SIZE)
                 for i in range(-WIDTH // BLOCK_SIZE, WIDTH * 2 // BLOCK_SIZE)]
        objects = [*floor, Block(0, HEIGHT - BLOCK_SIZE * 2,     BLOCK_SIZE),
                   Block(BLOCK_SIZE * 3, HEIGHT - BLOCK_SIZE * 4, BLOCK_SIZE), fire]

        while run:
            clock.tick(FPS)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    break
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP and player. jump_count < 2:
                        player.jump()

            player.loop(FPS)
            fire.loop()
            MovementService.handleMove(player, objects)
            GraphicsService.draw(self.window, bg, image,
                                 player, objects, self.offsetX)

            self.handleBackgroundScrolling(player)

        pygame.quit()
        quit()

    def handleBackgroundScrolling(self, player):
        if (player.rect.right - self.offsetX >= WIDTH - SCROLL_AREA_WIDTH and player.x_vel > 0) or (player.rect.   left - self.offsetX <= SCROLL_AREA_WIDTH and player.x_vel < 0):
            self.offsetX += player.x_vel


if __name__ == '__main__':
    Game()
