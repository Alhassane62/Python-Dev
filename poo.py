class Personne:
    def __init__(self, nom, prenom, age):
        self.nom = nom
        self.prenom = prenom
        self.age = age
        
        
    def se_presenter(self):
        print(f"Bonjour, je m'appelle {self.prenom} {self.nom} et j'ai {self.age} ans.")
        
personne1= Personne("Doe", "John", 30)
objet2 = Personne("Smith", "Jane", 25)


print(f"nom : {personne1.nom}, prénom : {personne1.prenom}, âge : {personne1.age}")
print(f"nom : {objet2.nom}, prénom : {objet2.prenom}, âge : {objet2.age}")

personne1.se_presenter()



class Calculatrice:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def addition(self):
        print(f"La somme de {self.x} et {self.y} est : {self.x + self.y}")
    
    def difference(self):
        print(f"La difference de {self.x} et {self.y} est : {self.x - self.y}")
        
        
cal1 = Calculatrice(2,5)
cal1.addition()
cal1.difference()
    
    
    
class Compte:
    def __init__(self, nom, solde):
        self.nom = nom
        self.__solde = solde
        
    def afficher(self):
        print(f"Bonjour {self.nom} votre solde est {self.__solde}")
        
    def depot(self):
        a = int(input('Entre le montant : '))
        d = self.__solde + a
        print(f"Vous avez un depot {a}, votre solde est de {d}")
        
   
        
    def retrait(self):
        r = float(input('Entrez le montant a retirer : '))
        if r >= self.__solde :
            print('Solde insuffisant !')
        else:
            print(f'Vous avez retier {r}. Votre solde est {self.__solde - r}')

c1 = Compte('ALhassane', 50000)
c1.afficher()

c1.depot()
c1.retrait()


class Etudiant(Personne):
    def __init__(self, tel, mail, matricule):
        self.tel = tel
        self.mail = mail
        self.matricule = matricule
        
    def afficherr(self):
        print(f"Bonjour {self.tel}")
        

e1 = Etudiant('624366064', 'alhassangsdiallo@gmail.com', '554052222')
# e1.se_presenter()

e1.afficherr()
        
        
    
    




