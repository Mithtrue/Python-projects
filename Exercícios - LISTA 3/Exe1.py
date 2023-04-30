numberlist=[]

for i in range(0,5):
    numberlist.append(int(input("Digite cinco números INTEIROS, um de cada vez: ")))

for i in range(0,5):
    print(f"O vetor na casa {i} é: {numberlist[i]}")