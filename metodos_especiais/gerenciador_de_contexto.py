# file = open('jogadores.txt', 'a', encoding='utf8')
# file.write('Ronaldo\nRomário')
# file.close()
#
# i = 1
#
# files = []
# while True:
#     print('Tentativa %s' % i)
#     i += 1
#     with open('jogadores.txt', 'rb') as file:
#         files.append(file)
#         for jogador in file:
#             try:
#                 jogador = jogador.decode('ascii')
#             except UnicodeDecodeError:
#                 print('Deu erro')
#             else:
#                 print(jogador)
from random import randint


class AcessoARede:
    def __enter__(self):
        self.erro = randint(0, 2) == 0
        print(id(self), self.erro)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('Executou Exit. Erro: %s ' % self.erro)
        return True


for i in range(50):
    with AcessoARede() as acesso:
        print('Dentro do with', id(acesso))
        if acesso.erro:
            raise Exception()
