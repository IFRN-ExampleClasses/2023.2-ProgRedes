import sys, os, time, platform, random

MAX_VOLTAS = 10

# ------------------------------------------------------------
def carro_f1(nomePiloto: str):
    t_inicio = time.time()
    for voltas in range(1, MAX_VOLTAS+1):
        velocidadeCarro = random.randint(50,100)
        time.sleep(1/velocidadeCarro)
        print(f'\t\tPiloto: {nomePiloto} ..... volta {voltas} em {1/velocidadeCarro:.5f} segundos')
    t_fim = time.time()
    d_tempo = t_fim - t_inicio
    print(f'\t{nomePiloto} concluiu a prova em {d_tempo} segundos')
# ------------------------------------------------------------

if platform.system() == 'Windows':
    os.system('cls')
else:
    os.system('clear')

print('-'*80)
print('Grande Prêmio Natal/RN 2023 da CORRIDA MALUCA')
print('-'*80)

try:
    print('\nÉ DADA A LARGADA...\n')

    carro_f1('PENELOPE CHARMOSA')
    carro_f1('DICK VIGARISTA')
    carro_f1('PETER PERFEITO')
    carro_f1('RUFUS LENHADOR')
except:
    print(f'\nA CORRIDA NÃO PODE SER INICIADA... {sys.exc_info()[0]}')
else:
    print('\nBANDEIRA QUADRICULADA AGITADA...')
finally:
    print('\nFIM DA CORRIDA...')

