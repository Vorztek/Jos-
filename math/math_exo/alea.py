import random
import numpy


# Objectif :

#Créer un fichier avec 15 000 mots aléatoires

# -------------
# Grande étapes :


# -------------
# Moyens utilisés (modules, variable, utilisation de liste, dictionnaire) :


# -------------
# Pseudo code - facultatif mais recommandé pour un exercice moyen/important :

liste = []

with open(r"C:\Users\vorzt\Documents\python\math\math_exo\liste_francais.txt") as file:
    contenue = file.readlines()
    liste.append(contenue)
    
    
with open('exo.txt','w') as diary:
    for i in range(0,len(liste[0])):
        n = random.randint(0,len(liste[0]))
        b = liste[0][n]
        diary.write(b)





