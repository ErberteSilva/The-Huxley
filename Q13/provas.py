gabarito = input()

dados_gerais = dict()
while True:
  dados = input().split()
  if dados == ['9999']:
    break
  aluno = dados[0]
  resposta = dados[1]
  dados_gerais[aluno] = resposta
notas = dict()
cont_notas = dict()
acima_media = 0
for aluno, resposta in dados_gerais.items():
  for questao in range(10):
    if gabarito[questao] == resposta[questao]:
      notas[aluno] = notas.get(aluno,0) + 1
  notas[aluno] = notas.get(aluno,0) 
  cont_notas[notas[aluno]] = cont_notas.get(notas[aluno], 0) + 1
  if notas[aluno] >= 6:
    acima_media += 1
  print(aluno, float(notas[aluno]))
print("%.1f" %(acima_media / int(aluno) * 100) + "%")
maior_frequencia = [0,0]
for acertos, repeticoes in cont_notas.items():
  if repeticoes > maior_frequencia[1]:
    maior_frequencia[0] = acertos
    maior_frequencia[1] = repeticoes
print(float(maior_frequencia[0]))