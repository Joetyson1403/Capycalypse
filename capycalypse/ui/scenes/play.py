import pygame

from capycalypse.logic.player import Player
from capycalypse.ui.scenes.scene import Scene


class PlayScene(Scene):
    """Scène de jeu : relie le joueur (logique) au clavier et à l'écran."""

    def __init__(self, app):
        super().__init__(app)
        self.player = Player()                                      # Plus tard (T13) : self.world.player

    def update(self, dt):
        # 1. Lire les touches : get_pressed() est vrai tant que la touche est enfoncée.
        keys = pygame.key.get_pressed()
        mouse_down = pygame.mouse.get_pressed()[0]                  # [0] = clic gauche
        self.player.thrusting = keys[pygame.K_SPACE] or mouse_down  # ESPACE ou clic = poussée

        # 2. Faire avancer la physique du joueur (gravité, poussée, limites).
        self.player.update(dt)

    def draw(self, screen):
        screen.fill((255, 122, 26))                                 # Fond orange
        p = self.player
        # Pour l'instant, le capybara est un simple rectangle marron.
        pygame.draw.rect(screen, (160, 103, 58), (p.x, p.y, p.width, p.height))
