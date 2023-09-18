while True:
    numero1 = input('Qual é o primeiro numero: ')
    operador = input('Qual é o operador(+-/*): ')
    numero2 = input('Qual é o segundo numero: ')

    numero_valido = None
    numero1_f = 0
    numero2_f = 0

    try:
        numero1_f = float(numero1)
        numero2_f = float(numero2)
        numero_valido = True
    except:
        numero_valido = None

    operador_valido = '-+/*'
    
    if operador not in operador_valido:
        print('Digite um operador válido!')
        continue

    if numero_valido is None:
        print('Um ou ambos numeros são invalidos')
        continue

    if operador == '+':
        print(f'{numero1_f} + {numero2_f} = {numero1_f + numero2_f}')
    elif operador == '-':
        print (f'{numero1_f} - {numero2_f} = {numero1_f - numero2_f}')
    elif operador == '/':
        print (f'{numero1_f} / {numero2_f} = {numero1_f / numero2_f}')
    elif operador == '*':
        print (f'{numero1_f} * {numero2_f} = {numero1_f * numero2_f}')
    else:
        print('Algum erro ocorreu!')
    
    sair = input('Deseja [S]air? ou digite algo para continuar ')
    if sair == 's' and 'S':
        print('Voce saiu do programa')
        break
    else:
        continue