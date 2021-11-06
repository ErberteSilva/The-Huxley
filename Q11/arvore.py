
def contar_madeira(quantidade_madeira,arvores,alvo_madeira):
    total_madeira=list()
    for i in range(quantidade_madeira):
        final_madeira=0
        for n in range(i+1,quantidade_madeira):
            final_madeira+=arvores[n]-arvores[i]
        total_madeira.append(final_madeira)
        
    for i in range(quantidade_madeira-1,-1,-1):
        if total_madeira[i]>=alvo_madeira:
            return i

quantidade_madeira,alvo_madeira=[int(i) for i in input().split()]
arvores=[int(i) for i in input().split()]
arvores.sort()
altura_corte=contar_madeira(quantidade_madeira,arvores,alvo_madeira)
print(arvores[altura_corte])