etudiant = {'age': 20, 'sexe': 'M'}

etudiant['nom'] = input('Entrez votre nom : ')
etudiant['ville'] = input('Entrez votre ville : ')
etudiant['note'] = float(input('Entrez une note : '))
etudiant.pop('ville')
print(etudiant.values())
print(etudiant.keys())
print(etudiant.items())

for x, y in etudiant.items():
    print(f'{x} : {y}')