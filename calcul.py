# demander nombre 1 et 2 
numberA = input("Entrez un premier nombre :")
numberB = input("Entrez un deuxieme nombre :")

# additionner 1 et 2 
result = int(numberA) + int(numberB)
# afficher resultat

print("Voici le resultat de " + str(numberA) + "+" + str(numberB) + ": "+ str(result))

print("coucou") if result > 20 else print ("bye") 