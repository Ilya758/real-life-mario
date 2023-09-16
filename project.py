import pygame
from src.constants import FPS, HEIGHT, WIDTH, BLOCK_SIZE
from src.entities import Player, Block, Ground
from src.services import EventManagerService, GraphicsService, MusicService


def main():
    Game()

def createPlayer(music):
    return Player([0, 450, 50, 50], music)
    

def drawGameOverScreen(window):
    window.fill((0, 0, 0))
    font = pygame.font.SysFont('arial', 40)
    title = font.render('Game Over', True, (255, 255, 255))
    window.blit(title, (800 / 2 - title.get_width() / 2, 600 / 2 -title.get_height() / 3))
    pygame.display.update()
    return True

def handleGameLoop(self, test = False):
    ground = Ground(self.window).grid
    objects = [*ground, Block(0, HEIGHT - BLOCK_SIZE * 2, BLOCK_SIZE)]

    if test:
        return True

    while True:
        self.clock.tick(FPS)
        self.eventManager.handleEvents()

        if self.player.lifes == 0:
            drawGameOverScreen(self.window)
        else:
            self.player.loop(FPS, objects)
            GraphicsService.draw(self.window, self.player, objects)



class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption('Platformer')
        self.window = pygame.display.set_mode((WIDTH, HEIGHT))
        self.music = MusicService()
        self.clock = pygame.time.Clock()
        self.player = createPlayer(self.music)
        self.eventManager = EventManagerService(self.player)
        self.music.playMainTrack()
        handleGameLoop(self, False)


if __name__ == '__main__':
    main()
