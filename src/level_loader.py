import pytmx

from pytmx.util_pygame import load_pygame

class Level:
    def __init__(self, filepath):
        self.tiled_map = load_pygame(filepath)
        self.layers = self.tiled_map.layers
        return
