from src.constants import HEIGHT, WIDTH
from src.services import MusicService
from project import Game, createPlayer, drawGameOverScreen, handleGameLoop
import pygame

def test_createPlayer():
    pygame.init()
    assert 3 == createPlayer(MusicService()).lifes

def test_drawGameOverScreen():
    pygame.init()
    assert True == drawGameOverScreen(pygame.display.set_mode((WIDTH, HEIGHT)))

def test_handleGameLoop():
    pygame.init()
    assert True == handleGameLoop(Game())