# Imports
from capycalypse.ui.app import App
from capycalypse.ui.scenes.play import PlayScene

if __name__ == "__main__":                   # Lorsque "run python files" est appelé depuis le fichier main
    app = App()                              # Crée l'objet App (fenêtre) puis lance la boucle du jeu
    app.change_scene(PlayScene(app))         # Le jeu démarre directement sur la partie (le menu viendra en T19)
    app.run()
