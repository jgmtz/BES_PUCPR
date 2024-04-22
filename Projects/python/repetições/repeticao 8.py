binario = input('insira um numero binario: ')
decimal = 0
posicao = 0
while posicao < len(binario):
    digito = int(binario[posicao])
    exp = len(binario) - posicao - 1
    decimal += digito * (2 ** exp)
    posicao += 1
print(f'o numero em decimal é {decimal}')