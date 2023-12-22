import sys, os, time, platform, random, threading

MAX_VOLTAS = 10

lstPilotos = ['PENELOPE CHARMOSA','DICK VIGARISTA   ', 
              'PETER PERFEITO   ','RUFUS LENHADOR   ']

lstPodium = list()

#------------------------------------------------------------
def carro_f1(nomePiloto: str):
    t_inicio = time.time()
    for voltas in range(1, MAX_VOLTAS+1):
        velocidadeCarro = random.randint(50,100)
        time.sleep(1/velocidadeCarro)
        msg = f'\t\tPiloto: {nomePiloto} ..... volta {voltas:>2} em {1/velocidadeCarro:.5f} segundos'
        if voltas < MAX_VOLTAS:
            print(msg)
        else:
            print(f'{msg} ..... RECEBEU BANDEIRADA')
    t_fim = time.time()
    d_tempo = t_fim - t_inicio
    #print(f'\t{nomePiloto} concluiu a prova em {d_tempo:.5f} segundos')
    lstPodium.append([nomePiloto, round(d_tempo,5)])
#------------------------------------------------------------

if platform.system() == 'Windows':
    os.system('cls')
else:
    os.system('clear')

print('-'*80 + '\nGrande Prêmio Natal/RN 2023 da CORRIDA MALUCA\n' + '-'*80)

try:
    # Instanciar as THREADS na memória (solicitar recursos ao SO)
    print('\nGRID DE LARGADA...')
    threadsPilotos = list()
    for i in range(len(lstPilotos)):
        piloto = threading.Thread(target=carro_f1, args=[lstPilotos[i]])
        threadsPilotos.append(piloto)
        print(f'\t\tPiloto: {lstPilotos[i]} ..... Posição {i+1}')

    print('\nÉ DADA A LARGADA...\n')
    for thread in threadsPilotos: thread.start()
    for thread in threadsPilotos: thread.join()
except:
    print(f'\nA CORRIDA NÃO PODE SER INICIADA... {sys.exc_info()[0]}')
else:
    print('\nBANDEIRA QUADRICULADA AGITADA...')
    print('\nPODIUM...')
    for podium in lstPodium:
        print(f'\t{podium[0]} (Tempo de Corrida: {podium[1]})')
finally:
    print('\nFIM DA CORRIDA...')

