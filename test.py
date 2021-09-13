import time
start_time = time.time()
liste = []
liste_paire = []
chiffre2 = int(input("Chiffre 2 : "))

for i in range(1, chiffre2 + 1):
    liste.append(i)
        
for i in liste:
        if i % 2 == 0:
            liste_paire.append(i)
    
elapsed_time = time.time() - start_time
print(elapsed_time, len(liste_paire))
