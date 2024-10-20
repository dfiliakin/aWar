import logging
from pathlib import Path
import random
import pygame
import os


class Palette:
    FOLDER = None
    FILE_EXTENSION = ".png"

    @property
    def px_to_image(self) -> dict[tuple[int, int, int], pygame.surface.Surface]:
        raise NotImplementedError(".sprites mapping should be defined in children.")

    def _load_tiles_from_dir_by_prefix(self, prefix):
        images = []

        for image_path in os.listdir(self.FOLDER):
            if image_path.startswith(prefix) and image_path.endswith(
                self.FILE_EXTENSION
            ):
                logging.debug(f"Image to load: {image_path}")
                image = pygame.image.load(
                    Path.joinpath(self.FOLDER, image_path)
                ).convert_alpha()
                images.append(image)

        return images

    def get_image_by_px(self, px: tuple[int, int, int]) -> pygame.surface.Surface:
        logging.debug(f"px: {px}")

        image = random.choice(self.px_to_image.get(px))
        logging.debug(f"image: {image}")

        return image
