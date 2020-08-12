# Automation tools

### Replace chars
``replace_chars.py`` permet de remplacer des charactères par d'autres charactères dans tous les fichiers de la même extension

### BA Helper
``ba_helper`` permet de faire fonctionner, de manière un peu nul, le plugin pour VSCode ``Cucumber (Gherkin) Full Support``. 
Pour que l'autocomplétion fonctionne, il faut que les steps dans les fichiers features soient développés. 
``ba_helper`` permet de lire tous les fichiers features, et créer un fichier Java contenant les steps développés. 
Ainsi, les BA peuvent avoir l'autocomplétion de leur fichier récent, sans attendre l'implémentation côté automatisation. 