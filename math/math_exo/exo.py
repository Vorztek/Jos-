from gen_nombre2 import gen_number
import random

a = random.randint(0,10)
notecomplete = []
listemama = []
listeok = []
listentm = []

def note(a):
    if a <= 5:
        return "Ntm"
    elif a <= 9:
        return "Ok"
    else:
        a == 10
        return "Mama"

def liste1():
    for i in range(0,50):
        a = random.randint(0, 10)
        notecomplete.append(note(a))


    for i in notecomplete:
        if i == "Ntm":
            listentm.append(i)
        elif i == "Ok":
            listeok.append(i)
        else:
            listemama.append(i)

        a,b,c = len(listentm) ,len(listeok) ,len(listemama)
        m = (a / (a + b + c)) * 100
        n = (b / (a + b + c)) * 100
        o = (c / (a + b + c)) * 100
    return m ,n ,o

print(liste1())

