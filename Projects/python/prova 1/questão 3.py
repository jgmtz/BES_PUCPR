num = int(input('digite um número: '))
soma = 0
for i in range(1, num):
    if num % i == 0:
        soma += i
if num == soma:
    print(f' {num} é um número perfeito')
else:
    print(f'{num} não é um número perfeito')