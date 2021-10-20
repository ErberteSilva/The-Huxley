def vantagem(c_1,c_2,x):
    conTox(c_1,float)
    conTox(c_2,float)
    maxdif=0
    for cont in range(x):
        difer=c_1[cont]-c_2[cont]
        if difer>maxdif:
            maxdif=difer
    return(maxdif)

def conTox(lista,x):
    for cont in range(len(lista)):
        lista[cont]=x(lista[cont])

tamanho=int(input())
votosc_1=input().split()
votosc_2=input().split()

print("%.2f"%vantagem(votosc_1,votosc_2,tamanho))