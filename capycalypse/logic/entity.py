class Entity:
	def __init__(self, x, y, width, height):
		self.x = x
		self.y = y
		self.width = width
		self.height = height
		self.active = True

	def update(self):
		raise NotImplementedError
