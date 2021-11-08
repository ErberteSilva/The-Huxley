while True:
  quantidade = int(input())
  alunos =[]
  if quantidade ==0:
    break
  for i in range(quantidade):
    nome = input()
    camisetas = input()
    cor,tamanho = camisetas.split(' ')
    alunos.append({'nome': nome,'cor':cor,'tamanho':tamanho})
  ordem = sorted(sorted(sorted(alunos,key = lambda x: x['nome']), key = lambda x : x['tamanho'],reverse = True), key = lambda x : x['cor'])
  print()
  for aluno in ordem:
    print(aluno['cor'] + ' ' +aluno['tamanho']+' '+aluno['nome'])