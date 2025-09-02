import json

chemin = "D:/Python/CoursPython/doc/lecture.json"

# me pas oublier de changer le mode d ecriture "w" ou lecture "r" ou "a"
# pour  ajouter au fichier

# with open(chemin, "w") as f:
#     json.dump("Bonjour", f)

with open(chemin, "r") as f:
    print(type(json.load(f)))
