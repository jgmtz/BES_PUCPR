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
