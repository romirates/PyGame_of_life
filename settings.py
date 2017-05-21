class Settings():
    def __init__(self):
        # parametre de la fenetre
        self.screen_width = 800 
        self.screen_height = 600
        self.color_bg = (250, 250, 250)
        # parametre carre
        self.rect_dim = 10
        self.espacement = 2
        self.rect_color_dead = (0, 0, 0)
        self.rect_color_alive = (255, 255, 0)
        self.rect_color_test = (40, 0, 40) 
        self.run_game = False
