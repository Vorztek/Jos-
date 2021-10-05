#cette fonction sert a generer des nombres une liste de aleatoire de -100
#à un chiffre que vous choisissez

import random

liste2 = []
liste3 =[]
liste4 = []
for i in range(0,20):
    n = random.randint(-100,100)
    liste2.append(n)

for i in liste2:
    if i < 0:
        liste3.append(i)

for i in liste3:
    i += i * 0.5
    #print(i)


for i in liste3:
    i+= i ** 2 ** 2 ** 2
    #print(i)

def gen_number(o,p):
    for i in range(0,o):
        n = random.randint(0,p)
        liste4.append(n)
    return liste4

#o = nombre de valeur voulue
#p = valeur max
print(gen_number(1,3))