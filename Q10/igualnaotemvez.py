def removerrep(lista):
    for cont in lista:
        for cont2 in range(lista.count(cont)-1):
            lista.pop(lista.index(cont))

def ordenar(lista):
    desorg=lista.copy()
    lista.clear()
    org=lista
    for cont in range(len(desorg)):
        org.append(min(desorg))
        desorg.pop(desorg.index(min(desorg)))

def conTox(lista,x):
    for cont in range(len(lista)):
        lista[cont]=x(lista[cont])


tamanho=int(input())
listanum=input().split()

conTox(listanum,int)
removerrep(listanum)
ordenar(listanum)
conTox(listanum,str)

print(' '.join(listanum))