def inverse(nun):
    return int(str(nun)[::-1])


nun = int(input('Digite um número: '))
reverso = inverse(nun)
print(f'O reverso do número {nun} é: {reverso}')