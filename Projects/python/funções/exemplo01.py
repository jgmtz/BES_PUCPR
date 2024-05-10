

def get_int_number(msg):
    while True:
        try:
            num = int(input(msg))
            return num
        except:
            print('numero invalido')


def get_biggest_number(nums):
    return max(nums)
nums = []
for i in range(3):
    n = get_int_number(f'digite o {i + 1} nuemro: ')

print(f'o maior numero é {get_biggest_number}')