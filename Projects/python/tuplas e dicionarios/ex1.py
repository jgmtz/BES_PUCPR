
cardapio = {
'x-burguer': ['pao', 'hamburguer'],
'x-salada': ['pao', 'hamburguer', 'tomate'],
'x-bacon': ['pao', 'hamburguer', 'tomate', 'bacon'],
'x-egg': ['pao', 'hamburguer', 'ovo'],
'x-tudo': ['pao', 'hamburguer', 'tomate', 'hamburguer', 'bacon', 'ovo']
}


print('x-burguer: pao, hamburguer')
print('x-salada: pao, hamburguer, tomate')
print('x-bacon: pao, hamburguer, tomate, bacon')
print('x-egg: pao, hamburguer, ovo')
print('x-tudo: pao, hamburguer, tomate, hamburguer, bacon, ovo')
pedido = ''
while True: 
    estoque = {'pao': 10, 'hamburguer': 12, 'tomate': 5, 'bacon': 5, 'ovo': 5 }   
    pedido = input('o que deseja pedir (0 para sair)? ')
    if pedido == 'x-burger':
        estoque.update({'pao': -1})
        
    if pedido not in cardapio:
        print('item não localizado no cardápio')
    print(estoque)
    
    



''';
- Digitando “0” deve sair do programa;
- Digitando o nome do produto pode ter uma das seguintes possibilidades:
- Se o item não consta no cardápio exibir a mensagem “Item não localizado no
cardápio”;
- Se não tiver os ingredientes para o preparo do produto em estoque mostrar uma
mensagem para cada ingrediente faltante “Infelizmente acabou o {ingrediente}”;
- Se for possível produzir o produto, reduzir as quantidades de estoque e mostrar a
mensagem “um {produto} saindo no capricho!!!”;
- O programa deve continuar fazendo os pedidos até que o usuário decida sair do
mesmo'''