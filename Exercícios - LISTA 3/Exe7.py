listAge= []
listWeight= []
listAger= []
listWeightr= []

for i in range(5):
    listAge.append(int(input(f"Digite a idade da {i + 1}ª pessoa: ")))
    listWeight.append(int(input(f"Digite o peso da {i + 1}ª pessoa: ")))

for i in range (1, len(listAge) + 1):
    listAger.append(listAge[-i])
    listWeightr.append(listWeight[-i])

print(f"Lista de idade: {listAge}, lista na ordem inversa: {listAger}")
print(f"Lista de peso: {listWeight}, lista na ordem inversa: {listWeightr}")
