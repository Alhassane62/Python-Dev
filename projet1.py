print("---- Bienvenue sur Le Coffre-Fort de la Banque ---- \n")

code = "2026"
point = 100
essaie = 0
saisie = ""


while code != saisie and point >0:
    saisie = input("Entrez le code du coffre-fort : ")
    essaie += 1
    point  -= 20
    
    
    if saisie != code:
        
        if saisie < code:
            print(f"Code incorrect, essayez un code plus grand. Il vous reste {point} points.\n")
        elif saisie > code:
            print(f"Code incorrect, essayez un code plus petit. Il vous reste {point} points.\n")
            
print(f"Code correct ! Vous avez ouvert le coffre-fort en {essaie} essais.")    
    
    

