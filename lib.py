#biblioteca com as funções matemáticas

def tabuada(val):
    for cont in range(0,11):
        print(f'{cont} X {val} = {cont * val}')

def fatorial(val):
    if val > 1:
        fat = val * fatorial(val - 1)
        return fat
    else:
        return 1


print(f'\n{64}! = {fatorial(64)}\n')


#teste
#print(tabuada(2))
