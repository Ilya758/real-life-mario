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
        self.clock = pygame.time.Clock()
        self.player = Player([0, 450, 50, 50], self.music)
        self.eventManager = EventManagerService(self.player)
        self.music.playMainTrack()
        self.handleGameLoop()

    def handleGameLoop(self):
        fire = Fire(100, HEIGHT - BLOCK_SIZE - 64, 16, 32)
        fire.on()
        ground = Ground(self.window).grid
        objects = [*ground, Block(0, HEIGHT - BLOCK_SIZE * 2,     BLOCK_SIZE), fire]

        while True:
            self.clock.tick(FPS)
            self.player.loop(FPS, objects)
            self.eventManager.handleEvents()
            GraphicsService.draw(self.window, self.player, objects)
            fire.loop()


if __name__ == '__main__':
    Game()
