def crazy(ineedtosleep):
    if ineedtosleep=='0':
        return ''
    else:
        return crazy(input())+ineedtosleep+'\n'
    
print(crazy(input()))