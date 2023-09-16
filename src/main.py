import pygame
from constants import FPS, HEIGHT, WIDTH, BLOCK_SIZE
from entities import Player, Block, Ground
from services import EventManagerService, GraphicsService, MusicService


def main():
    Game()

class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption('Platformer')
        self.window = pygame.display.set_mode((WIDTH, HEIGHT))
        self.music = MusicService()
        self.clock = pygame.time.Clock()
        self.player = Player([0, 450, 50, 50], self.music)
        self.eventManager = EventManagerService(self.player)
        self.music.playMainTrack()
        self.handleGameLoop()

    def drawGameOverScreen(self):
        self.window.fill((0, 0, 0))
        font = pygame.font.SysFont('arial', 40)
        title = font.render('Game Over', True, (255, 255, 255))
        self.window.blit(title, (800 / 2 - title.get_width() / 2, 600 / 2 - title.get_height() / 3))
        pygame.display.update()

    def handleGameLoop(self):
        ground = Ground(self.window).grid
        objects = [*ground, Block(0, HEIGHT - BLOCK_SIZE * 2, BLOCK_SIZE)]

        while True:
            self.clock.tick(FPS)
            self.eventManager.handleEvents()

            if self.player.lifes == 0:
                self.drawGameOverScreen()
            else:
                self.player.loop(FPS, objects)
                GraphicsService.draw(self.window, self.player, objects)


if __name__ == '__main__':
    main()
