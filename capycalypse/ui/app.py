import pygame

from capycalypse import config

class App:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((config.WIDTH, config.HEIGHT))   # Taille de l'écran
        pygame.display.set_caption("Capycalypse")                              # Nom du jeu sur la fenêtre
        self.clock = pygame.time.Clock()                                       # Commencer un timer
        self.running = True

    def run(self):
        while self.running:
            dt = self.clock.tick(config.FPS) / 1000                            # Le Delta Time est mis sur 1000 secondes depuis l'image précédente
            for event in pygame.event.get():
                if event.type == pygame.QUIT:                                  # Arrêtre le jeu
                    self.running = False
            self.screen.fill((28, 23, 24))
            pygame.display.flip()                                              # Affiche ce qu'on a dessiné
        pygame.quit()
