pontos1 = 0
pontos2 = 0
pontosnecessarios = int(input('defina a quantidade de pontos necessários paraque o jogo acabe: ' ))
while pontos1 < pontosnecessarios and pontos2 < pontosnecessarios:
    jogador1 = int(input('pedra, papel ou teroura? (1, 2 e 3): '))
    jogador2 = int(input('pedra, papel ou teroura? (1, 2 e 3): '))
    if jogador1 == 1:
        if jogador2 == 1:
            print('sem pontos adicionais ')
        if jogador2 == 2:
            print('ponto pro jogador 2 ')
            pontos2 += 1
        if jogador2 == 3:
            print(' ponto pro jogador 1 ')
            pontos1 += 1
    if jogador1 == 2:
        if jogador2 == 1:
            print('ponto pro jogador 1 ')
        if jogador2 == 2:
            print('sem pontos adicionais ')
            pontos2 += 1
        if jogador2 == 3:
            print(' ponto pro jogador 2 ')
            pontos1 += 1
    if jogador1 == 3:
        if jogador2 == 1:
            print('ponto pro jogador 2 ')
        if jogador2 == 2:
            print('ponto pro jogador 1 ')
            pontos2 += 1
        if jogador2 == 3:
            print('sem pontos adicionais ')
            pontos1 += 1
if pontos1 == pontosnecessarios:
    print('jogador 1 venceu')
if pontos2 == pontosnecessarios:
    print('jogador 2 venceu') 
    

        