# demander nombre 1 et 2 
numberA = input("Entrez un premier nombre :")
numberB = input("Entrez un deuxieme nombre :")

print(type(int(numberA)))
if numberA.isdigit() and numberB.isdigit:
        result = int(numberA) + int(numberB)
        print("Voici le resultat de " + str(numberA) + " + " + str(numberB) + " : "+ str(result))
else: print("Erreur : Veuillez entrer uniquement des nombres.")

