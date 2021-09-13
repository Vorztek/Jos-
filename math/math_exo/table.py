chiffre1 = int(input("Table de : "))
chiffremax = int(input("Jusqu'a : "))

valeur_incremante = 0

while valeur_incremante != chiffremax:
    valeur_incremante += 1
    print(" {} * {} = {}\n".format(chiffre1,valeur_incremante, valeur_incremante * chiffre1))
