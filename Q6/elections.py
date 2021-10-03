<<<<<<< HEAD
stop = 0
capone = 0
baba = 0
valid = 0
white = 0
out = 0
while (stop == 0) :
    vote = int(input())
    if(vote) == 83 :
        baba = baba+1
        valid = valid+1
    elif(vote) == 93 :
        capone = capone+1
        valid = valid + 1
    elif(vote) == 0 :
        white = white+1
        valid = valid+1
    elif(vote) == -1 :
        stop = stop+1
    else :
        out = out+1

a = float((baba*100)/valid)
b = float((capone*100)/valid)

print(baba)
print(capone)
print(white)
print(out)
if (baba > capone):
    print('83')
elif (capone > baba):
    print('93')
else:
    print('93')

print('%.2f' % (a))
print('%.2f' % (b))
=======
stop = 0
capone = 0
baba = 0
valid = 0
white = 0
out = 0
while (stop == 0) :
    vote = int(input())
    if(vote) == 83 :
        baba = baba+1
        valid = valid+1
    elif(vote) == 93 :
        capone = capone+1
        valid = valid + 1
    elif(vote) == 0 :
        white = white+1
        valid = valid+1
    elif(vote) == -1 :
        stop = stop+1
    else :
        out = out+1

a = float((baba*100)/valid)
b = float((capone*100)/valid)

print(baba)
print(capone)
print(white)
print(out)
if (baba > capone):
    print('83')
elif (capone > baba):
    print('93')
else:
    print('93')

print('%.2f' % (a))
print('%.2f' % (b))
>>>>>>> b049166c5accd187c83afb409b12b8f996ed29e8
