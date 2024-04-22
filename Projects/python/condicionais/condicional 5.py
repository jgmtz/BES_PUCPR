destino = input('qual seu destino? (insira 1 para região norte, 2 para região nordeste, 3 para região centro-oeste e 4 para região sul) ')
retorno = input('sua viagem inclui retorno? (responda com sim ou não) ')
if destino == '1':
    if retorno == 'sim':
        preco = '900,00'
    else:
        preco = '500,00'
if destino == '2':
    if retorno == 'sim':
        preco = '650,00'
    else:
        preco = '350,00'
if destino == '3':
    if retorno == 'sim':
        preco = '600,00'
    else:
        preco = '350,00'
if destino == '4':
    if retorno == 'sim':
        preco = '550,00'
    else:
        preco = '300,00'
print(f'o preço total da passagem é R${preco}')