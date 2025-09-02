d = {"prenom" : "deafmute",
     "profession": "influenceur muscu",
     "ville": "Rennes"}


print(d["profession"])

d["profession"] = "Streamer"
print(d["profession"])

for cle, valeur in d.items():
    print(cle, valeur)