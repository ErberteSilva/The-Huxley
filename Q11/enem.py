def busca(insc,x):
    first = 0
    last = len(insc)-1 

    while first <= last:
        half = ((first+last)//2)
        if insc[half] == x:
            return half
        elif x < insc[half]:
            last = half - 1 
        else : 
            first = half + 1
    return - 1 


n_inscritos = int(input())
insc = [int(input())for i in range(n_inscritos)]
notas = [int(input())for i in range(n_inscritos)]
n_consulta = int(input())

for i in range(n_consulta):
    ans = busca(insc,int(input()))
    if ans != -1 :
        print(notas[ans])
    else:
        print("NAO SE APRESENTOU")