# importation de la librairie os
import os

# Demande l'emplacement de ce fichier à l'aide de la librairie os et de sa fonction getcwd()
current_path = os.getcwd()

# Variable d'environnement que l'on retrouve dans tous les fichiers .py
current_file = __file__

# Liste des fichiers à l'emplacement contenu dans la variable current_path
file_names = os.listdir(current_path)

# Boucle for
# Traitement des éléments de la liste *file_names* élément par élément
# Chaque élément sera stocké dans la variable *file_name*
for file_name in file_names:
    # Affichage de la variable *file_name*
    print(file_name)
