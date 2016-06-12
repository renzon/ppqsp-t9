def truncar(texto:str, largura:'int > 0'=80) -> str:
    '''devolve o texto truncado no primeiro espaço até a largura,
           ou no primeiro espaço após a largura, se existir'''
    termino = None
    if len(texto) > largura:
        pos_espaco_antes = texto.rfind(' ', 0, largura)
        if pos_espaco_antes >= 0:
            termino = pos_espaco_antes
        else:
            pos_espaco_depois = texto.rfind(' ', largura)
            if pos_espaco_depois >= 0:
                termino = pos_espaco_depois
    if termino is None:
        return texto.rstrip()
    else:
        return texto[:termino].rstrip()


print(truncar('dfsdfsd s df sdf sdf sdfsdf'))
print(truncar(1))