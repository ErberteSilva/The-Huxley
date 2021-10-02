M = int(input())
N = int(input())
m = M
v = 1
if M*v <=N: 
    while M*v <=N: 
       m = M
       m = m*v
       v = v+1
else:
    print("sem multiplos menores que",N)
print(m)