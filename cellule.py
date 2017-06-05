import pygame
import math
from pygame.sprite import Sprite
class Cellule(Sprite):
    """define a cell """
    def __init__(self, screen, settings, pos):
        super().__init__()
        #pointer to the "windows"
        self.screen = screen
        #a rectangular sprite
        self.rect = pygame.Rect(0, 0, settings.rect_dim, settings.rect_dim)
        #x-y position of the spire
        self.rect.bottomright = pos
        #alive statut
        self.alive = False
        #default color
        self.color = settings.rect_color_dead
        #list of the neighbour 
        self.neighbour = []
        #number of alive neighbour :( 
        self.neighbour_alive = 0

    def alive_neigbr(self):
        """update the number of alive neighbour """
        self.neighbour_alive = 0
        if self.neighbour:
            for cell in self.neighbour:
                if cell.alive: self.neighbour_alive += 1

    def update(self, settings):
        """update the state of the cell """
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
        """change the color of the cell defined by the settings"""
        if self.alive:
            self.color = settings.rect_color_alive
        else:
            self.color = settings.rect_color_dead

    def draw_cellule(self):
        """draw the cell on the board with the pygame tools"""
        pygame.draw.rect(self.screen, self.color, self.rect)
