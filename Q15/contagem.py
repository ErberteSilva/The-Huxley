while True:
    cont = [0,0,0,0,0,0,0,0,0,0]
    entrada=[int(i) for i in input().split()]
    if entrada[0]==entrada[1]==0:
        break

    for i in range(entrada[0],entrada[1]+1):
        for j in str(i):
            if int(j) == 0:
                cont[0] += 1 
            elif int(j) == 1:
                cont[1] += 1
            elif int(j) == 2:
                cont[2] += 1
            elif int(j) == 3:
                cont[3] += 1
            elif int(j) == 4:
                cont[4] += 1
            elif int(j) == 5:
                cont[5] += 1
            elif int(j) == 6:
                cont[6] += 1
            elif int(j) == 7:
                cont[7] += 1
            elif int(j) == 8:
                cont[8] += 1
            else:
                cont[9] += 1

    saida=[str(i) for i in cont]
    print(' '.join(saida))