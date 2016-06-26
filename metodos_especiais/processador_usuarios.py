class Processador():
    def processar(self):
        nome_da_fonte = self.obter_nome_da_fonte()
        print(nome_da_fonte)
        for usuario in self.usuarios():
            print(usuario)

    def obter_nome_da_fonte(self):
        """
        Deve retornar o nome da fonte
        :return: str
        """
        raise NotImplementedError()

    def usuarios(self):
        """
        Deve retornar iteravel com usuarios
        :return:
        """
        raise NotImplementedError()


class ProcessadorFalso(Processador):
    def obter_nome_da_fonte(self):
        return 'Fonte Falsa'

    def usuarios(self):
        return 'Renzo Rogerio Guido Arthur'.split()


processador = ProcessadorFalso()
processador.processar()
