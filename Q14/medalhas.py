def divisao_medalhas():
    dados = input()
    dic = {}
    while dados != '*':
        pais,medalha = dados.split(',')
        medalha_atual = dic.get(pais, (0,0,0))
        ouro = medalha_atual[0]
        prata = medalha_atual[1]
        bronze = medalha_atual[2]
        if medalha == 'ouro':
            ouro += 1
        if medalha == 'prata':
            prata += 1
        elif medalha == 'bronze':
            bronze += 1
        dic[pais] = (ouro, prata, bronze, pais)
        dados = input()
    return dic

def quadro_medalhas(dic):
    lista = list(dic.values())
    lista.sort(reverse = True)
    i = 1
    for (ouro, prata, bronze, pais) in lista:
        print('%d)%s ouro:%d prata:%d bronze:%d' % (i, pais, ouro, prata, bronze))
        i += 1

dic = divisao_medalhas()
quadro_medalhas(dic)