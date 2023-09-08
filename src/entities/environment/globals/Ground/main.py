import random
from constants import BLOCK_SIZE, HEIGHT
from entities.environment.units import Block


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

    def prepareBlocks(self, start, end, isHole=False, pos=1):
        return [Block(i * BLOCK_SIZE, HEIGHT - BLOCK_SIZE * pos, BLOCK_SIZE, isHole)
                for i in range(start, end)]

    def prepare(self):
        middle = 4.5
        self.groundFactory()
        self.groundFactory(middle)

    def groundFactory(self, pos=1):
        cooldown = False
        to = 450
        step = 2
        for tile in range(0, to):
            hole = bool(random.randint(0, 1))
            len = random.randint(0, step)
            if (cooldown):
                self.grid.extend(self.prepareBlocks(
                    tile, tile + len, False, pos))
                cooldown = False
            else:
                self.grid.extend(self.prepareBlocks(
                    tile, tile + len, hole, pos))
                cooldown = True
            tile += len

# TODO: replace ground
# look at dynamic backgrounds
# change main player sprite
# create fart animation on double jump
