vetor1= "JÃ ER"
vetor2="OOPDO"
vetor3='0123456789'
vetorlist= []
for i in range(0,5):
    vetorlist.append(vetor1[i])
    vetorlist.append(vetor2[i])

for i in range(0,10):
    if i == 0:
        vetor3= vetor3.replace(vetor3[i], vetorlist[i])
    elif i % 2 == 0:
        vetor3 = vetor3.replace(vetor3[i], vetorlist[i])
    else:
        vetor3 = vetor3.replace(vetor3[i], vetorlist[i])

print(vetor3)