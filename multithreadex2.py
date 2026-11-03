import multiprocessing
import time
import random

def somar_linha(id_linha, valores):
    soma = 0
    for valor in valores:
        soma += valor
        time.sleep(0.2)
    print(f"Linha #{id_linha} | Valores: {valores} | Soma: {soma}")

if __name__ == "__main__":
    processos = []
    
        for id_linha in range(1, 4):
        valores = [random.randint(1, 100) for _ in range(5)]
        p = multiprocessing.Process(target=somar_linha, args=(id_linha, valores))
        processos.append(p)
        p.start()

    for p in processos:
        p.join()