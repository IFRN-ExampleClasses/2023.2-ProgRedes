import random, os, sys

# ----------------------------------------------------------------------
# Gerando uma lista N elementos com valores entre 1 e 1.000.000
try:
    n = int(input('Informe a quantidade de elementos da lista: '))
except ValueError:
    print('\nERRO: O Valor informado não é um inteiro válido...\n')
    sys.exit()
except:
    print(f'\nERRO DESCONHECIDO: {sys.exc_info()[0]}')
    sys.exit()
else:
    if (n <= 0):
        print(f'\nAVISO: Informe um valor inteiro positivo...\n')
        sys.exit()

    lstValores = [random.randint(1, 1000000) for _ in range(n)]

# ----------------------------------------------------------------------
# Excrevendo a lista em um arquivo
DIRATUAL    = os.path.dirname(os.path.abspath(__file__)) 
NOMEARQUIVO = DIRATUAL + '\\valores_nao_ordenados.txt'
try:
    arq_output = open(NOMEARQUIVO, 'w')
except:
    print(f'\nERRO DESCONHECIDO: {sys.exc_info()[0]}')
    sys.exit()
else:
    for i in lstValores: arq_output.write(f'{i}\n')
    arq_output.close()