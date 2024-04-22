produto = float(input('qual o preço do produto selecionado? '))
pagamento = input('qual o meio de pagamento?(1 para à vista e em dinheiro/cheque, 2 para à vista e em cartão de crédito, 3 para 2 vezes sem juros e 4 para 3 vezes com juros) ')
if pagamento == '1':
    desconto = 10/100
elif pagamento == '2':
    desconto = 15/100
elif pagamento == '3':
    desconto = 0
elif pagamento == '4':
    desconto = -15/100
else:
    exit('não temos esse meio de pagamento')
precofinal = produto -(produto*(desconto) )
print(f'o valor a pagar de acordo com seu meio de pagamento é {precofinal}')