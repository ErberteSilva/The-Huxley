rep = int(input())

for i in range(rep):
  vogais = input()
  frase = input()
  contagem = 0
  for n in vogais:
    contagem = contagem + frase.count(n)
  print(contagem)