print("Bem vindo ao restaurante Boca Feliz!!!")
estoque = {'pao': 10, 'hamburguer': 12, 'tomate': 5, 'bacon': 5, 'ovo': 5}
cardapio = {
    'x-burguer': ['pao', 'hamburguer'],
    'x-salada': ['pao', 'hamburguer', 'tomate'],
    'x-bacon': ['pao', 'hamburguer', 'tomate', 'bacon'],
    'x-egg': ['pao', 'hamburguer', 'ovo'],
    'x-tudo': ['pao', 'hamburguer', 'tomate', 'hamburguer', 'bacon', 'ovo']
}

while True:
    print(cardapio)
    escolha = input("O que deseja pedir (0 para sair)? ")

    if escolha == '0':
        print("Saindo do programa. Até mais!")
        break
    elif escolha not in cardapio:
        print("Item não localizado no cardápio")
        continue

    sem_ingrediente = []
    for ingrediente in cardapio[escolha]:
        if ingrediente not in estoque or estoque[ingrediente] == 0:
            sem_ingrediente.append(ingrediente)

    if sem_ingrediente:
        for ingrediente in sem_ingrediente:
            print(f"Infelizmente acabou o {ingrediente}")
    else:
        print(f"Um {escolha} saindo no capricho!!!")
        for ingrediente in cardapio[escolha]:
            estoque[ingrediente] -= 1
