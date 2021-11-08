encomenda = int(input())
cardapio = {}
for i in range(encomenda):
  codigo = int(input())
  descricao = input('')
  custo = float(input())
  cardapio[codigo] = custo

preco_final = 0
identificacao = int(input())
while identificacao != 0:
    quantidade = int(input())
    if quantidade > 0 and identificacao in cardapio:
        preco_final += cardapio[identificacao] * quantidade
    identificacao = int(input())
print('%.2f' % preco_final)