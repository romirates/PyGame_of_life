import pygame, os, sys
from pygame.locals import *
from pygame.sprite import Sprite, Group
from settings import Settings

import game_functions as gf
"""
Main :
- init the pygame tools
- init the game grid as a matrix 
- start the game as a infine loop, check keyboard event and cell "mutation" each loop

"""
pygame.init()
clock = pygame.time.Clock()
settings = Settings()
screen = pygame.display.set_mode(
    (settings.screen_width, settings.screen_height))
pygame.display.set_caption("game of life")

pos =   (
        settings.rect_dim+settings.espacement, 
        settings.rect_dim+settings.espacement
        )
supergrid = []
gf.create_cells(screen, settings, supergrid, pos)
gf.create_neighbour(supergrid)
screen.fill(settings.color_bg)
gf.init_grid(supergrid)

while True:
    #number of frame per second (default : 10)
    clock.tick(10)
    gf.check_event(supergrid, settings)
    gf.update_screen(screen, settings, supergrid)
