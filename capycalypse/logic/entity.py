class Entity:
    """Tout objet du jeu qui a une position et une taille."""

    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.active = True

    def update(self, dt, scroll_speed):
        raise NotImplementedError(
            "Chaque entité doit écrire sa propre update()")

    def hitbox(self):
        """Retourne le rectangle de collision (x, y, largeur, hauteur)."""
        return (self.x, self.y, self.width, self.height)

    def collides(self, other: "Entity") -> bool:
        x1, y1, width1, height1 = self.hitbox()
        x2, y2, width2, height2 = other.hitbox()
        if x1 < x2 + width2 and x2 < x1 + width1 and y1 < y2 + height2 and y2 < y1 + height1:
            return True
        return False
