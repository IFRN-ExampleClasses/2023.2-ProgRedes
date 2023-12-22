import sys, os, time, platform, random, threading

MAX_VOLTAS = 10

# ------------------------------------------------------------
def carro_f1(nomePiloto: str):
    t_inicio = time.time()
    for voltas in range(1, MAX_VOLTAS+1):
        velocidadeCarro = 50 #random.randint(50,100)
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

    # Instanciar as THREADS na memória (solicitar recursos ao SO)
    piloto_1 = threading.Thread(target=carro_f1, args=['PENELOPE CHARMOSA'], name='P1')
    piloto_2 = threading.Thread(target=carro_f1, args=['DICK VIGARISTA']   , name='P2')
    piloto_3 = threading.Thread(target=carro_f1, args=['PETER PERFEITO']   , name='P3')
    piloto_4 = threading.Thread(target=carro_f1, args=['RUFUS LENHADOR']   , name='P4')

    # Iniciar a execução das THREADS
    piloto_1.start()
    piloto_2.start()
    piloto_3.start()
    piloto_4.start()

    # Unir as THREADS ao processo principal  
    piloto_1.join()
    piloto_2.join()
    piloto_3.join()
    piloto_4.join()
except:
    print(f'\nA CORRIDA NÃO PODE SER INICIADA... {sys.exc_info()[0]}')
else:
    print('\nBANDEIRA QUADRICULADA AGITADA...')
finally:
    print('\nFIM DA CORRIDA...')

