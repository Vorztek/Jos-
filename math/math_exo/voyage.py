# TP9 Utilisons des fonctions pour calculer les coûts de votre voyage:¶
# - Définissez une fonction appelée hotel_cost avec un argument nuits comme entrée. 
#  L'hôtel coûte 140€ par nuit. Ainsi, la fonction hotel_cost devrait renvoyer 140 * nuits.
# -Définissez une fonction appelée plane_ride_cost qui prend en entrée une chaîne city. 
#  La fonction doit renvoyer un prix différent selon l'emplacement, similaire à l'exemple de code ci-dessous.
#  Vous trouverez ci-dessous les destinations valides et leurs tarifs aller-retour correspondants.
# "Paris": 183, "Lyon": 220, "Marseille": 222 ,"Surfers Paradise": 475
# Sous votre code existant, définissez une fonction appelée rental_car_cost avec un argument appelé jours. 
# Calculez le coût de la location de la voiture: Chaque jour, vous louez la voiture coûte 40€. (Coût = 40 * jours) si vous louez la voiture pour 7 jours ou plus, 
# vous obtenez 50€ de réduction sur votre total (coût- = 50). Alternativement (elif), 
# si vous louez la voiture pour 3 jours ou plus, vous obtenez 20€ de réduction sur votre total. 
# Vous ne pouvez pas bénéficier des deux réductions en même temps. Renvoyez ce coût puis,
# définissez une fonction appelée trip_cost qui prend deux arguments, ville et jours. 
# Demandez à votre fonction de renvoyer la somme des fonctions rental_car_cost (jours), hotel_cost (jours) et plane_ride_cost (ville).
# Modifiez la fonction trip_cost avec. 
# Ajoutez un troisième argument, spending_money. Modifiez ce que fait la fonction trip_cost. Ajoutez la variable "spending_money" à la somme qu'elle renvoie.


def hotel_cost(jours):
    return 140 * jours

def plane_ride(ville):
    liste_ville = {"Paris": 183, "Lyon": 220, "Marseille": 222 ,"SurfersParadise": 475}
    a = liste_ville[ville]
    return a

def rental_car_cost(jours):
    if jours >= 7:
        cout = 40 * jours - 50
    elif jours >= 3:
        cout = 40 * jours - 20
    else:
        cout = 40 * jours
    return cout


def trip_cost(ville, jours , money):
    return hotel_cost(jours) + rental_car_cost(jours) + plane_ride(ville) + money


print(trip_cost("Lyon",7 , 300))
