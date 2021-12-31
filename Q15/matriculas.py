alunos_1 = list()
alunos_2 = list() 
alunos_total = list()
alunos_rep = list()

entrada = input()
alunos_1=entrada.split()


entrada = input()
alunos_2 = entrada.split()

alunos_total = alunos_1 + alunos_2

for i in range(len(alunos_total)):
    cont = alunos_total.count(alunos_total[i])
    if cont>1:
        alunos_rep.append(alunos_total[i])

resp = list(dict.fromkeys(alunos_rep))
print(' '.join(resp))