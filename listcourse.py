courses = []
# boucle tant que utilisateur dis ajouter ou retirer de la liste
answer = input("Ajouter un element à la liste de course : 'add' \nSupprimer un element a la liste de course : 'del'\nOu sauvegarder et sortir 'save':")
while True:    
    # si ajouter a la liste
    if answer == "add":
        added=input("Que voulez vous ajouter ? : ")
        courses.append(added)
        answer = input("Ajouter un element à la liste de course : 'add' \nSupprimer un element a la liste de course : 'del'\nOu sauvegarder et sortir 'save':")
    # si retirer 
    elif answer == "del":
        print("Liste de courses :")
        for item in courses:
            print("- "+ item)
        deleted=input("Que voulez vous retirer ? : ")
        courses.remove(deleted)
        answer = input("Ajouter un element à la liste de course : 'add' \nSupprimer un element a la liste de course : 'del'\nOu sauvegarder et sortir 'save':")
    #  si save sortir de la boucle et afficher la liste de course
    elif answer == "save":
        for item in courses:
            print("Liste de courses :")
            print("- "+ item)
        break
    else :
        print("Commande inconnue\n")
        break


    # REVOIR LE CODE AVEC SYSTEM DE FONCTION ET MENU (CHOIX CHIFFRES)