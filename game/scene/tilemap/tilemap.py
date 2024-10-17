from PIL import Image


class TileMap:

    def __init__(self, path="assets/bg_maps/69_bg_map.png"):
        self.image = Image.open(path)
        self.width, self.height = self.image.size
        self.pxs = self.image.load()

        self.matrix = []
        for y in range(self.height):
            row = []
            for x in range(self.width):

                row.append(None)

            self.matrix.append(row)
