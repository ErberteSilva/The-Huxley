dic = {}
contagem=0
cont = 0
maior_idade = 0
while True:
    idade = int(input())
    if idade == -1:
        break
    dados = input()
    dic[idade] = dados
    cont= cont+1 
    dados_separados = dic[idade].split()
    if 18<= idade <=35 and dados_separados[0]== "f" and dados_separados[1]=="l"and dados_separados[2]=="v":
        contagem = contagem + 1
    if idade > maior_idade:
        maior_idade = idade
porcentagem = (contagem/cont*100) 
print("Mais velho:", maior_idade)
print("Mulheres com olhos verdes, loiras com 18 a 35 anos: %.2f" %porcentagem + "%",sep='')

