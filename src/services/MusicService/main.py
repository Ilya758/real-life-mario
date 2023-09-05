import pygame
from os.path import join

from enums import TrackName


class MusicService:
    def __init__(self):
        self.music = pygame.mixer.music
        self.music.set_volume(0.2)
        self.loadTrack(TrackName.MainTheme.value)

    def loadTrack(self, trackPath):
        self.music.load(join(f'../assets/music/{trackPath}.mp3'))
        self.music.play(loops=-1)

    def setVolume(self, volume):
        self.music.set_volume(volume)
