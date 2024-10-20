import logging
import sys
from pathlib import Path
from random import randint

import pygame

from game.player import Player
from game.scene.camera.camera import Camera
from game.scene.objects.tree import Tree
from game.scene.tilemap.ground_palette import GroundPalette
from game.scene.tilemap.tilemap import TileMap

logging.basicConfig(level=logging.INFO)

pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
pygame.event.set_grab(True)

# setup camera
camera = Camera()

# setup player
player = Player((640, 360), camera.objects)

# setup background
ground_tiles = TileMap(
    palette=GroundPalette(),
    camera_group=camera.background,
).load_tiles(path="./assets/bg_maps/69_bg_map.png")

# setup trees
for i in range(100):
    random_x = randint(1000, 2000)
    random_y = randint(1000, 2000)
    Tree((random_x, random_y), camera.objects)

# run
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()

        if event.type == pygame.MOUSEWHEEL:
            camera.zoom_scale += event.y * 0.03

    camera.update()
    camera.custom_draw(player)

    pygame.display.update()
    clock.tick(60)
