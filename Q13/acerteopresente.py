quant = int(input())
dic ={}
for i in range(quant):
    participante = input().split()
    nome = participante[0]
    presentes = participante[1:]
    dic[nome]=presentes

while(True):
    presente_esperado = input()
    if presente_esperado == "FIM":
        break
    pessoa, presente = presente_esperado.split()
    #lista = dic.get(pessoa)
    if presente in dic[pessoa]:
        print("Uhul! Seu amigo secreto vai adorar")
    else:
        print("Tente Novamente!")