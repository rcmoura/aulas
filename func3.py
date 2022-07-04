def pesquise(lista,valor):
    if valor in lista:
        return lista.index(valor)
    return None

L = [10,20,25,30,98,78,47]
print(pesquise(L,78))