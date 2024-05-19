data = input("Digite a data no formato DD/MM/AAAA: ")
partes = data.split('/')
if len(partes) != 3:
    print("NULL")
else:
    dia, mes, ano = map(int, partes)
    if not (1 <= dia <= 31 and 1 <= mes <= 12 and ano > 0):
        print("NULL")
    else:
        meses = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho', 'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro']
        print(f"{dia} de {meses[mes - 1]} de {ano}")