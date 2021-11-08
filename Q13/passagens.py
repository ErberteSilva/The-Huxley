dic = dict()

for i in range(37):
  voos_disponiveis, vagas = [int(u) for u in input().split()]
  dic[voos_disponiveis] = vagas
while True:
  In_value = input()
  if In_value == '9999':
    break
  rg, viagem = [int(i) for i in In_value.split()]
  if dic.get(viagem, 0) > 0:
    print(rg)
    dic[viagem] -= 1
  else:
    print("INDISPONIVEL")