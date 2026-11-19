class Entity:
	"""Tout objet du jeu qui a une position et une taille."""

	def __init__(self, x, y, width, height):
		self.x = x
		self.y = y
		self.width = width
		self.height = height
		self.active = True

	def update(self, dt, scroll_speed):
		raise NotImplementedError("Chaque entité doit écrire sa propre update()")

	def hitbox(self):
		"""Retourne le rectangle de collision (x, y, largeur, hauteur)."""
		return (self.x, self.y, self.width, self.height)
