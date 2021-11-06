def result(leng,validar):
    if lenght==1:
        return 3
    else:
        if validar:
            return 4+result(lenght -1,False)
        else:
            return 1+result(lenght -1,True)

print(result(int(input()),True))