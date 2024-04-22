word = input('digite uma palavra: ')
inv = ''
for l in word:
    inv = l + inv
if word == inv:
    print(f'a palavra {word} é um palindromo')
else:
    print(f' a palavra {word} não é um palíndromo')