from funcoes.flask_poc import rotear, rota

@rota('/')
def home(nome):
    return 'Home Page %s' % nome

@rota('/users')
def usuarios():
    return ('Karen', 'Arthur')



fcn = rotear('/')
print(fcn('Renzo'))
fcn = rotear('/users')
print(fcn())
