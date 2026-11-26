# tests/test_app.py : vérifie le système de scènes (T07)
import os
os.environ["SDL_VIDEODRIVER"] = "dummy"   # pygame sans vraie fenêtre (à mettre AVANT d'importer pygame)

import pygame

from capycalypse.ui.app import App
from capycalypse.ui.scenes.scene import Scene
from capycalypse.ui.scenes.demo_scene import DemoScene


def test_au_depart_il_n_y_a_pas_de_scene():
    app = App()
    assert app.scene is None


def test_change_scene_remplace_la_scene():
    app = App()
    premiere = Scene(app)
    deuxieme = Scene(app)
    app.change_scene(premiere)
    app.change_scene(deuxieme)
    assert app.scene is deuxieme


def test_la_scene_connait_l_app():
    app = App()
    scene = Scene(app)
    assert scene.app is app


def test_espace_fait_changer_de_scene():
    app = App()
    depart = DemoScene(app)
    app.change_scene(depart)

    espace = pygame.event.Event(pygame.KEYDOWN, key=pygame.K_SPACE)   # on simule l'appui sur ESPACE
    app.scene.handle_event(espace)

    assert app.scene is not depart                  # la scène a changé
    assert app.scene.color == (120, 60, 200)        # la nouvelle scène est violette