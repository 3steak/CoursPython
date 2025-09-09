projets = ["pr_Harry","pr_Game_Of_Thrones", "Jumanji" ]

class Utilisateur :
    def __init__(self, nom, prenom):
        self.nom = nom
        self.prenom = prenom

    def __str__(self):
        return f"Utilisateur {self.nom} {self.prenom}"
    
    def afficher_projets(self):
        for projet in projets:
            print(projet)


# heritage de la classe mere vers fille
# on utilise la fct super() pour acceder aux methodes de la mere
class Junior(Utilisateur):
    def __init__(self, nom, prenom):
        super().__init__(nom, prenom)

paul = Junior("Paul", "Heta")
print(paul)
paul.afficher_projets()

