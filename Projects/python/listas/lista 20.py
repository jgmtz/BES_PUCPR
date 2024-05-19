total_colaboradores = 0
total_gasto_abonos = 0
valor_minimo_abono = 100
maior_valor_abono = 0
print("Projeção de Gastos com Abono")
print("============================")
while True:
    salario = float(input("Salário: "))
    if salario == 0:
        break
    abono = salario * 0.2 if salario * 0.2 >= valor_minimo_abono else valor_minimo_abono
    total_colaboradores += 1
    total_gasto_abonos += abono
    if abono > maior_valor_abono:
        maior_valor_abono = abono
    print(f"R$ {salario:.2f} - R$ {abono:.2f}")
print(f"Foram processados {total_colaboradores} colaboradores")
print(f"Total gasto com abonos: R$ {total_gasto_abonos:.2f}")
print(f"Valor mínimo pago a {total_colaboradores} colaboradores")
print(f"Maior valor de abono pago: R$ {maior_valor_abono:.2f}")
