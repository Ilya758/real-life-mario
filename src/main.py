import pygame
from constants import FPS, HEIGHT, WIDTH, BLOCK_SIZE
from entities import Player, Fire, Block, Ground
from services import EventManagerService, GraphicsService, MusicService


class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption('REAL-LIFE-MARIO')
        self.window = pygame.display.set_mode((WIDTH, HEIGHT))
        self.music = MusicService()
        self.player = Player([0, 450, 50, 50], self.music)
        self.eventManager = EventManagerService(self.player)
        self.music.playMainTrack()
        self.handleGameLoop()

    def handleGameLoop(self):
        clock = pygame.time.Clock()
        bg, image = GraphicsService.getBackground('Blue.png')
        fire = Fire(100, HEIGHT - BLOCK_SIZE - 64, 16, 32)
        fire.on()
        ground = Ground(self.window).grid
        objects = [*ground, Block(0, HEIGHT - BLOCK_SIZE * 2,     BLOCK_SIZE),
                   Block(BLOCK_SIZE * 3, HEIGHT - BLOCK_SIZE * 4, BLOCK_SIZE), fire]

        while True:
            clock.tick(FPS)
            self.eventManager.handleEvents()
            self.player.loop(FPS, objects)
            GraphicsService.draw(self.window, bg, image, self.player, objects)
            fire.loop()


if __name__ == '__main__':
    Game()
