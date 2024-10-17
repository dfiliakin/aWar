from pathlib import Path
from utils.utils import cached
import pygame
import os


class Palette:
    SIZE = (32, 32)
    FILE_EXTENSION = ".png"

    def __init__(self, dir: Path):
        self.dir = dir

    def _load_images_from_dir_by_prefix(self, prefix):
        images = []
        for image_path in os.listdir(self.dir):
            if image_path.startswith(prefix) and image_path.endswith(
                self.FILE_EXTENSION
            ):
                image = pygame.image.load(image_path).convert_alpha()
                image = pygame.transform.scale(image, self.SIZE)

        return images


class GroundPalette(Palette):
    @property
    @cached()
    def bare_ground(self):
        return self._load_images_from_dir_by_prefix("bare_ground")

    @property
    @cached()
    def grass(self):
        return self._load_images_from_dir_by_prefix("grass")
