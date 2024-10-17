import pygame


class Tile(pygame.sprite.Sprite):
    def __init__(
        self,
        pos: pygame.Vector2,
        group: pygame.sprite.Group,
        size: pygame.Vector2,
    ) -> None:

        super().__init__(group)

        self.size = size
        self.image = pygame.transform.scale(
            pygame.image.load("assets/sprites/tree.png").convert_alpha(),
            self.size,
        )
        self.rect = self.image.get_rect(topleft=pos)
