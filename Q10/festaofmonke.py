def ord(lista):
    descarte=lista.copy()
    lista.clear()
    listaord=lista
    for cont in range(len(descarte)):
        listaord.append(min(descarte))
        descarte.pop(descarte.index(min(descarte)))

nomes=list()
separador=['-' for cont in range(50)]

while True:
    listnome=input()
    if nome=='FIM':
        break
    nomes.append(listnome)

while True:
    ord(nomes)
    print('\n'.join(nomes))
    lenght=int(input())
    if lenght==0:
        break
    for cont in range(lenght):
        nomes.append(input())
    print(''.join(separador))