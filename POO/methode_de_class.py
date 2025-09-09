class Voiture:
    voiture_crees = 0
    def __init__(self, marque, vitesse, prix):
        Voiture.voiture_crees += 1
        self.marque = marque
        self.vitesse = vitesse
        self.prix = prix
        
    
    @classmethod
    # cls pour class
    def lamborghini(cls):
        return cls(marque="Lamborghini", vitesse=250, prix=200000)
    
    @classmethod
    def porche(cls):
        return cls(marque="Porche", vitesse=200, prix=180000)
    


    # methode static

    @staticmethod
    def afficher_nb_voitures():
        print(f"Vous avez {Voiture.voiture_crees} voitures dans votre garage.")

if __name__ == "__main__":
    lambo = Voiture.lamborghini()
    porche = Voiture.porche()

    print(lambo.marque)
    print(porche.marque)
    
    Voiture.afficher_nb_voitures()