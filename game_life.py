import pygame, os, sys
from pygame.locals import *
from pygame.sprite import Sprite, Group
from settings import Settings

import game_functions as gf
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
        
grid = []
supergrid = []
grp_to_update = Group()
gf.create_cellule(screen, settings, supergrid, grid, pos)
gf.check_neighbour(supergrid)
screen.fill(settings.color_bg)
gf.init_grid(supergrid)

while True:
    clock.tick(10)
    gf.check_event(supergrid, settings, grp_to_update)
    gf.update_screen(screen, settings, grp_to_update, supergrid)
