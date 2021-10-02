InValue = input().split()
N,C = int(InValue[0]), int(InValue[1])
n = 0
p = 0
state = 'N'
while n < N :
    var = input().split()
    S,E = int(var[0]), int(var[1])
    p = p+(S-E)
    if p > C :
        state = 'S'
    n = n+1
print(state)

