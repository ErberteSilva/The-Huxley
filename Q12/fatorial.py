def FAT(In_value):
    if In_value<=1:
        return(1)
    else:
        return(In_value*FAT(In_value-1))

while True:
    In_value=int(input())
    if In_value==-1:
        break
    print(FAT(In_value))