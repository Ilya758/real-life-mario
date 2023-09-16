import random
from src.constants import BLOCK_SIZE, HEIGHT
from src.entities.environment.units import Block


class Ground:
    def __init__(self, window) -> None:
        self._grid = []
        self.window = window
        self.prepare()

    @property
    def grid(self):
        return self._grid

    @grid.setter
    def grid(self, blocks):
        self._grid = blocks

    def prepareBlocks(self, start, end, isHole=False, pos=1, isGlass = False):
        return [Block(i * BLOCK_SIZE, HEIGHT - BLOCK_SIZE * pos, BLOCK_SIZE, isGlass, isHole)
                for i in range(start, end)]

    def prepare(self):
        middle = 4.5
        self.groundFactory()
        self.groundFactory(middle, True)

    def groundFactory(self, pos=1, isGlass = False):
        cooldown = False
        to = 450
        step = 2
        for tile in range(0, to):
            hole = bool(random.randint(0, 1))
            len = random.randint(0, step)
            if (cooldown):
                self.grid.extend(self.prepareBlocks(
                    tile, tile + len, False, pos, isGlass))
                cooldown = False
            else:
                self.grid.extend(self.prepareBlocks(
                    tile, tile + len, hole, pos, isGlass))
                cooldown = True
            tile += len

