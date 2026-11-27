# tests/test_menu.py : vérifie le menu principal (T19)
import os
os.environ["SDL_VIDEODRIVER"] = "dummy"   # pygame sans vraie fenêtre (AVANT d'importer pygame)

import pygame

from capycalypse.ui.app import App
from capycalypse.ui.scenes.menu import MenuScene
from capycalypse.ui.scenes.play import PlayScene


def press(menu, key):
    """Simule l'appui sur une touche dans le menu."""
    menu.handle_event(pygame.event.Event(pygame.KEYDOWN, key=key))


def make_menu():
    app = App()
    menu = MenuScene(app)
    app.change_scene(menu)
    return app, menu


def test_le_menu_commence_sur_jouer():
    app, menu = make_menu()
    assert menu.selected == 0


def test_fleche_bas_descend():
    app, menu = make_menu()
    press(menu, pygame.K_DOWN)
    assert menu.selected == 1


def test_fleche_bas_apres_le_dernier_revient_en_haut():
    app, menu = make_menu()
    for _ in range(3):                      # 0 → 1 → 2 → 0
        press(menu, pygame.K_DOWN)
    assert menu.selected == 0


def test_fleche_haut_depuis_jouer_va_tout_en_bas():
    app, menu = make_menu()
    press(menu, pygame.K_UP)                # 0 → 2 (Quitter)
    assert menu.selected == 2


def test_entree_sur_jouer_lance_la_partie():
    app, menu = make_menu()
    press(menu, pygame.K_RETURN)
    assert isinstance(app.scene, PlayScene)   # la scène affichée est maintenant la partie


def test_entree_sur_quitter_ferme_le_jeu():
    app, menu = make_menu()
    press(menu, pygame.K_UP)                # va sur "Quitter"
    press(menu, pygame.K_RETURN)
    assert app.running is False