def velkmh(V0, A, T):
    vkm=float(V0+A*T)
    vm = float(vkm*3.6)
    return(vm)

def invalue():
    return(float(input()))

def slowest(a,b,c):
    speed=(a+b-abs(a-b))/2
    speed=(speed+c-abs(speed-c))/2
    return('%.1f'%speed)

speed1,speed2,speed3=velkmh(invalue(),invalue(),invalue()),velkmh(invalue(),invalue(),invalue()),velkmh(invalue(),invalue(),invalue())
SlowestCar=(slowest(speed1,speed2,speed3))
print(SlowestCar)
