from threading import Thread
from time import sleep, time


def esperar(i):
    sleep(2)
    print(i)


def testar(n):
    threads = tuple(Thread(target=esperar, args=(i,)) for i in range(n))
    for i, t in enumerate(threads, 1):
        t.start()
    for t in threads:
        t.join()


testar(2047)
