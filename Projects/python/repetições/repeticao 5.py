paisA = 5000000
natA = 3/100
paisB = 7000000
natB = 2/100
ano = 0
while paisA <= paisB:
    paisA *= 1 + natA
    paisB *= 1 + natB
    ano +=1
print(f'tempo necessário para que a população A ultrapasse a população B: {ano} anos')