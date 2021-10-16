
def calculo(v1,v2,perc):
    if v1<=v2:
        return(v1*perc)
    else:
        return((v2)*perc)

renda=float(input())
renda=renda-2000
f=0
if renda>0:
    f=calculo(renda,1000,0.08)
    renda=renda-1000
if renda>0:
    f=f+calculo(renda,1500,0.18)
    renda=renda-1500
if renda>0:
    f=f+renda*0.28

if f!=0:
    print("R$ %.2f"%f) 
else:
    print("Isento")