import sys
import funcoes

# ----------------------------------------------------------------------
# Gerando uma lista N elementos com valores entre 1 e 1.000.000
try:
    n     = int(input('Informe a quantidade de elementos da lista: '))
    v_min = int(input('Informe o menor valor da lista: '))
    v_max = int(input('Informe o maior valor da lista: '))
except ValueError:
    print('\nERRO: O Valor informado não é um inteiro válido...\n')
    sys.exit()
except:
    print(f'\nERRO DESCONHECIDO: {sys.exc_info()[0]}')
    sys.exit()
else:
    retGerarLista = funcoes.gerar_lista(n, v_min, v_max)

    #retGerarLista => ( ___, ___ )
    #retGerarLista[0] -> True ou False
    #retGerarLista[1] => [...] ou None

# ----------------------------------------------------------------------
# Excrevendo a lista em um arquivo
if retGerarLista[0]:
    retSalvarArquivo = funcoes.salvar_lista(retGerarLista[1], 'valores_nao_ordenados.txt')

if retSalvarArquivo:
    print('\nArquivo Salvo com Sucesso...')