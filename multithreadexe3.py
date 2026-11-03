import multiprocessing
import time
import random

DISTANCIA_MAXIMA = 30

def sapo_correndo(id_sapo):
    distancia_percorrida = 0
    
    while distancia_percorrida < DISTANCIA_MAXIMA:
        salto = random.randint(0, 5)
        distancia_percorrida += salto
        print(f"Sapo #{id_sapo} pulou {salto} cm e já percorreu {distancia_percorrida} cm.")
        time.sleep(0.1)
        
    print(f"--> O Sapo #{id_sapo} CHEGOU À LINHA DE CHEGADA!")

if __name__ == "__main__":
    processos = []
    
    print("--- INÍCIO DA CORRIDA DE SAPOS ---")
    
    for id_sapo in range(1, 6):
        p = multiprocessing.Process(target=sapo_correndo, args=(id_sapo,))
        processos.append(p)
        p.start()

    for p in processos:
        p.join()
        
    print("--- FIM DA CORRIDA ---")