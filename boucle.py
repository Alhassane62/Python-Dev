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
    

# chalenge sur un mot 

nom = input("Entrez un mot : ")

# for i in range(len(nom)-1, -1, -1):
#     print(nom[i], end="")

for i in range(4): 
    print(nom)
# for i in nom:
#     print(i)

print ("------------------------------------ \n")

for i in range(0, len(nom), 2):
    print(nom[i], end="")



print ("------------------------------------ \n")

y = 0

for i in nom:
    y += 1
print(f"le nombre de caractère dans le mot {nom} est : {y}")

print ("------------------------------------ \n")

t = 0
for i in range(len(nom)):
    if nom[i] != " ":
        t += 1
   
print(f"le nombre de caractère dans le mot {nom} est : {t}")

print ("------------------------------------ \n")


mt = input("Entrez une phrase : ")
y = int(input("Entrez un le premier nombre : "))
z = int(input("Entrez un le deuxieme nombre : "))

for i  in range(y, z):
    print(mt)
    
    
