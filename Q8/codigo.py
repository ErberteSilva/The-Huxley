decode = " abcdefghijklmnopqrstuvwxyz"
while 1 > 0 :
    message = input().split()
    secret = ''
    for i in message:
        secret = secret + decode[int(i)]

    if secret.lower() == "fim" :
        break
    else :
        print(secret)
