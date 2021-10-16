rep = int((input()))
for i in range(rep):
    word = input().lower()
    word = word.replace(' ', '')
    reverse = word[::-1]
    
    if word == reverse:
        print("SIM")
    else:
        print("NAO")