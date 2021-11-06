def FAT(In_value):
    if In_value<=1:
        return(1)
    else:
        return(In_value*FAT(In_value-1))

def skinny(listadecompras):
    if len(listadecompras)==1:
        if listadecompras[0]%3==0:
            return FAT(int(listadecompras[0]))
        else:
            return 0
    else:
        if listadecompras[0]%3==0:
            return (FAT(int(listadecompras[0]))+skinny(listadecompras[1:]))
        else:
            return 0+skinny(listadecompras[1:])

listadecompras=[int(input())for i in range(5)]
print(skinny(listadecompras))