# Tests du Spawner (T17).
# Chaque test suit 3 étapes : préparer, agir, vérifier.
# On passe random.Random(42) au Spawner : le hasard est toujours le même, donc les tests aussi.

import random

from capycalypse import config
from capycalypse.logic.obstacles import Bird, Missile
from capycalypse.logic.spawner import Spawner

DT = 1 / 60  # une image à 60 FPS


class FakeWorld:
    # Faux World avec seulement ce dont le Spawner a besoin.
    # À remplacer par le vrai World quand T13 sera dans develop.
    def __init__(self):
        self.speed = config.START_SPEED
        self.obstacles = []


def test_pas_d_obstacle_tout_de_suite():
    # Préparer
    spawner = Spawner(random.Random(42))
    world = FakeWorld()

    # Agir : une seule image
    spawner.update(DT, world)

    # Vérifier : le joueur a le temps avant le premier obstacle
    assert world.obstacles == []


def test_un_obstacle_apparait_apres_l_ecart():
    # Préparer
    spawner = Spawner(random.Random(42))
    world = FakeWorld()

    # Agir : 2 secondes à 400 px/s = 800 px, plus que MAX_GAP (700)
    for _ in range(120):
        spawner.update(DT, world)

    # Vérifier
    assert len(world.obstacles) >= 1


def test_l_ecart_reste_dans_les_limites():
    # Préparer
    spawner = Spawner(random.Random(42))
    world = FakeWorld()

    # Agir + vérifier à chaque image
    for _ in range(1000):
        spawner.update(DT, world)
        assert spawner.distance_until_next <= config.MAX_GAP


def test_l_ecart_entre_deux_obstacles_est_assez_grand():
    # Préparer
    spawner = Spawner(random.Random(42))
    world = FakeWorld()
    distance = 0
    spawn_distances = []  # distance parcourue au moment de chaque apparition

    # Agir : 1 minute de jeu
    for _ in range(60 * 60):
        count_before = len(world.obstacles)
        spawner.update(DT, world)
        distance += world.speed * DT
        if len(world.obstacles) > count_before:
            spawn_distances.append(distance)

    # Vérifier : entre deux obstacles, au moins MIN_GAP et au plus MAX_GAP (+ une image)
    for i in range(1, len(spawn_distances)):
        gap = spawn_distances[i] - spawn_distances[i - 1]
        assert gap >= config.MIN_GAP
        assert gap <= config.MAX_GAP + world.speed * DT


def test_les_obstacles_arrivent_sans_fin():
    # Préparer
    spawner = Spawner(random.Random(42))
    world = FakeWorld()

    # Agir : 5 minutes de jeu
    for _ in range(60 * 60 * 5):
        spawner.update(DT, world)

    # Vérifier : 5 min à 400 px/s = 120'000 px, donc au moins 120'000 / MAX_GAP obstacles
    assert len(world.obstacles) >= 120000 // config.MAX_GAP


def test_un_obstacle_apparait_a_droite():
    # Agir
    obstacle = Spawner(random.Random(1)).create_obstacle()

    # Vérifier : il commence hors de l'écran, à droite
    assert obstacle.x >= config.WIDTH


def test_les_obstacles_restent_dans_l_ecran():
    # Préparer
    spawner = Spawner(random.Random(42))
    ground_top = config.HEIGHT - config.GROUND_HEIGHT

    # Agir + vérifier sur 500 obstacles
    for _ in range(500):
        obstacle = spawner.create_obstacle()
        if isinstance(obstacle, Bird):
            # Avec l'ondulation, l'oiseau ne doit sortir ni en haut ni dans le sol
            assert obstacle.y - config.BIRD_AMPLITUDE >= 0
            assert obstacle.y + obstacle.height + config.BIRD_AMPLITUDE <= ground_top
        else:
            assert obstacle.y >= 0
            assert obstacle.y + obstacle.height <= ground_top


def test_il_y_a_des_oiseaux_et_des_missiles():
    # Préparer
    spawner = Spawner(random.Random(42))

    # Agir
    obstacles = [spawner.create_obstacle() for _ in range(50)]

    # Vérifier : les deux types apparaissent
    assert any(isinstance(o, Bird) for o in obstacles)
    assert any(isinstance(o, Missile) for o in obstacles)


def test_meme_graine_meme_hasard():
    # Préparer : deux spawners avec la même graine
    spawner_a = Spawner(random.Random(42))
    spawner_b = Spawner(random.Random(42))

    # Agir
    a = [spawner_a.create_obstacle() for _ in range(10)]
    b = [spawner_b.create_obstacle() for _ in range(10)]

    # Vérifier : exactement les mêmes obstacles
    assert [(type(o), o.y) for o in a] == [(type(o), o.y) for o in b]
