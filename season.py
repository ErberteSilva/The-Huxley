day = int(input())
month = int(input())
def EstacaoAno(day, month) :

    if month == 1:
        season = ("VERAO")
    if month == 2:
        season = ("VERAO")
    if month == 3:
        if day <= 20:
            season = ("VERAO")
        else:
            season = ("OUTONO")
    if month == 4:
        season = ("OUTONO")
    if month == 5:
        season = ("OUTONO")
    if month == 6:
        if day <= 20:
            season = ("OUTONO")
        else:
            season = ("INVERNO")
    if month == 7:
        season = ("INVERNO")
    if month == 8:
        season = ("INVERNO")
    if month == 9:
        if day <= 20:
            season = ("INVERNO")
        else:
            season = ("PRIMAVERA")
    if month == 10:
        season = ("PRIMAVERA")
    if month == 11:
        season = ("PRIMAVERA")
    if month == 12:
        if day <= 20:
            season = ("PRIMAVERA")
        else:
            season = ("VERAO")
    return(season)

print(EstacaoAno(day, month))