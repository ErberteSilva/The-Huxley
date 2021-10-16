investimento, acrescimo, anos = input().split()

investimento = float(investimento)
acrescimo = float(acrescimo)
anos = int(anos)
tempo = anos * 4
montante = investimento
for i in range(1, tempo + 1):
  lucro = montante * (acrescimo)
  montante = investimento * (1 + acrescimo)**i
  
  print('Rendimento:','%.2f' %lucro, 'Montante:', '%.2f' %montante)