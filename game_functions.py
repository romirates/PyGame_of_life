import sys
import random
from itertools import chain
import pygame
from cellule import Cellule

def init_grid(supergrid):
    #for grid in supergrid:
    #    for cell in grid:
    for cell in chain.from_iterable(supergrid):
        cell.draw_cellule()

def set_cells_rand(supergrid, settings):
    #for grid in supergrid:
    #    for cell in grid:
    for cell in chain.from_iterable(supergrid):
        if random.randrange(2):
            cell.alive = True
        else:
            cell.alive = False
        cell.update(settings)
def check_event(supergrid, settings):
    """will check keyboard event
    """
    for event in pygame.event.get():
        if event.type == pygame.QUIT :
            sys.exit()
        #mouse button left : alive cell
        if pygame.mouse.get_pressed()[0]:
            for cell in chain.from_iterable(supergrid):
                if cell.rect.collidepoint(pygame.mouse.get_pos()):
                    cell.alive = True
                    cell.update(settings)
        #mouse button right : dead cell
        elif pygame.mouse.get_pressed()[2]:
            for cell in chain.from_iterable(supergrid):
                if cell.rect.collidepoint(pygame.mouse.get_pos()):
                    cell.alive = False
                    cell.update(settings)
        #space button : start / pause
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if settings.run_game:
                    settings.run_game = False
                else:
                    settings.run_game = True
        #r button : randomized
            elif event.key == pygame.K_r:
                set_cells_rand(supergrid, settings)

def create_cells(screen, settings, supergrid, pos):
    """create and place the cells accordings to the parameters'"""
    grid = []
    while pos[1] <= settings.screen_height:
        new_cell = Cellule(screen, settings, pos)
        grid.append(new_cell)
        #si le nouveau cube ne peut être placer plus à gauche (+x) descend d'un rand vers le bas (+y)
        if (pos[0]+settings.rect_dim+2*settings.espacement) > settings.screen_width:
            supergrid.append(grid)
            grid = []
            pos =   (
                    settings.rect_dim+settings.espacement, 
                    pos[1]+settings.espacement+settings.rect_dim
                    )
        #sinon deplace d'un rang vers la gauche (+x)
        else:
            pos = (pos[0]+settings.rect_dim+settings.espacement, pos[1])

def create_neighbour(supergrid):
    """create the neighbourhood of each cell"""
    for i, grid in enumerate(supergrid):
        for j, cell in enumerate(grid):
            if j != 0:
                #left
                cell.neighbour.append(supergrid[i][j-1])
                if i != 0:
                    #up_left
                    cell.neighbour.append(supergrid[i-1][j-1])
                if i != (len(supergrid)-1):
                    #down_left
                   cell.neighbour.append(supergrid[i+1][j-1])
            if j != (len(grid)-1):
                #right
                cell.neighbour.append(supergrid[i][j+1])

                if i != 0:
                    #up_right
                    cell.neighbour.append(supergrid[i-1][j+1])
                if i != (len(supergrid)-1):
                    #down_right
                    cell.neighbour.append(supergrid[i+1][j+1])
            if i != 0:
                #up
                cell.neighbour.append(supergrid[i-1][j])
            if i != (len(supergrid)-1):
                #down
                cell.neighbour.append(supergrid[i+1][j])

def update_screen(screen, settings, supergrid):
    if settings.run_game:
        for cell in chain.from_iterable(supergrid):
            cell.alive_neigbr()
        for cell in chain.from_iterable(supergrid):
            cell.update(settings)
            
    pygame.display.flip()
