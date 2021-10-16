Invalue = input()
while Invalue != "FIM" :
    
    vertices = Invalue.split()
    v1,v2,v3 = int(vertices[0]), int(vertices[1]), int(vertices[2])

    if v1 < abs(v2+v3) and v2 < abs(v1+v3) and v3 < abs(v2+v1) :
        if v1 == v2 == v3:
            f = "EQUILATERO"
        elif v1 == v2 or v2 == v3 or v3 == v1 :
            f = "ISOSCELES"
        else :
            f = "ESCALENO"
    else :
        f = "INVALIDO"
    print(f)
    Invalue = input()

