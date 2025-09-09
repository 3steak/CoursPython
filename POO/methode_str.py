class Voiture:
    def __init__(self, marque, vitesse):
        self.marque = marque
        self.vitesse = vitesse
        

    # indique la représentation en chaîne de caractères de l'objet.
    def __str__(self):
        return f"Votre voiture est une {self.marque}, sa vitessse max est de {self.vitesse}."

if __name__ == "__main__":
    porsche = Voiture("Porsche", 200)
    print(porsche)
    

