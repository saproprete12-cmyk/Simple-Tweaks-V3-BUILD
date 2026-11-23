SIMPLE TWEAKS V3 — VERSION WINDOWS SANS PYTHON À INSTALLER

Objectif
Le programme final est un .exe autonome : l'utilisateur final n'a PAS besoin d'installer Python.
Le workflow de compilation utilise Python uniquement sur une machine Windows de compilation (GitHub Actions).

Créer le programme d'installation
1. Crée un dépôt GitHub et ajoute tous les fichiers de ce dossier à la racine.
2. Dans GitHub, ouvre l'onglet Actions.
3. Lance le workflow « Build Windows installer » avec Run workflow.
4. À la fin, télécharge l'artefact « SimpleTweaks-Windows-Installer ».
5. Il contient SimpleTweaks_Setup_V3.exe.

Sur le PC où tu installes Simple Tweaks :
- Double-clique SimpleTweaks_Setup_V3.exe.
- Aucun Python, pip ou PyInstaller n'est nécessaire.
- L'application est installée dans Program Files et un raccourci Démarrer/Bureau est créé.

Important : je ne peux pas compiler un binaire Windows depuis cet environnement Linux. Ce pack automatise la compilation sur un runner Windows et produit l'installateur final. Le binaire final n'est donc pas encore inclus dans cette archive.
