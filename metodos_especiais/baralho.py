from collections import namedtuple, Sequence
from itertools import product

Carta = namedtuple('Carta', 'naipe valor')


class Baralho(Sequence):
    def __init__(self):
        naipes = '♣♡♠♢'
        valores = ''.join(map(str, range(2, 11)))
        valores += 'QJKA'
        self._cartas = [Carta(*t) for t in product(naipes, valores)]

    def __repr__(self):
        return repr(self._cartas)

    def __getitem__(self, item):
        return self._cartas[item]

    def __len__(self):
        return len(self._cartas)


baralho = Baralho()
print(baralho)
print(baralho[0])
print(baralho[:5])

for c in baralho:
    print(c)

print(baralho[-1])
# print(baralho[56])
as_de_paus = Carta('♣', 'A')
print(as_de_paus in baralho)
## Métodos que nao funcionam implementando somente __getitem__
print(baralho.count(as_de_paus))
print(baralho.index(as_de_paus))
print(list(reversed(baralho)))
