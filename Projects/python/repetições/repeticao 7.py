a = 0
while True:
    palavra = input('insira uma palavra (enter para encerrar): ')
    if palavra == '':
        break
    for i in palavra:
        if i == 'a':
            a += 1
print(f'sua frase tem {a} letras a ')