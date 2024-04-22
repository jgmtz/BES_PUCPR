num = input('digite um número para decompor: ')
dec = ''
exp = len(num) -1
for n in num:
    if exp == len(num) -1:
        dec += f'{num}'
    else:
        dec += f' + {num}'
    if exp > 1:
        dec += f' x10^{exp}'
    elif exp == 1:
        dec += f' x 10'