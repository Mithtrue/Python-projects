notaslist= []

for i in range(1,5):
    notaslist.append(int(input(f"Digite a {i}º nota: ")))


notasTotal= 0
for i in notaslist:
    notasTotal= i + notasTotal

media= notasTotal / 4

print(f"A média aritmética das 4 notas é: {media}")