from datetime import timedelta, datetime
from random import randint
from threading import Thread
from time import strftime

_tarefas = []

EXECUTADA = 'EXECUTADA'
ESPERANDO = 'ESPERANDO'


class _Tarefa:
    def __init__(self, chamavel):
        self._chamavel = chamavel
        self._status = ESPERANDO

    def __call__(self):
        if self.deve_executar():
            self._chamavel()
            self._status = EXECUTADA
        return self.status

    @property
    def status(self):
        return self._status

    def deve_executar(self):
        return NotImplementedError('Deve definir critério de execução')

    def __repr__(self):
        return 'Tarefa(%s)' % self.status


class _TarefaIntervalo(_Tarefa):
    def __init__(self, chamavel, intervalo):
        super().__init__(chamavel)
        delta = timedelta(seconds=intervalo)
        self._inicio = datetime.now() + delta

    def deve_executar(self):
        return self._inicio <= datetime.now()


def executar_depois(chamavel, intervalo):
    """
    Adiciona invocável em loop de evento para ser executada depois de um intervalo
    :param chamavel: Chamável a ser executado
    :param intervalo: Intervalo de chamada em segundos
    :return: Tarefa
    """
    t = _TarefaIntervalo(chamavel, intervalo)
    _tarefas.append(t)
    return t


def executar_aleatoriamente(chamavel):
    intervalo = randint(1, 10)
    return executar_depois(chamavel, intervalo)


def inicar_loop_de_eventos_sincrono():
    global _tarefas
    while _tarefas:
        for tarefa in _tarefas:
            tarefa()
        _tarefas = list(filter(lambda t: t.status == ESPERANDO, _tarefas))


def inicar_loop_de_eventos_assincrono():
    Thread(target=inicar_loop_de_eventos_sincrono).start()


if __name__ == '__main__':
    fmt = '%H:%m:%S'
    inicio = strftime(fmt)


    def executar_em_intervalo():
        agora = strftime(fmt)
        print('Criada em %s executada em %s' % (inicio, agora))


    executar_depois(executar_em_intervalo, 5)
    executar_depois(executar_em_intervalo, 2)
    executar_aleatoriamente(executar_em_intervalo)

    inicar_loop_de_eventos_sincrono()
