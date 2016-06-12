from time import strftime


def tempo_atual(func):
    print(strftime('%H:%M:%S'))
    return func


def ola_mundo():
    return 'Olá Mundo'


ola_mundo = tempo_atual(ola_mundo)


def hello_world():
    return 'Hello World'


hello_world = tempo_atual(hello_world)

print(ola_mundo())
print(hello_world())
