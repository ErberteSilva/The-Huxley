my_list=[]
for i in range(101):
    my_list.append(input())

for n in range(100):
    if my_list[n] == my_list[-1]:
        print(n)
