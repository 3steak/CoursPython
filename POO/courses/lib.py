import json
import os

from constants import DATA_DIR, LOGGER

class Liste(list):
    # "list" pour heriter des methodes de list comme append etc
    def ajouter(self, element):
        if not isinstance(element, str):
            raise ValueError("La liste doit contenir que des mots.")
        
        if element in self:
            LOGGER.error(f"{element} est deja dans la liste.")
            return False
        
        self.append(element)
        return True

    def enlever(self, element):
        if not element in self:
            raise ValueError("L'element n'est pas dans la liste")
        self.remove(element)
        return True

    def afficher(self):
        print(f"Ma liste de {self.nom} :")
        for element in self:
            print(f"- {element}")
            
    def sauvegarder(self):
        chemin = os.path.join(DATA_DIR, f"{self.nom}.json")
        if not os.path.exists(DATA_DIR):
            os.makedirs(DATA_DIR)
        
        with open(chemin, "w") as f:
            json.dump(self, f, indent=4)

        return True

    def __init__(self, nom):
        self.nom = nom

if __name__ == "__main__":
    print("Hello")

liste = Liste("courses")
liste.ajouter("Pommes")
liste.ajouter("Poires")
liste.ajouter("Peches")
liste.afficher()
liste.sauvegarder()