dia = int(input('digite seu dia de nascimento(xx): '))
mes = int(input('digite seu mês de nascimento(xx): '))
ano = int(input('digite seu ano de nascimento(xxxx): '))
exibicao = int(input('como quer exibir sua data de nascimento?(1 para data simples, 2 para data abreviada e 3 para data completa): '))

if exibicao == 1:
    print(f'{dia:02d}/{mes:02d}/{ano}')
elif exibicao == 2:
    if mes == 1:
        mesabreviado = "jan"
    if mes == 2:
        mesabreviado = 'abr'
    if mes == 3:
        mesabreviado = 'mar'
    if mes == 4:
        mesabreviado = 'abr'
    if mes == 5:
        mesabreviado = 'mai'
    if mes == 6:
        mesabreviado = 'jun'
    if mes == 7:
        mesabreviado = 'jul'
    if mes == 8:
        mesabreviado = 'ago'
    if mes == 9:
        mesabreviado = 'set'
    if mes == 10:
        mesabreviado = 'out'
    if mes == 11:
        mesabreviado = 'nov'
    if mes == 12:
        mesabreviado = 'dec'
    print(f'{dia:02d}/{mesabreviado}/{ano}')
elif exibicao == 3:
    if mes == 1:
        mescompleto = 'janeiro'
    if mes == 2:
        mescompleto = 'fevereiro'
    if mes == 3:
        mescompleto = 'março'
    if mes == 4:
        mescompleto = 'abril'
    if mes == 5:
        mescompleto = 'maio'
    if mes == 6:
        mescompleto = 'junho'
    if mes == 7:
        mescompleto = 'julho'
    if mes == 8:
        mescompleto = 'agosto'
    if mes == 9:
        mescompleto = 'setembro'
    if mes == 10:
        mescompleto = 'outubro'
    if mes == 11:
        mescompleto = 'novembro'
    if mes == 12:
        mescompleto = 'dezembro'
    print(f'{dia:02d} de {mescompleto} de {ano}')