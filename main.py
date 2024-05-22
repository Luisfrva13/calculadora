while True:
    # INFORME OS NÚMEROS
    n1 = str(input('Informe o primeiro número:')).replace(',' , '.')
    n2 = str(input('Informe o segundo número:')).replace(',', '.')

    # CONVERTER PARA NÚMEROS DECIMAIS
    n1 = float(n1)
    n2 = float(n2)

    
    print('Informe a operação desejada:\n')

    print('"+" para somar.')
    
    print('"-" para subtrair.')

    print('"*" para multipilicar.')

    print('"/" para dividir.')

    print('"%" para encontrar o resto da divisão.')

    print('"x" para encerrrar.')

    op = input('operação desejada:')

    match op:
        case '+':
            print(f'A soma é {n1} + {n2}.')
        case '-':
            print(f'A subtração é {n2} + {n2}.')
        case '*':
            print(f'A multiplicação é {n1} + {n2}.')
        case '/':
            print(f'A divisão é {n1} / {n2}.')
        case '%':
            print(f'O resto da divisão é {n1} % {n2}.')
        case _: 
            print('Operação invalida')
            continue



