import pygame
import math
from pygame.sprite import Sprite
class Cellule(Sprite):
    """definie les cellules du jeu de la vie"""
    def __init__(self, screen, settings, pos):
        super().__init__()
        self.screen = screen
        self.rect = pygame.Rect(0, 0, settings.rect_dim, settings.rect_dim)
        self.rect.bottomright = pos
        self.alive = False
        self.color = settings.rect_color_dead
        self.neighbour = []
        self.neighbour_alive = 0

    def alive_neigbr(self):
        self.neighbour_alive = 0
        if self.neighbour:
            for cell in self.neighbour:
                if cell.alive: self.neighbour_alive += 1

    def update(self, settings):
        if settings.run_game:
            if self.alive:
                if self.neighbour_alive < 2 or self.neighbour_alive > 3:
                    self.alive = False
            else:
                if self.neighbour_alive == 3:
                    self.alive = True
        self.set_color(settings)
        self.draw_cellule()
                
    def set_color(self, settings):
        if self.alive:
            self.color = settings.rect_color_alive
        else:
            self.color = settings.rect_color_dead

    def draw_cellule(self):
        pygame.draw.rect(self.screen, self.color, self.rect)