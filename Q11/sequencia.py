lenght,height=[int(i) for i in input().split()]
matriz=[[int(u)for u in input().split()]for i in range(lenght)]
listaseq=list()

for i in matriz:
    previous=contagem=seq=0
    for u in i:
        if u>=previous:
            contagem+=1
        else:
            contagem=1
        if contagem>seq:
            seq=contagem
        previous=u
    listaseq.append(seq)

for i in range(len(seq)):
    print("Linha %d: %d"%(i,seq[i]))

print("Maior Sequencia:",max(seq))