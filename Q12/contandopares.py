def contagem(In_value):
    if len(In_value)==1:
        if int(In_value)%2==0:
            return 1
        else:
            return 0
    else:
        if int(In_value[0])%2==0:
            return 1+contagem(In_value[1:])
        else:
            return contagem(In_value[1:])

print(contagem(input()))