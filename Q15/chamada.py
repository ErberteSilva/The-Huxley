entrada = input().split()
n = int(entrada[0])
k = int(entrada[1])
alunos = list()
for i in range(n):
    alunos.append(input())
alunos.sort()
print(alunos[k-1]) 