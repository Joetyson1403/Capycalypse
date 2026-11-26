# Création de systèmes de scènes
class Scene:
    """Classe de base : chaque écran du jeu hérite de la classe Scene."""

    # Méthode pour initialiser la scène
    def __init__(self, app):
        self.app = app              # pour pouvoir changer de scène

    # Méthode pour "écouter" si le joueur appuie sur une touche
    def handle_event(self, event):
        pass

    # Méthode pour mettre à jour la logique du jeu (positions, score...) à chaque image
    def update(self, dt):           # dt c'est Delta Time, le temps écoulé depuis la dernière image
        pass                        # la logique, à chaque image

    # Méthode pour dessiner la scène
    def draw(self, screen):
        pass                        # le dessin, à chaque image