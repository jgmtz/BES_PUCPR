def positive(numero):
    if numero > 0:
        return 'P'
    else:
        return 'N'


n = float(input("Digite um número: "))
resultado = positive(n)
print(resultado)