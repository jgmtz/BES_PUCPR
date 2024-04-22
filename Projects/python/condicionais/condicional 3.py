jogador1 = input('par ou impar? ')
jogador2 = input('par ou impar? ')
if jogador1 == 'par' and jogador2 == 'par':
    exit('rodada não valeu')
if jogador2 == 'impar' and jogador1 == 'impar':
    exit('rodada não valeu')
num1 = int(input('insira um número inteiro de 1 a 5: '))
num2 = int(input('insira um número inteiro de 1 a 5: '))
if num1 < 0 or num1 > 5:
    exit('rodada não valeu')
if num2 < 0 or num2 > 5:
    exit('rodada não valeu')
soma = (num1 + num2) % 2
if soma == 0 and jogador1 == 'par':
    print('jogador 1 ganhou')
if soma == 1 and jogador1 == 'impar':
    print('jogador 1 ganhou')
if soma == 0 and jogador2 == 'par':
    print('jogador 2 ganhou')
if soma == 1 and jogador2 == 'impar':
    print('jogador 2 ganhou')