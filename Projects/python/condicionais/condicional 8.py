dia = int(input('digite um dia: '))
mes = int(input('digite um mes: '))
ano = int(input('digite um ano: '))
hora = int(input('digite uma hora: '))
minuto = int(input('digite um minuto: '))
segundo = int(input('digite um segundo: '))
if dia > 31 or mes > 12 or hora > 23 or minuto > 59 or segundo > 59:
    exit('data inválida')
acrescentar = int(input('qual unidade deseja acrescentar?(1 para dia, 2 para mes, 3 para ano, 4 para hora, 5 par minuto, seis para segunfo) '))
quantidade = int(input('qual quantidade deve ser acrescentada? '))
if acrescentar == 1:
    dia += quantidade
elif acrescentar == 2:
    mes += quantidade
elif acrescentar == 3:
    ano += quantidade
elif acrescentar == 4:
    hora += quantidade
elif acrescentar == 5:
    minuto += quantidade
elif acrescentar == 6:
    segundo += quantidade
if segundo >= 60:
    minuto += segundo // 60
    segundo %= 60
if minuto >= 60:
    hora += minuto // 60
    minuto %= 60
if hora >= 24:
    dia += hora
    hora %= 24
if dia >= 31:
    mes += dia // 31
    dia %= 31
if mes >= 12:
    ano += mes // 12
    mes %= 12
print(f'{dia}/{mes}/{ano}')