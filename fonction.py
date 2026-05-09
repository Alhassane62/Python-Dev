def bonjour():
    print("Bonjour, comment ça va ?")

bonjour()


def bonjour_par_nom(nom):
    print(f"Bonjour {nom}, comment ça va ?")

bonjour_par_nom('Alassane')

def addition(a, b):
    somme = a + b
    return somme


resultat = addition(5, 10)
print(f"Le résultat de l'addition est : {resultat}")



def calculatrice():
    a = float(input("ENtre la première valeur : "))
    b = float(input("Entre la deuxième valeur : "))
    print("Choisissez l'opération :")
    print("1. Addition")
    print("2. Soustraction")
    print("3. Multiplication")
    print("4. Division")
    choix = input("Entrez votre choix (1/2/3/4) : ")
    
    if choix == '1':
        # somme = a + b
        print(f"Le résultat de l'addition est : {addition(a, b)}")
    elif choix == '2':
        difference = a - b
        print(f"Le résultat de la soustraction est : {difference}")
    elif choix == '3':
        produit = a * b
        print(f"Le résultat de la multiplication est : {produit}")
    elif choix == '4':
        if b != 0:
            quotient = a / b
            print(f"Le résultat de la division est : {quotient}")
        else:
            print("Erreur : Division par zéro n'est pas autorisée.")

calculatrice()


def verifier_admission():
    a = float(input("Entrez une note  : "))
    b = float(input("Entrez une deuxieme note : "))
    c = float(input("Entrez une troisième note : "))
    moyenne = (a + b + c) / 3
    return moyenne 
moyenne = verifier_admission()
if moyenne >= 10:
    print(f"Félicitations ! Vous êtes admis avec une moyenne de {moyenne:.2f}.")
else:
    print(f"Désolé, vous n'êtes pas admis. Votre moyenne est de {moyenne:.2f}.")
    
    

    


    
 