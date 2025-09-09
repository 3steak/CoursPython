class Vehicule : 
    def avance(self):
        print("le vehicule démarre")


class Voiture(Vehicule):
    def avance(self):
        # j apelle la methode parente et y ajoute quelque chose
        #  === POLYMORPHISME
        super().avance()
        print("La voiture roule")

class Avion(Vehicule):
    def avance(self):
        super().avance()
        print("L'avion vole")

v = Voiture()
a = Avion()
v.avance()
a.avance()