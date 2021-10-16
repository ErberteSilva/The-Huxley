def contagem(palavra):
    num_buracos = 0
    for i in palavra:
            if i == "A" or i == "D" or i == "O" or i == "P" or i == "R" :
                num_buracos = num_buracos+1
            elif i == "B" :
                num_buracos = num_buracos+2
    return(num_buracos)

rep = int(input())
for n in range(rep):
    contar = input().upper()
    print(contagem(contar))
