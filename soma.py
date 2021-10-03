n = int(input())
c = 0
v = 0
while c < n :
    if c % 3 == 0 or c % 5 == 0:
        v = v + c 
    c = c+1

print(v)
