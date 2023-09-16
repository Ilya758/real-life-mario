import pygame
from src.enums import GameEventType


class EventManagerService:
    def __init__(self, player) -> None:
        self.player = player

    def handleEvents(self):
        for event in pygame.event.get():
            match event.type:
                case pygame.QUIT:
                    pygame.quit()
                    quit()
                case pygame.KEYDOWN:
                    if event.key == pygame.K_w and self.player.jumpCount < 2:
                        self.player.jump()
                case GameEventType.OutOfTheLowestBoundary.value:
                    self.player.recoverFromFall()
                case _:
                    continue
