forca=int(input())
intel=int(input())
destr=int(input())
sneak=int(input())
fatbi=int(input())

if forca > 5 and destr >5 and fatbi > 5 :
    prof = "Knight"
elif forca < 5 and intel > 5 and sneak > 5 and fatbi < 5:
    prof = "Mage"
elif forca > 5 and intel > 5 and destr >5 and sneak > 5 and fatbi < 5:
    prof =  "Paladin"
else :
    prof = "Orc"

print(prof)