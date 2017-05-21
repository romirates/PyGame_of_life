import sys
import random
import pygame
from cellule import Cellule
def init_grid(supergrid):
    for grid in supergrid:
        for cell in grid:
            cell.draw_cellule()

def set_cellule_rand(supergrid, settings):
    for grid in supergrid:
        for cell in grid:
            if random.randrange(2):
                cell.alive = True
            else:
                cell.alive = False
            cell.update(settings)
def set_group(supergrid, grp_to_update):
    for grid in supergrid:
        for cell in grid:
            cell.alive_neigbr()
            if cell.alive:
                grp_to_update.add(cell)
                for neigbr in cell.neighbour:
                    grp_to_update.add(neigbr)

    

def update_grp(grp_to_update):
    grp = grp_to_update.copy()
    grp_to_update.empty()
    for cell in grp:
        cell.alive_neigbr()
        if cell.alive:
            grp_to_update.add(cell)
            for neigbr in cell.neighbour:
                grp_to_update.add(neigbr)

def check_event(supergrid, settings, grp_to_update):
    """fonction generique de gestion des events"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT :
            sys.exit()
        if pygame.mouse.get_pressed()[0]:
            for grid in supergrid:
                for cell in grid:
                    if cell.rect.collidepoint(pygame.mouse.get_pos()):
                        cell.alive = True
                        cell.update(settings)
        elif pygame.mouse.get_pressed()[2]:
            for grid in supergrid:
                for cell in grid:
                    if cell.rect.collidepoint(pygame.mouse.get_pos()):
                        cell.alive = False
                        cell.update(settings)
                        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if settings.run_game:
                    settings.run_game = False
                else:
                    settings.run_game = True
                    set_group(supergrid, grp_to_update)
            elif event.key == pygame.K_r:
                set_cellule_rand(supergrid, settings)
def create_cellule(screen, settings, supergrid, grid, pos):
    """fonction qui va cree et positionner les cellules selon les paramètres"""
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

def check_neighbour(supergrid):
    """check the neighbourhood of each cellule"""
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

def update_screen(screen, settings,  grp_to_update, supergrid):
    #screen.fill(settings.color_bg)
    if settings.run_game:
        """smarthly updated cell (don't really work)
        grp_to_update.update(settings)
        update_grp(grp_to_update)"""
        """full retard way"""
        for grid in supergrid:
            for cell in grid:
                cell.update(settings)
        for grid in supergrid:
            for cell in grid:
                cell.alive_neigbr()

    pygame.display.flip()
