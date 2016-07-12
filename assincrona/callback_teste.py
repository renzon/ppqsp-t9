from functools import partial
from time import sleep, time

from assincrona import loop


def esperar(i):
    sleep(2)
    print(i)


def testar(n):
    for i in range(n):
        loop.executar_depois(partial(esperar, i), 2)
    loop.inicar_loop_de_eventos_assincrono()
    fim = time()


testar(4098)
