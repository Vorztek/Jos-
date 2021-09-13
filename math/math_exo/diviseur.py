# liste des diviseurs d'un nombre entier

liste3 = []


def diviseur(entier):
    for i in range(1, entier):
        if entier % i == 0:
            liste3.append(i)
    return liste3

print(diviseur(1700))

