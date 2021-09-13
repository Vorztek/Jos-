liste = []



def calcul():
    p = 1
    for i in range(0, 1000 * p, p):
        liste.append(i)
        p = p + 1
    if p > 50:
        return liste

print(calcul())