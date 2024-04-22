nome = ''
nomecompelto = input('insira seu nome completo: ')
parcial = ''
for i in nomecompelto:
    if i != ' ':
        parcial += i
    else:
        if nome == '':
            nome = parcial
        parcial = ''
nome += f' {parcial}'
print(f'nome completo: {nome}')