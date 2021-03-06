import functools
from time import strftime, time


def tempo_atual(func):
    @functools.wraps(func)
    def logadora():
        print('Função {} Tempo: {}'.format(func.__name__, strftime('%H:%M:%S.%s')))
        inicio = time()
        resultado = func()
        print('Executou em %s' % (time() - inicio))
        return resultado

    return logadora


@tempo_atual
def ola_mundo():
    """
    Olá
    :return:
    """
    return 'Olá Mundo'


@tempo_atual
def hello_world():
    """
    Hello
    :return:
    """

    return 'Hello World'


print(ola_mundo())
print(hello_world())
print(ola_mundo())
print(ola_mundo)
print(help(ola_mundo))
print(hello_world)
print(help(hello_world))
