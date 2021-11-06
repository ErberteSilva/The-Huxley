size=int(input())
via=[[int(i)for i in input().split()]for u in range(size)]

height=lenght=ending=last_height=last_lenght=0
while True:
    if size-1==height==lenght:
        print('OK')
        break
    elif height==size-1 and lenght!=size-1 and not(ending):
        if via[lenght][height] and via[lenght+1][height] and last_lenght!=lenght+1:
            last_lenght=lenght
            lenght+=1
            last_height=500
        elif via[lenght][height] and via[lenght][height-1] and height-1!=last_height:
            last_height=height
            height-=1
            last_lenght=500
        elif via[lenght][height] and via[lenght-1][height] and last_lenght!=lenght-1:
            last_lenght=lenght
            lenght-=1
        else:
            ending=1
    elif lenght==size-1 and height!=size-1 and not(ending):
        if via[lenght][height] and via[lenght][height+1] and height+1!=last_height:
            last_height=height
            height+=1
            last_lenght=500
        elif via[lenght][height] and via[lenght][height-1] and height-1!=last_height:
            last_height=height
            height-=1
            last_lenght=500
        elif via[lenght][height] and via[lenght-1][height] and last_lenght!=lenght-1:
            last_lenght=lenght
            lenght-=1
        else:
            ending=1
    elif height!=0 and not(ending):
        if via[lenght][height] and via[lenght+1][height] and last_lenght!=lenght+1:
            last_lenght=lenght
            lenght+=1
            last_height=500
        elif via[lenght][height] and via[lenght][height+1] and height+1!=last_height:
            last_height=height
            height+=1
            last_lenght=500
        elif via[lenght][height] and via[lenght][height-1] and height-1!=last_height:
            last_height=height
            height-=1
            last_lenght=500
        elif via[lenght][height] and via[lenght-1][height] and last_lenght!=lenght-1:
            last_lenght=lenght
            lenght-=1
        else:
            ending=1
    elif height==0 and not(ending):
        if via[lenght][height] and via[lenght+1][height]and last_lenght!=lenght+1:
            last_lenght=lenght
            lenght+=1
            last_height=500
        elif via[lenght][height] and via[lenght][height+1] and height+1!=last_height:
            last_height=height
            height+=1
        elif via[lenght][height] and via[lenght-1][height] and last_lenght!=lenght-1:
            last_lenght=lenght
            lenght-=1
        else:
            ending=1
    else:
        print('NOT OK')
        break