# Boucle for 

for x in range(5):
    print(x)


print ("------------------------------------")

for i in range(5): 
    print("Bonjour tout le monde !")


x = 0

for i in range(1,50):
    x = x + i 
    print(f"la somme de 1 à {i} est : {x}")
    
a = int(input("Entrez la premiere valeur : "))
c = int(input("Entrez la deuxime valeur : "))
b = 0

for y in range(a, c + 1):
    b += y 
    print(f"la somme de 1 à {y} est : {b}")
    

