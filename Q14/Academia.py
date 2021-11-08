dados ={}
for i in range(100):
    nome = input()
    if nome == "SAIR":
        break
    senha = int(input())
    situacao = input()
    dados[senha] = nome, situacao

while True:
    checagem = int(input())
    if checagem == -1:
        break
    cliente = list()
    if checagem in (dados.keys()):
        cliente = dados[checagem]
        if cliente[1] == 'P':
            print(cliente[0],", seja bem-vindo(a)!",sep='')
        else:
            print("Não está esquecendo de algo, ",cliente[0],"? Procure a recepção!",sep='')
    else:
        print("Seja bem-vindo(a)! Procure a recepção!")  

