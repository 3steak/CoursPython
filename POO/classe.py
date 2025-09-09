class Voiture:

    def __init__(self, marque, couleur):
        self.marque = marque
        self.couleur = couleur

    # methode
    def get_brand(self):
        print(self.marque)


voiture_01 = Voiture("lambo","bleu")


voiture_01.get_brand()