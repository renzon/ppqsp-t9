from time import strftime


def tempo_atual(func):
    print(strftime('%H:%M:%S'))
    func()


def  ola_mundo():
    return 'Olá Mundo'


def hello_world():
    return 'Hello World'

print(tempo_atual(ola_mundo))
print(tempo_atual(hello_world))


