n1 = int(input())
n2 = int(input())
n3 = int(input())

M = m = n1

if M < n2:
    M = n2
if M < n3:
    M = n3

if m > n2:
    m = n2
if m > n3:
    m = n3
inter = (n1+n2+n3) - (M+m)
print(inter)