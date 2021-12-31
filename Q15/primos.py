def priminho(n) :
    for cont in range(2,n):
        if n%cont == 0:
            return False
    return True

primos=[int(i) for i in input().split()]

resultado = 1

for i in primos:
    if i <=1:
        resultado = False
        break
    elif priminho(i):
        resultado *= i
    else:
        resultado = False

if resultado == False :
    print("SEM PRODUTO")
else:
    print(resultado)
