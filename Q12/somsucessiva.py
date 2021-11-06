def result(n,i):
    if n==0 or i==0:
        return 0
    else:
         return i+result(i,n-1)
        
print(result(int(input()),int(input())))