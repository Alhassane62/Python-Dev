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
