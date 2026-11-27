import pygame

from capycalypse.logic.world import World
from capycalypse.ui.background import ScrollingBackground, make_placeholder_background
from capycalypse.ui.scenes.scene import Scene
from capycalypse.logic.obstacles import Bird, Missile


class PlayScene(Scene):
    """Scène de jeu : relie le monde (logique) au clavier et à l'écran."""

    def __init__(self, app):
        super().__init__(app)
        self.world = World()                                                     # Tout l'état de la partie (T13)
        self.background = ScrollingBackground(make_placeholder_background())     # Fond qui défile (T14)

    def update(self, dt):
        # 1. Lire les touches : get_pressed() est vrai tant que la touche est enfoncée.
        keys = pygame.key.get_pressed()
        mouse_down = pygame.mouse.get_pressed()[0]                         # [0] = clic gauche
        self.world.player.thrusting = keys[pygame.K_SPACE] or mouse_down   # ESPACE ou clic = poussée

        # 2. Faire avancer toute la partie (joueur, obstacles, distance), puis le fond.
        self.world.update(dt)
        self.background.update(dt, self.world.speed)                       # Le fond suit la vitesse du jeu

    def draw(self, screen):
        self.background.draw(screen)                                       # D'abord le fond (derrière)
        p = self.world.player
        # Pour l'instant, le capybara est un simple rectangle marron.
        pygame.draw.rect(screen, (160, 103, 58), (p.x, p.y, p.width, p.height))   # Puis le capybara (devant)

        b = Bird(10,200)

        pygame.draw.rect(screen, (160, 103, 58), (b.x, b.y, b.width, b.height))    # Dessine un oiseau (en rectangle)

        m = Missile(10,100)

        pygame.draw.rect(screen, (255,0,0), (m.x, m.y, m.width, m.height))         # Dessine un missile (en rectangle)