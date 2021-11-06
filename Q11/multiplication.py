lenghtA,heightA_lenghtB,heightB=[int(i) for i in input().split()]

matriz_A=[[int(j) for j in input().split()]for i in range(lenghtA)]
matriz_B=[[int(j) for j in input().split()]for i in range(heightA_lenghtB)]

prov=list()
result=list()
for i in range(lenghtA):
    for u in range(heightB):
        soma=0
        for j in range(heightA_lenghtB):
            soma+=matriz_A[i][j]*matriz_B[j][u]
        prov.append(str(soma))
    result.append(prov.copy())
    prov.clear()

for i in result:
    print(" ".join(i))