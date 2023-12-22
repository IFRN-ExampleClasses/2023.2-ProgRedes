#https://docs.python.org/3/library/logging.html
import sys, os, time, platform, random, threading, logging, logging.config

#------------------------------------------------------------
MAX_VOLTAS  = 100
LST_PILOTOS = ['PENELOPE CHARMOSA', 'DICK VIGARISTA   ', 
               'PETER PERFEITO   ', 'RUFUS LENHADOR   ']
QT_PILOTOS  = len(LST_PILOTOS)

#------------------------------------------------------------
logging.config.fileConfig('log_config.ini')
loggerPiloto  = logging.getLogger('piloto')
loggerChegada = logging.getLogger('chegada')

lstPodium = list()

#------------------------------------------------------------
def carro_f1(nomePiloto: str):
    t_inicio = time.time()
    for voltas in range(1, MAX_VOLTAS+1):
        velocidadeCarro = random.randint(50,100)
        time.sleep(1/velocidadeCarro)
        msg = f'Piloto: {nomePiloto} ..... volta {voltas:>2} em {1/velocidadeCarro:.5f} segundos'
        if voltas < MAX_VOLTAS:
            print(f'\t\t{msg}')
            loggerPiloto.info(msg)
        else:
            print(f'\t\t{msg} ..... RECEBEU BANDEIRADA')
            loggerChegada.warning(f'{msg} ..... RECEBEU BANDEIRADA')
    t_fim = time.time()
    d_tempo = t_fim - t_inicio
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
    for i in range(QT_PILOTOS):
        piloto = threading.Thread(target=carro_f1, args=[LST_PILOTOS[i]])
        threadsPilotos.append(piloto)
        print(f'\t\tPiloto: {LST_PILOTOS[i]} ..... Posição {i+1}')
except:
    print(f'\nA CORRIDA NÃO PODE SER INICIADA... {sys.exc_info()[0]}')
else:
    print('\nÉ DADA A LARGADA...\n')
    for thread in threadsPilotos: thread.start()
    for thread in threadsPilotos: thread.join()

    print('\nBANDEIRA QUADRICULADA AGITADA...')
    
    print('\nPODIUM...')
    for podium in lstPodium:
        print(f'\t{podium[0]} (Tempo de Corrida: {podium[1]})')
finally:
    print('\nFIM DA CORRIDA...')

