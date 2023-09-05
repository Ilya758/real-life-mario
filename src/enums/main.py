from enum import Enum


class TrackName(Enum):
    Boss = 'boss'
    Credits = 'credits'
    MainMenu = 'main-menu'
    MainTheme = 'main-theme'


class Jump(Enum):
    Default = 0
    Single = 1
    Double = 2


class Y_AxisBoundary(Enum):
    Highest = 50
    Lowest = 500


class GameEventType(Enum):
    GameOver = 0
    OutOfTheLowestBoundary = 1
