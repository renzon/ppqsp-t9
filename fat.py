def fatorial(n):
    '''Retorna n!'''
    return 1 if n <= 1 else n * fatorial(n - 1)


fat = fatorial
fat.nome = 'foo'
print(fat.nome)
print(fat(5))
print(fat(200))
print(fat.__name__)
print(fat.__doc__)
print(fat.__code__)
