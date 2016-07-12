from threading import Thread
from time import sleep, time


def esperar(i):
    sleep(2)
    print(i)


def testar(n):
    inicio = time()
    threads = tuple(Thread(target=esperar, args=(i,)) for i in range(n))
    for i, t in enumerate(threads, 1):
        t.start()
    for t in threads:
        t.join()
    fim = time()
    print('Tempo total: %s (s)' %(fim-inicio)/1000)


testar(2047)
