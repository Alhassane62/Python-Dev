# x = int(input("Entrez un Entier : "))
# y = float(input("Entrez un nombre : "))

# #Division
# if y > 0:
#     div = x / y 
#     print(f"la division de {x} et {y} est : {div}\n")
# else:
#     print("Erreur : Division par zéro n'est pas autorisée.\n")
#     print("vous ne pouvez pas diviser par zéro.")

# # Modulo
# if y != 0:
#     mod = x % y 
#     print(f"le modulo de {x} et {y} est : {mod}\n")
# else:
#     print("Erreur y est null \n")
#     print("vous ne pouvez pas faire le modulo par zéro.")
    
    
    
nom = input("Quel est votre nom ? ")
note1 = float(input("Entrez la première note : "))
note2 = float(input("Entrez la deuxième note : "))
note3 = float(input("Entrez la troisième note : "))

# som = note1 + note2 + note3
# moy = som / 3

moy = (note1 + note2 + note3) / 3

if moy >= 10:
    print(f"Félicitations {nom}, vous avez réussi avec une moyenne de {moy:.2f} !")
elif moy >= 7:
    print(f"{nom}, vous avez une moyenne de {moy:.2f}. Vous êtes en zone de rattrapage.")
else:
    print(f"Désolé {nom}, vous avez échoué avec une moyenne de {moy:.2f}.")
    
