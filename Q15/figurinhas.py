quantidade = int(input())
Serial_Maria = list()
Serial_Joao = list()
soma_Maria = 0 
soma_Joao = 0

for i in range (quantidade):
    serial = int(input())
    if (serial % 2) == 0:
        if serial in Serial_Joao:
            Serial_Joao.append(serial)
        else: 
            Serial_Joao.append(serial)
            soma_Joao = soma_Joao+serial
    else:
        if serial in Serial_Maria:
            Serial_Maria.append(serial)
        else: 
            Serial_Maria.append(serial)
            soma_Maria = soma_Maria+serial
print(len(Serial_Joao))
print(len(Serial_Maria))
if soma_Joao > soma_Maria :
    print(soma_Joao)
else:
    print(soma_Maria)