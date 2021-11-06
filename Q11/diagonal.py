def processar_quadro(diag,ordem,elementos):
    resultado=0

    if diag=='acima':
        for i in range(ordem):
            for j in range(i+1,ordem):
               resultado+=elementos[i][j]
    else:
        for i in range(1,ordem):
            for j in range(i):
                resultado+=elementos[i][j]
        
    return(resultado)

diag=input()
numero_base=int(input())
ordem=int(input())
elementos=[[int (i) for i in input().split()] for j in range(ordem)]

print(processar_quadro(diag,ordem,elementos)>numero_base)