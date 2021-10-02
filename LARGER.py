def larger(a,b):
    ans=((a+b+abs(a-b))//2)
    return(ans)

InValue = input().split()
N1,N2,N3 = int(InValue[0]), int(InValue[1]), int(InValue[2])
LN= larger((larger(N1,N2)),N3)
print(LN, "eh o maior")
