# TODO : Calculer les quantités de matériaux nécessaires pour fabriquer un nombre donné de baguettes magiques.

nombre_baguettes = int(input("Nombre de baguettes a fabriquer : "))
bois = nombre_baguettes * 3
coeur_creature = nombre_baguettes
vernis = nombre_baguettes * 10

print(f"Voici les materiaux requis pour la fabrication de {nombre_baguettes} baguettes magiques:")
print("-", bois, "piece(s) de bois")
print("-", coeur_creature, "coeur(s) de creatures magiques")
print("-", vernis, "ml de vernis")
