def conTox(sleep,x):
    for cont in range(len(sleep)):
        sleep[cont]=x(sleep[cont])

listing=input().split()
conTox(listing,int)
print(max(listing))