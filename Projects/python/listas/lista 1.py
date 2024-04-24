'''
Criar um programa que solicita ao usuário 6 números, calculando
sua média. Mostrar ao usuário uma lista com os números iguais
ou acima da média e uma lista com os números abaixo da média.
'''
nums = []
for i in range(6):
    num = int(input(f'digite o {i+1}° numero: '))
    nums.append(num)
media = sum(nums)/len(nums)
media_up = []
media_down = []
for num in nums:
    if num>= media:
        media_up.append(num)
    else:
        media_down.append(num)
print(f'numeros abaixo da media: {media_down}')
print(f'numeros acima da media: {media_up}')