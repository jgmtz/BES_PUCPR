'''
criar um app que calcule as raizes de um polinomio quadratico de acordo com bhaskara
a saber: f(x) = ax² + bx + c
raizes = (-b +- raiz(delta)) / 2a
delta = b² - 4ac
'''
def initial_message():
    print('esse programa calcula as raizes de um polinomio do tipo ax² + bx + c')

    
    
def get_parameters(msg):
    print(msg)
    while True:
        try:
            a, b, c = map(int, list(input('').split(' ')))
            return a, b, c
        except:
            print('dados invalidos')
            
            
def calc_delta(a, b, c):
    return  b ** 2 - 4 * a * c


def calc_bhaskara(a, b, c):
    delta = calc_delta(a, b, c)
    if delta < 0:
        return None, None
    elif delta == 0:
        raiz = -b / 2 * a
        return raiz, raiz
    else:
        raiz1 = ((-b + raiz(delta)) / 2 * a)
        raiz2 = ((-b +- raiz(delta)) / 2 * a)
        return raiz1, raiz2
    
    
def show_output_messages(raiz1, raiz2):
    if raiz1 == None:
        print('raizes imaginarias')
    elif raiz2 == raiz1:
        print(f'duas raizes de valr {raiz1}')
    else: 
        print(f'duas raizes de valores {raiz1} e {raiz2}')
    
    
def start():
    initial_message()
    msg = 'informe so valores de a, b, c: '
    show_output_messages(calc_bhaskara(get_parameters(msg)))
start()
