import math
a = float(input('digite o valor de a: '))
b = float(input('digite o valor de b: '))
c = float(input('digite o valor de c: '))
delta = (b*b) - 4*a*c
raiz1 = (- (b) + math.sqrt(delta)) /(2*a)
raiz2 = (- (b) - math.sqrt(delta)) /(2*a)
print(f'as raízes são {raiz1} e {raiz2}')