class Facture:
    # Constructeur de la classe Facture
    def __init__(self, id, numero, montant):
        self.id = id
        self.numero = numero
        self.montant = montant
 
    # Méthode pour afficher une facture
    def __repr__(self):
        # f-string pour afficher une facture (formatted string literal)
        return f"{self.numero} : {self.montant} €"

    # Méthode pour obtenir un attribut d'une facture
    def get(self, attribute):
        match attribute:
            case 1:
                return self.id
            case 2:  
                return self.numero
            case 3:
                return self.montant
            case  _:
                return None   
    
    
class CombinaisonFactures:
    # Constructeur classe CombinaisonFactures
    def __init__(self, factures, rechercher):
        self.factures = factures
        self.rechercher = rechercher
        self.nombre_combinaisons = 0
        self.combinaisons_trouvees = []

    # Méthode pour trouver les combinaisons
    def trouver_combinaisons(self, combinaison_actuelle=[], index=0):
        somme_combinaison = sum(facture.get(3) for facture in combinaison_actuelle)
        if combinaison_actuelle and somme_combinaison == self.rechercher:
            # Ajouter la combinaison trouvée
            self.combinaisons_trouvees.append(combinaison_actuelle)
            self.nombre_combinaisons += 1

        if index >= len(factures):
            return

        
        for i in range(index, len(factures)):
            # Appeler la fonction récursivement
            self.trouver_combinaisons(combinaison_actuelle + [self.factures[i]], i + 1)

    # Méthode pour obtenir les résultats
    def get_resultats(self):
        # Appeler la méthode pour trouver les combinaisons
        self.trouver_combinaisons()
        return self.nombre_combinaisons, self.combinaisons_trouvees

# Liste des factures avec identifiants
factures = [
    Facture(1,  'FA001', 11.5),
    Facture(2,  'FA002', 3.68),
    Facture(3,  'FA003', 5.38),
    Facture(4,  'FA004', 2.21),
    Facture(5,  'FA005', 8.69),
    Facture(6,  'FA006', 20.99),
    Facture(7,  'FA007', 12.5),
    Facture(8,  'FA008', 25.43),
    Facture(9,  'FA009', 10.75),
    Facture(10, 'FA010', 30),
    Facture(11, 'FA011', -5.58),
    Facture(12, 'FA012', -1.85),
    Facture(13, 'FA013', -11.54),
    Facture(14, 'FA014', -9.11),
    Facture(15, 'FA015', -21.01)
] 

# Valeur a rechercher
rechercher = float(input("montant rechercher : "))

# Créer une instance de la classe CombinaisonFactures
combinaison_factures = CombinaisonFactures(factures, rechercher)
nombre_combinaisons, combinaisons_trouvees = combinaison_factures.get_resultats()

print("Valeur rechercher : ", rechercher)
print("nombre de combinaisons trouvées: ", nombre_combinaisons)
print("Combinaisons trouvées:")


for i in combinaisons_trouvees:
    print( "combinaison :", i)
    for facture in i:
        print(facture)
print("_____________________")
print(combinaisons_trouvees)
print(f"{nombre_combinaisons} combinaisons trouvées")
