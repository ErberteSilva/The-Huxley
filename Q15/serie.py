def eh_primo(n) :
    for cont in range(2,n):
        if n%cont == 0:
            return False
    return True

def proximo_primo(n):
    if eh_primo(n):
        return n
    else:
        return proximo_primo(n+1)
    
def fatorial(n):
    if n<=1:
        return(1)
    else:
        return(n*fatorial(n-1))

rep=int(input())
valor_final=0
cont=0
reposta_textual=""
for x in range(rep):
    cont+=1
    prox_primo=proximo_primo(cont)
    valor_final+=fatorial(cont)/prox_primo
    reposta_textual+=str(cont)+'!/'+str(prox_primo)+" + "

print(reposta_textual[:-3])
print("%.2f"%valor_final)