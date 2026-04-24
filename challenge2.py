prix = float(input("Entrez le prix du produit : "))

if prix > 30000 :
    red =  prix - (prix * 0.3)
    print(f"Le prix après une réduction de 30% est : {red:.2f} GNF")
else:
    red =  prix + (prix * 0.3)
    print(f"Le prix après une augmentation de 30% est : {red:.2f} GNF")
    
    

