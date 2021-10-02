day = float(0)
S = float(0)
s = float(0)
total_days = 0
balance = float(0)
while day < 7 :
  s = S
  S = float(input())
  if S-s >= 0.5 and day >=1:
      total_days = total_days+1
  balance = balance + S
  day = day + 1
print("R$ %.2f" %balance)
print(total_days)
