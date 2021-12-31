while True:
    entrada = input()
    if entrada == "sair":
        break
    start = entrada.split('@')
    if len(start[0]) <1 :
        print("errado")
    else:
        if start[1].count('.')!=2:
            print("errado")
        else:
            finish = start[1].split('.')

            if len(finish[0]) < 1 or len(finish[1])< 1 or len(finish[2])<1 :
                print("errado")
            else:
                print("certo")
                    
