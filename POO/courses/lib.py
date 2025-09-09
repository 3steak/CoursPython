import logging
LOGGER = logging.getLogger()

class Liste(list):
    # list pour heriter des methodes de list comme append etc
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
    
    def __init__(self, nom):
        self.nom = nom

if __name__ == "__main__":
    print("Hello")
