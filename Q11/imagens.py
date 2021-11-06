lenght_1,height_1 = [int(i) for i in(input().split())]
In_value_1=[[int(i)for i in input().split()]for u in range(lenght_1)]

lenght_2,height_2 = [int(i) for i in(input().split())]
In_value_2=list()
for cont in range(lenght_2):
    for i in input().split():
        for u in i:
            In_value_2.append(int(u))

segment=list()
for contagem_1 in range(0,lenght_1):
    if contagem_1+lenght_2>lenght_1:
                break
    for contagem_2 in range(0,height_1):
        if contagem_2+height_2>height_1:
                    break
        segment_aux=list()
        for cont_linaux in range(contagem_1,lenght_2+contagem_1):
            for cont_colaux in range(contagem_2,height_2+contagem_2):
                segment_aux.append(In_value_1[cont_linaux][cont_colaux])
        segment.append(segment_aux.copy())

contagem_final=0
for i in segment: 
    if In_value_2==i:
        contagem_final+=1
print(contagem_final)
