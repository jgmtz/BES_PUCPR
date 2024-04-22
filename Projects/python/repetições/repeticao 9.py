num = int(input('insira um numero: '))
hexadecimal = ''
hexa = num
while hexa > 0:
    resto = hexa % 16
    hexa //= 16
    if resto < 10:
        hexadecimal = str(resto) + hexadecimal
    elif resto == 10:
        hexadecimal = 'A' + hexadecimal
    elif resto == 11:
        hexadecimal = 'B' + hexadecimal
    elif resto == 12:
        hexadecimal = 'C' + hexadecimal
    elif resto == 13:
        hexadecimal = 'D' + hexadecimal
    elif resto == 14:
        hexadecimal = 'E' + hexadecimal
    elif resto == 15:
        hexadecimal = 'F' + hexadecimal
print(f'o numero hexadecimal é {hexadecimal}')
