frutas = 'banana caqui pequi abacaxi maça'.split()

print(frutas)

print(sorted(frutas))
print(frutas)
print(sorted(frutas, key=len))


def invertida(fruta):
    return ''.join(reversed(fruta))


print(invertida('Python'))
print(sorted(frutas, key=invertida))
print(sorted(frutas, key=lambda f: f[::-1]))


print((lambda f: f[::-1])('Renzo'))

print(type(lambda f: f[::-1]))
print(type(invertida))
