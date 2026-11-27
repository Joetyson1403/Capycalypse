import pygame

from capycalypse import config
from capycalypse.ui.scenes.scene import Scene


class MenuScene(Scene):
    """Menu principal : choisir Jouer, Meilleur score ou Quitter."""

    OPTIONS = ["Jouer", "Meilleur score", "Quitter"]                # Les choix affichés, dans l'ordre

    def __init__(self, app):
        super().__init__(app)                                       # Appelle le __init__ de Scene → self.app = app
        self.selected = 0                                           # Index du choix sélectionné (0 = "Jouer")
        self.font = pygame.font.Font(None, 64)                      # Police par défaut (None), taille 64

    def handle_event(self, event):
        if event.type != pygame.KEYDOWN:                            # On ne réagit qu'aux touches appuyées
            return
        if event.key == pygame.K_DOWN:                              # Flèche bas : choix suivant
            self.selected = (self.selected + 1) % len(self.OPTIONS) # % : après le dernier, revient au premier car OPTIONS vaut 3
        elif event.key == pygame.K_UP:                              # Flèche haut : choix précédent
            self.selected = (self.selected - 1) % len(self.OPTIONS) # % : avant le premier, va au dernier
        elif event.key == pygame.K_RETURN:                          # ENTRÉE : valide le choix
            self.choose()

    def choose(self):
        if self.selected == 0:                                      # "Jouer"
            from capycalypse.ui.scenes.play import PlayScene        # Import ici : évite l'import circulaire
            self.app.change_scene(PlayScene(self.app))              # Lance la partie
        elif self.selected == 2:                                    # "Quitter"
            self.app.running = False                                # Arrête la boucle du jeu → ferme la fenêtre
        # "Meilleur score" (1) : sera ajouté en T27

    def draw(self, screen):
        screen.fill((28, 23, 24))                                   # Fond gris très foncé
        for i, text in enumerate(self.OPTIONS):                     # enumerate donne l'index (i) ET le texte
            color = (255, 210, 63) if i == self.selected else (255, 255, 255)   # Jaune si sélectionné, sinon blanc
            image = self.font.render(text, True, color)             # Transforme le texte en image (True = bords lisses)
            screen.blit(image, image.get_rect(center=(config.WIDTH // 2, 300 + i * 80)))   # Centré, un choix tous les 80 px