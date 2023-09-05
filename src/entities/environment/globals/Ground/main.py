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

    def prepareBlocks(self, start, end, isHole=False):
        return [Block(i * BLOCK_SIZE, HEIGHT - BLOCK_SIZE, BLOCK_SIZE, isHole)
                for i in range(start, end)]

    def prepare(self):
        self.grid = [
            *self.prepareBlocks(0, 10), *self.prepareBlocks(10, 12, True), *self.prepareBlocks(12, 13), *self.prepareBlocks(13, 14, True), *self.prepareBlocks(15, 16)]
