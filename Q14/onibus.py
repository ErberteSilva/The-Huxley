contagem = []
cliente = {}
idade = []
while True:
   cliente["num"] = int(input())
   if cliente["num"] == -1:
      break
   cliente["data"] = input()
   cliente["de"] = input()
   cliente["para"] = input()
   cliente["horario"] = input() 
   cliente["poltrona"] = int(input())
   cliente["idade"] = int(input())
   idade.append(cliente["idade"])
   cliente["nome"] = input()
   contagem.append(cliente)
   cliente = {}
for cliente in contagem:
   if cliente["idade"] > (sum(idade)/len(idade)) and cliente["poltrona"] % 2 == 0:
      print(cliente["nome"])