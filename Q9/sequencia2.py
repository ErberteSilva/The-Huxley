num = (input()).split()
num_1 = int(num[0])
num_2 = int(num[1])
for i in range(1,num_2+1):
    if i % num_1 == 0:
        print(i)
    else:
        print(i,end=' ')
