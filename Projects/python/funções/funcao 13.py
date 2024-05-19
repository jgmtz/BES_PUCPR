def desenhar_retangulo(linhas=1, colunas=1):
    linhas = max(1, min(linhas, 20))
    colunas = max(1, min(colunas, 20))

    # Desenha o retângulo
    for i in range(linhas):
        if i == 0 or i == linhas - 1:
            print('+' + '-' * (colunas - 2) + '+')
        else:
            print('|' + ' ' * (colunas - 2) + '|')


linhas_input = int(input("Digite o número de linhas (1 a 20): "))
colunas_input = int(input("Digite o número de colunas (1 a 20): "))

desenhar_retangulo(linhas_input, colunas_input)
