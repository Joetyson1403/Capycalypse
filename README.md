# Capycalypse

Jeu d'arcade en Python / Pygame.

## Installation

1. Installer Python 3.13 depuis [python.org](https://www.python.org/) (cocher « Add python.exe to PATH »).
2. Cloner le dépôt et ouvrir un terminal dans le dossier du projet.
3. Créer et activer l'environnement virtuel, puis installer les dépendances :

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

> Sous PowerShell, si `activate` est bloqué, exécuter une fois :
> `Set-ExecutionPolicy -Scope CurrentUser RemoteSigned`

Vérifier l'installation de pygame :

```bash
python -c "import pygame; print(pygame.version.ver)"
```

## Lancer le jeu

```bash
python main.py
```

## Lancer les tests

```bash
python -m pytest
```
