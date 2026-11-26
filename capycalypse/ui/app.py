# Imports : ordre conseillé par python 1.standard, 2.externes, 3.notre code
# 1. Bibliothèque standard
import ctypes                  # Fonctions de Windows (icône dans la barre des tâches)
import sys                     # Savoir sur quel système on est (Windows, Mac, Linux)


from pathlib import Path       # Construire des chemins de fichiers

# 2 Bibliothèque externe
import pygame                  # Fenêtre, dessin, clavier

# 3 Notre propre code
from capycalypse import config # Nos constantes (taille, FPS...)

# ---------- Constantes du fichier -----------

# Chemin de l'icône Capybara : app.py → ui → capycalypse → racine, puis assets/images
ICON_PATH = Path(__file__).resolve().parent.parent.parent / "assets" / "images" / "icon.png"

class App:
    def __init__(self):
        if sys.platform == "win32":                                            # Windows : notre icône dans la barre des tâches
            ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID("capycalypse.jeu")
        pygame.init()
        pygame.display.set_icon(pygame.image.load(ICON_PATH))                  # Icône Capybara dans la fenêtre du jeu
        self.screen = pygame.display.set_mode((config.WIDTH, config.HEIGHT))   # Taille de l'écran
        pygame.display.set_caption("Capycalypse")                              # Nom du jeu sur la fenêtre
        self.clock = pygame.time.Clock()                                       # Horloge qui limite le jeu à FPS images/s
        self.running = True

    def run(self):
        while self.running:
            dt = self.clock.tick(config.FPS) / 1000                            # Temps depuis l'image précédente, en secondes
            for event in pygame.event.get():
                if event.type == pygame.QUIT:                                  # Arrête le jeu
                    self.running = False
            self.screen.fill((28, 23, 24))
            pygame.display.flip()                                              # Affiche ce qu'on a dessiné
        pygame.quit()