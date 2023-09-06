import pygame
from os.path import join

from enums import TrackName, ChannelAction


class MusicService:
    def __init__(self):
        self.mixer = pygame.mixer
        self.music = self.mixer.music
        self.music.set_volume(0.05)
        self.channels = self.initMixerChannels()

    def makeSound(self, channelName, volume):
        sound = pygame.mixer.Sound(f'../assets/music/{channelName}.mp3')
        sound.set_volume(volume)

        return sound

    def initMixerChannels(self):
        channels = [['jump', 0.25], ['death', 0.5], ['fart', 0.05]]

        return {ch: [i + 1, self.makeSound(ch, vol)] for i, [ch, vol] in enumerate(channels)}

    def playMainTrack(self, trackPath=TrackName.MainMenu.value):
        self.music.load(join(f'../assets/music/{trackPath}.mp3'))
        self.music.play(loops=-1)

    def setVolume(self, volume):
        self.music.set_volume(volume)

    def triggerSoundAction(self, name, action: ChannelAction):
        [id, sound] = self.channels[name]
        channel = self.mixer.Channel(id)

        match action:
            case ChannelAction.Play.value:
                channel.play(sound, loops=0)
            case ChannelAction.Stop.value:
                channel.stop()
