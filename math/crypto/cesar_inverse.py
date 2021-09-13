from ascii import asc_ii



alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
ponc = " !.,:?'"
phrase = "Nolot merguez"
binaire = []
ponct_add = ""
phrase_trad = ""

for i in phrase:
    if i not in ponc:
        trade_letter = alphabet.find(i)
        phrase_trad += alphabet[(trade_letter - 10) % 26]
    else:
        phrase_trad +=  i

for i in asc_ii(phrase_trad):
    bin_create = bin(i)
    binaire.append(bin_create)

#print(binaire.count("0b1110101"))

#print(phrase_trad, asc_ii(phrase_trad),binaire)

print(binaire)