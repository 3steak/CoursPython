chemin = "D:/Python/CoursPython/doc/fichier.txt"


with open(chemin) as f:
    print(f.read())

with open(chemin, "a") as f:
    f.write("bonjour ")
    
