#créer un nombre aleatoire entre 0 et 1000
#demander a l'utilisateur un nombre entre 0 et 1000
#Si le nombre indiqué par l'utilisateur est < print plus si il est > print moins

import random




def jeu():   
    valeur_finale = random.randint(0,10)
    valeur_joueur = int(input("Nombre: "))
    while  valeur_joueur != valeur_finale:
        if valeur_joueur > valeur_finale:
            print("moins!")
            
        if valeur_joueur < valeur_finale:
            print("plus")
         
        valeur_joueur = int(input("Nombre: "))

    if valeur_joueur == valeur_finale:
        print("gg")
            
        
        
print(jeu())
