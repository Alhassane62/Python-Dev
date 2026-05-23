class Etudiant:
    def __init__(self, nom, note):
        self.nom = nom
        self.note = note
        
    def afficher(self):
        print(f"Vous etes {self.nom} avec la note {self.note}")
    
    
    def afficher_admission(self):
        if self.note >= 10:
            print(f"Felicitations {self.nom}! Admis avec {self.note}")
        else :
            print(f"Desolé {self.nom} vous avez {self.note}")
            
            
e1 = Etudiant('Diallo Alhssane', 12)
e2 = Etudiant("Sadio Toure", 9)

e1.afficher()
e1.afficher_admission()

print("----------------------------")

e2.afficher()
e2.afficher_admission()



class Client:
    def __init__(self, nom, prenom, tel):
        self.nom = nom
        self.prenom = prenom
        self.tel = tel 
        
        
        
    
    


class CompteCourant(Client):
    def __init__(self, nom, prenom, tel, numCompte, type, solde):
        super().__init__(nom, prenom, tel)
        self.numCompte = numCompte
        self.type = "Courant"
        self.__solde = solde
        
    def depot(self, d):
        print(f"Bonjour ! Vous avez effectuer un versement {self.numCompte} de {d}. Solde {self.__solde + d} sur votre compte {self.type}")
    
    
    def retrait(self, r):
        if r >= self.__solde :
            print('Solde insufusuant !')
        else:
            print(f"Vous avez effectuer un decaissement {self.numCompte} de {r}. Solde {self.__solde - r} sur votre compte {self.type}")
            





c1 = CompteCourant("Toure", "Sadio", '224624366064', 6000142523, '', 500000)

c1.depot(50000000)
c1.retrait(10000)




        
    
    
