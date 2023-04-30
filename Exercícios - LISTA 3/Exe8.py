listA=[]

for i in range(10):
    listA.append(int(input(f"Digite o {i + 1}º número inteiro: ")))

soma= 0
for i in range(10):
    elevado= listA[i]**2
    print(f"{listA[i]}² = {elevado}")
    soma += elevado
print(f"A soma de todos os números ao quadrado da lista {listA} é igual a: {soma} ")