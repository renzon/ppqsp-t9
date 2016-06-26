from abc import ABC, abstractmethod


class Processador(ABC):
    def processar(self):
        """
        Processa fonte de usuarios.
        Devem ser implementados métodos obter_nome_da_fonte e
        usuarios
        :return: None
        """
        nome_da_fonte = self.obter_nome_da_fonte()
        print(nome_da_fonte)
        for usuario in self.usuarios():
            print(usuario)

    @abstractmethod
    def obter_nome_da_fonte(self):
        """
        Deve retornar o nome da fonte
        :return: str
        """

    @abstractmethod
    def usuarios(self):
        """
        Deve retornar iteravel com usuarios
        :return: iterable
        """


class ProcessadorFalso(Processador):
    def obter_nome_da_fonte(self):
        return 'Fonte Falsa'

    def usuarios(self):
        return 'Renzo Rogerio Guido Arthur'.split()


processador = ProcessadorFalso()
processador.processar()
