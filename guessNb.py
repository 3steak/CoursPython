import random

# print("Bien joué") if number_to_guess == guess else print("Dommage le nombre était : "+ number_to_guess)

# enregistrer le nbr to guess
number_to_guess = str(random.randint(0,10))

#  enregistrer le nbr de chance
attempt = 5
# enregistrer la regle
# afficher regles
# input guess
guess_rule = "Deviner le nombre compris entre 0 et 10"
guess_input = input(f"Il vous reste {attempt} chances :")
 # tant que attempte != 0
        # continue
        # si guesss != nbre to guess
        # continue
        # sinon si == GG 
    # sinon plus chance
while attempt > 1:
   if guess_input != number_to_guess:
    print(guess_rule)
    attempt -= 1
    guess_input = input(f"Il vous reste {attempt} chances :") 
   else:
    print("GG")
    break
else: print(f"Dommage !\n Le nombre était {number_to_guess}")
# (c'est plus ou c est moins)


