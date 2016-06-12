def gerar_acumulador():
    acumulador = 0

    def acumular(i):
        nonlocal acumulador
        acumulador += i
        return acumulador

    return acumular


acumular = gerar_acumulador()

print(acumular(1))
# acumulador += 5
print(acumular(2))
