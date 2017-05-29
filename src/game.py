import level_loader

class Game:
    def __init__(self):
        self.level = None
        self.tilewidth = 0
        self.tileheight = 0
        self.background_color = "black"
        return

    def loadLevel(self):
        self.level = level_loader.Level("../assets/map.tmx")
        self.tilewidth = self.level.tiled_map.tilewidth
        self.tileheight = self.level.tiled_map.tileheight
        if self.level.tiled_map.background_color:
            self.background_color = self.level.tiled_map.background_color
        return

    def update(self):
        return
