a = int(input())
b = int(input())
c = 1
f = 0
while c <50 :
    if c % a == 0 and c % b == 0:
        f = f+1
    c = c+1
print(f)
