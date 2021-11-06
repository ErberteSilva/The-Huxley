def seq_d(In_value):
    if In_value%2!=0:
        return seq_d(In_value-1)
    else:
        print(In_value)
        if In_value==0:
            return 0
        else:
            seq_d(In_value-2)

seq_d(int(input()))