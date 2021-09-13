def decimal_to_binary(n):
    """Convertit un nombre décimal n en un nombre binaire
    Renvoie le nombre binaire dans une chaîne de caractères"""
    
    binary = ""
    while n > 0 :
        binary = str(n%2) + binary
        n = n // 2

    return binary

print(decimal_to_binary(10000000000000000))