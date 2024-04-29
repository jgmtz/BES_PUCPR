'''Criar um programa que efetua o cadastro de pessoas com nome,
rg e cpf por meio de tuplas, adicionando elas a uma lista.
Imprimir a lista ao final do programa.'''

people = []
while True:
    name = input('digite o nome: ')
    rg = input('digite o rg: ')
    cpf = input('digite o cpf: ')
    person = (name, rg, cpf)
    people.append(person)
    resp = input('deseja continuar cadastrando? (s/n): ')
    if resp == 'n':
        break
print(f'lista de pessoas: {people}')
print(f'nome: {person[0]}')
print(f'rg: {person[1]}')
print(f'cpf: {person[2]}')
