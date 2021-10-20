def conTox(lista,x):
    for cont in range(len(lista)):
        lista[cont]=x(lista[cont])

lenght=input()
values=input().split()
conTox(values,int)
print("Menor valor: %d"%min(values))
print('Posicao: %d'%(values.index(min(values))))