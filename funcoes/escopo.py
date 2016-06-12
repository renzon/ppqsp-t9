def gerar_acumulador():
    acumulador = {'v': 0}

    def acumular(i):
        acumulador['v'] += i
        return acumulador['v']

    return acumular


acumular = gerar_acumulador()

print(acumular(1))
# acumulador += 5
print(acumular(2))
