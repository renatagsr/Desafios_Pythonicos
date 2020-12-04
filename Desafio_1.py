"""
01. Donuts

Dado um contador inteiro do número de donuts, retorne uma string com o formato 'Number of donuts: <count>' onde <count>
é o número recebido. Entretanto, se o contador for 10 ou mais, use a palavra 'many' ao invés do contador.
Exemplo: donuts(S) retorna 'Number of donuts: 5' e donuts(23) retorna 'Number of donuts: many'.
"""

def count_donuts(count):
    #first solution
    '''if count < 10:
        print(f'Donuts({count}). Number of Donuts: many')
    else:
        print(f'Number of Donuts: {count}')'''
    #Clean solution
    return print(f'Number of donuts{count}: {count if count < 10 else "many"}')

# --- Auxiliar Code ---

def test(f, in_, expected):
    """
    Executa a função f com o parâmetro in_ e compara o resultado com expected.
    :return: Exibe uma mensagem indicando se a função f está correta ou não.
    """
    out = f(in_)

    if out == expected:
        sign = '✅'
        info = ''
    else:
        sign = '❌'
        info = f'e o correto é {expected!r}'

    print(f'{sign} {f.__name__}({in_!r}) retornou {out!r} {info}')

# Test code
if __name__ == '__main__':
    count_donuts(4)
    count_donuts(9)
    count_donuts(10)
    count_donuts(99)

