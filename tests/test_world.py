from capycalypse import config
from capycalypse.logic.entity import Entity
from capycalypse.logic.world import World


def test_la_distance_augmente_avec_la_vitesse():
    world = World()
    world.update(1.0)                                 # 1 seconde à 400 px/s
    assert world.distance_px == config.START_SPEED    # = 400


def test_le_temps_avance():
    world = World()
    world.update(0.5)
    world.update(0.5)
    assert world.time == 1.0


def test_rien_ne_bouge_apres_game_over():
    world = World()
    world.game_over = True
    world.update(1.0)
    assert world.distance_px == 0

# Faux obstacle pour tester
class FakeObstacle(Entity):

    def update(self, dt, scroll_speed):
        self.active = False


def test_les_obstacles_inactifs_sont_supprimes():
    world = World()
    world.obstacles.append(FakeObstacle(0, 0, 10, 10))
    world.update(0.016)
    assert world.obstacles == []