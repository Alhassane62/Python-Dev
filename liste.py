# les liste 
#creation d'une liste

liste = ["Alassane", "Diallo", 25,"Conakry"]

print(len(liste)) # pour connaitre le nombre d'element dans la liste

# afficher l'element d'une liste

#1er Position

print(liste[3])

# fonction append 
liste.append("Python")
print(f"liste avec append: {liste}")
# fonction insert

liste.insert(1, "Dev")
print(f"liste avec insert: {liste}")

# la fonctio supprime un element 
liste.remove('Diallo')
print(liste)

# fonction pop 

liste.pop()
print(liste)

# fonction reverse 

liste.reverse()
print(liste)

print(liste[-1])


# fonction sort 
liste.append('Alassane')
#liste.sort()
print(liste)

print(liste.count("Alassane"))
a = liste.copy()
print(a)

a.insert(0, 'Bonjour')



print(liste.index('Conakry'))

for x in liste:
    print(x)
    
#print(liste.max())

liste.remove('Alassane')

print(liste.count('Alassane'))
