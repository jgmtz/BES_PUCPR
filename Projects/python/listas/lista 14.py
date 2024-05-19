perguntas = ["Telefonou para a vítima?","Esteve no local do crime?","Mora perto da vítima?","Devia para a vítima?","Já trabalhou com a vítima?"]
respostas = []
for pergunta in perguntas:
    resposta = input(f'{pergunta} (sim/não): ')
    if resposta not in ['sim', 'não']:
        print('responda com sim ou não ')
        resposta = input(f'{pergunta} (sim/não): ')
    respostas.append(resposta)
sim = respostas.count('sim')
if sim == 2:
    classificação = 'suspeito'
elif sim == 3 or sim == 4:
    classificação = 'cumplice'
elif sim == 5:
    classificação = 'assassino'
else:
    classificação = 'Inocente'
print(classificação)
        