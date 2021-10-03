n = int(input())
N = int(input())
v = n 
p = 0 

if N > n:
    while v<=N :
        if v >= 0 :
            p = p+v
        v = v+1
else :
    v = N
    while v<=n :
        if v >= 0 :
            p = p+v
        v = v+1
print(p)