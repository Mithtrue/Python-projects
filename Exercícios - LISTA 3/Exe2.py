listnumber=[]
for i in range(1,6):
    listnumber.append(int(input(f"Digite cinco números começando pelo {i}º: ")))

for i in range(len(listnumber) - 1, -1, -1):
    print(f"O o vetor da casa {i} é: {listnumber[i]}")
