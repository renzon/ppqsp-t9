_roteador = {}


def rotear(path):
    return _roteador[path]


def rota(path):
    def decorador(func):
        _roteador[path] = func
        return func

    return decorador
