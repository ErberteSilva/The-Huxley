while True:
    n,m =[int(i) for i in input().split()]
    if n == 0 and m == 0 :
        break
    dic ={}
    for i in range(n):
        traduzir, traduzido= input().split(sep=" -> ")
        dic[traduzir]=traduzido
    texto_final=list()
    for i in range(m):
        texto = input()
        for traduzir, traduzido in dic.items():
            texto = texto.replace(traduzir,traduzido)
        texto_final.append(texto)
    for texto in texto_final:
        print("".join(texto))