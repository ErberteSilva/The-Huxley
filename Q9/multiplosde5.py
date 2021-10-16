A, B = input().split()
bottom = int(A)
upper = int(B)
outValue = ''

for i in range(bottom, upper + 1):
  if i%5 == 0:
    outValue = outValue + str(i) + '|'
print(outValue[:-1])