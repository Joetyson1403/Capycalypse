# Imports
from capycalypse.ui.app import App
from capycalypse.ui.scenes.demo_scene import DemoScene

if __name__ == "__main__":                   # Lorsque "run python files" est appelé depuis le fichier main
    app = App()                              # Crée l'objet App (fenêtre) puis lance la boucle du jeu
    app.change_scene(DemoScene(app))
    app.run()