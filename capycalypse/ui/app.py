import pygame

from capycalypse import config

class App:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((config.WIDTH, config.HEIGHT))   # Taille de la fenêtre
        pygame.display.set_caption("Capycalypse")                              # Nom du jeu sur la fenêtre
        self.clock = pygame.time.Clock()                                       # Horloge qui limite le jeu à FPS images par seconde
        self.running = True
        self.scene = None                                                      # La scène affichée (menu, partie...)

    def change_scene(self, scene):
        self.scene = scene                                                     # Remplace l'écran affiché

    def run(self):
        while self.running:
            dt = self.clock.tick(config.FPS) / 1000                            # Temps depuis l'image précédente : millisecondes → secondes
            for event in pygame.event.get():
                if event.type == pygame.QUIT:                                  # Clic sur la croix : arrête le jeu
                    self.running = False
                else:
                    self.scene.handle_event(event)                             # 1. écouter
            self.scene.update(dt)                                              # 2. calculer
            self.scene.draw(self.screen)                                       # 3. dessiner
            pygame.display.flip()                                              # Affiche ce qu'on a dessiné
        pygame.quit()