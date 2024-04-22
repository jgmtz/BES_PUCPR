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