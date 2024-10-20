import logging
from pathlib import Path
from PIL import Image
import pygame

from game.scene.tilemap.palette import Palette
from game.scene.tilemap.tile import Tile


class TileMap:
    SIZE = pygame.Vector2(64, 64)

    def __init__(self, palette: Palette, camera_group: pygame.sprite.Group):
        self.palette = palette
        self.camera_group = camera_group

    def load_tiles(self, path: Path):
        image = Image.open(path)
        width, height = image.size
        pxs = image.load()

        for y in range(height):
            row = []
            for x in range(width):
                logging.debug(f"{x, y}: {pxs[x, y]}")
                pos = pygame.Vector2(x * self.SIZE.x, y * self.SIZE.y)
                logging.debug(f"pos: {pos}")

                tile = Tile(
                    image=pygame.transform.scale(
                        self.palette.get_image_by_px(pxs[x, y]), self.SIZE
                    ),
                    pos=pos,
                    group=self.camera_group,
                    size=self.SIZE,
                )
                row.append(tile)
