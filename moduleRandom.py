import random
r = str(random.randint(0,10))

guess = input("Deviner le nombre :")
print("Bien joué") if r == guess else print("Dommage le nombre était : "+ r)