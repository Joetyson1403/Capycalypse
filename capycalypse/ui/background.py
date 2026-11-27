# capycalypse/ui/background.py
import pygame
from capycalypse import config

class ScrollingBackground:
    def __init__(self, image, speed_factor=0.5):
        # Appelé une fois, quand on crée le fond    
        self.image = image                                  # L'image à faire défiler
        self.offset = 0                                     # Décalage vers la gauche, en pixels, commence a 0 (à gauche de l'écran)
        self.speed_factor = speed_factor                    # Le fond va moins vite que le jeu : 0.5 = 2× moins vite que les obstacles (profondeur)

    # Appelé a chaque image (60x par seconde) pour calculer le décalage.
    def update(self, dt, scroll_speed):
        self.offset += scroll_speed * self.speed_factor * dt # Combien le fond glisse
        self.offset %= self.image.get_width()               # Revient à 0 : boucle infinie

    # Appelé à chaque image, après update
    def draw(self, screen):
        # Avec offset = 300 → x = -300 : les 300 premiers pixels de l'image sont cachés
        x = -self.offset
        while x < screen.get_width():                       # Recolle l'image jusqu'à couvrir l'écran
            screen.blit(self.image, (x, 0))                 # "blit" coller l'image sur l'écran
            x += self.image.get_width()                     # L'image suivante se colle juste à droite

def make_placeholder_background():
    """Fond de test : ciel orange + immeubles gris (en attendant les vrais graphismes de T30)."""
    image = pygame.Surface((config.WIDTH, config.HEIGHT))
    image.fill((255, 122, 26))                                         # Ciel orange
    x = 0
    for h in [300, 420, 250, 380, 460, 280, 350, 400]:
        pygame.draw.rect(image, (70, 62, 64), (x, config.HEIGHT - h, 150, h))   # Un immeuble
        x += 160
    return image
