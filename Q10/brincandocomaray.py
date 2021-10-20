def conTox(listing,x):
    for cont in range(len(listing)):
        listing[cont]=x(listing[cont])



lenght=input()
position=input().split()
position.reverse()
print(' '.join(position))
position.reverse()

position.append(position[0])
position.pop(0)
print(' '.join(position))

conTox(position,int)
position.sort(reverse=True)
conTox(position,str)
print(' '.join(position))