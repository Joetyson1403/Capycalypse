from capycalypse.logic.entity import Entity
from capycalypse import config
import math


class Obstacle(Entity):
    def update(self, dt, scroll_speed):
        # Avancement
        self.x = self.x - dt * scroll_speed

        # Détection dehors écran
        if self.x + self.width < 0:
            self.active = False

    def is_dangerous(self):
        return True  # Pour T28


class Bird(Obstacle):
    def __init__(self, x, y):
        # Tailles oiseaux risquent de changer en fonction des assets
        super().__init__(x, y, config.BIRD_WIDTH, config.BIRD_HEIGHT)
        # Variable interne pour oscillation
        self.time = 0
        self.base_y = y

    def update(self, dt, scroll_speed):
        self.time += dt
        self.y = self.base_y + \
            math.sin(self.time * config.BIRD_PULSATION) * config.BIRD_AMPLITUDE


class Missile(Obstacle):
    def __init__(self, x, y):
        super().__init__(x, y, config.MISSILE_WIDTH, config.MISSILE_HEIGHT)

    def update(self, dt, scroll_speed):
        super().update(dt, scroll_speed+config.MISSILE_EXCESS_SPEED)
