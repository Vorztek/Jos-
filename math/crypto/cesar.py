alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
ponc = " !.,:?'"
phrase = ""

ponct_add = ""
phrase_trad = ""

for i in phrase:
    if i not in ponc:
        trade_letter = alphabet.find(i)
        phrase_trad += alphabet[(trade_letter + 10) % 26]
    else:
        phrase_trad +=  i

print(phrase_trad)
        
    
    