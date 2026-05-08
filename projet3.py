etudiants = []

while True:
    print("=== Menu ===")
    print("1. Ajouter un étudiant")
    print("2. Afficher les étudiants")
    print("3. Afficher les admis")
    print("4. Afficher les meilleurs étudiants")
    print("5. Quitter")
    choix = input("Entrez votre choix : ")
    
    if choix == '1':
        nom = input ("Entre le nom de l\'etudiant : ")
        age = int(input ("Entre l\'age de l\'etudiant : "))
        note = float(input ("Entre la note de l\'etudiant : "))
        
        etudiant = {
            'nom': nom, 
            'age': age, 
            'note': note
            }
        
        etudiants.append(etudiant)
        print("Etudiant ajouter avec succes !")
    elif choix == '2':
        if len(etudiants) == 0:
            print("Aucun etudiant n\'a été ajouté.")
        else:
            print("=== Liste des étudiants ===")
            for e in etudiants: 
                print(f"Nom : {e['nom']}, Age : {e['age']}, Note : {e['note']}")
    elif choix == '3':
        print('== Les Admsi ===')
        for e in etudiants:
            if e['note'] >= 10:
                print(f"{e['nom']} a Admis.")
    elif choix == '4':
        print('== Les Meilleurs Étudiants ===')
        meuilleuer_note = 0
        meilleur_etudiant = ""
        somme = 0
        
        for e in etudiants:
            somme += e['note']
            if e['note'] > meuilleuer_note:
                meuilleuer_note = e['note']
                meilleur_etudiant = e['nom']
        print(f'Le meilleur étudiant est {meilleur_etudiant} avec une note de {meuilleuer_note}')
        # print(f'La moyenne de la classe est {sum(e["note"] for e in etudiants) / len(etudiants)}')
        print(f'la moyenne de la classe est {somme / len(etudiants)}')

    elif choix == '5':
        print("Au revoir !")
        break
    else:
        print("Choix invalide. Veuillez réessayer.")
    
    
        


#for i in range(2):
    # nom = input ("Entre le nom de l\'etudiant : ")
    # age = int(input ("Entre l\'age de l\'etudiant : "))
    # note = float(input ("Entre la note de l\'etudiant : "))
    
    # etudiant = {
    #     'nom': nom, 
    #     'age': age, 
    #     'note': note
    #     }
    
    # etudiants.append(etudiant)
    
    # print()
    
    
# print("=== Autres methode d\'affichage ===")
# for cle, val in etudiants.items():
#     print(f"{cle} : {val}")

# print("=== Affichage des informations ===")

# somme = 0

# for e in etudiants: 
#     print(f"Nom : {e['nom']}, Age : {e['age']}, Note : {e['note']}")
#     somme += e['note']
    
#     if e['note'] >= 10:
#         print(f"{e['nom']} a Admis.")
#     else:
#         print(f'{e["nom"]} a Echoué.')
    
    
#     if e['note'] > meuilleuer_note:
#         meuilleuer_note = e['note']
#         meilleur_etudiant = e['nom']

# print(f'le meilleur etudiant est {meilleur_etudiant} avec une note de {meuilleuer_note}')
# print(f'la moyenne de la classe est {somme / len(etudiants)}')
        