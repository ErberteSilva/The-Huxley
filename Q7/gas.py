US = float(input())/3.8
BR = float(input())
doletas = float(input())

UStoBR = US * doletas

print("Gasolina EUA: R$ %.2f" %UStoBR)
print("Gasolina Brasil: R$ %.2f" %BR)

if UStoBR == BR: 
    print ("Igual")
elif UStoBR < BR:
    print("Mais barata nos EUA")
else :
    print("Mais barata no Brasil")
