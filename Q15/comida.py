rep = int(input())

for i in rep:
    cont = 0
    quantidade = float(input())
    while quantidade >1:
        quantidade = quantidade/2
        cont =+ cont
        print(cont,"dias")
