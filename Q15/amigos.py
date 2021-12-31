amigos = list()
notamigos = list()
while True:
    entrada = input()
    if entrada == "FIM":
        break
    votacao = entrada.split()
    if votacao[1] == "YES":
        amigos.append(votacao[0])
    else:
        notamigos.append(votacao[0])

melhor_amigo = 0
lenght_anterior = 0

for i in range(len(amigos)):
    lenght = len(amigos[i])
    if lenght > lenght_anterior:
        lenght_anterior = lenght
        melhor_amigo = amigos[i]

amigos.sort()
notamigos.sort()

amigos_final = list(dict.fromkeys(amigos))
for i in range(len(amigos_final)):
    print(amigos_final[i])
for i in range(len(notamigos)):
    print(notamigos[i])
print('\n')
print("Amigo do Habay:")
print(melhor_amigo)
