'''Criar um programa que efetua cadastro de produtos e preços. Caso o
produto já existe, pergunta se o usuário pretende atualizar o valor.
Imprimir o dicionário ao final do programa em formato de lista.'''
products = {}
while True:
    product = input('digite o nome do produto: ')
    if product in products:
        resp = input('produto ja existe, deseja atualizar seu valor?: ')
        if resp == 's':
            new_value = float(input('digite o novo valor: '))
            products[product] = new_value
    else:
        value = float(input('digite o valor do produto: '))
        products[product] =  value
    resp = input('deseja continuar cadastrando (s/n): ')
    if resp == 'n':
        break
for key, value in products.items():
    print(f'{key} - {value}')