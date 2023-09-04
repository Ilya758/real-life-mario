from enum import Enum

BG_COLOR = (255, 255, 255)
WIDTH, HEIGHT = 800, 600
FPS = 60
PLAYER_VEL = 5
BLOCK_SIZE = 96
SCROLL_AREA_WIDTH = 200


class TrackName(Enum):
    Boss = 'boss'
    Credits = 'credits'
    MainMenu = 'main-menu'
    MainTheme = 'main-theme'
