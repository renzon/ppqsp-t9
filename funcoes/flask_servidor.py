from funcoes.flask_poc import rotear, rota, permitir, ADMIN, GERENTE

@rota('/')
def home(nome):
    return 'Home Page %s' % nome

@rota('/users')
@permitir(ADMIN)
def usuarios(usuario):
    print(usuario)
    return ('Karen', 'Arthur')

@rota('/gerentes')
@permitir(GERENTE)
def gerentes(usuario, idade):
    print(usuario, idade)
    return ('Adinan', 'Victor')


fcn = rotear('/')
print(fcn('Renzo'))
fcn = rotear('/users')
print(fcn('renzo')) # execução com sucesso
print(fcn('nao admin')) # execução não acontece

fcn = rotear('/gerentes')
print(fcn('rogerio', 18)) # execução com sucesso
print(fcn('nao gerente', 44)) # execução não acontece
