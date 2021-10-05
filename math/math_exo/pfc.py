#: Créer un programme qui jouer à Pierre feuille ciseaux, et donne le gagnant de chaque partie
#Créer un CSV avec le résultat de chaque partie et l'évolution du nombre de fois où chaque élément a gagné. 
# La phrase devra être pour chaque résultat dans le CSV (par exemple pour 1000 parties) :
#1000ème partie, Pierre contre feuille, la feuille gagne, les scores sont d'actuellement: 35% feuille, 48% pierre et 27% pour ciseaux
#Créer ensuite un programme qui joue au premier programme et qui enregistre le nombre de parties nécessaires pour atteindre l'équilibre de 33% pour chaque élément
#Créer un graphe (matplotlib) avec en abscisse le nombre de parties (1 000 minimum) et en ordonnée le nombre de parties nécessaires pour atteindre l'équilibre
from random import *
import csv

liste_resultat = []
player1 = randint(1,3)
player2 = randint(1,3)

def pfc():
    for i in range(0,1000):
        player1 = randint(1,3)
        player2 = randint(1,3)
        
        if player1 == 1:
            player1 = "pierre"
        elif player1 == 2:
            player1 = "feuille"
        elif player1 == 3:
            player1 = "ciseaux" 
        if player2 == 1:
            player2 = "pierre"
        elif player2 == 2:
            player2 = "feuille"
        elif player2 == 3:
            player2 = "ciseaux"

if player1 =="pierre"  and player2 =="feuille" :
    winner= player2
elif player1 =="pierre"  and player2 =="ciseaux" :
    winner= player1
elif player1 =="feuille"  and player2 =="pierre" :
    winner= player1
elif  player1 =="feuille" and player2 =="ciseaux" :
    winner= player2
elif player1 =="ciseaux" and player2 =="pierre" :
    winner= player2
elif player1 =="ciseaux" and player2 =="feuille" :

liste_resultat.append(winner)
