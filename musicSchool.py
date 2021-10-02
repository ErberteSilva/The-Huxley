grade = float(input())
absence = int(input())
def ClassificaAluno (notas,faltas):
    if faltas <=10:
        if notas <7:
            state=("REPROVADO")

        elif notas <9.5 :
            state=("APROVADO")

        else :
            state=("APROVADO COM LOUVOR")
    else:
        state=("REPROVADO POR FALTAS")
    return (state)
print(ClassificaAluno(grade, absence))
