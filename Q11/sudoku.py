def decisao(In_value):
    for i in sudoku:
        for j in i:
            if i.count(j) != 1:
                return "NAO"

    sudoku2=[[In_value[n][i] for n in range(9)]for i in range(9)]

    for i in sudoku2:
        for j in i:
            if i.count(j) != 1:
                return "NAO"
    
    return "SIM"

instancias=int(input())
for cont in range(instancias):
    sudoku=[[int(u) for u in input().split()]for i in range(9)]
    print("Instancia",cont+1)
    print(decisao(sudoku))
    print()
    sudoku.clear()