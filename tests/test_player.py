from capycalypse import config
from capycalypse.logic.player import Player


def test_player_initializes_with_default_state():
	player = Player()

	assert (player.x, player.y) == (200, config.HEIGHT / 2)
	assert (player.width, player.height) == (64, 48)
	assert player.vy == 0
	assert player.thrusting is False


def test_player_update_applies_gravity_and_limits_fall_speed():
	player = Player()
	player.update(dt=1)

	assert player.vy == config.MAX_FALL_SPEED
	assert player.y == config.HEIGHT / 2 + config.MAX_FALL_SPEED


def test_player_thrust_accelerates_upward_and_limits_speed():
	player = Player()
	player.thrusting = True
	player.update(dt=1)

	assert player.vy == -config.MAX_FALL_SPEED
	assert player.y == config.HEIGHT / 2 - config.MAX_FALL_SPEED
