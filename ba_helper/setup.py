"""Fichier d'installation de mon script ba_helper.py."""

from cx_Freeze import setup, Executable

# On appelle la fonction setup
setup(
    name = "ba_helper",
    version = "1.0.1",
    description = "Ce programme aide à l'autocomplétion avec le plugin Cucumber pour VSCode",
    executables = [Executable("app/app.py")],
)

# Pour la suite, exécuter la commande suivante : python.exe setup.py build
