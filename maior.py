M = int(input())
N = int(input())
m = 0
v = 0
while m <= N :
    if m % M == 0 :
        v = m 
    m = m+1 
if v != M :
    print(v)
else :
    print("sem multiplos menores que",N)