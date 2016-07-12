from threading import Thread
from time import sleep


def esperar():
    sleep(2)


def testar(n):
    threads = tuple(Thread(target=esperar) for i in range(n))
    for i, t in enumerate(threads, 1):
        print(i)
        t.start()
    for t in threads:
        t.join()


testar(2047)
