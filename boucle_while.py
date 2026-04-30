## Boucle while
mot_passe = "2020"
saisie = ""
tentatives = 0

while mot_passe != "2020":
    saisie = input("Entrez le mot de passe : ")
    tentatives += 1
    if saisie != mot_passe:
        print("Mot de passe incorrect, essayez à nouveau.\n")
        
print(f"Mot de passe correct ! Nombre de tentatives : {tentatives}")


print ("------------------------------------ \n")

pv = 100
tour = 1

while pv > 0:
    print(f"Tour {tour} : PV = {pv}")
    pv -= 15
    tour += 1
    if pv < 20 : 
        print(f"Attention sante critique ! pv {pv} ")
    
        
print(f"la personne est mort avec  PV = {pv}")
        
        
