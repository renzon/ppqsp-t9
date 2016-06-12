from time import strftime


def tempo_atual(func):
    print(strftime('%H:%M:%S'))
    return func


@tempo_atual
def ola_mundo():
    return 'Olá Mundo'


def hello_world():
    return 'Hello World'


hello_world = tempo_atual(hello_world)

print(ola_mundo())
print(hello_world())
