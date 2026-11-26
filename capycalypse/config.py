WIDTH = 1280
HEIGHT = 720
FPS = 60
GROUND_HEIGHT = 60  # hauteur du sol en bas de l'écran

# Physique du joueur (pixels par seconde, ou par seconde²)
GRAVITY = 1800  # tire vers le bas
THRUST = 3200  # pousse vers le haut quand on appuie
MAX_FALL_SPEED = 900

# Défilement et difficulté
START_SPEED = 400  # vitesse du décor au départ
MAX_SPEED = 1100
ACCELERATION = 8  # pixels/s gagnés chaque seconde
PIXELS_PER_METER = 50

# Génération des obstacles (en pixels de distance)
MIN_GAP = 350
MAX_GAP = 700

# Taille obstacle oiseau
BIRD_WIDTH = 48
BIRD_HEIGHT = 32

# Paramètres oscillation oiseau
BIRD_PULSATION = 4
BIRD_AMPLITUDE = 60

# Taille obstacle missile
MISSILE_WIDTH = 80
MISSILE_HEIGHT = 24

# Vitesse en + du missile (Pour aller + vite que le décor)
MISSILE_EXCESS_SPEED = 500
