lenght=int(input())
values=[[],[]]
for cont in range(2):
    for cont2 in range(lenght):
        values[cont].append(int(input()))

for cont in range(lenght):
    print(values[0][cont])
    print(values[1][cont])