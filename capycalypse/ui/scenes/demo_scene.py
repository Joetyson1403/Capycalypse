import pygame

from capycalypse.ui.scenes.scene import Scene


class DemoScene(Scene):
    """Scène de démo : fond orange, ESPACE passe au violet."""

    def __init__(self, app, color=(255, 122, 26)):
        super().__init__(app)
        self.color = color

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            self.app.change_scene(DemoScene(self.app, (120, 60, 200)))

    def draw(self, screen):
        screen.fill(self.color)