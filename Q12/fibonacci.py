
def fibomano(lenght):
    if lenght==0:
        return ''
    else:
        return str(manofibo(0,0,lenght))+' '+fibomano(lenght-1)

def manofibo(nxt,previous,lenght):
    if lenght<=1:
        return nxt
    else:
        nxt = nxt + previous
        previous = nxt - previous
        if(nxt == 0):
            nxt = nxt + 1
        return manofibo(nxt,previous,lenght-1)

print(fibomano(int(input())))