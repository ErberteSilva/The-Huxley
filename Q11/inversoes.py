lenght = int(input())
lista =[int(input()) for i in range(lenght)]



def bubble (lista,lenght):

    steps = 0
    for i in range(lenght-1, 0, -1) :
        for n in range(i):
            if lista[n] > lista[n+1] :
                lista[n], lista[n+1] = lista[n+1], lista[n]
                steps = steps+1
    return steps

print(bubble(lista, lenght))

