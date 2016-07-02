_ouvintes = []

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


def executar_depois(chamavel, intervalo):
    """
    Adiciona invocável em loop de evento para ser executada depois de um intervalo
    :param chamavel: Chamável a ser executado
    :param intervalo: Intervalo de chamada em segundos
    :return: tarefa
    """
