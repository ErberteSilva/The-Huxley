valor = float(input())
if 0 > valor > 100 :
    print("Fora de intervalo")
elif 0 < valor > 25 :
    print("[0,25]")
elif 25 < valor > 50 :
    print("(25,50]")
elif 50 < valor > 75 :
    print("(50,75]")
elif 75 < valor > 100 :
    print("(75,100]")