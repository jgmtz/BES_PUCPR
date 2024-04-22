dia1, mes1, ano1 = map(int, input("data1").split("/"))
dia2, mes2, ano2 = map(int, input("data1").split("/"))
b1 = (ano1 % 4 == 0 and ano1 % 100 != 0) or ano1 % 400
dy1 = 365 * ano1 + ano1 // 4 - ano1 // 400
diames1 = 0
for mes in range(mes1, 13):
    if mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12:
        diames1 += 31
    elif mes == 2:
        diames1 += 28
        if b1: diames1 += 1
    else:
        diames1 += 30
dias1 = dy1 - diames1 + dia1
b2 = (ano2 % 4 == 0 and ano2 % 100 != 0) or ano2 % 400
dy2 = 365 * ano2 + ano2 // 4 - ano2 // 400
diames2 = 0
for mes in range(mes2, 13):
    if mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12:
        diames2 += 31
    elif mes == 2:
        diames2 += 28
        if b2: diames2 += 1
    else:
        diames2 += 30
days2 = dy2 - diames2 + dia2
dif_days = abs(dias1 - days2)
print(f"Diferença de dias: {dif_days}")