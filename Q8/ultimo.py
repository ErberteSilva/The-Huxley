frase=input()

if frase.rfind(' ')==-1:
    num=0
else:
    num=frase.rfind(' ')+1

print(frase[num:len(frase)])