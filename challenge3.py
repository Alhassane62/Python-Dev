x = int(input("Entrez un Entier : "))
y = float(input("Entrez un nombre : "))
o = input("Entrez une opération (+, -, *, /, %) : ")

# Addition 

if o == '+': 
    print(f"la somme de {x} et {y} est : {x + y}\n")
# Soustraction
elif o == '-':
    print(f"la différence de {x} et {y} est : {x - y}\n")
    
# Multiplication
elif o == '*':
    print(f"la produit de {x} et {y} est : {x * y}\n")
#Division
elif o == '/':
    if y != 0:
        print(f"la division de {x} et {y} est : {x / y}\n")
    else:
        print("Erreur : Division par zéro n'est pas autorisée.\n")
        print("vous ne pouvez pas diviser par zéro.")
# Modulo
elif o == '%':
    if y != 0:
        print(f"le modulo de {x} et {y} est : {x % y}\n")
    else:
        print("Erreur : Modulo par zéro n'est pas autorisé.\n")
        print("vous ne pouvez pas faire le modulo par zéro.")
   
    
    