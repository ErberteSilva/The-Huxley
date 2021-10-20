lenght=int(input())
listing=[int(input()) for cont in range(lenght)]
average=(sum(listing)/len(listing))
print("%.2f"%average)

listing_x=0
for cont in listing:
     if cont>=average*1.1:
         listing_x+=1
print(listing_x)

listing_x=0
for cont in listing:
     if cont<=average*0.9:
         listing_x+=1
print(listing_x)