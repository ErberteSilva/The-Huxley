vot_sim = 0
vot_nao = 0
vot_nulo = 0
voto = str(input()).lower()
while voto != "encerrar":
    if voto == "sim":
        vot_sim = vot_sim+1
    elif voto == "nao":
        vot_nao = vot_nao+1
    else :
        vot_nulo = vot_nulo+1
    voto = str(input()).lower()
if vot_sim > (vot_nulo + vot_nao) :
    print("COM FOGOS")
else :
    print("SEM FOGOS")