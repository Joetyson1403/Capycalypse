import pygame

from capycalypse.logic.world import World
from capycalypse.ui.background import ScrollingBackground, make_placeholder_background
from capycalypse.ui.scenes.scene import Scene
from capycalypse.logic.obstacles import Bird, Missile
from capycalypse.logic.spawner import Spawner


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
        
        # Vérifier si game over
        if self.world.game_over == True:
            self.stop()

    def draw(self, screen):
        self.background.draw(screen)                                       # D'abord le fond (derrière)
        p = self.world.player
        # Pour l'instant, le capybara est un simple rectangle marron.
        pygame.draw.rect(screen, (160, 103, 58), (p.x, p.y, p.width, p.height))   # Puis le capybara (devant)

        obstacles = self.world.obstacles
        for obstacle in obstacles:
            if(type(obstacle) == Bird):
                pygame.draw.rect(screen, (0, 0, 255), (obstacle.x, obstacle.y, obstacle.width, obstacle.height))
            if(type(obstacle) == Missile):
                pygame.draw.rect(screen, (255, 0, 0), (obstacle.x, obstacle.y, obstacle.width, obstacle.height))
    
    def stop(self):
        # TODO : A revoir car pas arret sur image mais création du début de la scène de test
        self.background = ScrollingBackground(make_placeholder_background(), speed_factor=0)