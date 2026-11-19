# Règles Git et contribution — Capycalypse

Le code du sprint vit sur `develop`. La branche `main` ne reçoit qu'une fusion depuis `develop` à la fin de chaque sprint.

- **Une tâche = une branche**, créée depuis `develop`, puis une Pull Request (PR) vers `develop`, relue et fusionnée par un **autre** membre de l'équipe.
- **Nommage des branches** : `type/Tnn-description-courte` en minuscules, sans accents ni espaces (`feature`, `test`, `docs`, `chore`, ou `fix/<numéro>-<description>`).
- **Règle d'or** : aucun `import pygame` dans `capycalypse/logic/`.

## Cycle de travail pour une tâche

```bash
# 1. Partir d'un develop à jour
git switch develop
git pull

# 2. Une branche par tâche (nom dans l'issue)
git switch -c feature/T09-gravite-poussee

# 3. Travailler, puis enregistrer
git add .
git commit -m "T09 : gravité et poussée du joueur"

# 4. Envoyer, puis ouvrir la PR vers develop sur GitHub
git push -u origin feature/T09-gravite-poussee
```

## Avant d'ouvrir une Pull Request vers `develop`

1. Vérifier que toutes les cases « C'est terminé quand » de la tâche sont cochées.
2. Mettre sa branche à jour avec `develop` (`git merge develop`) pour régler les éventuels conflits en local.
3. Lancer `python -m pytest` (tous les tests doivent passer) et `python main.py`.
4. Cibler **`develop`** (jamais `main` en cours de sprint) et indiquer `Closes #<numéro>` de l'issue dans la description.
