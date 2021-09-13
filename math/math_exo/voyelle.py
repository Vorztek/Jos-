#!TZ5BZPnpsa8pn3mTZnLInM)KBMNBgiH0Y1eipiOPTxFCqXwaQXytKTjH8c(SFRKSn2ghcnHMRjpkVibjlRD1Qv7(ZYezQzoWenZezBI8nrvkPvQbVau5YEJh7tcm7(on9QMOfeMp1Z1SRUjI6o2JndhWlpWmWeXitGppy5CcCZlDXZOwtyEHZnryxAsdrZWuXFden01ZL38qM46xiR0Ny55AdQcb7tgKQD8YOagXDsWuZUv4s1paZc2J93yQl1F6(RdHU0HoJcMWQ87Zz8zEuxOYdB3Dq7(MOqMJjAAqWC))17F)n4jELOEVNy0QZ7cQSS27bdnMzDsChwRmCh(Kte94LMOl9y2e2HEoEmqL7Qz2TmFYH)7kIFBWRmiUHTTNakj66qmJSA0XHooRgD(uAajEoIW7uCyWupwV58bSVCU92y)aq(mSnn0hetzOayhgtNiBuifCGC0Q3eJoSYTg)iwQi6DeHlZyqGhszwoeZwGde06)7Xeg25Vos6USA0HEEo2E3aIff4zL4UDq5YLH73p8Y(cNSiT6sS1v2mV5Ph)AIXVMy8Rjg)LlvL3yWQtyUyNph3PgLJvq(Gg8JMmb(iFe6phBj1y51Bfjhtulh6D3Hz2Rgna00akuLVfggpGSIACSLYqyCGU1n4ySvaOGO(npQZqe3nygm0mr6LkxIlopWdgH9TiU2u3jGDIHNXDJWbyrhZ8UbjvjrHa5APUsZVnn18eiOOcW4LgiRmEjsAVBHJj21cMOZ5qkhfDCfdcnUiCcN5Uw(oEyrOHayy7kw5nleSeX9PLd23FJA95UaBu5CIv(k5ALdDI7A9jGr5tm(Y5xO5HUrvjhsRlW7qhNo2r2c5svmSYvNFtG1an3bVKB4jl4Qo6JeSdSScztUmC8y564p2(KZoE4jcNnrZqWLO3AIU4WMObxGg0S)G1x8mgrCr0zTpbUhWlM4NmsajmHrTL9B)JKLoNAZxjxLxY7gqE963
#exception dans la boucle for if i (on utlise 2 fois i parce qu'on cherche le meme element)

def calcul():
    
    phrase = """!TZ5BZPnpsa8pn3mTZnLInM)KBMNBgiH0Y1eipiOPTxFCqXwaQXytKTjH8c(SFRKSn2ghcnHMRjpkVibjlRD1Qv7(ZYezQzoWenZezBI8nrvkPvQbVau5YEJh7tcm7(on9QMOfeMp1Z1SRUjI6o2JndhWlpWmWeXitGppy5CcCZlDXZOwtyEHZnryxAsdrZWuXFden01ZL38qM46xiR0Ny55AdQcb7tgKQD8YOagXDsWuZUv4s1paZc2J93yQl1F6(RdHU0HoJcMWQ87Zz8zEuxOYdB3Dq7(MOqMJjAAqWC))17F)n4jELOEVNy0QZ7cQSS27bdnMzDsChwRmCh(Kte94LMOl9y2e2HEoEmqL7Qz2TmFYH)7kIFBWRmiUHTTNakj66qmJSA0XHooRgD(uAajEoIW7uCyWupwV58bSVCU92y)aq(mSnn0hetzOayhgtNiBuifCGC0Q3eJoSYTg)iwQi6DeHlZyqGhszwoeZwGde06)7Xeg25Vos6USA0HEEo2E3aIff4zL4UDq5YLH73p8Y(cNSiT6sS1v2mV5Ph)AIXVMy8Rjg)LlvL3yWQtyUyNph3PgLJvq(Gg8JMmb(iFe6phBj1y51Bfjhtulh6D3Hz2Rgna00akuLVfggpGSIACSLYqyCGU1n4ySvaOGO(npQZqe3nygm0mr6LkxIlopWdgH9TiU2u3jGDIHNXDJWbyrhZ8UbjvjrHa5APUsZVnn18eiOOcW4LgiRmEjsAVBHJj21cMOZ5qkhfDCfdcnUiCcN5Uw(oEyrOHayy7kw5nleSeX9PLd23FJA95UaBu5CIv(k5ALdDI7A9jGr5tm(Y5xO5HUrvjhsRlW7qhNo2r2c5svmSYvNFtG1an3bVKB4jl4Qo6JeSdSScztUmC8y564p2(KZoE4jcNnrZqWLO3AIU4WMObxGg0S)G1x8mgrCr0zTpbUhWlM4NmsajmHrTL9B)JKLoNAZxjxLxY7gqE9635B96oO5jXZhh"""
    nbr_element = 0
    compteur = 0
    compteur2 = 0
    compteur3 = 0
    
    liste_consone = ["b","c","d","f","g","h","j","k","l","m","n","p","q","r","s","t","v","w","x","z"]
    liste_voy = ["a", "e", "i", "o", "u", "y"]
    liste_spe = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "!", "(", ")"]
    
    phrase = phrase.lower()
    for i in phrase:
        nbr_element += 1
        if i in liste_voy:
            compteur += 1
        
        if i in liste_spe:
            compteur2 += 1
        
        if i in liste_consone:
            compteur3 += 1
        
        compteur = (compteur / (compteur + compteur2 + compteur3)) * 100
        compteur2 = (compteur2 / (compteur + compteur2 + compteur3)) * 100
        compteur3 = (compteur3 / (compteur + compteur2 + compteur3)) * 100
    return "Voyelles:{}".format(compteur), "Carac spe: {}".format(compteur2),"consone: {}".format(compteur3), nbr_element
    
    
print(calcul())
        
    

        

