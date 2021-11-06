lenght=int(input())
In_value=[[int(i)for i in input().split()]for u in range(lenght)]
result=[[0 for i in range(lenght)]for u in range(lenght)]

def dobrar_diagonal(lenght,matriz) :
    for i in range(lenght):#dobra a diagonal secundária
        matriz[i][lenght-1-i]=str(matriz[i][lenght-1-i]*2)

def inverter_diagonal(lenght,matriz) :
    for i in range(lenght):
        result[i][i]=str(matriz[lenght-1-i][lenght-1-i])

def transpos(lenght, matriz):
    for i in range(lenght):
	    for n in range(i+1,lenght):
	    	result[n][i]=str(matriz[i][n])
	    	result[i][n]=str(matriz[n][i])
        
dobrar_diagonal(lenght, In_value)
inverter_diagonal(lenght, In_value)
transpos(lenght, In_value)

for i in result:
		print(" ".join(i)+' ')