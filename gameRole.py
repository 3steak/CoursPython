import random

# JOUEUR
    # VIE
legolas_life = 5
    # ATTAQUE
legolas_attack = 2
    # POTION
potion = 2

# ENEMI
    # VIE
squeezi_life = 5
    # ATTAQUE RANDOM
squeezi_attack = str(random.randint(1,3))

# GAME
    # JOUEUR VIE + POTION RESTANTE
    # ENEMI VIE
    # FIN OU NON 
    # ATTAQUE OU POTION ?
    # DEROULER :
        # ATTAQUE OU POTION
        # ATTAQUE ENEMI = RANDOM
        # ATTAQUE A X NBR

while legolas_life or squeezi_life > 0:
    print(f"Legolas a {legolas_life} de vie et {potion} de potions")
    print(f"Squeezi a {squeezi_life} de vie\n")
    if potion > 0:
        potion_choice = "Prendre une potion 2 :"
    choice = input(f"Attaquer 1\n{potion_choice}")
    squeezi_attack = random.randint(1,3)
    if choice == 1:
       squeezi_life -= legolas_attack
    elif choice == 2:
        legolas_life += 2
        potion -= 1
    else:
        print("Rentrer le bon choix")
    legolas_life -= squeezi_attack


    if legolas_life == 0:
        print("Vous etes mort")
        break
    if squeezi_life == 0:
        print("Squeezi est mort\nVous avez gagné")
        break
