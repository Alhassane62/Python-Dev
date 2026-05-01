# Haccker 
import random
code_pc = random.randint(1000, 9999)
#print(f"Le code du pc est : {code_pc}")
batterie = 100
saisie = 0

while code_pc != saisie and batterie > 0:
    saisie = int(input("Entrez le code du pc : "))
    if saisie != code_pc:
        batterie -= 25
        
        if saisie < code_pc:
            print(f"Code incorrect, essayez un code plus grand. Il vous reste {batterie} % de batterie.\n")
        else :
            print(f"Code incorrect, essayez un code plus petit. Il vous reste {batterie} % de batterie.\n")
    
if saisie == code_pc:
    print("Code correct ! Vous avez réussi à hacker le pc.")
    
if batterie <= 0:
    print("Batterie épuisée ! Vous avez échoué à hacker le pc.")
        