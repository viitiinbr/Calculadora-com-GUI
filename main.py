# Sitesma matemático
from lib import fatorial, tabuada
while True:

    print('\n\t\t\t -- Sistema Matemático -- \n')

    print('1. fatorial')
    print('2. tabuada')
    print('3. sair')

    # ler a opção do usuário
    op = int(input('Informe a opção desejada: \n'))

    if op == 1:
        #calcula fatorial
        print('\n\t - Calcula o fatorial \n')
        num = int(input('Informe o número: '))
        fat = fatorial(num)
        print(f'\n\t\t\t{num}! = {fat}\n')

    elif op == 2:
        print('\n\t - Calcula a tabuada - \n')
        num = int(input('informe o numero: \n'))
        tabuada(num)
        print(f'\n\t\t\t {num}  ')

    elif op == 3:
        print('\n\t\t\t - Até mais! -')




