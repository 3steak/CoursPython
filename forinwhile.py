numbers = [1,2,3,4,5]
for i in numbers:
    print(i)
    if i == 2:
        print("i = 2")

i=0
while i < 6:
    print(i)
    i+=1


nombre = 7

for i in range(11):
    # utilisation de f-string
    print(f"{i} x {nombre} = {i * nombre}")