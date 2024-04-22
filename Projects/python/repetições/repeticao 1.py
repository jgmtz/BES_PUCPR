massainicial = float(input('digite a massa do material radioativo: '))
tempo = 0
while massainicial > 0.5:
    massainicial /= 2
    tempo += 50
print(f'a massa final é {massainicial} gramas e o tempo necessario foi {tempo} segundos')
    