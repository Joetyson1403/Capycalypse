from capycalypse import config
from capycalypse.logic.player import Player
from capycalypse.logic.spawner import Spawner


class World:
    # Tout ce qui existe pendant une partie

    def __init__(self):
        self.player = Player()
        self.spawner = Spawner()
        self.obstacles = []                   # remplis plus tard par le Spawner (T17)
        self.coins = []                       # remplis plus tard (T22)
        self.speed = config.START_SPEED       # vitesse du défilement, en pixels/seconde
        self.distance_px = 0                  # distance parcourue depuis le début
        self.time = 0                         # temps écoulé depuis le début, en secondes
        self.game_over = False                # True quand le joueur a perdu (T18)
        self.events = []                      # messages pour l'interface : "coin", "hit"...

    def update(self, dt):
        if self.game_over:                    # partie perdue : plus rien ne bouge
            return

        self.time += dt
        self.distance_px += self.speed * dt   # distance = vitesse × temps
        
        # Ajout d'un obstacle (Spawner gère lui même les timing + la liste)
        self.spawner.update(dt, self)

        self.player.update(dt)
        for obstacle in self.obstacles:
            obstacle.update(dt, self.speed)

        # On garde seulement les obstacles encore actifs (pas sortis de l'écran)
        self.obstacles = [o for o in self.obstacles if o.active]   # Fabreique une nouvelle liste avec chaque obstable o de la liste, seulement si o.active est vrai
        
        # Verif collisions
        for obstacle in self.obstacles:
            if obstacle.is_dangerous() and self.player.collides(obstacle):
                self.game_over = True
                self.events.append("Hits")