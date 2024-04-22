a = int(input('insira o 1º do seu cpf: '))
b = int(input('insira o 1º do seu cpf: '))
c = int(input('insira o 1º do seu cpf: '))
d = int(input('insira o 1º do seu cpf: '))
e = int(input('insira o 1º do seu cpf: '))
f = int(input('insira o 1º do seu cpf: '))
g = int(input('insira o 1º do seu cpf: '))
h = int(input('insira o 1º do seu cpf: '))
i = int(input('insira o 1º do seu cpf: '))
j = int(input('insira o 1º do seu cpf: '))
k = int(input('insira o 1º do seu cpf: '))

calculo1 = (a*10) + (b*9) + (c*8) + (d*7) + (e*6) + (f*5) + (g*4) + (h*3) + (i*2)
calculo2 = (a*11) + (b*10) + (c*9) + (d*8) + (e*7) + (f*6) + (g*5) + (h*4) + (i*3) + (j*2)

divisao1 = (calculo1 * 10) % 11
divisao2 = (calculo2 * 10) % 11

if divisao1 == 10:
    divisao1 = 0
if divisao2 == 10:
    divisao2 = 0

if divisao1 == j and divisao2 == k:
    print("Seu CPF é válido")
else:
    print("CPF inválido")