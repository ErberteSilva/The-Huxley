convidados_matilda = list()
convidados_irmao = list()
while True:
    entrada = input()
    if entrada != "FIM":
        convidados_matilda.append(entrada)
    else:
        break
while True: 
    entrada = input()
    if entrada != "FIM":
        convidados_irmao.append(entrada)
    else:
        break
convidados_irmao.sort()
convidados_matilda.sort()
convidados = convidados_matilda + convidados_irmao
convidados.sort()

for i in range(len(convidados_matilda)):
    print(convidados_matilda[i])
print('-'*50)
for i in range(len(convidados_irmao)):
    print(convidados_irmao[i])
print('-'*50)
for i in range(len(convidados)):
    print(convidados[i])
