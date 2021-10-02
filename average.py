def average(g1,g2,g3,g4) :
    finalG = (((g1*1)+(g2*2)+(g3*3)+(g4*4))/(1+2+3+4))

    return(finalG)

grades = input().split()
g1,g2,g3,g4 = float(grades[0]), float(grades[1]), float(grades[2]), float(grades[3])

if (average(g1,g2,g3,g4)) >= 9:
    print("aprovado com louvor")
elif (average(g1,g2,g3,g4)) >= 7 :
    print("aprovado")
elif (average(g1,g2,g3,g4)) < 3  :
    print("reprovado")
else :
    print("prova final")

