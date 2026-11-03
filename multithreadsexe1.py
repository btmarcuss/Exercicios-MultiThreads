import multiprocessing
import time

def tarefa(id_processo):
    time.sleep(0.5)
    print(f"Thread #{id_processo}")

if __name__ == "__main__":
    processos = []

    for i in range(1, 6):
        p = multiprocessing.Process(target=tarefa, args=(i,))
        processos.append(p)
        p.start()

    for p in processos:
        p.join()