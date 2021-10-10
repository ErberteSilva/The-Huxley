consumo = int(input())


def contagem(m,M,tarifa) :
    f=0
    while f<m and f<M:
        f=f+1
    return f*tarifa

def uso(consumo):
    valor=7
    
    if consumo>10:
        valor=valor+contagem(consumo-10,20,1)
    if consumo>30:
        valor=valor+contagem(consumo-30,100-30,2)
    if consumo>100:
        valor=total+valor(consumo-100,consumo-100,5)
    return valor

print(uso(consumo))