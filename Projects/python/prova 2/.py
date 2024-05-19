dicionario = {}
quantidade_total = int(input('qual a quantidade de liquido ingerida ao longo do dia?: '))
quantidade_acumulada = 0
for i in range(quantidade_total):
    liquido = input('qual liquido voce tomou?: ')
    qtd = int(input('qual a quantidadede desse liquido? '))
    quantidade_acumulada +=qtd
    if quantidade_acumulada > quantidade_total or qtd > quantidade_total:
        print('quantidade de liquido não correspondente: ')
        break
    dicionario[liquido] = qtd
print(dicionario)
