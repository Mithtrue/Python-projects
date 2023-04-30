listSenha=[]
listVogais= []
listConsoantes= []

for i in range(1,11):
    listSenha.append(input(f"Digite o {i} caractere: "))

for i in listSenha:
    if i in "AEIOUaeiou":
        listVogais.append(i)
    else:
        listConsoantes.append(i)

print(f"A lista {listConsoantes} possui: {len(listConsoantes)} consoantes")
print(f"A lista {listVogais} possui: {len(listVogais)} vogais")