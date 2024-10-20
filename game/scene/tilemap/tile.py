import pygame


class Tile(pygame.sprite.Sprite):
    def __init__(
        self,
        image: pygame.surface.Surface,
        pos: pygame.Vector2,
        group: pygame.sprite.Group,
        size: pygame.Vector2,
    ) -> None:

        super().__init__(group)

        self.size = size
        self.image = image
        self.rect = self.image.get_rect(topleft=pos)
