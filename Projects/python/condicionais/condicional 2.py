peso = float(input("digite seu peso: "))
altura = float(input('digite sua altura: '))
imc = peso/(altura * altura)
f1 = 18.5
f2 = 25
f3 = 30
if imc < f1:
    condicao = 'abaixo do peso'
elif imc < f2:
    condicao = 'peso normal'
elif imc < f3:
    condicao = 'acima do peso'
else:
    condicao = 'obeso'
print(f'de acordo com seu peso e altura, sua condição é: {condicao}')