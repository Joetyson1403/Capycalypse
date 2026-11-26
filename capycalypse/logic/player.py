from capycalypse import config
from capycalypse.logic.entity import Entity


class Player(Entity):
	def __init__(self):
		super().__init__(x=200, y=config.HEIGHT / 2, width=64, height=48)
		self.vy = 0  # vitesse verticale en pixels/seconde
		self.thrusting = False  # True quand le joueur appuie

	def update(self, dt, scroll_speed=0):
		# 1. L'accélération : la gravité tire vers le bas, la poussée vers le haut.
		acceleration = config.GRAVITY
		if self.thrusting:
			acceleration -= config.THRUST

		# 2. La vitesse change selon l'accélération.
		self.vy += acceleration * dt
		self.vy = max(
			-config.MAX_FALL_SPEED,
			min(self.vy, config.MAX_FALL_SPEED),
		)

		# 3. La position change selon la vitesse.
		self.y += self.vy * dt
		self.keep_on_screen()

	def keep_on_screen(self):
		# 1. Le plafond : on ne peut pas sortir par le haut.
		if self.y < 0:
			self.y = 0
			self.vy = 0

		# 2. Le sol : le bas autorisé = hauteur écran - sol - taille du joueur.
		lowest = config.HEIGHT - config.GROUND_HEIGHT - self.height
		if self.y > lowest:
			self.y = lowest
			self.vy = 0
