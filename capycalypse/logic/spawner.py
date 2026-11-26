import random

from capycalypse import config
from capycalypse.logic.obstacles import Bird, Missile


class Spawner:
    def __init__(self, rng=None):
        # Générateur de hasard (dans les tests : random.Random(42) pour avoir toujours le même hasard)
        if rng is None:
            rng = random.Random()
        self.rng = rng

        # Distance (en pixels) à parcourir avant le prochain obstacle
        # Au début on attend l'écart max pour laisser le temps au joueur
        self.distance_until_next = config.MAX_GAP

    def update(self, dt, world):
        # Le compteur diminue de la distance parcourue par le décor
        self.distance_until_next = self.distance_until_next - world.speed * dt

        # Compteur arrivé à 0 : nouvel obstacle + nouvel écart au hasard
        if self.distance_until_next <= 0:
            world.obstacles.append(self.create_obstacle())
            self.distance_until_next = self.rng.uniform(config.MIN_GAP, config.MAX_GAP)

    def create_obstacle(self):
        # Choix du type d'obstacle au hasard
        obstacle_class = self.rng.choice([Bird, Missile])

        # Haut du sol (les obstacles ne doivent pas rentrer dedans)
        ground_top = config.HEIGHT - config.GROUND_HEIGHT

        # Hauteur au hasard, en restant dans l'écran
        if obstacle_class == Bird:
            # L'oiseau monte et descend de BIRD_AMPLITUDE : on garde cette marge en haut et en bas
            lowest = ground_top - config.BIRD_HEIGHT - config.BIRD_AMPLITUDE
            y = self.rng.uniform(config.BIRD_AMPLITUDE, lowest)
        else:
            lowest = ground_top - config.MISSILE_HEIGHT
            y = self.rng.uniform(0, lowest)

        # Création juste à droite de l'écran (pas encore visible)
        return obstacle_class(config.WIDTH, y)
