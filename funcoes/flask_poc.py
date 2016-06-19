import functools

_roteador = {}


def rotear(path):
    return _roteador[path]


def rota(path):
    def decorador(func):
        _roteador[path] = func
        return func

    return decorador


# Resolvendo decorator de segurança

ADMIN = 'ADMIN'
GERENTE = 'GERENTE'
_grupos = {ADMIN: {'renzo', 'arthur'}, GERENTE: {'rogerio'}}


def permitir(grupo):
    usuarios_do_grupo = _grupos[grupo]
    def decorador(func):
        @functools.wraps(func)
        def nova_funcao(usuario, *args, **kwargs):
            if usuario in usuarios_do_grupo:
                return func(usuario, *args, **kwargs)
            print('Desculpe, acesso negado')

        return nova_funcao

    return decorador
