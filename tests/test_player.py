# Tests de la classe Player (T11).
# Chaque test suit 3 étapes :
#   1. préparer : créer un joueur
#   2. agir     : appeler update() une ou plusieurs fois
#   3. vérifier : assert (si c'est faux, le test devient rouge)
# Rappel : dans pygame, y grandit vers le bas (y = 0 est le haut de l'écran).

from capycalypse import config
from capycalypse.logic.player import Player


def test_player_initializes_with_default_state():
	# Préparer : un joueur tout neuf.
	player = Player()

	# Vérifier : il commence au milieu à gauche, immobile, sans poussée.
	assert (player.x, player.y) == (200, config.HEIGHT / 2)
	assert (player.width, player.height) == (64, 48)
	assert player.vy == 0
	assert player.thrusting is False


def test_le_joueur_tombe_sans_poussee():
	# Préparer : on retient la hauteur de départ.
	player = Player()
	start_y = player.y

	# Agir : 0,1 seconde sans appuyer, seule la gravité agit.
	player.update(0.1)

	# Vérifier : y a grandi, donc le joueur est descendu.
	assert player.y > start_y


def test_le_joueur_monte_avec_poussee():
	# Préparer : le joueur appuie (poussée active).
	player = Player()
	player.thrusting = True
	start_y = player.y

	# Agir : 10 images à 60 FPS (0,016 s chacune).
	for _ in range(10):
		player.update(0.016)

	# Vérifier : y a diminué, donc le joueur est monté.
	assert player.y < start_y


def test_le_joueur_ne_sort_pas_par_le_haut():
	# Préparer : le joueur appuie en continu.
	player = Player()
	player.thrusting = True

	# Agir : 300 images (environ 5 secondes), largement assez pour atteindre le haut.
	for _ in range(300):
		player.update(0.016)

	# Vérifier : il est bloqué tout en haut, pas au-dessus (T10).
	assert player.y == 0


def test_le_joueur_reste_au_dessus_du_sol():
	# Préparer : le joueur n'appuie pas, il va tomber.
	player = Player()

	# Agir : 300 images, largement assez pour toucher le sol.
	for _ in range(300):
		player.update(0.016)

	# Vérifier : il est posé sur le sol, pas en dessous (T10).
	# Bas autorisé = hauteur de l'écran - hauteur du sol - taille du joueur.
	assert player.y == config.HEIGHT - config.GROUND_HEIGHT - player.height
