import matplotlib.pyplot as plt

liste1 = []
liste2 = []
meo = [0]
def nbr(valeur):
    if valeur < 2:
        return False

    for i in range(2,valeur):
        if valeur % i == 0:
            return False
    meo.append(valeur)
    return True

def liste_nbr_premier(maxrange):
    compteur = 1
    for i in range(2,maxrange):
          if i not in meo:
            if nbr(i):               
                compteur += 1
    a = (compteur / maxrange) * 100
    return a

def pourcentage(pourc):
    for i in range(2,pourc):
       liste2.append(liste_nbr_premier(i))
       
    return liste2


plt.plot(pourcentage(1000))
plt.show()

#print(pourcentage(300))